<!-- D-R1-STATUS: ACTIVE LAW -->

# Ensemble Website - Current State

Updated: 2026-09-15

## Authority
Design/website authority: `Rylascoo/Ensemble-Website`; engineering/product truth: `Rylascoo/Ensemble-Project/CURRENT_STATE.md`. Bootstrap: `AGENTS.md`; workflow: `docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md`; durable role: `docs/DESIGN_CONTINUITY.md`; ledger: `docs/evidence/DESIGN_LEDGER.md`.

## Production
Website Placeholder V2.2 is live on `www.kymaean.com`; production main is `b33c242c4b21322df9e04a70a40adffe2df4b777` after PR #71. The frozen Stage, integrated Threshold-K-as-K lockup, `Coming Soon`, corrected social card, motion behavior, accessibility behavior and no-analytics boundary remain unchanged.

Tall computer-browser portrait behavior is corrected: phones through 599 CSS px retain the accepted 160vw / 54.9% crop; portrait widths from 600px upward use continuous Stage width `calc(200vw - 240px)` and doorway-axis lockup `calc(56.125% - 7.35px)`. Wide/landscape rendering remains unchanged.

## Production verification
Exact-main workflows pass: publication boundaries #827 and document structure #609. All nine live public assets match exact `main` Git blobs; production returns HTTP 200 with `Cache-Control: public, max-age=0, must-revalidate, no-transform`; no analytics beacon is present.

Live Edge/CDP passes 2048x1199, 1235x647, 1227x1422, the Director-observed 1138x1354 tall-browser shape, 768x1024, 390x844 and 320x640 with zero horizontal overflow, contained identity and exact 1672x941 Stage source. At 320x640, 200% text remains contained, reduced motion has zero running animations, and forced colors hides the Stage while retaining identity.

## Responsive visual law
`docs/KYMAEAN_WEBSITE_V2_2_RESPONSIVE_VISUAL_STANDARD_01.md` remains Website Sol regression authority. Governing principle: preserve relationships before preserving objects; portrait views are curated crops of the same frozen Stage world.

## Frozen cross-lane boundary
`PKT-STAGE-CORE-02` and `APP-SYN-01` remain untouched. Website V2.2 creates no app UI, cast-size, state, palette, color-semantic, interaction, or final-brand authority.

## Branch lifecycle
PR #71 source branch `site/v2-2-tall-browser-crop-2026-09-15` was a strict ancestor of main with zero unique commits, archived at tag `archive/site/v2-2-tall-browser-crop-2026-09-15` -> `cc556130f6a8e485d8db25c3c1fccd59ee6d76da`, then deleted remotely.

**Exact next action:** hold the live V2.2 website stable. Any later Website Sol visual/CSS change starts from current `main` and must pass the responsive visual standard plus repository/publication/accessibility checks before production promotion.
