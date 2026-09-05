# KYMAEAN LANE A — TAKE ACCEPTANCE 01

Status: LANE A BUILDABLE REFINEMENT / DESIGN EVIDENCE / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Date: 2026-09-05

## Purpose

Add the missing live-authority transition inside the revived O0 Stage:

```text
Candidate Performance
-> consequence review
-> terminal consequence package
-> Accept / Reject / Another Take
-> successful atomic commit only for Accepted
-> history + changed current state
```

## Authority contract

- Candidate Performance is provisional and must read as **not history**.
- State Authority decides consequences as Approved / Rejected / RequiresReview.
- Hard rejection is unwaivable; explicit review may resolve reviewable consequences.
- Approved means commit-eligible, not already true.
- A Take exists only after consequence review is terminal.
- Take disposition and consequence disposition are independent.
- Acceptance alone is not history; successful atomic commit makes the exact Accepted Performance plus every Approved consequence effective together.
- Rejected consequences remain non-effective provenance.
- Rejected / Another Take material remains non-effective; successful commit consumes the current opportunity.

ODR-19 remains open. This tests a Review-oriented surface without freezing final acceptance modes.

## Surface thesis

> **Review consequence, not prose.**

The exact candidate remains visible in the living Stage as `CANDIDATE · NOT HISTORY`. The adjacent surface answers **What would change if this becomes history?** rather than asking the creator to rewrite, score, or inspect model reasoning.

Consequence rows demonstrate: already-terminal Approved; explicit-review required; and explicitly Rejected while the Performance can still be accepted. Human-facing wording must never imply a proposal is already true.

## Actions

**Accept Take** — disabled until every consequence is terminal. Success UI appears only after atomic commit succeeds, then the Performance becomes `ACCEPTED · HISTORY` and the consumed opportunity is no longer shown as current.

**Reject Take** — Performance and proposed consequences remain non-effective; rejection is creator/application authority, not fiction.

**Another Take** — keeps the candidate out of history and requests another Performance. The prototype deliberately does not equate this UI phrase with `E0TakeDisposition.Alternate`; branch/rehearsal retention remains open.

## O0 refinement

Preserved: dark restrained Stage, cast-first composition, Character accents, current-opportunity cue, readable recent Performance, restrained controls, serif Performance text and quiet authority labels.

Corrected from O0: no provider-as-identity metadata; opportunity separated from identity; proposed/effective authority explicit; consequence review appears progressively rather than as permanent dashboard chrome.

## Semantic/accessibility requirements

Candidate/history/rejected meaning is textual, not color-only. Character identity and Current Opportunity are explicitly named. Keyboard focus is visible; reduced-motion removes transition dependence. No WinUI, screen-reader, forced-colors or device validation is claimed.

## Executable evidence

`prototypes/lane-a/take-acceptance-01.html` contains five states: Needs Review, Ready, Committed, Rejected, Another Take. Prototype story content is non-canon.

## Audit corrections

The iterative render audit corrected: hidden consequence rows; committed Performance still labeled candidate; stale Current Opportunity after commit; relationship wording that overclaimed observation; and approved-count drift after rejecting a consequence.

Final bounded result: **no material authority contradiction found within prototype scope.**

## Next implication

Connect successful commit into O0 Archive / changed-present causality without inventing a next Current Opportunity transition before application authority defines it.
