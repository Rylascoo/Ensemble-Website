<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website V2.2 — Mascot Integration Production Verification 01

Status: PRODUCTION LIVE / EXACT-MAIN + LIVE PASS
Date: 2026-09-17
PR: #102
Merged main: `d51d43e89bddc7178a4d3fd366f9e8a54ead2753`
Cloudflare production version: `677c6a98-34d3-48c4-bf5a-3534007b3442`
Live origin: `https://www.kymaean.com/`

## Exact-main gate

PR #102 squash-merged only after L-199 Director promotion authorization and clean exact-head GitHub/Cloudflare checks. The squash merge tree is byte-identical to the approved source head tree.

Both exact-main repository validation jobs passed. Cloudflare Workers production build completed successfully for the exact merged main commit.

## Live byte and header verification

All eleven deployable public assets match the exact merged Git blobs byte-for-byte: `index.html`, `styles.css`, `atmosphere.css`, `modes.css`, `motion.js`, `favicon.svg`, `apple-touch-icon.png`, `social-card.jpg`, `stage-v2-2.webp`, `bellweather-person.webp`, and `bellweather-presence.webp`.

The frozen Stage remains unchanged at SHA-256 `c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`. Live root returns HTTP 200 with the expected no-transform cache policy; `/index.html` canonically redirects 307 to `/`. No analytics injection was detected.

## Live browser verification

Direct Edge/CDP against `https://www.kymaean.com/` passes the same nine viewport matrix: 2048×1199, 1235×647, 1138×1354, 1227×1422, 768×1024, 600×900, 599×900, 390×844 and 320×640. Every viewport has zero horizontal overflow, centered identity and contained wordmark.

Keyboard, wheel, touch/swipe, reverse navigation, rapid retargeting and focus retention remain correct. The interrupted-empty ghost check resolves to PERSON with only the PERSON carrier visible. Reduced-motion parity reports zero running animations; the 200% text proxy remains contained; browser forced-colors fallback remains active and usable.

Live wide and mobile PERSON captures preserve the reviewed hierarchy: Bellweather is encountered at human scale without overlapping the identity; TRACE and OTHER LIFE remain world evidence rather than becoming additional mascot presentations.

Canonical browser evidence: `docs/evidence/WEBSITE_V2_2_MASCOT_INTEGRATION_PRODUCTION_BROWSER_EVIDENCE_01.json`.

## Unrelated publication hygiene

The pre-existing apex redirect quirk remains unchanged: `https://kymaean.com/` first redirects to `https://www.kymaean.com//`. It predates this promotion and did not affect the successful `www` production verification. It remains separate publication-maintenance debt rather than a PR #102 regression.

**Result:** PR #102 production promotion is verified complete. No contrary live signal requires rollback or correction.
