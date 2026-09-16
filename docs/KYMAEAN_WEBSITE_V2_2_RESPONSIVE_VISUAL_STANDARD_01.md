<!-- D-R1-STATUS: ACTIVE LAW -->

# KYMÆAN Website V2.2 Responsive Visual Standard 01

## Scope
This is Website Sol law for the temporary public V2.2 website only. It does not create app/UI, shared-brand, cast-size, interaction, color-semantic, or final-brand authority.

The Director established three practical composition references from live production on 2026-09-15:
- **Wide:** 2048 × 1199.
- **Mini-wide:** 1235 × 647.
- **Portrait / “phone-screen shaped”:** 1227 × 1422.

## Governing principle
**Preserve relationships before preserving objects.** Narrower views are curated crops of the same Stage world, not alternate artwork or independently redesigned posters.

## Invariants
- `KYMÆAN` → `COMING SOON` remains one coherent identity lockup; the doorway remains a subordinate environmental threshold rather than a lockup alignment target.
- The complete visible identity is centered to the user viewport at 50%, independently of the doorway axis; the identity → COMING SOON → doorway relationship remains visually coherent without sharing one horizontal axis.
- Threshold K remains integrated as the visible `K`; no redundant standalone logo is added above it.
- The frozen Stage artwork is not regenerated or recomposed by breakpoint.
- Amber / neutral / blue retain left / center / right order.
- The doorway remains mysterious and subordinate; it must not become a portal spectacle.
- The Stage rim remains structural support rather than the focal element.
- The identity remains fully contained with deliberate side breathing room.

## Shape-specific expectations
### Wide — 2048 × 1199 reference
Full Stage expression. All three presences read clearly; the doorway is subordinate but unmistakable; the identity has generous negative space; the Stage rim is visible without dominating.

### Mini-wide — 1235 × 647 reference
The same composition is compressed rather than redesigned. All three presences, doorway and identity hierarchy remain legible. Architectural edge cropping may tighten while the Stage still reads as one complete shared environment.

### Portrait / phone-screen shaped — 1227 × 1422 reference
A curated vertical crop of the same world. The center presence and doorway become primary. Amber and blue may partially leave frame but must remain visibly implied at opposite edges. The Stage rim must not overpower the identity/threshold sequence.

Tall computer-browser portrait windows must not fall back to the full-height `cover` crop, because that can over-zoom the 16:9 Stage and collapse the side-presence relationship. The V2.2 implementation therefore keeps the established phone crop through 599 CSS px and, from 600 CSS px upward in portrait orientation, widens continuously with `width: calc(200vw - 240px)`. The Stage crop remains continuous at 599/600 while the lockup is independently fixed at `left: 50%`, revealing progressively more Stage context on wider portrait browser windows without pulling the identity toward the doorway.

## Regression rule
Any future website visual/CSS/publication change must be checked against all three reference shapes before production promotion. A pass requires no horizontal overflow, contained viewport-centered identity, preserved identity → center presence → doorway hierarchy, preserved left/center/right presence logic, and no breakpoint-specific replacement artwork.

When narrow cropping forces a choice, preserve the identity → center presence → doorway → shared Stage relationship before preserving outer architecture or the full extents of the side presence volumes.

## Production baseline
V2.2 was promoted by PR #68 merge `e5aea65a315dd9331092e75213d7825f1d2cf25a`; the approved responsive page payload is `85f40392225349442ac992aac4b4cfe9cc00eb8a`. The social-card consistency repair is `e588dc01bf2ce37bc8d65ed53b4ad06fbbf4290f`.
