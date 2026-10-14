# Changelog: country pack India

## 0.3.0 (draft, 10 Oct 2026)

Decisions applied
- Limitation: two years counted from the date of purchase (was: from when the fault started). Rule `limitation_counted_from_purchase` replaces `limitation_counted_from_fault_start`. Over 24 months since purchase with no warranty and no plan now returns `out_of_pocket` with the `limitation_passed` message, with or without a defect signal. Exactly 24 months is still inside.
- Notice before complaint: now a required step in Covered's flow (`required_in_app`), never described as a legal duty. Rule `notice_step_in_flow` replaces `notice_optional_but_useful`. The complaint carries a `notice_fact` paragraph (Annexure A-6).
- Filing mode: new `routes.filing_mode` (self, advocate, unsure). The Vakalatnama row in the Index appears only for the advocate path. No Vakalatnama template.
- Right to Repair: portal home page read (primary). It searches by company or product name; model lookup is not confirmed. Rule `right_to_repair_portal` rewritten and now primary_checked for what it states.
- Rules `no_minimum_warranty`, `no_presumption_of_defect_at_delivery`, `no_notice_required_before_filing` reworded so the effect on the app is stated.

Golden cases: 24 (was 23). Changed: in08, in10 (boundary at exactly 24 months), in13 (no question, limitation passed), in21 (25 months since purchase). New: in24 (30 months, no signal).

Templates: limitation line counts from purchase; notice template is a flow step; complaint adds the notice paragraph; new field `notice_date`.

Validator: new engine order (warranty, plan, limitation from purchase, defect signal), checks for the notice step, filing mode and purchase-based limitation line.

Removed: NOTES.md (maintained by the team separately).

## 0.2.0 (draft, 10 Oct 2026)
Full rebuild after the Section A to E review: 9 templates, 23 golden cases, rebuilt validator, renderer, workflow.

## 0.1.0
Original draft (not in this archive).
