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
The original V2.2 website baseline was promoted by PR #68 merge `e5aea65a315dd9331092e75213d7825f1d2cf25a`, with social-card consistency repair `e588dc01bf2ce37bc8d65ed53b4ad06fbbf4290f`. The viewport-centered B optical-spacing successor was promoted by PR #75 merge `4a847ddd942598bba6e8e8a6febd4e9ce9f3c65d`.

The current approved production identity successor was promoted by PR #85 merge `137636fe57c36235d2f8f45c87e96b5bd12e0768`: the same exact historical Threshold K paths presented at 1.03× with transform `translate(22.92783 8.89104) scale(.43054)`, exact O3 `YMÆAN`, retained B spacing, viewport centering and unchanged frozen Stage (`c3db042c590ad97bb44d39e9840a5d7259cd0352f2915dadb5a00df896e945c3`). Production social card V5 is SHA-256 `36faecf3022c269f40eb10364f26c0f40b350eedd4d27f1ec92b08de0b5b04a6`. Production closeout is Design Ledger L-186 and `docs/evidence/WEBSITE_V2_2_APPARENT_SIZE_PARITY_PRODUCTION_CLOSEOUT_01.md`.
