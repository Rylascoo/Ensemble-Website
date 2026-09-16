<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website V2.2 — Viewport-Centered Successor Production Closeout 01

Status: PRODUCTION VERIFIED / SOURCE BRANCH ARCHIVED / FUTURE LETTER-SIZE STUDY RECORDED
Date: 2026-09-15
Production authority at closeout: `main@e5f6f66fa78b5e44745515a20ced368a6df52e25`
PR #75 merge: `4a847ddd942598bba6e8e8a6febd4e9ce9f3c65d`

## Production verification

`www.kymaean.com` was checked after PR #75 promotion and again against current `main`. PR #77 advanced `main` only with Bellweather mascot continuity; `git diff 4a847ddd..e5f6f66 -- site/public` is empty, so the current public-site payload is the exact PR #75 successor payload.

All nine served public assets match current-main Git blobs byte-for-byte: `index.html`, `styles.css`, `atmosphere.css`, `modes.css`, `motion.js`, `favicon.svg`, `apple-touch-icon.png`, `social-card.jpg`, and `stage-v2-2.webp`. Production retains `Cache-Control: public, max-age=0, must-revalidate, no-transform`; no Cloudflare analytics injection was detected.

The frozen Stage remains 74,740 bytes / SHA-256 `c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`. The V4 social card remains 92,205 bytes / SHA-256 `900838f5ddbdd0867c7c1f6ef6d2e4349e2766ae5ca1425a73ee1d1e3c739d1b`.

Live Edge/CDP passes 2048x1199, 1235x647, 1138x1354, 1227x1422, 768x1024, 600x900, 599x900, 390x844 and 320x640 with zero horizontal overflow, contained 50% viewport-centered identity and intrinsic 1672x941 Stage. The 320x640 200% text proxy, reduced motion and forced colors also pass.

Visual inspection confirms the production result matches the selected B direction: viewport ownership is clear, `COMING SOON` remains associated with the wordmark, and the doorway remains a subordinate environmental threshold rather than the lockup axis.
## Source-branch lifecycle

The promoted source branch `site/v2-2-viewport-lettering-successor-2026-09-15` resolved to `6f94c806bc57ecf548b249dbb885f29ca2ff5ada`. Against current main it was a strict ancestor with `main..branch = 0` unique commits.

Archive tag `archive/site/v2-2-viewport-lettering-successor-2026-09-15` was created and remotely read back at that exact SHA before the remote source branch was deleted. No unique work was discarded.

## Future Director lettering preference

The Director would eventually like the website lettering to read as **more equal in apparent size across the complete `KYMÆAN` wordmark**, especially the visible Threshold K relative to `YMÆAN`.

This preference does **not** modify the current production acceptance and does not authorize a Threshold K path redesign. When website lettering is next reopened, begin with a deterministic non-production size-parity study using the current production lockup as control. Prefer intact-group presentation changes such as uniform scale/placement before considering any path edit; preserve the frozen Stage, viewport centering, selected B spacing logic, `COMING SOON` relationship, responsive/publication/accessibility behavior and no-analytics boundary unless separately reopened.

The study should distinguish mathematical dimensions from optical equality: compare apparent cap height, visual mass and baseline relationship at wide, mini-wide and tall browser shapes before deciding whether any change is warranted.

**Closeout result:** current production is verified and the completed successor branch lifecycle is closed. Future apparent-size balancing is recorded as a separate later website lettering question, not as an unreviewed production change.

**APPROVED BY STANDING DIRECTOR DELEGATION — CLEAN PRODUCTION CLOSEOUT / FUTURE LETTER-SIZE QUESTION PRESERVED.**