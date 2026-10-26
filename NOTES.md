# NOTES: whirlpool-top-load-washer

Sources, per-card routing data and open items for `pack.yaml`. Shared facts, prevention list and open tasks are in `products/Whirlpool/WHIRLPOOL-WASHERS-README.md`.

Source document: "Covered — Whirlpool India Washing Machine Fault Reference", dated 24 Oct 2026 (`Downloads/Covered — Whirlpool India Washing Machine Fault Reference.md`).

## Models covered (fully automatic top-load)

"Popular" means repeatedly featured on Indian retailer and price-aggregator lists in 2026, not audited sales. The rating-plate photo selects the pack.

| Series | Example models seen in 2026 listings | Indicative price (₹) | Display / codes |
|---|---|---|---|
| Whitemagic | Elite 7 kg (31684); Premier GenX 7 kg; Royal GenX 6.5 / 7 kg; Classic GenX 6.5 kg | 16,965 (Premier GenX 7 kg) | Digital display; letter codes or LED blink patterns by model. Older models use LED blinks. |
| Stainwash | Stainwash Pro 7.5 kg | 20,890 | Digital display |
| 360° Bloomwash / BW Pro | BW Pro 10 kg (31593); 360 Bloomwash Pro 10 kg (31688); 360 BW Pro INV H8 8.5 kg; Bloomwash Ultra 6.5 kg | not in source | Digital display; inverter motor on Pro models |
| Magic Clean GenX | Magic Clean 7.0 GenX (31585) | not in source | Digital display |

Recommended demo model: Whitemagic Elite 7 kg or a 360° Bloomwash Pro. Live demo cases are the lid and child lock card (`lid_and_child_lock`) and the unbalance card (`balance_and_spin`): both deterministic, safe, fixed in under a minute.

Model-specific points the doc supports (the schema has no per-model field, so they live here and in `aliases`):

| Model or series | What differs |
|---|---|
| Older Whitemagic (e.g. LSE805 manual) | Lid opened during wash, rinse or spin triggers a timed beep and cycle LEDs flashing at 1 Hz. Entered as the "LED blink 1 Hz with beep" code. |
| 360° Bloomwash / BW Pro | Inverter motor on Pro models. A 2024 Bloom Wash Pro owner reported the machine stopping on every program, with noise, within a month of purchase (Voxya). Feeds the `stops_or_error_code` and `grinding_noise` paths. |
| BW Pro 10 kg (31593) | Warranty: 36 months product, 10 years motor (Croma). Longer than the pack's 24-month hint, so always read the warranty card. |
| All fully automatic top-loads | Digital display, so the code table applies. Exact display text may differ from the global Whirlpool site. |

## Fault-to-symptom map (doc fault table rows)

| Doc # | Fault | Symptom id | Card |
|---|---|---|---|
| 1 | Won't drain | `not_draining` | `drain_check` |
| 2 | Not filling / slow fill | `not_filling` | `fill_check` |
| 3 | Won't start / lid error | `lid_or_wont_start` | `lid_and_child_lock` |
| 4, 5 | Vibration / unbalance; not spinning | `shaking_or_not_spinning` | `balance_and_spin` |
| 7 | Grinding or roaring in spin | `grinding_noise` | `noise_check` |
| 6, 11 | Stops mid-cycle / frozen / dead; no power | `stops_or_error_code` | `power_and_code_reset` |
| 8, 9 | Leaking; excess suds | `leak_or_suds` | `leak_and_suds_check` |
| 10 | Bad smell / black specks | `smell_or_specks` | `tub_clean` |

The schema allows 8 symptoms, so the doc's 11 faults are merged where the fix overlaps. Rows 6 and 7 are the rights-path rows in the doc: the user cards end in `escalate`, and the claim letters are the downstream Act step.

## Card routing data (the schema has no fields for these, so they are also in each card's `source`)

| Card | Tier | failing_part_if_unresolved |
|---|---|---|
| drain_check | Self | drain pump |
| fill_check | Assisted (hose at the machine) | inlet valve |
| lid_and_child_lock | Self | lid lock |
| balance_and_spin | Self (load), Assisted (feet) | suspension or drum |
| noise_check | Self | bearing (service, no DIY) |
| power_and_code_reset | Self | control board (PCB) |
| leak_and_suds_check | Assisted | hose or valve |
| tub_clean | Self | none (`let_go`) |

The doc gives no `chargeable_if_technician` data for Whirlpool, so it is not invented here. Evidence to capture on every technician exit: photo of the display code, rating plate, invoice and installation record, and any damage photos.

## Rights moments (from the doc, for the Act step)

1. **Bearing versus motor** (`noise_check`, golden g09). Owners argue a 10-year motor warranty should cover bearings and seals; bearing repairs after the 2-year comprehensive period were refused (consumercomplaints.in). Use the `ended_defect` letter.
2. **Repeat PCB failure inside warranty** (`power_and_code_reset`, golden g10). A third failure supports a replacement or refund remedy line, not another repair. One owner replaced the PCB three times in a year.
3. **Installation date versus purchase date as warranty start.** The authorised engineer installs, so the installation record matters. Hence `purchase_date` asks for both dates.

Voltage-damage claims will be contested under "site conditions" exclusions, so cards ask about a stabiliser before any PCB verdict.

## Left out on purpose

- **India top-load display text.** The codes are verified on Whirlpool's global help site only. Each carries "pending India manual check" in `source`. Download the manuals for Whitemagic Elite and 360° Bloomwash Pro from whirlpoolindia.com and verify every code, then remove the marker.
- **Helpline numbers.** Toll-free 1800-208-1800 comes from a secondary blog (DigiRake), and helpdeskindia@whirlpool.com appears only on a Croma listing. Neither is in any `say` line. Confirm on whirlpoolindia.com first, then add to a verified-contacts list.
- **Panel, PCB, motor, bearing and inlet-valve work, any burning smell.** These are the doc's hard stops. They appear only as safety stops and `escalate` routes.
- **Fault frequency.** The doc ranks faults by an ordinal estimate, not measured counts; no public dataset gives Whirlpool fault counts for India. Symptom order follows that estimate.

## Unverified lines

1. **Lint filter location on every top-load model.** `drain_check` and `noise_check` say "see your manual".
2. **Child-lock key combination per model.** `lid_and_child_lock` says "see your manual".
3. **Inlet hose position and mesh cleaning per model** (`fill_check`). The doc lists it as the best DIY fix; model positions are not verified.
4. **Tub Clean cycle name per model** (`tub_clean`). The card says "if your model has one". `time_minutes` is 30 because the cycle runs unattended; hands-on time is a few minutes.
5. Do not tilt or move a loaded machine; wait for the drum to stop before opening the lid (standard practice, unverified).
6. Rating plate on the back of the machine.
7. `LF`, `Lo FL`, `F8 E1`, `drn`, `F9 E1`, `OL` come from Mr. Appliance, a US third-party site. `CL` comes from NoBroker (India, third-party). `F7 E1`, `Sud` and `Sd` come from Whirlpool's front-load help page, so their top-load use is pending the manual check.

## Warranty hint basis

`typical_months: 24` and the 60-month motor figure are the low end of the doc's pattern, "2 years comprehensive plus 5–10 years on the motor" (Bajaj Finserv). The doc says the pack must read warranty from the card or brand site and never assume a default, so these are hints only. Exclusions seen in a listing: outer cabinet and plastic parts, site conditions outside recommended operating conditions, removed or altered serial number.

## Other open points

- Hindi was drafted by the pack author's assistant and has not been read aloud to a native speaker (definition of done item 5).
- `expect_coverage` values assume the India country pack (`country-pack-in-v0.3.0`), which is not in this folder. Two are judgement calls: g09 (bearing after 2.5 years, `statutory_rights`, based on the doc's dispute route) and g10 (repeat PCB inside warranty, `brand_warranty`, with the remedy line handled in the claim letter). Raise any mismatch with the country pack owner.
- `owner: "@swatirai"` is reused from the LG packs; confirm the handle.
