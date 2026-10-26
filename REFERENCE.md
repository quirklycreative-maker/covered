# Covered: Samsung India Washing Machine Pack Reference

**Version:** 1.0 (final input for the product pack YAML)
**As of:** 24 Oct 2026
**Market:** India (`market: in`)
**Brand:** Samsung

This file consolidates the fault research, the popular-model analysis, and the verification work. It also includes the corrections that came from reading Samsung India's warranty page directly.

It is written to be converted into the product pack YAML. Field names in backticks follow the product-pack spec and the India country pack. Match them to `pack.schema.json` before running the validator.

---

## 0. What changed versus the earlier drafts

Read this section before reusing any earlier text.

| Topic | Earlier draft said | Final position | Source |
|---|---|---|---|
| Comprehensive warranty | Unverified | 24 months for semi-automatic, top-load and front-load machines, counted from the purchase date | [Samsung India warranty page](https://www.samsung.com/in/support/warranty/) |
| Motor warranty | "20 years" vs "10 years", unresolved | Depends on purchase date (see section 6.2). Parts only. | Same page |
| Voltage damage | "No published exclusion found" | **Excluded.** Abnormal voltage and lightning are listed exclusions for home appliances. | Same page |
| Hoses and wiring | Hose "excluded" only when chewed | **Never covered.** Cable, wiring, piping and consumables are outside warranty, even within the 24 months. | Same page |
| Rodent damage | "Excluded per warranty card" | **Unconfirmed for washing machines.** The rats clause on the website sits under mobiles and notebooks only. The card itself has not been read. | Same page; one consumer complaint |
| Item 9 | Misread as "error code 200" | Means coding 200 consumer complaints into the fault taxonomy. There is no Samsung error code 200. | — |

---

## 1. Scope and method

### 1.1 Purpose

This reference is the source content for the Samsung washing-machine product pack. It covers:

- the most common faults, ranked by frequency;
- the best DIY fix for each fault, and the related error codes;
- popular Samsung India models;
- the safety layer, warranty hints and golden cases.

### 1.2 How the frequency ranking was built

There is no public dataset that ranks Samsung India faults by frequency. Samsung does not publish its service-ticket mix, and the National Consumer Helpline reports complaints by sector, not by fault.

The ranking is triangulated from four signals:

| Signal | What it contributes |
|---|---|
| Samsung's "frequently displayed" code list | Which code families users see most often: 4C/4E, 5C/5E, door, Ub/UE ([Samsung](https://www.samsung.com/ie/support/home-appliances/check-out-the-information-codes-on-my-washing-machine/)) |
| India market mix | Weighting: top-load is 67.85% of units and fully automatic is 54.65% (2025) ([Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/india-washing-machine-market)) |
| Indian complaint records | Which faults turn into service tickets and disputes (Voxya, consumercomplaints.in, Samsung Community) |
| India operating conditions | Voltage swings, low tank pressure, hard water, rodents |

### 1.3 Confidence

- **List membership:** well supported.
- **Order within each tier:** judgement, not measured counts.
- **Card 12 (semi-automatic):** not yet sourced.
- **Pitch rule:** do not quote any fault-frequency number until item 9 in section 9 is done.

### 1.4 Pack conventions applied in the fix cards

- Safety steps come first in a card.
- Steps contain no if/then logic.
- Any question for the user sits in a `check`.
- Every card closes with an escalation route and a coverage note.
- Every user-facing string needs `hi`. The Hindi strings in this file are drafts and still need expert review.

---

## 2. Popular Samsung India models

Samsung publishes no unit sales by model. The list below is the set of models that Indian retailers feature as top sellers or top picks in 2026 ([The News Minute / Bajaj Finance](https://www.thenewsminute.com/partner/samsung-washing-machines-in-2026-which-model-is-worth-buying-for-your-home), [Croma top-load](https://www.croma.com/unboxed/best-top-load-washing-machines-in-india-2026-smart-and-efficient-picks), [Croma overall](https://www.croma.com/unboxed/best-washing-machines-in-india-2026-top-picks-for-every-home)).

| Model | Type | Capacity | Fault-relevant features | Card set |
|---|---|---|---|---|
| WT75B3200RR | Semi-automatic | 7.5 kg | No display and no codes; Magic Filter; twin tub with a spin-lid interlock | Card 12, plus cards 2, 9 and 11 |
| WA65A4002VS | Top-load, entry | 6.5 kg | LED code display; Magic Filter inside the drum; no front drain filter | Top-load cards 1-11 |
| WA70BG4441YY | Top-load, EcoBubble | 7 kg | EcoBubble pre-foams the detergent, so suds and dosing matter more | Top-load cards; card 6 weighted up |
| WA80F08B3BTL | Top-load, AI and Wi-Fi | 8 kg | Inverter motor; AI VRT+ vibration control; SmartThings connected | Top-load cards + SmartThings diagnostics |
| WW70R22EK0X | Front-load, entry | 7 kg | Front drain filter and emergency hose; door lock; heater | Front-load cards 1-11 |
| WW90DG5U24ASTL | Front-load, AI | 9 kg | AI wash; motor-warranty claim moment | Front-load cards + card 8 coverage |
| WW90DG6U24ABTL | Front-load, AI and Wi-Fi | 9 kg | SmartThings connected | Front-load cards + SmartThings diagnostics |

### 2.1 Identify step: model prefix

Retailer listings consistently show this prefix pattern:

- **WA** = fully automatic top-load
- **WW** = fully automatic front-load
- **WT** = semi-automatic
- India-market units carry a **/TL** suffix

This is supported by Cashify, Bajaj Finserv, Croma, Amazon.in and Flipkart. It is not a published Samsung rule, and one IndiaMART listing contradicts it. Confirm it on 3 to 5 models in the samsung.com/in catalogue before the pack routes on it.

### 2.2 What the machine type changes

**Drain filter location**
- Front-load: a front filter behind a hatch. There is a hot-water scald risk.
- Top-load and semi-automatic: the Magic Filter inside the drum, plus the drain hose.

**Door lock**
- Front-load: the door locks during the cycle and under Child Lock.
- Top-load: the lid usually does not lock. Opening it under Child Lock starts a forced drain.

**Direct fault reading**
- Wi-Fi models: SmartThings offers a diagnostic mode ([Samsung UK](https://www.samsung.com/uk/support/skp/faq/1108987)). The app can ask the user to open SmartThings instead of photographing a blinking display.
- Status: not yet tested on an Indian unit.

---

## 3. Fault ranking

### 3.1 Tier A: frequent events, usually self-fixable

| Rank | `fault_id` | Fault | Samsung codes | Typical India cause | Route |
|---|---|---|---|---|---|
| 1 | `no_fill` | Water not filling | 4C, 4E, nF, E1 | Tap off; low pressure from the overhead tank; inlet mesh choked with sediment | Guided fix |
| 2 | `no_drain` | Not draining | 5C, 5E, nd, SE, E2 | Hose raised or kinked; Magic Filter or front filter clogged | Guided fix |
| 3 | `unbalance` | Unbalanced load, won't spin | UE, Ub, UB, Ur | Single heavy item; machine not level; transit fittings left in | Guided fix |
| 4 | `door_lid` | Door or lid error | dC, dE, dE1, LO, FL, dL | Lid not fully shut; clothing caught | Guided fix |
| 5 | `child_lock` | Buttons locked (not a fault) | CL, lock icon | Child Lock on | Guided fix, voice and caregiver mode |
| 6 | `leak_suds` | Leak, overflow, excess suds | LC, LE, OC, Sud | Loose hose; too much or wrong detergent | Guided fix; internal leak goes to service |

### 3.2 Tier B: service and complaint faults, money at stake

| Rank | `fault_id` | Fault | Signal | Why it matters | Route |
|---|---|---|---|---|---|
| 7 | `power_pcb` | Dead machine or mid-cycle stop | 9C1, 9C2, UC, AC/AE, blank display | Most expensive common repair; voltage is an exclusion | Emergency check, then cover check |
| 8 | `motor` | Motor failure, no spin | 3C, 3E; hum with no spin | Long motor part warranty that owners rarely know | Cover check, then claim |
| 9 | `wash_quality` | Poor wash, lint, stains, residue | No code | Highest emotional load in complaints | Guided checks, then a documented complaint |
| 10 | `rust_new` | Rust on a new machine | Visual | Replacement-grade claim in the first weeks | Seller first |
| 11 | `rodent` | Rodent damage | Visual; leads to rank 7 or 2 | Wiring and hoses are not covered | Out of pocket, plus prevention |
| 12 | `semi_auto` | Semi-automatic faults | No code | No display; physical interlocks | Card 12 (unsourced) |

### 3.3 Evidence for Tier B

Indian complaint records show each Tier B pattern:

- **Wash quality:** [stains persisting](https://voxya.com/consumer-complaints/-warranty-issues-in-washing-machine/20050) after repeated visits and a workshop inspection; [lint threads on clothes](https://voxya.com/consumer-complaints/samsung-wm-/123330) despite repeated troubleshooting.
- **Spin and lock:** a [spin problem](https://voxya.com/consumer-complaints/no-proper-service-and-response/23009) unresolved after several technician visits; a [water-locked machine](https://voxya.com/consumer-complaints/water-locked-issues-in-washing-machine/231969) unresolved for months.
- **Rust:** [rust on the drum](https://voxya.com/consumer-complaints/rusting-issue-in-brand-new-washing-machine/211348) of a brand-new machine.
- **Control board:** a [board replaced twice](https://nl.ifixit.com/Answers/History/659297) without a fix, with voltage blamed.
- **Rodents:** a buyer reports the [card excludes rodent damage](https://www.consumercomplaints.in/samsung-india-rat-panel-not-installed-in-the-newly-purchased-samsung-washing-machine-may-cause-damage-not-covered-under-warranty-c2379741). This is hearsay until the card is read.

---

## 4. Fault-by-model matrix

Weights are relative within each column:

- **High** = a primary card for that model
- **Med** = a regular card
- **Low** = rare or minor
- **—** = the fault does not apply

| Fault | Semi-auto WT75B3200RR | Top entry WA65A4002VS | Top EcoBubble WA70BG4441YY | Top AI/Wi-Fi WA80F08B3BTL | Front-load (WW70R22EK0X, WW90DG5U24ASTL, WW90DG6U24ABTL) |
|---|---|---|---|---|---|
| 1 No fill | Med (tap and hose only, no code) | High | High | High (app shows the code) | High |
| 2 No drain | High (drain knob, Magic Filter) | High | High | High | High (front filter, scald risk) |
| 3 Unbalance | High (spin tub, spin lid) | High | High | Med (AI VRT+ dampens vibration) | High |
| 4 Door/lid | Med (spin-lid interlock) | Med | Med | Med | High (door locks during the cycle) |
| 5 Child Lock | — | High | High | High | High (also locks the door) |
| 6 Leak/suds | Med | Med | High (EcoBubble) | Med | High (suds, door seal) |
| 7 PCB/power | Low (simple electrics) | High | High | High | High |
| 8 Motor | Med (capacitor/belt: hard stop) | Med | Med | Med | Med |
| 9 Wash quality | High | High | Med | Med | Med |
| 10 Rust | Low (plastic body) | Med | Med | Med | Med |
| 11 Rodents | High | High | High | High | High |

**Recommended demo:** fault 2 (5C) on WA65A4002VS.
- It is frequent, visible and safe to fix on stage.
- It branches to a claim when the code returns.

---

## 5. Fix cards

### Card 1 — `no_fill` — Water not filling

**`error_codes`:** 4C, 4E, nF, E1 (older models)
- `meaning.en`: The machine is not getting enough water.
- `meaning.hi` (draft): मशीन में पर्याप्त पानी नहीं आ रहा है।

**Hinglish intents:** "paani nahi bhar raha", "paani nahi aa raha machine mein"

**`steps`:**
1. `check`: Is the tap fully open, and is there water in the overhead tank?
2. Straighten the inlet hose so nothing presses on it.
3. Turn the tap off. Unscrew the hose from the back of the machine. Pull out the mesh filter with pliers, rinse it under the tap, and screw the hose back on. Samsung India advises cleaning this mesh twice a year ([Samsung India](https://www.samsung.com/in/support/home-appliances/how-to-resolve-4e-or-5e-codes-on-your-samsung-washing-machine)).
4. Switch off, wait, and restart. Tell the user that the buttons stay disabled for 3 minutes after a code appears.

**`escalate_when`:** the code returns with the tap open and the mesh clean. This points to the inlet valve or pressure sensor, so route to service.

**Coverage:**
- Inlet valve: covered within 24 months.
- Inlet hose: not covered (piping).

---

### Card 2 — `no_drain` — Not draining

**`error_codes`:** 5C, 5E, nd, SE, E2 (older models)
- `meaning.en`: The machine cannot drain the water.
- `meaning.hi` (draft): मशीन से पानी बाहर नहीं निकल रहा है।

**Hinglish intents:** "paani nahi nikal raha", "machine mein paani bhara hua hai"

**`safety_stop`** (front-load, first step):
- Water left after a hot cycle can scald. Let it cool for about an hour before opening the filter ([Samsung](https://www.samsung.com/ae_ar/support/home-appliances/how-to-fix-the-washing-machine-with-5c-error)).
- Unplug the machine. Put down a towel and a shallow tray.

**`steps`:**
1. Lower and straighten the drain hose, routed as the manual shows.
2. Detach the hose and flush it.
3. Top-load and semi-automatic: detach the Magic Filter inside the drum and wash it.
4. Front-load: pull out the emergency drain tube and drain into the tray. Turn the drain filter anti-clockwise to remove it, clean it, and refit it clockwise.
5. Run a drain or spin cycle to test.
6. `check`: Is the end of the hose chewed? If yes, route to card 11.

**`escalate_when`:** the filter and hose are clear but the code returns, or the pump hums with no water moving.

**Coverage:**
- Drain pump: covered within 24 months.
- Drain hose: not covered at any age (piping).

---

### Card 3 — `unbalance` — Unbalanced load, won't spin

**`error_codes`:** UE, Ub, UB, Ur (dc on some models)
- `meaning.en`: The load is unbalanced, so spinning has stopped for safety.
- `meaning.hi` (draft): कपड़े असंतुलित हैं, इसलिए सुरक्षा के लिए स्पिन रुक गया है।

**Hinglish intents:** "machine hil rahi hai", "spin nahi ho raha", "machine bahut awaaz kar rahi hai"

**`steps`:**
1. Pause the cycle. Wait for the lid to unlock. Untangle the load and spread it evenly.
2. Split a single heavy item, or add towels to balance it.
3. Level the machine and keep it at least 10 cm from each wall ([Samsung India](https://www.samsung.com/in/support/home-appliances/how-to-fix-ue-ub-error-in-samsung-washing-machine)).
4. `check` (new installation): have the shipping bolts or shipping base been removed?
5. Restart the spin.

**Calibration:**
- Front-load models have a calibration mode, but the button pair varies by model.
- No India manual has been read yet.
- Do not script it, and do not describe it on stage, until the demo model's manual is read.

**`escalate_when`:** UE shows on an empty drum. This points to the suspension or the sensor.

**Pending team decision (item 8):**
- Samsung India does not recommend a stand or trolley under the machine.
- Draft wording: do not recommend a stand or trolley; advise sealing base gaps and keeping the machine on a solid floor.

---

### Card 4 — `door_lid` — Door or lid error

**`error_codes`:** dC, dE, dE1, LO, FL, dL
- `meaning.en`: The door or lid is not closed or locked.
- `meaning.hi` (draft): दरवाज़ा या ढक्कन ठीक से बंद या लॉक नहीं है।

**Hinglish intents:** "dhakkan lock nahi ho raha", "darwaza nahi khul raha"

**`steps`:**
1. `check`: Is the Child Lock icon on? Yes routes to card 5.
2. Close the lid or door firmly.
3. `check`: Is clothing caught in the lid or the door seal?
4. Restart.
5. Front-load door won't open: wait for the cycle to end and the lock to release. Never force it.

**Code trap:** dC can mean three different things.
- A door error on some models.
- An unbalanced load on others ([Samsung](https://www.samsung.com/us/support/troubleshoot/TSG10000997/)).
- Child Lock on, when it blinks together with CL.

**`escalate_when`:** the latch is broken or the lid is cracked.
- In the first weeks, treat it as delivery damage and go to the seller.
- Lids and glass are cosmetic, plastic or glass parts, which are excluded from warranty.

---

### Card 5 — `child_lock` — Buttons locked (not a fault)

**`error_codes`:** CL, lock icon
- `meaning.en`: Child Lock is on. Only the power button works.
- `meaning.hi` (draft): चाइल्ड लॉक चालू है। केवल पावर बटन काम करेगा।

**Hinglish intents:** "koi button kaam nahi kar raha", "lock ka nishaan aa raha hai"

**`steps`:**
1. Find the two buttons marked with the lock icon. On most models these are the two buttons on the left, below the display ([Samsung](https://www.samsung.com/ca/support/home-appliances/samsung-washer-child-lock/)).
2. Hold both buttons for about 3 seconds.
   - On models with a temporary-off mode: hold once until the icon flashes, then hold again until it clears ([Samsung](https://www.samsung.com/sg/support/home-appliances/what-should-i-do-when-the-control-panel-buttons-are-not-operating-properly/)).
3. Say aloud: switching the machine off and on does not clear Child Lock.
4. Top-load: say aloud that opening the lid under Child Lock starts a forced drain. This is a safety feature, not a fault.

**`escalate_when`:** none.

**Product note:** this card is the strongest case for voice mode and caregiver mode. Confirm the button pair on the demo model's manual.

---

### Card 6 — `leak_suds` — Leak, overflow, excess suds

**`error_codes`:**
- LC / LE — `meaning.en`: Water leakage detected. `meaning.hi` (draft): पानी का रिसाव पाया गया।
- OC — `meaning.en`: Water has overflowed. `meaning.hi` (draft): पानी ज़रूरत से ज़्यादा भर गया है।
- Sud — `meaning.en`: Too many suds. `meaning.hi` (draft): बहुत ज़्यादा झाग बन गया है।

**Hinglish intents:** "neeche paani gir raha hai", "bahut jhaag ban raha hai"

**`safety_stop`** (first step):
- If there is water on the floor near a socket or extension board, do not touch the machine.
- Switch off at the wall switch or the MCB while standing on a dry spot.

**`steps`:**
1. Tighten both ends of the inlet hose. Re-seat the drain hose.
2. `check`: Was more detergent used than usual, or ordinary detergent in a front-loader?
3. For Sud: wait for the machine to clear the suds, run a rinse, and cut the next dose. EcoBubble models need a smaller dose.
4. For OC: turn the tap off and switch the machine off.

**`escalate_when`:** OC appears, or water comes from underneath while the hoses are dry.

**Coverage:**
- Waterlogging damage is an exclusion. A machine that stood in flood water is not covered.
- Hoses are not covered (piping).

---

### Card 7 — `power_pcb` — Dead machine or mid-cycle stop

**`error_codes`:**
- 9C1 / 9C2 / UC — `meaning.en`: Power supply or voltage problem. `meaning.hi` (draft): बिजली सप्लाई या वोल्टेज में समस्या।
- AC / AE — `meaning.en`: Internal communication error. `meaning.hi` (draft): मशीन के अंदर संचार में त्रुटि।
- Blank display: no code.

**Hinglish intents:** "machine beech mein band ho jaati hai", "machine on hi nahi ho rahi"

**`emergency_stop`** (first step):
- Triggers: burning smell, smoke, sparks, or a tingle from the body.
- Action: switch off at the MCB, do not touch the machine, and do not reset it.

**`steps`:**
1. Test the socket with another appliance.
2. Plug the machine straight into the wall, not into an extension board.
3. Unplug for 5 minutes, then plug back in.
4. `check`: Do the house lights dim or flicker when the machine stops? Record the answer.

**`escalate_when`:** every repeat.

**Coverage (corrected):**
- The control board is covered within 24 months for a defect.
- **Abnormal voltage and lightning are exclusions.** A written "voltage" finding is Samsung's ground to refuse ([Samsung India warranty](https://www.samsung.com/in/support/warranty/)).

**Claim prep:**
1. Collect the service request number at every visit.
2. Ask for the technician's finding in writing.
3. If the claim is refused on voltage, the user can argue a manufacturing defect under the Consumer Protection Act, especially for repeat failures with no voltage evidence at home. The country pack's `statutory_rights` path applies only with that defect argument; otherwise the verdict is `out_of_pocket`.

---

### Card 8 — `motor` — Motor failure, no spin

**`error_codes`:** 3C, 3E (and variants)
- `meaning.en`: Motor fault.
- `meaning.hi` (draft): मोटर में खराबी।

**Hinglish intents:** "drum ghoom nahi raha", "machine sirf ghoon-ghoon kar rahi hai"

**`safety_stop`:** a burning smell routes to the card 7 emergency stop.

**`steps`:**
1. Rule out card 3 first.
2. Reduce the load and restart once.

**`escalate_when`:** always.

**Coverage moment** ([Samsung India warranty](https://www.samsung.com/in/support/warranty/)):

| Purchase date | Digital Inverter motor | Induction motor |
|---|---|---|
| Before 1 Dec 2022 | 120 months | 60 months |
| 1 Dec 2022 to 31 Mar 2026 | 240 months, part only | 60 months, part only |
| From 1 Apr 2026 | 120 months, part only | 60 months, part only |

**App rules:**
- The app asks two things before any motor quote is paid:
  - Does the rating plate or box say "Digital Inverter"?
  - What is the purchase date on the invoice?
- After 24 months, the motor part is free but labour and the visit are paid.

---

### Card 9 — `wash_quality` — Poor wash, lint, stains, white residue

**`error_codes`:** none.

**Hinglish intents:** "kapde saaf nahi ho rahe", "kapdon par safed rui ya reshe aa rahe hain", "safed daag reh jaate hain"

**`steps`:**
1. Clean the Magic Filter. It also prevents card 2 ([Samsung India newsroom](https://news.samsung.com/in/samsung-launches-its-new-lineup-of-semi-automatic-washing-machines-keep-your-clothes-good-as-new-with-powerful-yet-gentle-washing/1000)).
2. Wash towels separately from dark clothes. Reduce the load. Raise the water level for large loads.
3. Dissolve powder detergent first, or switch to liquid. Undissolved powder leaves white marks in hard water.
4. Run Eco Tub Clean with the drum empty.
5. `check`: Has the problem lasted 3 washes with a clean filter and the correct dose?

**`escalate_when`:** the problem persists after step 5. Raise a documented complaint that logs every service request number. Repeat visits for one fault count as a defect signal in the country pack.

---

### Card 10 — `rust_new` — Rust on a new drum or cabinet

**`error_codes`:** none.

**Hinglish intents:** "nayi machine mein jung lag gaya"

**`steps`:**
1. `check`: Are coins, hairpins or metal zips leaving the marks? That is surface staining, not a defect.
2. Photograph the rust with the date visible. Stop using the machine.

**`escalate_when`:** rust is confirmed. Go to the seller first, inside the return window, then send a brand replacement letter.

**Coverage:**
- Samsung's terms require an inspection for transit damage, with a visiting charge.
- Transit damage is repaired at the user's cost.
- The letter must argue a manufacturing defect, not transit damage.

---

### Card 11 — `rodent` — Rodent damage

**`error_codes`:** none.

**Hinglish intents:** "chooha taar kaat gaya", "pipe kutra hua hai"

**`safety_stop`** (first step): chewed wiring means the machine must not be powered on.

**`steps`:**
1. Photograph the damage.
2. Prevention only:
   - Fit the rat mesh or pad if the model came with one.
   - Close any gaps in the base.
   - Samsung markets rodent protection on its semi-automatic range.

**Coverage (corrected):**
- **Verdict:** `out_of_pocket`.
- **Grounds:** cable, wiring and piping are outside warranty under Samsung's appliance terms ([Samsung India warranty](https://www.samsung.com/in/support/warranty/)).
- **Do not cite** a rodent exclusion until the washing-machine warranty card is read (item 3).

---

### Card 12 — `semi_auto` — Semi-automatic machines (WT series)

**Status:** unsourced. Check against a WT-series manual before shipping.

**`steps`:**
1. Close the spin lid fully. It is the safety interlock.
2. Spread the load evenly in the spin tub.
3. Turn the drain knob to drain.
4. Clean the Magic Filter.

**Hard stop:** capacitor, motor, belt and brake work. A capacitor can hold a charge.

---

## 6. Safety layer and warranty hints

### 6.1 Pack-level `escalate_when` routes to `emergency_stop`

Any of these triggers an emergency stop:

- burning smell, smoke or sparks;
- shock or tingle from the body;
- water near a live socket or extension board;
- chewed wiring;
- a child or pet inside the drum.

**Action:** switch off at the MCB and do not touch the machine.

**Hard limits for all cards:**
- No card instructs opening panels, testing wiring, or handling the capacitor or PCB.
- Front-load cards add a hot-water wait before any filter work.

### 6.2 `warranty_hints`

All hints are from the [Samsung India warranty page](https://www.samsung.com/in/support/warranty/), read 24 Oct 2026, unless noted.

```yaml
warranty_hints:
  comprehensive_months: 24          # semi-automatic, top-load and front-load
  starts_from: purchase             # "warranty applicable from customer purchase date"
  free_installation: once, within 6 months of purchase
  source: https://www.samsung.com/in/support/warranty/
  parts_with_longer_cover:
    - part: digital_inverter_motor
      rule: by purchase date (120 / 240 / 120 months, part only from 1 Dec 2022)
      source: https://www.samsung.com/in/support/warranty/
    - part: induction_motor
      months: 60   # part only from 1 Dec 2022
      source: https://www.samsung.com/in/support/warranty/
  not_covered_parts: [cosmetic, plastic, glass, bulbs, cable, wiring, piping, consumables]
  exclusions: [negligence_or_tampering, waterlogging_or_misuse, serial_removed, lightning, abnormal_voltage, transit_damage]
  rodent_exclusion: unverified       # on the website only for mobiles and notebooks; read the card
```

### 6.3 Other terms the app should know

| Term | Effect in the app | Source |
|---|---|---|
| Repaired parts carry only the unexpired warranty | Do not tell users a repair restarts the 24 months | Warranty page |
| Depreciation in lieu of repair when spares are unavailable | Tell users to ask for the depreciation offer in writing | Warranty page |
| Extended warranty must be registered within 2 weeks | Prompt registration at purchase (receipt-vault feature) | Warranty page |
| Exclusive jurisdiction of New Delhi courts | **Country-pack check:** confirm this does not bar a consumer from filing at the District Commission where they live | Warranty page |

---

## 7. Code map for the vision step

The C/E suffix depends on the model generation, so 4C and 4E are the same fault. The vision step maps every variant to one `fault_id`.

| Displayed | `fault_id` | Trap |
|---|---|---|
| 4C / 4E / nF / E1 | `no_fill` | Same fault across generations |
| 5C / 5E / nd / SE / E2 | `no_drain` | Same fault across generations |
| UE / Ub / UB / Ur | `unbalance` | — |
| dC | `door_lid`, `unbalance`, or `child_lock` | Resolve with machine type plus a lock-icon check |
| CL (+ blinking dC) | `child_lock` | Not a fault; power-cycling does not clear it |
| LC / LE | `leak_suds` | — |
| OC | `leak_suds` (overflow) | Safety step first |
| Sud | `leak_suds` (suds) | Weight higher on EcoBubble models |
| 3C / 3E | `motor` | Purchase-date motor tier |
| 9C1 / 9C2 / UC | `power_pcb` | Voltage exclusion |
| AC / AE | `power_pcb` | — |

---

## 8. Golden cases

All cases carry `market: in`. `expect_coverage` values follow the India country pack.

| ID | Model | User says or shows | `purchase_months` | Expected route | `expect_coverage` |
|---|---|---|---|---|---|
| s01 | WA65A4002VS | "Paani nahi bhar raha, 4C aa raha hai" | — | Card 1, fixed | — |
| s02 | WA65A4002VS | Photo of the panel showing 5C | — | Card 2, fixed | — |
| s03 | WW70R22EK0X | "5E aa raha hai, abhi garam paani wala wash kiya tha" | — | Card 2, hot-water safety step first, fixed | — |
| s04 | WA70BG4441YY | "Machine hil rahi hai, spin nahi ho raha" | — | Card 3, fixed | — |
| s05 | WW90DG5U24ASTL | "Darwaza nahi khul raha" + lock icon | — | Card 5; door unlocks once Child Lock is off | — |
| s06 | WA80F08B3BTL | "Koi button kaam nahi kar raha" | — | Card 5, fixed | — |
| s07 | WA70BG4441YY | "Bahut jhaag ban raha hai", Sud | — | Card 6, fixed with a lower dose | — |
| s08 | Any | "Jalne ki smell aa rahi hai" | — | Emergency stop | — |
| s09 | WW90DG6U24ABTL | 3C, Digital Inverter, motor quote received | 30 | Escalated; motor part free (240-month tier), labour paid | `brand_warranty` |
| s10 | WA65A4002VS | Stops mid-cycle, board replaced once | 14 | Escalated; collect service request numbers and the written finding | `brand_warranty` |
| s11 | WA65A4002VS | Board failed again; technician wrote "abnormal voltage" | 14 | Explain the voltage exclusion; offer the defect-complaint path | `out_of_pocket` |
| s12 | WA65A4002VS | Rust inside the drum | 0 | Seller replacement route | `brand_warranty` |
| s13 | WT75B3200RR | Hose and wires chewed | 8 | Safety stop; wiring and piping not covered | `out_of_pocket` |
| s14 | WA65A4002VS | Drain hose split, no rodents | 10 | Card 2; replacement hose paid by the user | `out_of_pocket` |

---

## 9. Open items before the YAML ships

| # | Item | Status | Owner | Next step |
|---|---|---|---|---|
| 1 | Warranty period and start date | **Done** | — | — |
| 2 | Motor warranty | **Done** | — | — |
| 3 | Rodent exclusion on the washing-machine card | Open | India-based team member | Photograph the card's exclusions page from a new unit |
| 4 | Calibration and Child Lock buttons | Open | Pack owner | Name the demo model (default WA65A4002VS); read its manual from samsung.com/in |
| 5 | Card 12, semi-automatic | Open | Pack owner | Read one WT-series manual from samsung.com/in |
| 6 | Model prefix rule | Supported, not closed | Pack owner | Check 3 to 5 models on samsung.com/in |
| 7 | SmartThings diagnostic | Open | Engineer + India-based member | Run it on a real Wi-Fi unit and screenshot the flow |
| 8 | Stand/trolley vs rodents | Drafted | Team | Approve or amend the sentence in card 3 |
| 9 | Measured frequency | Optional | Non-engineers; India-based member | Code 200 complaints against the 12 `fault_id`s; interview one service technician |

### Pitch rules until the open items close

- **Motor warranty:** say "10 years on the Digital Inverter motor, parts only, for purchases from 1 Apr 2026; 20 years applied to purchases from 1 Dec 2022 to 31 Mar 2026." Never imply that labour is covered.
- **Hoses and wiring:** say "not covered" (sourced).
- **Rodents:** say "reported" only, until the card is read.
- **Fault frequency:** quote no frequency number.
- **Calibration:** do not describe calibration until the demo model's manual is read.

---

## 10. Sources

**Samsung (opened)**
- [Samsung India warranty page](https://www.samsung.com/in/support/warranty/) (page dated 22 Oct 2026; read 24 Oct 2026)
- [Samsung India: 4C/4E and 5C/5E](https://www.samsung.com/in/support/home-appliances/how-to-resolve-4e-or-5e-codes-on-your-samsung-washing-machine)
- [Samsung India: UE/UB](https://www.samsung.com/in/support/home-appliances/how-to-fix-ue-ub-error-in-samsung-washing-machine)
- [Samsung India: UE/UB in Hindi](https://ushl.samsung.com/in/support/home-appliances/how-to-fix-ue-ub-error-in-samsung-washing-machine-hindi) (source for reviewing the Hindi strings)
- [Samsung Ireland: frequently displayed codes](https://www.samsung.com/ie/support/home-appliances/check-out-the-information-codes-on-my-washing-machine/)
- [Samsung US: error code list](https://www.samsung.com/us/support/troubleshoot/TSG10000997/)
- [Samsung Singapore: Child Lock](https://www.samsung.com/sg/support/home-appliances/what-should-i-do-when-the-control-panel-buttons-are-not-operating-properly/)
- [Samsung Canada: Child Lock](https://www.samsung.com/ca/support/home-appliances/samsung-washer-child-lock/)
- [Samsung UK: SmartThings diagnostic mode](https://www.samsung.com/uk/support/skp/faq/1108987)
- [Samsung UAE (Arabic): 5C and hot-water wait](https://www.samsung.com/ae_ar/support/home-appliances/how-to-fix-the-washing-machine-with-5c-error)
- [Samsung India newsroom: 20-year motor warranty](https://news.samsung.com/in/samsung-offers-20-year-warranty-on-its-digital-inverter-motor-for-washing-machines-stands-for-sustainability-through-durability)
- [Samsung India newsroom: semi-automatic range](https://news.samsung.com/in/samsung-launches-its-new-lineup-of-semi-automatic-washing-machines-keep-your-clothes-good-as-new-with-powerful-yet-gentle-washing/1000)

**Market and models**
- [Mordor Intelligence: India washing machine market](https://www.mordorintelligence.com/industry-reports/india-washing-machine-market)
- [The News Minute / Bajaj Finance: Samsung models 2026](https://www.thenewsminute.com/partner/samsung-washing-machines-in-2026-which-model-is-worth-buying-for-your-home)
- [Croma: best top-load 2026](https://www.croma.com/unboxed/best-top-load-washing-machines-in-india-2026-smart-and-efficient-picks)
- [Croma: best washing machines 2026](https://www.croma.com/unboxed/best-washing-machines-in-india-2026-top-picks-for-every-home)
- [NoBroker: Samsung error codes (India service guide)](https://www.nobroker.in/appliance-services/guides/samsung-washing-machine-error-codes/)

**Complaints and forums**
- [Voxya: rust on a new machine](https://voxya.com/consumer-complaints/rusting-issue-in-brand-new-washing-machine/211348)
- [Voxya: wash quality](https://voxya.com/consumer-complaints/-warranty-issues-in-washing-machine/20050)
- [Voxya: spin problem](https://voxya.com/consumer-complaints/no-proper-service-and-response/23009)
- [Voxya: water locked](https://voxya.com/consumer-complaints/water-locked-issues-in-washing-machine/231969)
- [consumercomplaints.in: rat pad and warranty](https://www.consumercomplaints.in/samsung-india-rat-panel-not-installed-in-the-newly-purchased-samsung-washing-machine-may-cause-damage-not-covered-under-warranty-c2379741)
- [iFixit: board replaced twice](https://nl.ifixit.com/Answers/History/659297)
