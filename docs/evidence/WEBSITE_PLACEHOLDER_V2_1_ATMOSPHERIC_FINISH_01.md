<!-- D-R1-STATUS: ACTIVE EVIDENCE -->

# Kymaean Website Placeholder V2.1 — Atmospheric Finish 01

Status: DIRECTOR-OPENED BOUNDED WEBSITE REFINEMENT / LOCAL PREFLIGHT PASS / CLOUDFLARE PREVIEW REVIEW NEXT / NOT FINAL BRAND FREEZE
Date: 2026-09-14
Workstream: WEB / SHARED BRAND
PR: #65
Branch: `site/placeholder-v2-1-atmospheric-finish-2026-09-14`

## Director scope

Increase the production value of the existing secrecy-first placeholder without adding product explanation or changing the approved identity hierarchy.

Locked public language remains:

- `KYMÆAN`
- `Something is taking shape.`
- `In development`

Threshold K and O3 geometry remain exact inherited identity evidence. This pass does not finalize broader palette, type, wordmark, trademark, app, Stage, CLR, or product authority.

## Approved refinement intent

The site should feel almost static at first, then reveal that the environment is quietly changing around an identity that remains fixed.

V2.1 therefore:

- keeps Threshold K geometrically and spatially stable;
- sequences field → Threshold K → KYMÆAN → tagline/status on ordinary motion settings;
- replaces the more obvious polygonal backdrop with softer materially ambiguous pressure/depth fields;
- keeps warm light scarce and subordinate;
- adds a tiny fine-pointer response that changes only field position/light pressure;
- remains complete with no pointer interaction and no motion;
- preserves the Director-approved tighter favicon optical framing from superseded PR #64 while keeping all three exact Threshold K paths unchanged;
- adds mobile safe-area treatment, Apple touch icon, Open Graph/Twitter metadata, and a 1200×630 social-sharing card using the same identity hierarchy.

## Implementation boundary

Deployable changes remain entirely under `site/` and use no framework, WebGL, remote font, analytics, provider call, product runtime, or external application dependency.

`motion.js` is progressive enhancement only. It activates on a fine pointer when reduced motion is not requested. The HTML/CSS composition is complete without it.

## Deterministic local preflight

A local Chromium preflight was run against the exact candidate source before GitHub publication.

Responsive/reflow:

- 1440×900: client width 1440 / scroll width 1440;
- 390×844: client width 390 / scroll width 390;
- 320×640: client width 320 / scroll width 320;
- 320×640 with 200% root-text-size approximation: client width 320 / scroll width 320.

Motion/accessibility:

- at initial load, Threshold K and O3 begin hidden under the authored reveal sequence and resolve fully;
- `prefers-reduced-motion: reduce`: mark animation `none`, field animation `none`, complete identity immediately visible;
- `forced-colors: active`: atmospheric field computes to `display:none`; identity/message remain, with no horizontal overflow;
- desktop pointer test moved the field from identity-neutral transform to approximately 2.25px × 1.61px while the Threshold K bounding box remained exactly 168×168 at the same x/y coordinates.

Finishing assets:

- `favicon.svg`: exact Threshold K paths; tighter framing only; light/dark browser-chrome fill adaptation;
- `apple-touch-icon.png`: 180×180 exact mark derivative;
- `social-card.jpg`: 1200×630 secrecy-first share card using Threshold K, O3, and the approved tagline.

## Next boundary

Review the actual Cloudflare non-production deployment of draft PR #65 on desktop and mobile, including the reveal sequence, long-dwell ambience, pointer response, and favicon. Correct any visible defect recursively before merge.

Do not merge to `main`, replace the current production placeholder, expand disclosure, or claim final brand authority until that deployed review is clean.
