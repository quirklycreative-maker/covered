#!/usr/bin/env python3
"""Validate the India country pack.

Run from the repository root:  python3 -I packs/validate_country.py
Needs: pyyaml, jsonschema>=4.   Exit code 1 on any error. Warnings never fail the run.

Checks
  1. Schema for country.yaml and templates.yaml.
  2. Cross-references: rule sources, template rules, outcome letters, form fields.
  3. Hindi: every {en, hi} pair complete, Devanagari present, placeholder parity,
     no gendered verb pairs, bracketed English for the formal terms.
  4. Templates: placeholders defined, no leftover [brackets] or TODO, no unused slots.
  5. Fee table and forum limits are consistent.
  6. Decision engine: replays every golden case.
"""
import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent
COUNTRY = ROOT / "countries" / "in" / "country.yaml"
TEMPLATES = ROOT / "countries" / "in" / "templates.yaml"
S_COUNTRY = ROOT / "schema" / "country.schema.json"
S_TEMPLATES = ROOT / "schema" / "templates.schema.json"

PH = re.compile(r"\{([a-z][a-z0-9_]*)\}")
DEVANAGARI = re.compile(r"[ऀ-ॿ]")
GENDER_PAIR = re.compile(r"\S+(?:ता|ती)/\S+(?:ती|ता)|\S*ूँगा/\S*ूँगी|\S*ूँगी/\S*ूँगा|\S+ा/\S+ी(?=[\s।,.]|$)")
LEFTOVER = re.compile(r"\[[^\]\n]*\]|TODO|TBD|XXX|lorem", re.I)
# Hindi formal term -> English that must be bracketed once in the same template.
BRACKET_TERMS = {
    "विपक्षी पक्ष": "Opposite Part",
    "शिकायतकर्ता": "Complainant",
    "शपथ-पत्र": "Affidavit",
    "सत्यापन": "Verification",
}
EJAGRITI_UPLOADS = ["Index", "Proforma", "Synopsis", "Memo of Parties", "Notarized Affidavit", "Vakalatnama", "Annexures"]

errors, warnings = [], []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def load(path):
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return json.loads(json.dumps(data, default=str, ensure_ascii=False))


def schema_check(data, schema_path, label):
    with open(schema_path, encoding="utf-8") as f:
        schema = json.load(f)
    for e in sorted(Draft202012Validator(schema).iter_errors(data), key=lambda e: list(e.path)):
        where = "/".join(str(p) for p in e.path) or "(root)"
        err(f"{label} schema: {where}: {e.message[:200]}")


def walk_pairs(node, path, out):
    """Collect every dict that has an 'en' string, so Hindi presence can be checked."""
    if isinstance(node, dict):
        if isinstance(node.get("en"), str):
            out.append((path, node))
        for k, v in node.items():
            walk_pairs(v, f"{path}/{k}", out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk_pairs(v, f"{path}[{i}]", out)


def check_pair(path, pair, parity=True):
    en, hi = pair.get("en"), pair.get("hi")
    if not isinstance(hi, str) or not hi.strip():
        err(f"hindi missing: {path}")
        return
    if not DEVANAGARI.search(hi):
        err(f"hindi has no Devanagari: {path}")
    if parity and set(PH.findall(en)) != set(PH.findall(hi)):
        err(f"placeholder mismatch en/hi: {path}: en={sorted(set(PH.findall(en)))} hi={sorted(set(PH.findall(hi)))}")
    if GENDER_PAIR.search(hi):
        err(f"gendered verb pair in hindi: {path}: {GENDER_PAIR.search(hi).group(0)}")


# ---------------------------------------------------------------- decision engine
def fee_for(price, slabs):
    for s in slabs:
        if s["up_to"] is None or price <= s["up_to"]:
            return s["fee"]
    return None


def forum_for(price, thr):
    if price <= thr["district_max"]:
        return "district"
    if price <= thr["state_max"]:
        return "state"
    return "national"


def decide(inp, cov):
    """Replay the who-pays logic. Returns a dict of what the app would do."""
    signals = set(inp.get("signals") or [])
    unit = inp.get("unit_warranty_months")
    if unit is None:
        return {"ask": ["unit_warranty_months"]}
    age = inp["purchase_months"]
    if inp.get("starts_from") == "installation":
        age = age - (inp.get("installation_gap_months") or 0)
    cover = max(unit, inp.get("part_cover_months") or 0)
    excluded = bool(inp.get("excluded_damage"))
    in_warranty = age <= cover and not excluded
    assumed = inp.get("warranty_source") == "pack_hint"
    out = {"assumed": assumed}
    if assumed:
        out["notice"] = "assumed_warranty_notice"

    card = inp.get("card") or {}
    card_plan = bool(card.get("paid_with_card") and card.get("benefit") == "extended_warranty" and card.get("benefit_active"))
    plan = bool(inp.get("plan_active")) or card_plan
    has_signal = bool(signals & set(cov["defect_signals"])) and not excluded

    passed = (not excluded) and inp["purchase_months"] > cov["limitation_months"]   # two years counted from purchase

    if in_warranty:
        out["outcome"] = "brand_warranty"
    elif plan:
        out["outcome"] = "protection_plan"
        out["addressee"] = "card_issuer" if card_plan and not inp.get("plan_active") else "plan_provider"
    elif passed:
        out["outcome"] = "out_of_pocket"
        out["message"] = "limitation_passed"
    elif has_signal:
        out["outcome"] = "statutory_rights"
        price = inp["price_inr"]
        out["forum"] = forum_for(price, cov["forum_thresholds_inr"])
        out["fee_inr"] = fee_for(price, cov["fee_slabs_inr"])
        if out["forum"] == "state":
            out["message"] = "forum_state"
        elif out["forum"] == "national":
            out["message"] = "forum_national"
    else:
        out["outcome"] = "out_of_pocket"
    out["letter"] = (cov["outcomes"].get(out["outcome"]) or {}).get("letter")
    return out


def replay_golden(country):
    cov = country["coverage"]
    seen = set()
    for case in country["golden_cases"]:
        if case["id"] in seen:
            err(f"golden case id repeated: {case['id']}")
        seen.add(case["id"])
        got = decide(case["input"], cov)
        for key, want in case["expect"].items():
            if got.get(key) != want:
                err(f"golden {case['id']}: {key}: expected {want!r}, got {got.get(key)!r}")
        for key in ("message", "notice"):
            ref = case["expect"].get(key)
            if ref and ref not in cov["messages"]:
                err(f"golden {case['id']}: {key} {ref!r} not in coverage.messages")
    outcomes = {c["expect"].get("outcome") for c in country["golden_cases"]}
    for o in cov["order"]:
        if o not in outcomes:
            err(f"no golden case produces outcome {o}")
    used = set()
    for c in country["golden_cases"]:
        used |= set(c["input"].get("signals") or [])
    for s in cov["defect_signals"]:
        if s not in used:
            warn(f"no golden case uses defect signal {s}")
    if not any("ask" in c["expect"] for c in country["golden_cases"]):
        err("no golden case expects the app to ask")
    if not any(c["expect"].get("assumed") is True for c in country["golden_cases"]):
        err("no golden case covers an assumed warranty")


# ---------------------------------------------------------------- country checks
def check_country(c):
    schema_check(c, S_COUNTRY, "country.yaml")
    src_ids = [s["id"] for s in c["sources"]]
    if len(src_ids) != len(set(src_ids)):
        err("duplicate source ids")
    rule_ids = [r["id"] for r in c["rules"]]
    if len(rule_ids) != len(set(rule_ids)):
        err("duplicate rule ids")
    kinds = {s["id"]: s["kind"] for s in c["sources"]}
    for r in c["rules"]:
        for s in r["sources"]:
            if s != "product_decision" and s not in kinds:
                err(f"rule {r['id']}: unknown source {s}")
        if r["verification"] == "primary_checked" and not any(kinds.get(s) == "primary" for s in r["sources"]):
            err(f"rule {r['id']}: primary_checked but no primary source")
        if r["verification"] == "product_decision" and "product_decision" not in r["sources"]:
            err(f"rule {r['id']}: product_decision rule should cite product_decision")
    for s in c["sources"]:
        used = any(s["id"] in r["sources"] for r in c["rules"])
        if not used:
            warn(f"source {s['id']} is not cited by any rule")

    pairs = []
    walk_pairs({k: v for k, v in c.items() if k not in ("sources", "rules", "golden_cases")}, "country", pairs)
    for path, p in pairs:
        check_pair(path, p)

    cov = c["coverage"]
    for o in cov["order"]:
        if o not in cov["outcomes"]:
            err(f"coverage.outcomes missing {o}")
        if o not in cov["messages"]:
            err(f"coverage.messages missing {o}")
    for key in ("limitation_passed", "assumed_warranty_notice", "forum_state", "forum_national"):
        if key not in cov["messages"]:
            err(f"coverage.messages missing {key}")
    slabs = cov["fee_slabs_inr"]
    if slabs[0]["fee"] != 0 or slabs[0]["up_to"] != 500000:
        err("fee table must start with Rs 5 lakh -> nil")
    bounds = [s["up_to"] for s in slabs[:-1]]
    if bounds != sorted(bounds) or len(set(bounds)) != len(bounds):
        err("fee slabs are not strictly increasing")
    fees = [s["fee"] for s in slabs]
    if fees != sorted(fees):
        err("fees decrease as value rises")
    if slabs[-1]["up_to"] is not None:
        err("last fee slab must be open-ended (up_to: null)")
    thr = cov["forum_thresholds_inr"]
    if not thr["district_max"] < thr["state_max"]:
        err("forum thresholds not ordered")
    if thr != {"district_max": 5000000, "state_max": 20000000}:
        warn("forum thresholds differ from G.S.R. 912(E) values (Rs 50 lakh, Rs 2 crore)")
    for key in cov["asks"]:
        if key not in ("unit_warranty_months", "fault_first_seen_months_ago"):
            warn(f"ask {key} is not known to the validator")

    ladder_ids = {x["template"] for x in c["routes"]["ladder"]}
    if cov["limitation_basis"] != "purchase_date":
        err("limitation_basis must be purchase_date (product decision, 10 Oct 2026)")
    notice = [x for x in c["routes"]["ladder"] if x["template"] == "notice_before_complaint"]
    if not notice or not notice[0].get("required_in_app") or notice[0].get("optional"):
        err("the notice step must be required_in_app (product decision), not optional")
    fm = c["routes"].get("filing_mode") or {}
    if set(fm.get("options", {})) != {"self", "advocate", "unsure"}:
        err("routes.filing_mode needs options self, advocate, unsure")
    ids_r = {r["id"] for r in c["rules"]}
    for need in ("limitation_counted_from_purchase", "notice_step_in_flow", "filing_mode_choice"):
        if need not in ids_r:
            err(f"rule {need} missing")
    for old in ("limitation_counted_from_fault_start", "notice_optional_but_useful"):
        if old in ids_r:
            err(f"old rule {old} still present")
    return ladder_ids


# ---------------------------------------------------------------- template checks
def check_templates(t, country, ladder_ids):
    schema_check(t, S_TEMPLATES, "templates.yaml")
    rules = {r["id"]: r for r in country["rules"]}
    catalog = t["field_catalog"]
    for name, f in catalog.items():
        if not DEVANAGARI.search(f.get("hi", "")):
            err(f"field_catalog.{name}: Hindi label missing or not Devanagari")
    ids = [x["id"] for x in t["templates"]]
    if len(ids) != len(set(ids)):
        err("duplicate template ids")
    used_fields = set()

    uploads = [b["upload"] for b in t["ejagriti_bundle"]]
    if uploads != EJAGRITI_UPLOADS:
        err(f"ejagriti_bundle uploads {uploads} != manual order {EJAGRITI_UPLOADS}")
    for b in t["ejagriti_bundle"]:
        if b["template"] and b["template"] not in ids:
            err(f"ejagriti_bundle: unknown template {b['template']}")
        if b["template"] is None and not b.get("note"):
            err(f"ejagriti_bundle: {b['upload']} has no template and no note")

    for outcome, spec in country["coverage"]["outcomes"].items():
        for ref in [spec.get("letter")] + list(spec.get("then") or []):
            if ref and ref not in ids:
                err(f"coverage.outcomes.{outcome}: unknown template {ref}")
    for ref in ladder_ids:
        if ref not in ids:
            err(f"routes.ladder: unknown template {ref}")
    form_fields = {f["field"] for f in country["routes"]["nch_form_fields"]}

    for tpl in t["templates"]:
        tid = tpl["id"]
        for r in tpl["rules"]:
            if r not in rules:
                err(f"{tid}: unknown rule {r}")
        for k in ("title", "note", "body"):
            check_pair(f"{tid}.{k}", tpl[k], parity=(k == "body"))
        slots = tpl.get("slots") or {}
        body_ph = set()
        for lang in ("en", "hi"):
            text = tpl["body"][lang]
            body_ph |= set(PH.findall(text))
            if LEFTOVER.search(text):
                err(f"{tid}.body.{lang}: leftover bracket or placeholder text: {LEFTOVER.search(text).group(0)!r}")
        for ph in body_ph:
            if ph not in catalog and ph not in slots:
                err(f"{tid}.body: placeholder {{{ph}}} not in field_catalog or slots")
        used_fields |= {p for p in body_ph if p in catalog}
        for sname, slot in slots.items():
            if sname not in body_ph:
                err(f"{tid}: slot {sname} is not used in the body")
            if sname in catalog:
                err(f"{tid}: slot {sname} shadows a field_catalog name")
            for okey, opt in slot["options"].items():
                path = f"{tid}.slots.{sname}.{okey}"
                check_pair(path, opt)
                for lang in ("en", "hi"):
                    ph = set(PH.findall(opt[lang]))
                    for p in ph:
                        if p not in catalog:
                            err(f"{path}.{lang}: placeholder {{{p}}} not in field_catalog")
                    used_fields |= ph
                    if LEFTOVER.search(opt[lang]):
                        err(f"{path}.{lang}: leftover bracket or placeholder text")
        # bracketed English for formal Hindi terms: once per template, after the first use
        hi_all = tpl["body"]["hi"] + " " + " ".join(o["hi"] for s in slots.values() for o in s["options"].values())
        for hi_term, en_stub in BRACKET_TERMS.items():
            if hi_term in hi_all and en_stub not in hi_all:
                err(f"{tid}: Hindi uses {hi_term} but never brackets the English ({en_stub}...)")
        for fm in tpl.get("form_map") or []:
            if fm["field"] not in form_fields:
                err(f"{tid}.form_map: {fm['field']} is not in routes.nch_form_fields")
            for p in fm.get("from") or []:
                if p != "body" and p not in catalog:
                    err(f"{tid}.form_map.{fm['field']}: {p} not in field_catalog")
                used_fields.add(p)
            if not fm.get("from") and not fm.get("choose"):
                err(f"{tid}.form_map.{fm['field']}: needs from or choose")
        if tid == "nch_grievance":
            missing = {f for f in form_fields if f not in {x["field"] for x in tpl.get("form_map") or []}}
            if missing:
                err(f"nch_grievance form_map misses form fields: {sorted(missing)}")
        if tid == "district_commission_complaint":
            if "limitation_line" not in slots or "within" not in slots["limitation_line"]["options"]:
                err("complaint must carry the limitation_line slot")
            for opt in slots["limitation_line"]["options"].values():
                if "cause_of_action_date" in opt["en"]:
                    err("complaint still uses the old single cause-of-action date")
            # relief clauses must appear in the reliefs_available rule text
            summary = rules["reliefs_available"]["summary"]
            for okey, opt in slots["relief_list"]["options"].items():
                m = re.search(r"\(([a-z])\)", opt.get("clause", ""))
                if not m or f"({m.group(1)})" not in summary:
                    err(f"relief {okey}: clause {opt.get('clause')} is not in rule reliefs_available")
            if slots["relief_list"]["options"]["remove_defect"].get("clause") != "39(1)(f)":
                err("defect removal must stay on s.39(1)(f); see rule reliefs_available")
            if "costs" not in slots["relief_list"]["options"]:
                err("complaint misses the costs relief (s.39(1)(m))")
            if "purchase" not in slots["limitation_line"]["options"]["within"]["en"]:
                err("complaint limitation_line must count from the date of purchase")
            if "notice_fact" not in slots:
                err("complaint misses the notice_fact slot")
            for need in ("fee_statement", "territorial_basis", "ground_defect", "ground_return", "ground_bill", "ground_deficiency"):
                if need not in slots:
                    err(f"complaint misses slot {need}")
        if tid == "brand_seller_letter":
            ro = slots.get("remedy_line", {}).get("options", {})
            if set(ro) != {"in_warranty", "ended_defect"}:
                err("brand_seller_letter needs two remedy variants: in_warranty and ended_defect")
            if "at no cost" in (ro.get("ended_defect", {}).get("en", "")):
                err("out-of-warranty remedy line must not claim a free repair")
            for need in ("imei_line", "installation_line", "registration_line", "warranty_line", "defect_origin_line"):
                if need not in slots:
                    err(f"brand_seller_letter misses slot {need}")
            if "service_request_no" not in PH.findall(tpl["body"]["en"]):
                err("brand_seller_letter misses the service request number")
        if tid == "plan_provider_claim":
            if set(slots.get("cover_line", {}).get("options", {})) != {"plan", "card"}:
                err("plan_provider_claim needs plan and card variants")

    for name in catalog:
        if name not in used_fields:
            warn(f"field_catalog.{name} is not used by any template")
    required_ids = {"brand_seller_letter", "plan_provider_claim", "nch_grievance", "notice_before_complaint",
                    "district_commission_complaint", "index", "synopsis_list_of_dates", "memo_of_parties", "affidavit"}
    if required_ids - set(ids):
        err(f"templates missing: {sorted(required_ids - set(ids))}")


def main():
    country, templates = load(COUNTRY), load(TEMPLATES)
    ladder_ids = check_country(country)
    check_templates(templates, country, ladder_ids)
    replay_golden(country)

    for who, d in (("country.yaml", country), ("templates.yaml", templates)):
        if d["pack"]["hindi_review"] == "pending":
            warn(f"{who}: Hindi review is pending; a native reader must review every hi string before release")
    counts = {}
    for r in country["rules"]:
        counts[r["verification"]] = counts.get(r["verification"], 0) + 1
    warn("rules by verification: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    for r in country["rules"]:
        if r["verification"] == "unverified":
            warn(f"unverified rule: {r['id']}")

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    n = len(country["golden_cases"])
    print(f"\n{len(country['rules'])} rules, {len(country['sources'])} sources, {len(templates['templates'])} templates, "
          f"{n} golden cases, {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
