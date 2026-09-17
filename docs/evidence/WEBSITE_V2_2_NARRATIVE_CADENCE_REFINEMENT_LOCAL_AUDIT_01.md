<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website V2.2 — Narrative Cadence Refinement Local Audit 01

Status: ISOLATED PRODUCTION CANDIDATE / LOCAL BROWSER PASS / HOSTED REVIEW NEXT / PRODUCTION UNCHANGED
Date: 2026-09-17
Base: `main@17a81a72b791eb8e5ef19c3fee721b5935fcb1ce`

## Director decision and problem statement

After reviewing the live Bellweather sequence, the Director agreed that the three explicit empty-Stage navigation positions made every other wheel gesture feel unresponsive. The approved refinement keeps the empty Stage as narrative grammar but removes it as a visitor-controlled destination.

Visitor-controlled order is now:

`PLACE -> PRESENCE -> PERSON -> TRACE -> OTHER LIFE`

The semantic law from L-194 remains intact: Bellweather disappears after PERSON, TRACE recedes before OTHER LIFE, and major narrative transitions still pass through an empty Stage rather than crossfading objects directly.
## Implementation

`site/public/motion.js` now exposes five semantic states instead of eight. PLACE -> PRESENCE responds directly; transitions between later narrative chapters automatically fade the current carrier out, hold the exact Stage empty, then reveal the requested next carrier.

Local timing is 280 ms fade-out plus a 300 ms fully empty hold; the next carrier begins revealing after 580 ms. The 300 ms hold is a production-candidate tuning value, not universal Kymaean law.

Rapid input retargets the pending destination while keeping the same transition window, so repeated commands do not prolong the empty Stage or flash an intermediate carrier. Home/End remain deterministic. Reduced-motion bypasses timed transition staging and moves directly through the same five semantic states with zero running animations.

`site/public/styles.css` changes only carrier/world-evidence transition timing: opacity 280 ms and transform 420 ms. No Stage, Bellweather carrier, identity, copy, metadata, or world-evidence geometry changed.

## Deterministic browser audit

Edge/CDP passes 2048x1199, 1235x647, 1138x1354, 1227x1422, 768x1024, 600x900, 599x900, 390x844 and 320x640 with zero horizontal overflow, exact viewport-centered identity, contained wordmark, and no carrier/brand overlap.
Forward wheel gestures settle exactly as `PRESENCE -> PERSON -> TRACE -> OTHER LIFE`; reverse wheel gestures settle exactly as `TRACE -> PERSON -> PRESENCE -> PLACE`. A single wheel gesture advances one meaningful chapter.

The automatic-empty proof observes logical target PERSON while render state is `empty`, with PRESENCE, PERSON, TRACE and OTHER LIFE all at opacity zero. Rapid retarget from a pending later chapter settles directly on the final requested carrier without duplicate or ghosted intermediate content.

Touch/swipe, keyboard arrows/Page keys/space, Home/End, focus retention and wheel burst locking remain correct. Reduced motion traverses `PRESENCE -> PERSON -> TRACE -> OTHER LIFE` directly with zero running animations. The 320x640 200% text proxy remains contained and browser forced-colors continues to hide scene imagery while preserving KYMÆAN / COMING SOON.

Canonical browser evidence: `docs/evidence/WEBSITE_V2_2_NARRATIVE_CADENCE_REFINEMENT_BROWSER_EVIDENCE_01.json`.

## Scope and visual integrity

Frozen Stage SHA-256 remains `c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`. Static PLACE, PRESENCE, PERSON, TRACE and OTHER LIFE compositions remain unchanged; this candidate changes interaction cadence only.

No app UI, product semantics, universal Character rule, Bellweather app placement, analytics, public copy, SEO/social metadata, or visual asset bytes are altered by this refinement.

**Exact next action:** commit/push the isolated candidate, require exact-head repository and Cloudflare success, verify the hosted preview directly, then stop for Director review before production promotion.

**APPROVED BY STANDING DIRECTOR DELEGATION — CLEAN RECURSIVE AUDIT.**
