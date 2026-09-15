<!-- D-R1-STATUS: ACTIVE LAW -->

# Ensemble Website - Current State

Updated: 2026-09-15

## Authority
Design/website authority: `Rylascoo/Ensemble-Website`; engineering/product truth: `Rylascoo/Ensemble-Project/CURRENT_STATE.md`. Bootstrap: `AGENTS.md`; workflow: `docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md`; durable role: `docs/DESIGN_CONTINUITY.md`; ledger: `docs/evidence/DESIGN_LEDGER.md`.

## Production
Website Placeholder V2.2 is live on `www.kymaean.com`. PR #68 merged as `e5aea65a315dd9331092e75213d7825f1d2cf25a`. The approved responsive page payload is `85f40392225349442ac992aac4b4cfe9cc00eb8a`; social-card repair payload is `e588dc01bf2ce37bc8d65ed53b4ad06fbbf4290f`.

Post-merge production verification passed: all nine public assets matched exact `main` Git blobs; `Cache-Control` retained `public, max-age=0, must-revalidate, no-transform`; no analytics beacon was present; 1440x900, 1024x768, 768x1024, 430x932, 390x844 and 320x640 had zero horizontal overflow; 320x640 also passed 200% text, reduced motion with zero running animations, and forced colors with the Stage hidden and identity retained. Main push workflows passed: publication boundaries #812 and document structure #594.

## Responsive visual law
`docs/KYMAEAN_WEBSITE_V2_2_RESPONSIVE_VISUAL_STANDARD_01.md` is the Website Sol regression authority. Director reference shapes are wide 2048x1199, mini-wide 1235x647, and portrait/phone-screen-shaped 1227x1422. Governing principle: preserve relationships before preserving objects; narrow views are curated crops of the same frozen Stage world.

## Frozen cross-lane boundary
`PKT-STAGE-CORE-02` and `APP-SYN-01` remain untouched. Website V2.2 creates no app UI, cast-size, state, palette, color-semantic, interaction, or final-brand authority.

## Branch lifecycle
Source branch `site/placeholder-v2-2-precision-2026-09-14` had zero commits unique from `main`, was archived at tag `archive/site/placeholder-v2-2-precision-2026-09-14` -> `93ba0516db6899f64fe3be06ac11a04934357074`, then deleted remotely. Temporary local CDP audit debris was removed.

**Exact next action:** hold the live V2.2 website stable. Any future Website Sol visual or CSS change starts from current `main`, preserves the frozen cross-lane boundary, and must pass the three-shape responsive visual standard plus repository/publication/accessibility checks before production promotion.
