# PR description (paste into GitHub; do not commit this file)

**Title:** `pack: lg-front-load-washer, lg-top-load-washer, lg-semi-auto-washer v0.1.0`

**Open as: Draft pull request.** The items under "Not done" are open, and these packs give safety-related guidance to end users.

## What this adds

Three LG washing-machine product packs for India, one per family, built from the "Covered — LG India Washing Machine Fault Reference" doc (https://claude.ai/artifact/61s6YQBaemFzpxF79TfhP7) and checked against LG India's owner's manuals on 25 Oct 2026.

| Pack | Models | Symptoms | Fix cards | Error codes | Golden cases |
|---|---|---|---|---|---|
| `lg-front-load-washer` | FHB1207Z2M/Z2W, FHP1209Z5M | 8 | 9 | 34 | 15 |
| `lg-top-load-washer` | T70VBMB1Z, T80VBMB4Z, THD08SJM/THD09SWM | 8 | 9 | 27 | 15 |
| `lg-semi-auto-washer` | P7020NGAZ, P1155SKAZ | 6 | 6 | none (the manual has none) | 13 |

Plus, in `products/LG/`: a `NOTES.md` per pack, `LG-WASHERS-README.md` (guide to the files), `LG-QUERY-PART-COVER.md` (English and Hindi drafts of the written query to LG) and `lg-manuals.yaml` (links to each model's LG India owner's manual with sha256; a reference index, not a pack).

Why three packs: the schema has no model or family field, caps symptoms at 8 and maps each symptom to one card. Codes such as `dE`, `dL` and `AE` differ by family. No change to the schema or `validate.py`.

**Layout:** packs are under `products/LG/<pack-id>/`, like `products/Whirlpool/...`. `validate.py`'s default glob (`products/*/pack.yaml`) does not find nested packs, so validate with explicit paths (see README section 5), or update the glob.

The manual PDFs are LG's copyright and are not committed; `lg-manuals.yaml` links to them.

## Checked

- `python validate.py` prints `OK` for all three packs when run with explicit paths, exit code 0.
- Every user-facing string has English and Hindi (422 text objects, none missing, checked by script).
- No step tells the user to open a panel, touch wiring, use the emergency release, or tilt a machine. Safety stops come first in each card and carry `stop_if`.
- Only LG-verified contacts are used (08069379999, WhatsApp 9711709999).
- Verified against the LG India manuals (marked `VERIFIED` in each card's `source`): front-load OE/drain filter, inlet filter, transit bolts, tub clean, door and drain-hose cautions, codes OE, 1E, dE, dE1, dE2, dE4, PF, PE, FE, tE, LE, AE; top-load hose height, clean-inlet-mesh procedure, lint filter location, codes dE, dr, LE1, AE, OE, E3, 1E, vS, dL, PE, FE, tE, LE, tcL, and the printed warranty; semi-auto drain hose, spin lid, sock on axle, power and timer checks, installation clearances, and the printed warranty.
- Corrected during the manual check: the lint filter is not a cause of OE; AE is a clutch error on top-loads and a leak code on the FHP1209Z5M only; the manuals say "door", not "lid", on top-loads.

## Not done (why this is a draft)

1. LG's 6- and 12-month part-cover scope is only partly answered. The top-load and semi-auto manuals print the warranty (2 years on parts, with exclusions; motor-only extension), which supports the 2-year warranty governing parts. It is not LG's written reply, and the front-load manuals have no warranty text. The query is drafted, not sent. Kept out of `warranty_hints` apart from the motor cover.
2. Codes not found in the manuals stay in the packs from the source doc (front-load: CE, Sud, EE, Ed1 to Ed5, nE, OPn, CL and numeric aliases; top-load: PF, CE, Sud, Sd, FF, UB, 0E, E1). Each says so in its `source`.
3. "Never tilt or move a loaded machine" is standard practice; the manuals only describe tilting an empty machine. The spin-run caution (more than 3 consecutive spin cycles, semi-auto) was read from a small-print page image and is cited in `source` only.
4. No technician has reviewed the Self and Assisted tiers for elderly suitability; reviewer name: ______
5. Hindi has not been read aloud to a native speaker (definition of done item 5).
6. Golden cases have not been run in CI. `expect_coverage` assumes `country-pack-in-v0.3.0`.
7. `owner: "@swatirai"` was a guess; confirm the handle. The FHB1207Z2M variant suffix differs between LG's page title and its manual link.
8. `lg-manuals.yaml` `online_manual_url` values were read from LG's page but not opened.

## Reviewer

Please check Hindi wording, the tier of each card, the layout note above, and the items above before this leaves draft.
