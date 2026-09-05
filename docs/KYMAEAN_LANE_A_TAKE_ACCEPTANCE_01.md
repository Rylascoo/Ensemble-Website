# KYMAEAN LANE A — TAKE ACCEPTANCE 01

Status: LANE A BUILDABLE REFINEMENT / DESIGN EVIDENCE / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Date: 2026-09-05

## Purpose

Add the missing live-authority transition to the revived O0 product family without creating a new module:

```text
Candidate Performance
-> consequence review
-> terminal consequence package
-> Accept / Reject / Another Take
-> successful atomic commit only for Accepted
-> history + changed current state
```

The surface remains part of the live Production/Stage experience.

## Exact authority basis

The current deterministic spine requires these distinctions:

- CandidatePerformance is provisional Performer output.
- State Authority decides each proposed consequence as Approved / Rejected / RequiresReview.
- Hard deterministic rejection is unwaivable.
- Explicit creator/authorized review may approve or reject reviewable mutations.
- `Approved` means commit-eligible, not already true/effective.
- A Take may bind only after State Authority is terminal Complete with no RequiresReview decision.
- Take disposition is independent from consequence disposition.
- Accepted Take is selected for later commit; it is not yet history merely because it is Accepted.
- A successful atomic causal commit makes the exact Accepted Performance and every Approved consequence effective together.
- Rejected consequences remain non-effective provenance.
- Rejected / Alternate / failed-before-Take / Accepted-but-failed-commit material remains non-effective.
- Successful commit consumes the current opportunity; rejected/request-another material does not silently become opportunity history.

ODR-19 still leaves final product acceptance modes open. This prototype therefore tests one **Review-oriented** creator surface without freezing Autopilot / Review / Strict Creator or equivalent modes.

## Surface thesis

> **Review consequence, not prose.**

The creator sees the exact candidate Performance in the living Stage, visibly marked:

> `CANDIDATE · NOT HISTORY`

The adjacent review surface answers:

> **What would change if this Take becomes history?**

It does not ask the creator to edit/model-score the Performance or expose engine diagnostics by default.

## Consequence presentation

The prototype demonstrates three distinct cases:

1. **Policy-approved consequence** — already terminal Approved, but still non-effective.
2. **Explicit-review consequence** — cannot proceed to a Take until the creator resolves it.
3. **Explicitly rejected consequence** — may remain provenance while an otherwise valid Performance can still become an Accepted Take.

The UI must never imply that a proposed consequence is true merely because it appears in review.

A reviewable consequence uses human-facing semantic language while retaining exact underlying authority. No confidence meters, numeric psychology, model rationale, provider identity or hidden reasoning are shown.

## Take actions

### Accept Take

Available only after every consequence decision is terminal.

Before commit, the candidate remains visually non-history.

A success confirmation may appear only after the atomic commit succeeds. The successful state changes the Performance marker to:

> `ACCEPTED · HISTORY`

and no longer presents the consumed opportunity as current.

### Reject Take

The Performance and all proposed consequences remain non-effective. Rejection is application/creator authority, not a fictional event inside the Production.

The existing opportunity remains effective unless later product authority establishes another transition.

### Another Take

User-facing action proposal:

> keep the current candidate out of history and request another Performance.

This prototype deliberately does **not** equate the button automatically with `E0TakeDisposition.Alternate`; final rehearsal/branch/alternate-retention UX remains open. The engine's Alternate disposition and the creator phrase `Another Take` may later map together, but that is a separate product decision.

## O0 reintegration

The prototype preserves O0 lineage through:

- dark restrained Stage;
- cast-first composition;
- Character-specific accent ancestry;
- current-opportunity cue;
- readable recent Performance;
- restrained creator controls;
- serif Performance language + quiet monospaced authority labels.

Later design laws correct O0 by keeping provider identity absent, separating opportunity from identity, making proposed-vs-effective authority explicit, and treating consequence review as progressive context rather than a permanent dashboard.

## Accessibility / semantics

- Candidate / history / rejected meaning is textual, not color-only.
- Current Opportunity has explicit text.
- Character identity remains named; color is redundant decoration only.
- Controls have visible keyboard focus.
- reduced-motion media query removes animation/transition dependence.
- no real WinUI/screen-reader/high-contrast validation is claimed.

## Rendered states

`prototypes/lane-a/take-acceptance-01.html` supports:

- Needs review;
- Ready for Take decision;
- Committed;
- Rejected;
- Another Take requested.

Prototype content is explicitly non-canon.

## Recursive audit corrections

1. Initial review render accidentally hid the consequence list because shared-state CSS classes conflicted; corrected and re-rendered.
2. Initial committed state still labeled the Performance `Candidate · not history`; corrected to accepted history.
3. Initial committed state still labeled Wren as Current Opportunity; corrected because successful commit consumes it.
4. Relationship example originally used `observation` language that could overstate epistemic authority; corrected to refer to the admitted/withheld claim instead.
5. Explicitly rejecting the relationship consequence now reduces the accepted-consequence count instead of leaving a false `3 approved` summary.

Final rendered pass: **no material authority contradiction found within this prototype scope.**

## Next design implication

The Stage now has a coherent authority bridge from provisional Performance to causal history.

The next refinement should connect the successful committed state into the revived O0 Archive / changed-present loop, without inventing the next Current Opportunity transition before the application architecture authorizes it.