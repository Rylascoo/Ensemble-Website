<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website V2.2 — Apparent-Size Parity Hosted Audit 01

Status: EXACT HOSTED PASS / DIRECTOR-CONFIRMED B / PRODUCTION UNCHANGED / MERGE PREPARATION NEXT
Date: 2026-09-16
Hosted candidate head: `0a8513d80ed4cfb348f71a24e4a8f9d119b27ad6`
Current base at candidate creation: `main@28177c126d8527c409c92a2ed935ded88ebd143f`
Cloudflare version: `4b9d1fc5-7c11-4f0b-92d4-4f5ae606cbff`
Commit preview: `https://4b9d1fc5-kymaean-site.wirylasc.workers.dev`

## Exact-head and hosted byte gates

Exact-head GitHub checks pass: `Repository publication boundaries` run #924 and `Document status structure` run #702.

Cloudflare Workers build `d5ddc24f-40f3-48fb-a98d-ebd9eaec6283` completed successfully for the exact candidate head.

All nine hosted public assets match the exact Git blobs byte-for-byte: `index.html`, `styles.css`, `atmosphere.css`, `modes.css`, `motion.js`, `favicon.svg`, `apple-touch-icon.png`, `social-card.jpg`, and `stage-v2-2.webp`.

The frozen Stage remains 74,740 bytes / SHA-256 `c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`. Candidate social card V5 is 92,344 bytes / SHA-256 `36faecf3022c269f40eb10364f26c0f40b350eedd4d27f1ec92b08de0b5b04a6`.

Hosted responses remain HTTP 200 with `Cache-Control: public, max-age=0, must-revalidate, no-transform` and `X-Robots-Tag: noindex`. Hosted HTML contains no Cloudflare analytics beacon/injection and references social-card revision `v=5`.

## Hosted browser matrix

Dedicated Edge/CDP against the commit preview passes 2048×1199, 1235×647, 1138×1354, 1227×1422, 768×1024, 600×900, 599×900, 390×844 and 320×640. Every shape has zero horizontal overflow, exact viewport-centered lockup, contained wordmark/status and intrinsic Stage dimensions 1672×941.

At 320×640, the 200% root-text proxy remains contained. Reduced-motion emulation reports zero running animations. Forced colors hides the Stage and preserves the complete identity/status.

## Visual assessment

- 2048×1199: the +3% K remains restrained and reads as part of `KYMÆAN` rather than a detached emblem.
- 1235×647: apparent-size parity is clearest under compression; K mass now relates more naturally to the O3 cap system without dominating it.
- 1138×1354: the enlarged K preserves quiet top rhythm, viewport ownership and doorway separation.
- Portrait/mobile: no crowding or clipping appears.
- Social card V5: the same correction survives the 1200×630 secondary surface without changing Stage composition or copy hierarchy.

No hosted evidence justifies another scale bracket, K path edit, spacing change, stroke-hierarchy change, vertical-rhythm change, Stage/crop change, copy change or additional generative imagery.

## Result

The Director-confirmed 1.03× Threshold K presentation passes the exact hosted recursive audit. Production `www.kymaean.com` remains unchanged at this checkpoint.

**Next boundary:** commit/push this hosted-audit continuity only, require exact-head repository checks and Cloudflare deployment readback for that continuity head, then mark PR #85 ready and promote with an exact-head merge guard only if no new contrary signal appears.
