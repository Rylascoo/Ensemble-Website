# Reference 17 / Crop 04 — Pre-Publication Candidate Presentation Package 01

Status: **PRE-GATE / NON-PRODUCTION / NOT ADOPTED / NOT PUBLISHED**

Authority baseline: `main@470eb0fc6b60bde20489fc22dd0cc2aca806a9b6`

This package converts the completed context-integration research into an implementation-shaped proposal without modifying `site/public/**`, advancing Reference 17, creating a new Design Ledger event, or resolving the concurrent PR #147 / PR #148 L-242 collision.

## 1. Candidate visual master

Visual master:
- `prototypes/website-reference17-doorway-crop-04/full-scene-diagnostic/REF17_CROP04_FULL_SCENE_DIAGNOSTIC.png`
- dimensions: 1672 × 941
- decoded-image SHA-256: `538be8b4c09aecbddccc36f52959ca1a9190bd57d4415151f48c0af40f74da33`
- Git blob: `beea3539f285d14299fbee0f74ad0d33028e0dc8`
- repository blob size: **2,364,961 bytes (~2.26 MiB)**

The PNG is the exact visual master for candidate preparation. It is **not** suitable as the direct public hero payload.

Current production comparison:
- `site/public/stage-v2-2.webp`
- 1672 × 941
- Git blob: `d694143b57cc259e0d4b95c783363f2555b0fbb0`
- payload: **74,740 bytes (~73 KiB)**

Current social card:
- `site/public/social-card.jpg`
- declared 1200 × 630
- Git blob: `6d19fdbf20482c4c80fba36bdf85496fc9190505`
- payload: **92,344 bytes (~90 KiB)**

## 2. Proposed public-hero derivative

A later publication branch should derive a deployment asset from the exact PNG master rather than altering the master itself.

Proposed deployment form:
- dimensions: retain **1672 × 941**;
- preferred first implementation: WebP, matching the current production delivery model;
- no crop baked into the asset;
- no wordmark, status copy, gradient, vignette or responsive mask baked into pixels;
- no artwork regeneration or repainting during encoding;
- preserve the master PNG separately as evidence.

Performance gate:
- current hero payload = 74,740 bytes;
- initial candidate budget = **≤149,480 bytes (2× current hero)**;
- exceeding 2× current hero requires an explicit visual-quality/performance justification before publication;
- the 2.26 MiB diagnostic PNG fails this deployment gate by construction.

The size budget is an implementation gate, not a visual-law claim.

## 3. Proposed desktop presentation

Desktop behavior should remain structurally unchanged because context study 01 passed it.

Proposed retained rules:
- fixed full-viewport scene;
- `object-fit: cover`;
- `object-position: 50% 49%`;
- existing top atmospheric overlay;
- existing wordmark geometry;
- existing centered identity hierarchy;
- existing reveal timing unless later performance testing shows a reason to change it.

Reason:
the 1672 × 941 candidate is already essentially 16:9 and preserves the whole-Stage hierarchy under the current desktop frame.

## 4. Proposed portrait presentation

The research incumbent replaces progressive portrait zoom with one stable composition rule.

Proposed portrait image rule:
```css
.scene-art {
  inset: auto auto 0 50%;
  width: 148vw;
  max-width: none;
  height: auto;
  transform: translateX(-50%);
  object-fit: contain;
  object-position: center;
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, #000 12%, #000 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, #000 12%, #000 100%);
}
```

Proposed portrait identity rule:
```css
.brand-lockup {
  top: max(25.5svh, calc(env(safe-area-inset-top) + 1rem));
  left: 50%;
  width: min(90vw, 24rem);
}
```

The existing `min-width: 600px` portrait image-width override should be removed rather than replaced with a second zoom formula.

Reason:
- current phone 160vw exposes about 1,045 source pixels horizontally;
- 148vw exposes about 1,130;
- current 768px portrait-tablet rule reaches 168.75vw and exposes only about 991;
- stable 148vw preserves approximately the same source fraction across portrait widths and keeps the doorway subordinate to the Stage.

## 5. Identity / overlay behavior

Preserve:
- wordmark as deterministic SVG/HTML overlay, never baked into artwork;
- `Coming Soon` as live text;
- same semantic hidden H1;
- same centered brand relationship;
- no additional slogan or explanatory copy in this placeholder phase.

Candidate review gate:
the wordmark must remain visually legible without requiring the background to be artificially darkened enough to damage Stage/light relationships.

If extra contrast is needed, adjust only the deterministic overlay/scene gradient after a separate comparison. Do not repaint the artwork master.

## 6. Accessibility and user-preference behavior

Retain current behavior:
- decorative scene image uses empty alt text;
- accessible brand name remains represented by the hidden H1;
- forced-colors mode hides the scene and uses system Canvas/CanvasText;
- prefers-reduced-motion disables animation;
- prefers-contrast may reduce scene prominence;
- safe-area insets remain respected;
- page remains functional if the scene asset fails to load.

No visual candidate is allowed to weaken these fallbacks.

## 7. Social-card implications

Do **not** automatically point `og:image` / Twitter image at the 1672 × 941 hero.

The social surface is 1200 × 630 (about 1.905:1), while the hero master is about 1.777:1. A direct `cover` crop would remove vertical information and could change the Stage/threshold hierarchy.

Required before any social-card replacement:
1. deterministic 1200 × 630 crop study from the exact visual master;
2. confirm Stage remains legible and doorway remains subordinate;
3. confirm identity treatment matches the existing separate-layer philosophy;
4. keep social asset payload at or below the current **92,344-byte** baseline when visually acceptable, or document any justified increase;
5. version the public URL only after the new social asset exists.

Until that proof exists, keep the current social card unchanged even if the hero is later adopted.

## 8. Cache and preload behavior

If publication is later authorized:
- give the new hero a new filename rather than silently replacing old bytes under `stage-v2-2.webp`;
- update preload and image `src` together;
- use one shared version identifier if query-versioning remains;
- ensure no HTML preload points at the retired V2.2 asset;
- avoid shipping both full hero payloads unless rollback architecture explicitly requires it.

## 9. Validation matrix before publication

Required static/browser checks:
- wide desktop 16:9;
- 1366 × 768;
- 1280 × 800;
- short landscape <=560px high;
- phone portrait around 390 × 844;
- narrow phone portrait around 320px wide;
- portrait tablet around 768 × 1024;
- large portrait tablet around 820–900px wide;
- safe-area device treatment;
- forced colors;
- prefers contrast;
- reduced motion;
- image-load failure.

Visual gates:
- Stage first;
- amber/blue outer territories remain primary;
- doorway discovered, not advertised;
- teal/plum remain subordinate;
- identity field remains calm;
- no fantasy-portal or app-UI reading introduced;
- no mobile/tablet composition flips hierarchy.

Performance gates:
- hero derivative ≤149,480 bytes unless explicitly justified;
- image dimensions remain declared;
- preload references exact candidate derivative;
- no duplicate hero fetch caused by preload/src mismatch.

Repository gates:
- `site/public/**` changes must be limited to the explicitly authorized publication patch;
- repository publication-boundary validator PASS;
- document status structure validator PASS;
- no CI bypass.

## 10. Rollback boundary

The public candidate, if later authorized, should be reversible by one small publication commit.

A rollback must be able to restore:
- `stage-v2-2.webp` reference;
- original preload line;
- original portrait `160vw` / tablet formula;
- original 18% mask fade;
- original 29.5svh portrait lockup;
- original social card, which should remain untouched in the first hero publication anyway.

Do not delete V2.2 source/evidence during initial publication. Retire it only after a later explicit cleanup gate.

## 11. Explicit non-scope

This package does not:
- authorize production adoption;
- create Crop 05;
- change Reference 17;
- widen Boundary 01;
- alter Bellweather;
- modify app semantics;
- alter Engineering;
- change `site/public/**`;
- change the Design Ledger or `CURRENT_STATE.md`;
- merge PR #147 or PR #148;
- resolve duplicate L-242 numbering.

## 12. Publication decision still required

A later Director gate must explicitly decide all of the following together:
1. adopt Crop-04 full-scene diagnostic as the temporary placeholder visual successor;
2. authorize creation of an optimized WebP derivative from the exact visual master;
3. authorize the 148vw stable portrait presentation;
4. authorize the bounded `site/public/**` patch;
5. keep social-card replacement out of scope unless its own 1200 × 630 proof has passed.

Until then, this package is implementation-shaped research only.
