<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website V2.2 — Mascot Integration Candidate Hosted Audit 01

Status: EXACT HOSTED PASS / DIRECTOR REVIEW NEXT / PRODUCTION UNCHANGED
Date: 2026-09-17
Candidate PR: #102
Candidate head: `287e8e15fdc6613ba87e056b628adb0c869992c5`
Base: `main@538fa349e046041e2759748d54fda176ac6a9749`
Cloudflare version: `a0edd4fd-fed4-41a9-bfeb-b545d8366d57`
Commit preview: `https://a0edd4fd-kymaean-site.wirylasc.workers.dev`

## Exact hosted gates

All five exact-head checks completed successfully: repository/document validation plus Cloudflare Workers build. The hosted root returns HTTP 200 with `Cache-Control: public, max-age=0, must-revalidate, no-transform` and `X-Robots-Tag: noindex`. `/index.html` canonically redirects 307 to `/`.

All eleven public assets match the exact Git blobs byte-for-byte: `index.html`, `styles.css`, `atmosphere.css`, `modes.css`, `motion.js`, `favicon.svg`, `apple-touch-icon.png`, `social-card.jpg`, `stage-v2-2.webp`, `bellweather-person.webp`, and `bellweather-presence.webp`.

Hosted HTML contains no Google Analytics, Tag Manager, Plausible, Segment, Mixpanel, Amplitude, Clarity, Cloudflare Insights, beacon, or other detected analytics injection. Frozen Stage bytes remain unchanged at SHA-256 `c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`.

## Hosted browser matrix

Direct Edge/CDP against the Cloudflare preview passes 2048×1199, 1235×647, 1138×1354, 1227×1422, 768×1024, 600×900, 599×900, 390×844, and 320×640 with zero horizontal overflow, exact viewport-centered identity, contained wordmark, and no PRESENCE/PERSON carrier overlap with the brand lockup.

Wheel/touch/keyboard progression, reverse navigation, rapid retargeting, focus retention, 200% text containment, reduced-motion parity with zero running animations, and browser forced-colors fallback all pass on the hosted candidate.

## Visual assessment

The hosted wide and mobile PERSON captures preserve the intended hierarchy: KYMÆAN remains primary, Bellweather is a human-scale encountered presence at the Stage edge, and she never overlaps the wordmark. TRACE reads as a quiet environmental clue rather than decoration. OTHER LIFE remains materially smaller, darker, and deeper in the Stage, so it does not become a second mascot or imply a specific relationship.

No hosted evidence justifies another carrier scale/crop change, Stage change, wordmark change, copy change, autoplay default, TRACE/W2 accumulation, or additional public explanation.

## Result and boundary

The production candidate passes the exact hosted recursive audit. `www.kymaean.com` remains unchanged; PR #102 remains draft.

**Next boundary:** Director reviews the hosted candidate. Do not merge, publish, or alter production before an explicit Director promotion decision.

Canonical browser evidence: `docs/evidence/WEBSITE_V2_2_MASCOT_INTEGRATION_CANDIDATE_HOSTED_BROWSER_EVIDENCE_01.json`.