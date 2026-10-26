# Whirlpool washing machines (India): Covered product packs

Three product packs that turn the "Covered — Whirlpool India Washing Machine Fault Reference" doc into data the Covered app, voice agent and tests can read. They follow the pack spec (the root `README.md`) and `schema/pack.schema.json`, and all three pass `validate.py`.

Owner: `@swatirai` (reused from the LG packs, please confirm). Status: v0.1.0, draft for review. Not yet merged, Hindi not yet read aloud to a native speaker, error codes pending the India manual check (section 6).

## 1. What is in this delivery

```
products/
  Whirlpool/
    WHIRLPOOL-WASHERS-README.md       this file
    whirlpool-semi-auto-washer/
      pack.yaml                       the pack: Superb Atom, Ace, Hydrowash / Magic Clean
      NOTES.md                        models, fault map, routing data, unverified lines
    whirlpool-top-load-washer/
      pack.yaml                       the pack: Whitemagic, Stainwash, 360° Bloomwash / BW Pro, Magic Clean GenX
      NOTES.md
    whirlpool-front-load-washer/
      pack.yaml                       the pack: Xpert Care, Fresh Care / XS / XO
      NOTES.md
PR-whirlpool-washers-v0.1.0.md        PR description (paste into GitHub; do not commit)
```

| File | Purpose | Who reads it |
|---|---|---|
| `pack.yaml` (x3) | Everything Covered knows about that Whirlpool family: how to identify it, error codes, symptoms, safe DIY fix cards, when to escalate, warranty hints, test cases. English and Hindi. | The app, the voice agent, CI, the RAG corpus build |
| `NOTES.md` (x3) | What the schema cannot hold: the model table, per-card tier and failing part, rights moments, what was left out and why, every unverified line. | Reviewers, whoever builds the country pack or RAG corpus |
| `WHIRLPOOL-WASHERS-README.md` | This guide. | Anyone picking the work up |
| `PR-whirlpool-washers-v0.1.0.md` | Ready-to-paste draft PR description. | You, when opening the pull request |

The root `README.md` (spec), `schema/`, `validate.py`, `products/_example/` and the LG packs are unchanged.

## 2. Why three packs and not one

The schema has no model or family field, allows at most 8 symptoms per pack, and maps each symptom to exactly one fix card. The doc itself says to key the pack by platform and model family, and the platforms differ:

- Semi-automatic: no display, no codes, symptom path only.
- Fully automatic top-load: digital display, letter codes, with an LED-blink fallback on older Whitemagic.
- Front-load: F-number codes that must come from the model manuals.

The same word means different things per platform (a door catch on a front-load, a lid lock on a top-load, a spin lid on a semi-auto), and the fixes differ. One pack per platform keeps every code and card tied to the right machine without changing the shared schema. This is the same split the LG delivery used.

## 3. Which pack for which model

The app picks the pack from the model number on the rating plate (`nameplate_fields.model`) or from the `aliases`, which list every series and model name below.

| Pack id | Series | Example models (2026 India listings) | Display / codes |
|---|---|---|---|
| `whirlpool-semi-auto-washer` | Superb Atom | Superb Atom 60I, 6 kg | none |
| | Ace | Ace XL 8.5 / 11 kg; Ace Supreme Pro 7 kg (30298); Ace Super Soak 8 kg | none |
| | Hydrowash / Magic Clean | Hydrowash Elite 9 kg (30312); Magic Clean 8.0 / 8.5 | none |
| `whirlpool-top-load-washer` | Whitemagic | Elite 7 kg (31684); Premier GenX 7 kg; Royal GenX 6.5 / 7 kg; Classic GenX 6.5 kg | digital; letter codes or LED blinks |
| | Stainwash | Stainwash Pro 7.5 kg | digital |
| | 360° Bloomwash / BW Pro | BW Pro 10 kg (31593); 360 Bloomwash Pro 10 kg (31688); 360 BW Pro INV H8 8.5 kg; Bloomwash Ultra 6.5 kg | digital; inverter motor on Pro |
| | Magic Clean GenX | Magic Clean 7.0 GenX (31585) | digital |
| `whirlpool-front-load-washer` | Xpert Care | 7 kg (33040, 33041); 9 kg (33049, 33027) | F-number codes |
| | Fresh Care / XS / XO | XS8014BYM52E 8 kg; XO9012BYM52E 9 kg; Fresh Care 6112 6 kg | F-number codes |

"Popular" means repeatedly featured on Indian retailer and price-aggregator lists in 2026, not audited sales. Prices, per-model warranty and the model-specific points are in each `NOTES.md`.

## 4. What is inside each pack.yaml

| Section | Semi-auto | Top-load | Front-load | What it does |
|---|---|---|---|---|
| `identification` | yes | yes | yes | Where the rating plate is; fields to read (brand, model, capacity, serial, purchase and installation date) |
| `error_codes` | none | 18 entries | 3 entries | Code to symptom, with the source URL on each. Front-load is thin on purpose (section 6) |
| `symptoms` | 8 | 8 | 8 | The big buttons the user picks, with English, Hindi and Hinglish phrases |
| `fix_cards` | 8 | 8 | 8 | Step-by-step safe fixes, one sentence per step, yes/no checks, safety stops first |
| `escalate_when` | 8 | 8 | 9 | When to stop and where to go: emergency stop, Whirlpool service, local technician, replace |
| `warranty_hints` | 24 months, motor 60 | 24 months, motor 60 | 24 months, motor 60 | A hint for the India country pack, not the final answer |
| `golden_cases` | 16 | 15 | 16 | Test conversations CI replays |

### The 11 faults from the doc, and where they went

| Doc # | Fault | Semi-auto | Top-load | Front-load |
|---|---|---|---|---|
| 1 | Won't drain | `drain_check` | `drain_check` | `drain_filter_clean` (pump filter, golden case 1) |
| 2 | Not filling | `fill_check` | `fill_check` | `fill_check` |
| 3 | Lid or door error | `power_check` | `lid_and_child_lock` | `door_and_child_lock` |
| 4 | Vibration / unbalance | `balance_and_noise` | `balance_and_spin` | `balance_and_transit` |
| 5 | Not spinning | `spin_check` | `balance_and_spin` | `balance_and_transit` |
| 6 | Stops / dead / PCB | `power_check` | `power_and_code_reset` | `power_and_code_reset` |
| 7 | Grinding / bearing | `balance_and_noise` | `noise_check` | `noise_check` |
| 8 | Leaking | `leak_check` | `leak_and_suds_check` | `leak_and_gasket_check` |
| 9 | Suds / residue | `suds_and_wash_quality` | `leak_and_suds_check` | `smell_and_suds` |
| 10 | Smell / specks | `tub_clean` | `tub_clean` | `smell_and_suds` |
| 11 | No power | `power_check` | `power_and_code_reset` | `power_and_code_reset` |

Faults are merged where the fix overlaps because of the 8-symptom cap. Row 3 on a semi-auto has no lid lock or child lock, so the start and power checks sit in `power_check`.

### Error codes: what is in and what is deliberately not

- **Top-load (18 entries):** Lid / LId, LdL, LdU, CL, the Whitemagic LED-blink fallback (1 Hz with a beep means the lid was opened), LF / Lo FL / F8 E1 (slow fill), drn / F9 E1 (not draining), Ofb / UL (unbalanced), OL (overloaded), Sud / Sd (suds), F7 E1 (motor speed sensing), and a generic `F# E#` entry with the official reset.
- **Front-load (3 entries):** Sud, Sd, F7 E1 from Whirlpool's front-load help page. India front-load F-codes (Xpert Care, Fresh Care) are **not** loaded from blogs: the doc found one India list giving F02 and F21 conflicting meanings on the same platform. They must come from the model manuals.
- **Semi-auto:** none.
- Every code carries its source URL. Codes verified only on Whirlpool's global site say "pending India manual check" in `source`.

### Reset procedures used in the cards

| Platform | Reset (from the doc) | Where it is |
|---|---|---|
| Fully automatic top-load | Start/Pause once to clear an F# E# code, then again to restart; unplug 5 minutes | `power_and_code_reset`, `lid_and_child_lock`, `balance_and_spin`, `fill_check` |
| Front-load | Pause or Cancel twice and Power once; if the code stays, unplug 5 minutes | `power_and_code_reset`, `door_and_child_lock`, `fill_check` |
| Semi-automatic | Timers to zero, off at the socket for 1 minute, restart | `power_check` |

One reset is a valid DIY step. A code that returns after it is a service case.

### Safety rules built into every card

- The doc's hard stops are never steps: opening any back or top panel; PCB, motor, bearing or inlet-valve work; any burning smell; draining a hot front-load before it cools. They appear only as safety stops and `escalate` routes.
- Anything with water, electricity or a spinning drum starts with a `safety_stop` step that carries a `stop_if`.
- Floor-level, hose and water-handling work is marked "ask a family member" or Assisted tier. Never tilt or move a loaded machine. On new front-loads the user is told to stop and ask the installer about transit bolts, not to remove them.
- No phone number or email appears anywhere in the packs, because the doc's only contacts are unconfirmed (see section 6).
- India-specific checks run first in the relevant cards: tap and overhead tank before the inlet valve, inlet mesh silt, stabiliser before any PCB verdict, gnaw marks on semi-autos, hand-wash detergent in automatics.

### Fix tiers, and where the extra fields live

Each card's `source` carries the tier (Self, Assisted) and `failing_part_if_unresolved`; each `NOTES.md` has the same data as a table. When the RAG corpus or country pack is built, read them from there. The doc has no `chargeable_if_technician` data for Whirlpool, so none is invented.

## 5. How to use the files

### Validate

Requires Python 3 with `pyyaml` and `jsonschema` (`pip install pyyaml jsonschema`). From the `packs/` folder:

```bash
python validate.py products/Whirlpool/whirlpool-semi-auto-washer/pack.yaml products/Whirlpool/whirlpool-top-load-washer/pack.yaml products/Whirlpool/whirlpool-front-load-washer/pack.yaml
```

Expected output is `OK` for each file and exit code 0. On this Windows machine Python is at `C:\Users\Recruitment Officer\AppData\Local\Programs\Python\Python312\python.exe`; open a new terminal so `python` is found.

What the validator checks: schema shape, every symptom points to a real card, `try_next_card` names a real card, every `safety_stop` has a `stop_if`, every error code and golden case points to a real symptom and card, golden ids are unique, and the pack has at least one safety stop. It does **not** check Hindi quality, whether the DIY steps are correct, whether a card exceeds 30 minutes, or whether golden cases behave as expected. The delivery was also checked with a separate script for: Hindi present on every user-facing string, at most 8 steps per card, safety stops first, no card over 30 minutes, no banned instruction in a step, no phone number, an `emergency_stop` route, every symptom has a golden case, and codes marked pending.

### Use in the app and the tests

- The app reads `nameplate_fields` and `brands` to identify the machine, shows `symptoms` as buttons, matches `phrases` and `aliases` against what the user says, and jumps from an `error_codes` entry straight to its symptom.
- The agent reads a fix card step by step, asks each `check`, and pauses at every `safety_stop`.
- CI replays `golden_cases`. The `expect_coverage` values assume the India country pack (`country-pack-in-v0.3.0`), which is not in this folder.
- The doc recommends a live demo of the lid / child-lock card and the unbalance card on a Whitemagic Elite or 360° Bloomwash Pro: both are deterministic, safe and fixed in under a minute.

### Push to GitHub

This folder is not a git repository yet. In your clone of the Covered repo, copy `products/Whirlpool/` into `packs/products/`, then:

```bash
git checkout -b pack/whirlpool-washers-v0.1.0
git add packs/products/Whirlpool
git commit -m "pack: whirlpool-semi-auto-washer, whirlpool-top-load-washer, whirlpool-front-load-washer v0.1.0"
git push -u origin pack/whirlpool-washers-v0.1.0
```

Open a pull request titled `pack: whirlpool washers v0.1.0`, as a draft until the open items in section 6 are closed. Paste `PR-whirlpool-washers-v0.1.0.md` as the description and do not commit it.

## 6. What is still open (do not ship to Demo Day without these)

| # | Item | Status | Where it shows up |
|---|---|---|---|
| 1 | Download the Whitemagic Elite, 360° Bloomwash Pro and Xpert Care manuals from whirlpoolindia.com and verify every error code against them | Open (task in the doc) | Every `error_codes` entry says "pending India manual check" |
| 2 | Pull the India front-load F-codes from the Xpert Care and Fresh Care manuals and add them | Open | `whirlpool-front-load-washer` has only Sud, Sd, F7 E1 |
| 3 | Confirm the Whirlpool helpline (1800-208-1800 is from a secondary blog; helpdeskindia@whirlpool.com is from a Croma listing) on whirlpoolindia.com, then add a verified-contacts list | Open | No contact appears in any `say` line |
| 4 | Lint filter place, child-lock key combination, inlet hose position, Tub Clean cycle name, and front-load filter cover and emergency hose place, per model | Open (needs the manuals) | Steps say "see your manual"; listed in each `NOTES.md` |
| 5 | Verify the standard-practice lines (no tilting a loaded machine, wait for the drum to stop, door-glass heat check, anticlockwise filter, transit bolts at the back), then have a technician review the Self and Assisted tiers for elderly suitability and record the reviewer's name | Open | Marked in each `NOTES.md` |
| 6 | Read the Hindi aloud, in Hindi, to someone who has not seen it | Open (definition of done item 5) | All `hi` strings |
| 7 | Run the golden cases in CI. `expect_coverage` values for g09 (bearing after 2.5 years) and g10 / g12 (repeat PCB failure) are judgement calls; raise any mismatch with the country pack owner | Open | `golden_cases` |
| 8 | Confirm `owner: "@swatirai"` | Open | `owner` in each pack |

## 7. Reference facts used (from the doc, per-model figures are listings, not warranty cards)

| Item | Detail |
|---|---|
| Typical warranty pattern | 2 years comprehensive plus 5 to 10 years on the motor (Bajaj Finserv). The pack must read it from the warranty card or brand site, never assume a default. |
| BW Pro 10 kg (31593) | 36 months product, 10 years motor (Croma) |
| Xpert Care 9 kg front-load | 5 years comprehensive, 10 years motor (Jidipi listing) |
| Fresh Care 6112 front-load | 2 years comprehensive, no motor figure (Flipkart) |
| 7 kg semi-automatic (rat protection) | 2 years, 5 years motor (IndiaMART listing) |
| Exclusions seen in one listing | Outer cabinet and plastic parts; site conditions outside recommended operating conditions; removed or altered serial number. Voltage-damage claims will be contested under "site conditions". |

### Rights moments (for the Act step)

1. **Bearing versus motor.** Owners argue a 10-year motor warranty should cover bearings and seals; bearing repairs after the 2-year comprehensive period were refused. Use the `ended_defect` letter.
2. **Repeat PCB failure inside warranty.** A third failure supports a replacement or refund remedy line, not another repair.
3. **Installation date versus purchase date** as warranty start. The authorised engineer installs, so the installation record matters; the packs ask for both dates.

### Prevention (the highest-value content, because the warranty may not pay for these)

| Risk | Prevention |
|---|---|
| Voltage fluctuation | Stabiliser; ask before any PCB verdict. A frozen display or repeated stops is the early signal. |
| Rodents (semi-automatics) | Inspect the base for chewed cables; a rat-protection model exists |
| Low pressure from overhead tanks | Check tank and tap before suspecting the inlet valve |
| Hard-water silt and scale | Clean the inlet mesh; run a descaler cycle |
| Hand-wash detergent in automatics | Use machine detergent in the dose on the pack |

## 8. Sources and what the evidence can and cannot say

Whirlpool Product Help (top-load HE, front-load and Lid error pages), the Whitemagic LSE805 service manual on ManualsLib, Mr. Appliance, NoBroker, Croma (BW Pro 31593 and the 2026 best-washers guide), MySmartPrice and PriceDekho price lists, BestPurifier, Bajaj Finserv, Flipkart, Jidipi, IndiaMART, DigiRake, and the consumercomplaints.in and Voxya complaint pages. The full list with URLs is in the source doc, and per-code sources are in each `pack.yaml`.

The fault ranking is an ordinal estimate, not a measured frequency. Whirlpool, the National Consumer Helpline and government surveys publish no fault counts by brand for India. Rank comes from how often a fault appears in India service guides and Whirlpool help pages, and how often it recurs in Indian complaint forums. The doc's definition of done asks for ten sourced faults; it documents eleven, and all eleven are covered.
