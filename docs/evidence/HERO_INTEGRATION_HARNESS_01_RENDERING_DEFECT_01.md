<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# HERO INTEGRATION HARNESS 01 — RENDERING DEFECT 01

Status: OPEN / DIRECTOR DISPOSITION REQUIRED / NO SILENT FIX
Date: 2026-09-06

## Defect

Harness 01 uses the canonical Threshold K and O3 SVG files through external `<img>` elements.

Both canonical SVGs express their visible geometry through `currentColor`:

- Threshold K uses `fill="currentColor"`;
- O3 uses strokes with `stroke:currentColor`.

When used as external image resources, that color does not inherit the intended HTML scaffold foreground color. In the observed deterministic harness rendering the assets resolve dark/black.

Desktop's returned candidate happens to provide a mid-value left field, so the dark identity geometry remains visible there. Mobile's fixed identity band is Mineral Theater Void, so the same dark geometry is nearly invisible.

## Why this matters

The defect is in the candidate-neutral evidence harness, not the Round 01 artwork.

Brand Integration and S6 must not be scored from a technically defective identity treatment.

The frozen method prohibits adapting the harness after a candidate exists without halting and explicitly reopening the harness/method boundary. Therefore this record does not correct the defect.

## Narrow candidate-neutral correction available

A technically minimal repair would preserve:

- exact canonical SVG geometry;
- all desktop/mobile frame dimensions;
- all copy geometry;
- all candidate crop/position rules;
- all current Harness 01 material/chrome roles;
- no candidate-specific masks/scrims/repositioning.

Only SVG color resolution would change so the canonical `currentColor` geometry receives the harness's already-defined neutral identity foreground (current `--ink`, `#ece9e0`) in a deterministic way.

One implementation option is to render the exact canonical SVG source inline under the existing wrapper color rather than through external `<img>` embedding. Another candidate-neutral adapter with exactly equivalent geometry/color behavior would be acceptable if audited before use.

No canonical Threshold K or O3 source asset should be edited merely to repair this harness.

## Decision required

Director may:

- **APPROVE NARROW CORRECTION** — permit only the candidate-neutral SVG color-resolution repair above, then rerun Harness 01 evidence on the unchanged Round 01 raw candidate and use the corrected harness unchanged for later qualifying candidates; or
- **REJECT / REOPEN MORE BROADLY** — halt the qualifying experiment for a wider harness/method review.

Approval of the narrow correction would not authorize a new render and would consume no additional qualifying round. It must not change Round 01 raw pixels or any crop/composition geometry.
