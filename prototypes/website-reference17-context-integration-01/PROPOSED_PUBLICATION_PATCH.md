# Proposed Publication Patch — Reference 17 / Crop 04 Placeholder Successor

Status: **DRY-RUN PATCH PLAN ONLY / NO PUBLIC MUTATION AUTHORIZED**

This file states the smallest expected `site/public/**` change set if a later Director gate authorizes publication.

## Allowed public-file surface

Expected:
1. **ADD** one optimized hero derivative, proposed name:
   `site/public/stage-reference17-crop04.webp`
2. **MODIFY** `site/public/index.html`
3. **MODIFY** `site/public/modes.css`

Expected unchanged:
- `site/public/styles.css`
- `site/public/atmosphere.css`
- `site/public/social-card.jpg`
- favicon / touch icon assets
- wordmark SVG geometry inside `index.html`
- accessibility semantics and metadata other than hero preload/src

Any additional public file in the eventual diff requires explicit review rather than silent scope expansion.

## index.html dry-run

Two hero references change together.

Current:
```html
<link rel="preload" href="/stage-v2-2.webp?v=2" as="image" type="image/webp" fetchpriority="high">
...
<img
  class="scene-art"
  src="/stage-v2-2.webp?v=2"
  width="1672"
  height="941"
  alt=""
  decoding="async"
  fetchpriority="high">
```

Proposed shape after an optimized derivative exists:
```html
<link rel="preload" href="/stage-reference17-crop04.webp?v=<PUBLICATION_VERSION>" as="image" type="image/webp" fetchpriority="high">
...
<img
  class="scene-art"
  src="/stage-reference17-crop04.webp?v=<PUBLICATION_VERSION>"
  width="1672"
  height="941"
  alt=""
  decoding="async"
  fetchpriority="high">
```

The exact publication version must be assigned by the publication change; this research branch does not invent it.

## modes.css dry-run

In the existing `@media (max-width: 900px) and (orientation: portrait)` block:

Current:
```css
.brand-lockup {
  top: max(29.5svh, calc(env(safe-area-inset-top) + 1rem));
  ...
}

.scene-art {
  ...
  width: 160vw;
  ...
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, #000 18%, #000 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, #000 18%, #000 100%);
}

.scene::after {
  background: linear-gradient(to bottom, rgba(9,11,12,0.12), transparent 45%);
}
```

Proposed:
```css
.brand-lockup {
  top: max(25.5svh, calc(env(safe-area-inset-top) + 1rem));
  ...
}

.scene-art {
  ...
  width: 148vw;
  ...
  -webkit-mask-image: linear-gradient(to bottom, transparent 0%, #000 12%, #000 100%);
  mask-image: linear-gradient(to bottom, transparent 0%, #000 12%, #000 100%);
}

.scene::after {
  background: linear-gradient(to bottom, rgba(9,11,12,0.10), transparent 41%);
}
```

In the existing `@media (min-width: 600px) and (orientation: portrait)` block:
- keep any needed brand-lockup inheritance only if necessary;
- **remove the scene-art progressive zoom override** using `calc(200vw - 240px)`;
- **remove the duplicate portrait scene overlay override** if it is identical to the main portrait candidate rule.

The goal is one stable portrait image composition from phone through portrait tablet.

## Social metadata dry-run

No first-publication change:
```html
<meta property="og:image" content="https://www.kymaean.com/social-card.jpg?v=5">
<meta name="twitter:image" content="https://www.kymaean.com/social-card.jpg?v=5">
```

A social-card successor remains a separate crop/integration proof.

## Rollback dry-run

A rollback reverses exactly:
- hero preload path;
- hero img src path;
- 148vw -> 160vw phone rule;
- 12% -> 18% top mask;
- 25.5svh -> 29.5svh portrait lockup;
- scene overlay candidate values;
- restores the current tablet `calc(200vw - 240px)` only if rollback is to the exact present production baseline.

The optimized candidate asset may remain in repository history; rollback does not require deleting evidence.

## Stop conditions

Do not execute this patch if:
- PR #147/#148 continuity remains unresolved in a way that would corrupt ledger numbering;
- hosted validators remain failing without understood repository health;
- optimized hero derivative exceeds the package performance gate without explicit justification;
- visual checks fail at phone or portrait-tablet width;
- the actual diff expands outside this bounded surface without Director review.
