# PR description (paste into GitHub; do not commit this file)

**Title:** `pack: whirlpool-semi-auto-washer, whirlpool-top-load-washer, whirlpool-front-load-washer v0.1.0`

**Open as: Draft pull request.** Items 1 to 7 below are not done, and these packs give safety-related guidance to end users.

## What this adds

Three Whirlpool washing-machine product packs for India, one per platform, built from the "Covered — Whirlpool India Washing Machine Fault Reference" doc (24 Oct 2026).

| Pack | Series | Symptoms | Fix cards | Error codes | Golden cases |
|---|---|---|---|---|---|
| `whirlpool-semi-auto-washer` | Superb Atom, Ace, Hydrowash / Magic Clean | 8 | 8 | none (no display) | 16 |
| `whirlpool-top-load-washer` | Whitemagic, Stainwash, 360° Bloomwash / BW Pro, Magic Clean GenX | 8 | 8 | 18 | 15 |
| `whirlpool-front-load-washer` | Xpert Care, Fresh Care / XS / XO | 8 | 8 | 3 | 16 |

Plus a `NOTES.md` per pack and `products/Whirlpool/WHIRLPOOL-WASHERS-README.md` (guide to the files).

Why three packs: the schema has no model or family field, caps symptoms at 8 and maps each symptom to one card; the doc says to key the pack by platform. No change to the schema or `validate.py`.

## Checked

- `python validate.py` prints `OK` for all three packs, exit code 0. `_example` and the three LG packs still print `OK`.
- Every user-facing string has English and Hindi (script check).
- No card has more than 8 steps or more than 30 minutes; safety stops come first in each card and carry `stop_if`; every pack has an `emergency_stop` route; every symptom has a golden case.
- No step tells the user to open a panel, touch wiring, work on the PCB, motor or bearing, remove transit bolts, use the emergency door release, or tilt a machine. No phone number or email appears in any pack.
- All 11 faults from the doc are covered.

## Not done (why this is a draft)

1. Error codes are verified on Whirlpool's global help site only, and each says "pending India manual check". The Whitemagic Elite, 360° Bloomwash Pro and Xpert Care manuals still need to be checked.
2. India front-load F-codes are not loaded (the doc found conflicting meanings for F02 and F21 in one blog). The front-load pack has only Sud, Sd and F7 E1.
3. The Whirlpool helpline (1800-208-1800, from a secondary blog) is unconfirmed, so no contact is in any `say` line.
4. Per-model positions are not verified: lint filter, child-lock key combination, inlet hose, front-load filter cover and emergency hose, Tub Clean cycle name. Steps say "see your manual".
5. "Standard practice" safety lines are not checked against the manuals, and no technician has reviewed the Self and Assisted tiers for elderly suitability; reviewer name: ______
6. Hindi has not been read aloud to a native speaker (definition of done item 5).
7. Golden cases have not been run in CI. `expect_coverage` assumes `country-pack-in-v0.3.0`; g09 (bearing after 2.5 years) and g10 / g12 (repeat PCB failure) are judgement calls.
8. `owner: "@swatirai"` was reused from the LG packs; confirm the handle.

## Reviewer

Please check Hindi wording, the tier of each card, and the items above before this leaves draft.
