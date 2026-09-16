<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website V2.2 — Apparent-Size Parity Study 01

Status: DIRECTOR CONFIRMED / B +3% THRESHOLD K SCALE SELECTED / PRODUCTION CANDIDATE AUDIT ACTIVE
Date: 2026-09-16
Baseline: `main@19780dd80a59ec87d7a6586e3dda99bbf0318f67`

## Reopened question

L-178 preserved a later website-lettering question: whether the visible Threshold K should read closer in apparent size to `YMÆAN` while preserving the exact historical K paths, O3 `YMÆAN`, B optical spacing, viewport centering, Stage, `COMING SOON` relationship, responsive/publication/accessibility behavior and no-analytics boundary.

This study changes only intact-group presentation scale/placement of Threshold K. It does not edit any K path, any `YMÆAN` path, spacing, stroke hierarchy, Stage bytes, crop law or production file.

## Deterministic comparison

Prototype: `prototypes/website-v2-2-letter-size-parity-study/index.html`.

A — current production control: Threshold K presentation scale `1.00×`.

B — optical parity candidate: Threshold K presentation scale `1.03×`, bottom anchored and horizontally center anchored to the control K.

C — upper-bound candidate: Threshold K presentation scale `1.05×`, using the same anchors.

All candidates retain the production B translations `Æ -3`, `A -3`, `N -4`. The exact frozen Stage is used at 2048×1199 wide, 1235×647 mini-wide and 1138×1354 tall.
## Measured geometry

At 2048×1199, control K renders 44.64×61.78 px while Y renders 53.75×60.82 px. The control K is therefore already about 1.6% taller mathematically, but materially narrower; the reopened issue is optical presence, not literal cap-height deficiency.

B renders K at 45.98×63.64 px: about 4.6% taller than Y while retaining the control baseline anchor. C renders 46.87×64.87 px: about 6.7% taller than Y. Relative results are invariant at mini-wide and tall because the study uses uniform SVG scaling.

Every candidate remains centered at exact viewport 50% with zero horizontal overflow. `YMÆAN`, status geometry and Stage/crop geometry are unchanged between A/B/C.

## Visual assessment

A remains valid and restrained, but the narrow filled K still reads slightly more like a preceding emblem than an equal member of the full `KYMÆAN` name at mini-wide and tall sizes.

B improves the apparent size relationship without changing the historical K drawing. The mark gains enough presence to join the wordmark while still reading as Threshold K; its bottom anchor keeps the baseline relationship stable and its modest upward growth does not compete with `Y` or the Stage architecture.

C crosses the useful boundary. The K begins to read perceptibly taller than the O3 cap system and starts to lead through size in addition to shape/mass. That weakens the intended equality rather than improving it.

No further scale bracket is materially justified before Director review: the control, a restrained correction and a clear upper bound answer the current question. B `1.03×` is the preferred non-production successor.

## Boundary

Production remains unchanged. No deployment, social-card revision, favicon change or shared-brand/app implementation is authorized by this study.

**Director decision:** B `1.03×` is confirmed. Materialize that exact intact-group presentation transform in the production-shaped candidate and require the full responsive/accessibility/publication/hosted gate before any production promotion.
