# Covered — product pack specification

A product pack is everything Covered knows about one kind of appliance, written as data in one folder. No code. One owner per pack. The app, the voice agent and the tests all read the same file, so when the pack is right, the whole product is right for that appliance.

This spec goes with three files in `packs/`:

- `schema/pack.schema.json` — the machine-checked shape of a pack
- `validate.py` — the checker CI runs on every pull request
- `products/_example/pack.yaml` — a complete, valid example (a split air conditioner) to copy

## 1. Where a pack lives

```
packs/
  products/
    <pack-id>/
      pack.yaml          the pack (required)
      images/            optional step photos referenced from the pack
      NOTES.md           optional: sources, open questions, what you could not verify
```

`<pack-id>` is lower case with hyphens, e.g. `split-ac`, `front-load-washer`. It never changes once merged.

## 2. What goes in a pack, top to bottom

| Field | What it is | Rules |
|---|---|---|
| `schema_version` | always `1` | bump only when this spec changes |
| `id` | the folder name | lower case, hyphens |
| `version` | `major.minor.patch` | patch for wording, minor for new cards or symptoms, major if the symptom ids change |
| `owner` | GitHub handle of the person responsible | reviews of this pack go to them |
| `display_name` | what the user sees | English required, Hindi strongly expected |
| `aliases` | other names people use, including Hinglish and Hindi | used to match what the user says |
| `identification` | how the app recognises the appliance | see 3 |
| `error_codes` | code → symptom, per brand | optional; every entry names its source |
| `symptoms` | 3–8 things the user can pick from | each points to one fix card |
| `fix_cards` | the self-fix instructions | see 4 |
| `escalate_when` | when to stop and hand over, and where | see 5 |
| `warranty_hints` | typical cover for this appliance type in India | the country pack decides; this is a hint |
| `golden_cases` | at least 10 test conversations | CI runs them; see 6 |

Every piece of user-facing text is an object with `en` and `hi` keys. English is required so the validator can check it; Hindi is what most users will hear, so a pack without Hindi is not done.

## 3. Identification

`nameplate_fields` lists what to read off the label: `brand` and `model` are always required; add what helps (capacity, star rating, serial). `where_to_look` tells the user, in plain words, where the sticker is. `brands` lists the brands the pack has actually been checked against; the app treats others as "probably similar, less certain".

## 4. Fix cards — the heart of the pack

A fix card is one thing to try, written for a person standing in front of the appliance with a phone in one hand.

- **One card, one attempt, under 30 minutes.** If it is longer, split it.
- **Steps are spoken aloud.** Write each step as one short sentence a voice can read: what to do, where, and what they should see. No sub-steps, no "if/then" inside a step; make a `check` instead.
- **A `check` is a yes/no question** the agent asks after a step ("Are the filters grey with dust?"). The app branches on it.
- **`safety_stop: true` steps come first in the card** and must carry a `stop_if`. The agent reads the stop condition slowly and waits for confirmation. Use it whenever the step involves electricity, gas, refrigerant, water near electrics, heights, or anything sharp or hot.
- **Never instruct the user to** open a sealed unit, touch wiring or terminals, bypass a safety switch, handle refrigerant or gas, or work on a live appliance. If the honest fix needs that, the card's only step is the safety line and `if_not_fixed: escalate`.
- `if_not_fixed` is one of `escalate` (go to who-pays), `try_next_card` (name it in `next_card`), or `let_go` (cheap item, not worth repairing). Most cards escalate.
- `parts` with a typical price in rupees helps the "is it worth it" conversation later; leave it out rather than guess.
- `source` says where the steps come from: a manual (with page), a brand support page, or "team member's own experience, verified on model X". Steps from memory with no source are fine for a first draft but must be marked in `NOTES.md` as unverified.

Write the English first, then the Hindi. Hindi should read like a neighbour talking, not a translated manual; keep the English words people actually use (filter, switch, remote, mode).

## 5. Escalation

`escalate_when` is a short list of conditions and where they lead:

- `emergency_stop` — sparks, smoke, burning smell, gas smell, water on electrics, anyone hurt. The agent stops the flow immediately. **Every pack must have one of these.**
- `brand_service` — the normal route when the self-fix fails; the country pack turns this into warranty / protection plan / rights / own cost.
- `technician` — a local repairer rather than the brand (older appliances, out-of-warranty cases).
- `replace` — repair clearly not worth it.

The optional `say` is the sentence the agent uses; keep it to two sentences and no promises.

## 6. Golden cases — how a pack proves it works

Ten or more small conversations, each saying what the user says and what the app must do. They are the pack's tests: CI replays them against the stubbed flow and fails the pull request if any expectation changes.

Cover at least: two phrasings per common symptom (one Hinglish), one error code, one safety stop, one case that gets fixed, one that escalates, and three with a `purchase_age` and the coverage you expect from the India country pack. If a case fails because the country pack is wrong, raise it with that pack's owner rather than bending your expectation.

## 7. Definition of done for a pack

A pack card on the board moves to Done when all of these hold:

1. `python packs/validate.py packs/products/<id>/pack.yaml` prints `OK`.
2. Every symptom has a card, every card has a source or an entry in `NOTES.md`, every pack has an `emergency_stop`.
3. Hindi present for every user-facing string.
4. Ten golden cases pass in CI.
5. Someone other than the owner has read the fix cards aloud, in Hindi, to someone who has not seen them, and that person could follow them.
6. Pull request reviewed and merged.

## 8. How to start a new pack in ten minutes

1. Copy `packs/products/_example` to `packs/products/<your-id>`, change `id`, `version: 0.1.0`, `owner`.
2. Write the 3–8 symptoms first; they decide everything else. Use the breakdown-situations list from the scoring workbook.
3. Write one fix card per symptom, English only, one sentence per step. Mark safety stops.
4. Run the validator; fix what it names.
5. Add the Hindi. Add ten golden cases. Run the validator again.
6. Open a pull request titled `pack: <id> v0.1.0`; CI validates and runs the cases.

If you only get to step 4, open the pull request anyway as a draft; a validated English-only pack is a useful half, and the Hindi can be a second card.

## 9. What the app does with the pack (so you know why fields exist)

Identify reads `nameplate_fields` and `brands`. Read shows `symptoms` as big buttons and matches `phrases` and `aliases` against what the user says; `error_codes` jump straight to a symptom. Fix reads the card step by step, asking each `check`, pausing at every `safety_stop`. Verify asks "did it work" and follows `if_not_fixed`. Cover hands `escalate_when` plus the user's purchase age to the country pack. Act drafts the claim with the identified brand and model. Golden cases drive all of this in CI without a real user.
