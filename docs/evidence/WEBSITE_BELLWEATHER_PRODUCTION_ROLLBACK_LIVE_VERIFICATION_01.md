<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website — Bellweather Production Rollback Live Verification 01

Status: ROLLBACK LIVE / PRE-BELLWEATHER V2.2 RESTORED
Date: 2026-09-17
Rollback PR: #105
Merged main: `741ced7e8171292cfb824ee37859cd4a1e0d189c`
Cloudflare production version: `63506ecd-394b-472b-8559-1d2032f949e9`
Live origin: `https://www.kymaean.com/`

## Exact-main result

PR #105 squash-merged after exact-head repository checks and Cloudflare preview passed. The merged `site/public/**` tree is exactly identical to the pre-Bellweather V2.2 tree at `538fa349e046041e2759748d54fda176ac6a9749`.

The frozen Stage remains SHA-256 `c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`.
## Live verification

Direct live readback confirms the nine served V2.2 assets match their exact `538fa349...` Git blobs byte-for-byte: `index.html`, `styles.css`, `atmosphere.css`, `modes.css`, `motion.js`, `favicon.svg`, `apple-touch-icon.png`, `social-card.jpg`, and `stage-v2-2.webp`.

The two Bellweather production assets now return absent/not found, as required. Live root returns HTTP 200 with `Cache-Control: public, max-age=0, must-revalidate, no-transform`; no analytics injection is detected.

The restored tree is the same previously validated V2.2 apparent-size-parity production experience. No new visual behavior was introduced by the rollback.

## Next boundary

The rollback closes the Bellweather production implementation. Existing Bellweather studies remain preserved as evidence but do not define the next website answer.
Website Sol may now begin one isolated non-production concept proposal covering homepage intent, atmosphere, narrative reveal, Bellweather's role if any, interaction grammar and mystery. The proposal must be reviewed by the Director before any production-shaped candidate is built.

The pre-existing apex redirect double-slash quirk remains separate publication-maintenance debt.

**Result:** the Bellweather production update is fully undone; production is restored to pre-Bellweather V2.2 and concept-first exploration is the only active website design boundary.
