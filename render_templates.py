#!/usr/bin/env python3
"""Generate packs/countries/in/TEMPLATES.md from country.yaml and templates.yaml.

  python3 -I packs/render_templates.py            write TEMPLATES.md
  python3 -I packs/render_templates.py --check    exit 1 if TEMPLATES.md is stale
"""
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent / "countries" / "in"
OUT = HERE / "TEMPLATES.md"


def load(name):
    with open(HERE / name, encoding="utf-8") as f:
        return yaml.safe_load(f)


def render():
    c, t = load("country.yaml"), load("templates.yaml")
    src = {s["id"]: s for s in c["sources"]}
    rules = {r["id"]: r for r in c["rules"]}
    L = []
    a = L.append
    a(f"# Covered India claim templates, {t['pack']['version']} ({t['pack']['status']})\n")
    a("> Generated from `templates.yaml` and `country.yaml`. Do not edit by hand.")
    a("> This is information, not legal advice. Covered drafts the paper; the user decides whether to send or file it.")
    a(f"> Hindi review: **{t['pack']['hindi_review']}**. Every Hindi line needs a native reader before release.\n")

    a("## e-Jagriti upload set\n")
    a("| Upload | Template | Note |\n|---|---|---|")
    for b in t["ejagriti_bundle"]:
        note = b.get("assumption") or (b.get("note") or {}).get("en", "")
        a(f"| {b['upload']} | {('`' + b['template'] + '`') if b['template'] else 'none'} | {note} |")
    a("")

    for tpl in sorted(t["templates"], key=lambda x: x["order"]):
        a(f"## {tpl['order']}. {tpl['title']['en']}")
        a(f"*{tpl['title']['hi']}*\n")
        a(f"`{tpl['id']}`\n")
        a(f"**Note:** {tpl['note']['en']}\n")
        a(f"**Note (hi):** {tpl['note']['hi']}\n")
        a("**Legal basis (rule, verification, source):**\n")
        for rid in tpl["rules"]:
            r = rules[rid]
            links = ", ".join(f"[{src[s]['title'][:70]}]({src[s]['url']})" if s in src else s for s in r["sources"])
            a(f"- `{rid}` ({r['verification']}): {r['summary']} Source: {links}")
        a("")
        slots = tpl.get("slots") or {}
        if slots:
            a("**Slots** (the app drops empty slots and picks the option that fits):\n")
            for sname, slot in slots.items():
                a(f"- `{{{sname}}}`: {slot['when']}")
                for okey, o in slot["options"].items():
                    clause = f" [{o['clause']}]" if o.get("clause") else ""
                    a(f"  - `{okey}`{clause}: {o['en']}")
                    a(f"    - हिन्दी: {o['hi']}")
            a("")
        if tpl.get("form_map"):
            a("**NCH form map:**\n")
            a("| Form field | Required | Filled from |\n|---|---|---|")
            for fm in tpl["form_map"]:
                how = ", ".join(fm.get("from") or []) or fm.get("choose", "")
                if fm.get("note"):
                    how += f" ({fm['note']})"
                a(f"| {fm['field']} | {'yes' if fm['required'] else 'no'} | {how} |")
            a("")
        a("### English\n")
        a("```text\n" + tpl["body"]["en"].rstrip() + "\n```\n")
        a("### हिन्दी\n")
        a("```text\n" + tpl["body"]["hi"].rstrip() + "\n```\n")

    a("## Field catalog\n")
    a("| Field | English label | हिन्दी | Kind |\n|---|---|---|---|")
    for k, f in t["field_catalog"].items():
        a(f"| `{k}` | {f['en']} | {f['hi']} | {f['kind']} |")
    a("")
    return "\n".join(L)


if __name__ == "__main__":
    text = render()
    if "--check" in sys.argv:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != text:
            print("TEMPLATES.md is stale. Run: python3 -I packs/render_templates.py")
            sys.exit(1)
        print("TEMPLATES.md is current")
    else:
        OUT.write_text(text, encoding="utf-8")
        print(f"wrote {OUT}")
