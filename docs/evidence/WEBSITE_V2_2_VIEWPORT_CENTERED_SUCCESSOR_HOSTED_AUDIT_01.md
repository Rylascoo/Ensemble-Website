<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website V2.2 — Viewport-Centered Successor Hosted Audit 01

Status: EXACT HOSTED PASS / PR #75 DRAFT / PRODUCTION UNCHANGED / MERGE PREPARATION NEXT
Date: 2026-09-15
Hosted head: `b9d5259a66f466e08c98e6a5b0a2465a119f7667`
Current base: `main@d7c23477cc12cef581ac241f2fbd9153d3c0ee98`

## Exact-head gates

GitHub Actions passed for the exact hosted head:

- `Repository publication boundaries` run #873 — success;
- `Document status structure` run #652 — success.

Cloudflare reported deployment success for exact commit `b9d5259a` and exposed commit preview `https://55b232db-kymaean-site.wirylasc.workers.dev`.

All nine served public assets matched the exact Git blobs at the hosted head byte-for-byte: `index.html`, `styles.css`, `atmosphere.css`, `modes.css`, `motion.js`, `favicon.svg`, `apple-touch-icon.png`, `social-card.jpg`, and `stage-v2-2.webp`.

The frozen Stage remains 74,740 bytes / SHA-256 `c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`. The repaired social card is 92,205 bytes / SHA-256 `900838f5ddbdd0867c7c1f6ef6d2e4349e2766ae5ca1425a73ee1d1e3c739d1b`.

Preview response policy remained `Cache-Control: public, max-age=0, must-revalidate, no-transform` with `X-Robots-Tag: noindex`. Hosted HTML contained both `social-card.jpg?v=4` declarations and no Cloudflare analytics beacon/injection.

## Hosted browser matrix

Dedicated Edge/CDP against the commit preview passed 2048x1199, 1235x647, 1138x1354, 1227x1422, 768x1024, 600x900, 599x900, 390x844 and 320x640. Every shape had zero horizontal overflow, exact viewport-centered lockup, contained wordmark/status and intrinsic Stage dimensions 1672x941.

At 320x640, the 200% text proxy remained contained. Reduced-motion emulation produced zero running animations. Forced colors hid the Stage and retained the complete identity/status.

## Visual assessment

- **2048x1199:** the lockup reads as intentionally viewport-owned; the doorway remains slightly right and subordinate without breaking the Stage's three-presence balance.
- **1235x647:** spacing B and the tighter status interval remain coherent under compression; architecture continues to frame rather than compete.
- **1138x1354:** the most important successor behavior survives: the identity stays centered while the doorway becomes a separate environmental threshold below/right.
- **320x640:** established portrait rhythm remains intact and restrained; the three-presence environment survives the crop.
- **Forced colors:** identity remains legible without relying on Stage imagery or color.

No hosted evidence exposes a defect that justifies reopening B spacing, O3 hierarchy, Threshold K geometry, vertical rhythm, Stage pixels, crop equations, copy, accessibility behavior or publication policy.

## Result

The production-shaped successor passes the exact hosted recursive audit. Production `www.kymaean.com` remains unchanged at this checkpoint.

**Next boundary:** commit/push this hosted-evidence continuity, require exact-head workflows and exact Cloudflare deployment readback for the continuity head, then mark PR #75 ready and merge with an exact-head guard if no new contrary signal appears; production verification follows immediately after merge.

**APPROVED BY STANDING DIRECTOR DELEGATION — CLEAN EXACT HOSTED RECURSIVE AUDIT.**
