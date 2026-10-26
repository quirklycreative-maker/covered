# LG washing machines (India): Covered product packs

Three product packs that turn the "Covered — LG India Washing Machine Fault Reference" doc into data the Covered app, voice agent and tests can read. They follow `PACK-SPEC` (the root `README.md`) and `schema/pack.schema.json`, and all three pass `validate.py`. Since 25 Oct 2026 they have also been checked against LG India's owner's manuals, which are linked in `lg-manuals.yaml`.

Owner: `@swatirai` (a guess, confirm the handle). Status: v0.1.0, draft for review. Hindi not yet read aloud to a native speaker; technician review of the DIY tiers not done (section 6).

## 1. What is in this delivery

```
products/LG/
  LG-WASHERS-README.md          this file
  LG-QUERY-PART-COVER.md        English and Hindi drafts of the written query to LG (task 1), not yet sent
  lg-manuals.yaml               links to the LG India owner's manuals, with sha256 (a reference index, not a pack)
  lg-front-load-washer/
    pack.yaml                   the pack: FHB1207Z2M, FHB1207Z2W, FHP1209Z5M
    NOTES.md                    sources, routing data, what the manuals settled, what is still unverified
  lg-top-load-washer/
    pack.yaml                   the pack: T70VBMB1Z, T80VBMB4Z, THD08SJM, THD09SWM
    NOTES.md
  lg-semi-auto-washer/
    pack.yaml                   the pack: P7020NGAZ, P1155SKAZ
    NOTES.md
```

| File | Purpose | Who reads it |
|---|---|---|
| `pack.yaml` (x3) | Everything Covered knows about that LG family: how to identify it, error codes, symptoms, safe DIY fix cards, when to escalate, warranty hints, test cases. Written in English and Hindi. | The app, the voice agent, CI, the RAG corpus build |
| `NOTES.md` (x3) | The things the schema cannot hold: the model table, per-card tier, chargeable and failing-part data, what the manuals settled, what was left out and why, every unverified line. | Reviewers, whoever converts to the country pack or RAG corpus |
| `lg-manuals.yaml` | Where each model's owner's manual is: LG India support page, PDF link, online manual link, page count, file size, date, sha256. | The app (to link or fetch the source manual), reviewers |
| `LG-QUERY-PART-COVER.md` | Drafts of the written query to LG about the part-cover table. | Whoever sends it |
| `LG-WASHERS-README.md` | This guide. | Anyone picking the work up |

The root `README.md` (spec), `schema/`, `validate.py` and `products/_example/` are unchanged.

### Layout note

The packs sit at `products/LG/<pack-id>/pack.yaml`, the same brand-folder layout the Whirlpool packs use (`products/Whirlpool/...`). The spec and `validate.py` expect `products/<id>/pack.yaml`, so the validator's default glob does not find nested packs. Pass explicit paths when validating (section 5). If the loader or CI uses the same default glob, either update it to `products/*/*/pack.yaml` or move the three folders up to `products/`. Nothing inside the packs depends on the folder depth.

## 2. Why three packs and not one

The schema has no model or family field, allows at most 8 symptoms per pack, and maps each symptom to exactly one fix card. The same code means different things per family: `dE` is a front-load door code, `dL` is the top-load lid code, and `AE` is a leak on the FHP1209Z5M front-load but a clutch error on top-loads. The fix differs too (a front-load drain filter is floor-level work for a family member, a top-load drain fix is a hose height). One pack per family keeps every code and every card tied to the right machine without changing the shared schema.

## 3. Which pack for which model

| Pack id | Models | Family |
|---|---|---|
| `lg-front-load-washer` | FHB1207Z2M, FHB1207Z2W (7 kg), FHP1209Z5M (9 kg, AI Direct Drive, ThinQ) | Front-load |
| `lg-top-load-washer` | T70VBMB1Z (7 kg), T80VBMB4Z (8 kg) Smart Inverter; THD08SJM / THD09SWM AI Direct Drive | Fully automatic top-load |
| `lg-semi-auto-washer` | P7020NGAZ (7 kg), P1155SKAZ (11 kg) | Semi-automatic |

The app picks the pack from the model number on the rating plate (`nameplate_fields.model`) or from the aliases. Each `NOTES.md` lists its models with key tech and Amazon India figures.

## 4. What is inside each pack.yaml

| Section | Front-load | Top-load | Semi-auto | What it does |
|---|---|---|---|---|
| `identification` | yes | yes | yes | Where the rating plate is, which fields to read (brand, model, capacity, serial, purchase date) |
| `error_codes` | 34 entries | 27 entries | none | Code to symptom, with the source on each. Semi-auto has none because its manual has no error-code table |
| `symptoms` | 8 | 8 | 6 | The big buttons the user picks, with English, Hindi and Hinglish phrases |
| `fix_cards` | 9 | 9 | 6 | Step-by-step safe fixes, one sentence per step, yes/no checks, safety stops first |
| `escalate_when` | 6 | 5 | 6 | When to stop and where to go: emergency stop, LG service, local technician |
| `warranty_hints` | 24 months, motor 120 months (parts only, labour extra) | 24 months, inverter motor 120 months | 24 months, wash motor 60 months | A hint for the India country pack, not the final answer |
| `golden_cases` | 15 | 15 | 13 | Test conversations CI replays |

Hindi is present on all 422 user-facing text objects (174, 160 and 88), checked by script. That says nothing about quality.

### How to read a code's `source`

- A line citing an owner's manual section and marked `VERIFIED` was read in the LG India manual on 25 Oct 2026.
- A code whose `source` says "not listed in the front-load owner's manuals" (or "top-load") comes from the source doc (LG help, LG Parts, third-party sites) and is not in the manual. Filter on that phrase if the app should show only manual-confirmed codes.
- A "standard practice" line is not in LG's text and has not been confirmed (section 6).

### Safety rules built into every card

- No panels, PCB, motor, wiring or gas. Never tilt or move a loaded machine (the manuals only describe tilting an empty machine, so this stays our rule).
- Anything with water, electricity or a spinning drum starts with a `safety_stop` step that carries a `stop_if`.
- Floor-level or water-handling work is marked "ask a family member" (Assisted tier). Technician cases end in `if_not_fixed: escalate`.
- Only LG-verified contacts appear: customer care 08069379999, WhatsApp 9711709999.

### Fix tiers, and where the extra fields live

The doc gives every fix a tier (Self, Assisted, Technician), `chargeable_if_technician` and `failing_part_if_unresolved`. The schema has no fields for them, so each card's `source` text carries them and each `NOTES.md` has the same data as a table. When the RAG corpus or country pack is built, read them from there.

## 5. How to use the files

### Validate

Requires Python 3 with `pyyaml` and `jsonschema` (`pip install pyyaml jsonschema`). From the `packs/` folder, pass explicit paths because the packs are nested one level deeper than the default glob:

```bash
python validate.py products/LG/lg-front-load-washer/pack.yaml products/LG/lg-top-load-washer/pack.yaml products/LG/lg-semi-auto-washer/pack.yaml
```

Expected output is `OK` for each file and exit code 0 (confirmed 25 Oct 2026). Running `python validate.py` with no arguments uses the glob `packs/products/*/pack.yaml`, which is relative to the folder you run it from and does not match nested packs, so it can print nothing and still exit 0. Do not read that as a pass.

On this Windows machine Python was installed to `C:\Users\Recruitment Officer\AppData\Local\Programs\Python\Python312\python.exe`; open a new terminal so `python` is found.

What the validator checks: schema shape, every symptom points to a real card, `try_next_card` names a real card, every `safety_stop` has a `stop_if`, every error code and golden case points to a real symptom and card, golden ids are unique, and the pack has at least one safety stop. It does not check Hindi quality, whether the DIY steps are correct, or whether golden cases behave as expected.

### Use in the app and the tests

- The app reads `nameplate_fields` and `brands` to identify the machine, shows `symptoms` as buttons, matches `phrases` and `aliases` against what the user says, and jumps from an `error_codes` entry straight to its symptom.
- The agent reads a fix card step by step, asks each `check`, and pauses at every `safety_stop`.
- CI replays `golden_cases`. The `expect_coverage` values assume the India country pack (`country-pack-in-v0.3.0`), which is not in this folder.

### Link the manuals in the app

`lg-manuals.yaml` has one entry per manual: `models`, `pack`, `support_page`, `pdf_url`, `online_manual_url`, `pdf_pages`, `pdf_bytes`, `page_date`, `sha256`.

- Link to `support_page` for users. It is the stable LG India page for the model, and LG moves the file behind it.
- Fetch `pdf_url` for the RAG build or an in-app viewer. Compare the `sha256` of what you get with the one recorded to see whether LG replaced the file; if it did, re-read the changed sections before trusting the `VERIFIED` lines.
- `online_manual_url` was read from LG's page but not opened, so treat it as unchecked.
- The PDFs are LG's copyright and are not in this repository. Seven were saved locally in `Downloads\lg-manuals\`; FHB1207Z2M and FHB1207Z2W share one identical file, and T70VBMB1Z and T80VBMB4Z share another, as do P7020NGAZ and P1155SKAZ.
- The semi-auto manual is a two-page image booklet in English and Hindi for the whole P115*/P105*/P70* range; its Hindi troubleshooting and safety text can serve as a reference for our Hindi.

### Convert to the RAG corpus

Task 7 in the handoff. Read `pack.yaml` for symptoms, codes and cards, and `NOTES.md` for tier, chargeable and failing-part data. Do not do this until the open items in section 6 are closed, and mirror whatever schema Samsung and Whirlpool use so all brands stay consistent.

### Push to GitHub

This folder is not a git repository. In your clone of the Covered repo, copy the `LG` folder into `packs/products/` (it brings the three packs, `lg-manuals.yaml`, this README and the query file), then:

```bash
git checkout -b pack/lg-washers-v0.1.0
git add packs/products/LG
git commit -m "pack: lg-front-load-washer, lg-top-load-washer, lg-semi-auto-washer v0.1.0"
git push -u origin pack/lg-washers-v0.1.0
```

Open a pull request titled `pack: lg washers v0.1.0`, as a draft until the open items in section 6 are closed. Draft PR text is in `PR-lg-washers-v0.1.0.md` in the `packs/` folder (outside `products/`); paste it into GitHub and do not commit that file.

## 6. Open items

| # | Item | Status | Where it shows up |
|---|---|---|---|
| 1 | Scope of LG's 6- and 12-month part-cover list. Send the written query to LG (email form on lg.com/in/support/contact-us or WhatsApp 9711709999) with three closed questions. | Partly answered, still open. The top-load and semi-auto manuals print the warranty: 2 years on all parts except plastic parts, consumables, filters, knobs, hoses and top cover, plus a motor-only extension (top-load inverter motor 8 more years; semi-auto wash motor 3 more years). That supports the 2-year warranty governing parts. It is not LG's written reply to the three questions, and the front-load manuals have no warranty text (they point to the warranty card). | `warranty_hints` carries only the motor cover; the claim template should say "confirm with service centre". Fallback if no reply in 10 working days: the 2-year warranty governs and the part list applies to repaired parts only. |
| 2 | Which semi-auto models show error codes | Closed. The manual has no error-code table, only a four-row Troubleshooting Guide. | `lg-semi-auto-washer` has no `error_codes` |
| 3 | Lint filter location on T70VBMB1Z, T80VBMB4Z, THD models | Closed. T70/T80 manual p.33. It is a lint-removal part on some models only, not a cause of OE. | `drain_hose_and_filter` now covers the hose and its height only |
| 4 | AE meaning on India models | Closed. FHP1209Z5M manual: water leakage, call for service. Not listed in the FHB1207Z2W/Z2M manual. On top-loads AE is a clutch error. | `error_codes` in the front-load pack (mapped to `leak`) and the top-load pack (clutch) |
| 5 | Standard-practice claims and technician review | Partly closed. Verified: transit bolts on new front-loads, semi-auto spin lid, inlet mesh procedure, drain hose lowered, hot-water caution on draining, leave door open to dry (supervised). Still standard practice: never tilt or move a loaded machine. Still open: a technician to review the Self and Assisted tiers for elderly suitability; reviewer name: ______ | `source` of each card, each `NOTES.md` |
| 6 | Read the Hindi aloud to someone who has not seen it | Open | All `hi` strings |
| 7 | Update the Claude Doc with the results of items 1 to 5 | Open | Doc sections 7 and 10 |
| 8 | Confirm the `owner` handle and the FHB1207Z2M variant suffix (page title ABMQEIL, online manual AMBQEIL) | Open | `owner` in each pack; `lg-manuals.yaml` |

Not done by `validate.py` and not done anywhere else yet: running the golden cases. There is no CI harness or India country pack in this folder.

## 7. Reference facts used (all from LG India warranty terms, charges effective 17 Feb 2026, taxes extra)

| Item | Semi-auto | Top-load | Front-load |
|---|---|---|---|
| Product warranty | 2 years | 2 years | 2 years |
| Motor cover | Wash motor 5 years in total (2 + 3 additional), parts only, service charge payable | Inverter or direct-drive motor 10 years in total (2 + 8 additional) | Direct-drive motor 10 years, parts only, labour extra |
| Out-of-warranty in-home visit | ₹550 | ₹650 | ₹750 |

For all families:

- **Excluded from the 2-year cover:** lint filter, knobs, inlet and outlet hoses, top covers (the printed top-load and semi-auto warranty text also lists plastic parts and consumables).
- **Chargeable even in warranty:** cleaning a blocked filter, calls caused by a cut-off water supply, checks where the product is not defective.
- **Other exclusions:** voltage outside tolerance, surges and dips, insect or vermin entry, improper installation.
- **Repeat fault:** no service charge if the complaint repeats within 3 months of the service invoice.
- **Transit damage:** report within 15 days of purchase.
- **Spares unavailable:** LG's depreciation policy applies instead of repair.

### Prevention (the highest-value content, because the warranty will not pay for these)

| Risk | Prevention |
|---|---|
| Voltage surges | Stabiliser or surge protector; unplug in storms; frequent PF is the early signal |
| Rodents | Rat mesh at the base (third-party job, about ₹300) |
| Low water pressure | Check tank and booster pump before booking; IE is usually supply, not the machine |
| Hard water, wrong detergent | Correct detergent type and dose; monthly tub clean with anti-limescale powder |
| Humidity | Keep off wet floors, ventilate, wipe dry |

## 8. Sources

LG India owner's manuals (links in `lg-manuals.yaml`, read 25 Oct 2026), LG India (Error codes explained, dated 10/01/2026; Warranty information, charges effective 17 Feb 2026; Laundry range), LG help (washer error codes), LG Parts, BestAppliance (LG vs Samsung 2026, updated 30 Sep 2026), Croma, and corroboration from Bajaj Finserv, Bison KB, NoBroker and consumer complaint sites. Full list and per-code sources are in each `pack.yaml` and the source doc: https://claude.ai/artifact/61s6YQBaemFzpxF79TfhP7

No public dataset ranks LG faults by frequency in India. The symptom order reflects evidence-weighted judgement, not measured frequency.
