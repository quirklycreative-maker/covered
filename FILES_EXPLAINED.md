# Country pack India v0.3.0: what each file is

Status: draft. Open items: native Hindi review of every Hindi string, and a lawyer's check of the section numbers against India Code. This is information, not legal advice.

## The three decisions this version applies
1. **Two years are counted from the date of purchase.** The Act counts from the day the cause of action arose, which can be later than purchase. Counting from purchase is the cautious reading: the app never promises more time than the Act gives. Cost: a user whose problem started late and was refused after month 24 is told the time may have run out. The message says a Commission can still hear a late complaint, but not to rely on it.
2. **The notice is a required step in Covered's flow.** It is not a legal duty. No law requiring it was found, and the app must never say it is.
3. **The app asks how the user will file: alone or through an advocate.** Alone: Covered prepares the papers. Advocate: the user hands the pack to the advocate, who supplies the Vakalatnama.

## Files

| File | What it is | Who uses it |
|---|---|---|
| `packs/countries/in/country.yaml` | The brain of the India pack. Sources (44), rules (48, each tied to a source and labelled primary_checked, secondary_only, unverified or product_decision), the who-pays order, the 24-month limit, forum limits, the 11-row fee table, every app message in English and Hindi, the warranty lookup steps, the intake flow, the route ladder, the filing-mode choice, the National Consumer Helpline form fields, contacts, and 24 golden cases. | Engineer builds the who-pays logic and screens from it. Country-pack owner edits it. |
| `packs/countries/in/templates.yaml` | The 9 papers, English and Hindi: brand/seller letter, plan or card claim, National Consumer Helpline grievance, notice, District Commission complaint, Index, Synopsis and List of Dates, Memo of Parties, notarised Affidavit. Also the field catalog (every blank the user fills) and the map to the e-Jagriti upload list. "Slots" are optional or alternative paragraphs the app picks. | Engineer fills the blanks and picks slots. Hindi reader reviews. |
| `packs/countries/in/TEMPLATES.md` | Readable copy of all templates with their legal basis. Generated; never edit by hand. | Anyone who wants to read the papers. Lawyer and Hindi reader review this one. |
| `packs/schema/country.schema.json` | The shape `country.yaml` must have. | Validator. |
| `packs/schema/templates.schema.json` | The shape `templates.yaml` must have. | Validator. |
| `packs/validate_country.py` | The gatekeeper. Checks the shape, that every rule cites a real source, that every Hindi line exists and carries the same blanks as the English, that no gendered Hindi verb pairs or leftover brackets remain, that the fee table and forum limits are sane, that the notice step, filing mode and purchase-based limitation are in place, and replays all 24 golden cases through the who-pays logic. Errors fail the build; warnings list open items. | CI and every contributor. |
| `packs/render_templates.py` | Builds `TEMPLATES.md`. `--check` fails if it is out of date. | CI. |
| `.github/workflows/packs.yml` | Runs the validator and the renderer check on every push or pull request that touches `packs/`. Must be copied to `.github/workflows/` at the repository root. | Country-pack owner, once. |
| `CHANGELOG.md` | What changed in each version. | Team. |
| `FILES_EXPLAINED.md` | This page. | Team. |

## How the who-pays logic reads (replayed by the validator)
1. Warranty running (counted from purchase or installation, as the brand's card says; longer part cover counts) and the damage is not excluded: **brand_warranty**.
2. Otherwise a plan, AMC, insurance or card extended warranty is active: **protection_plan**. A card counts only if the product was bought on it and the benefit is active. Purchase protection never counts.
3. Otherwise, more than 24 months since purchase: **out_of_pocket**, with the time-limit message.
4. Otherwise a defect signal is present (brand refused repair in warranty, same fault after repair, seller refused to take back defective goods): **statutory_rights**, "you may have a complaint". Forum and fee come from the price.
5. Otherwise: **out_of_pocket**, with the message that says what evidence to collect.

## Reading the three negative findings in the rules
- **No minimum warranty:** India has no legal minimum warranty, unlike the EU. The warranty is what the brand's card, site or the Right to Repair entry says, so the app must find it or ask.
- **No presumption of defect at delivery:** the EU presumes a defect that shows up in the first months was there at delivery. India does not; the consumer has to show the defect. This is why a product that merely fails after warranty, with no refusal and no repeat repair, is out_of_pocket and why the app asks for a written service-centre report. It appears in the rule list, golden cases in02 and in18, and the out_of_pocket message.
- **No notice required by law:** nothing found in the Act or rules. Covered still requires it as a step.

## Open for the team
- Hindi review (native reader) of all `hi` strings, then set `hindi_review: done` in both files.
- Lawyer or past complaint filer: tick section numbers against India Code; confirm purchase-date counting; confirm whether "Proforma" means the complaint in NCDRC proforma order.
- Engineer: warranty screen (source, start point, `assumed` banner), card questions, filing-mode screen, notice step with reply-period timer, Right to Repair lookup by company or product name followed by user confirmation of the model's terms.
- Decide the technician-report signal (not in the logic yet).
