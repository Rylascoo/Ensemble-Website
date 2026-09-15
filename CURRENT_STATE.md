<!-- D-R1-STATUS: ACTIVE LAW -->

# Ensemble Website - Current State

Updated: 2026-09-15

## Authority
Design/website authority: `Rylascoo/Ensemble-Website`; engineering/product truth: `Rylascoo/Ensemble-Project/CURRENT_STATE.md`. Bootstrap: `AGENTS.md`; workflow: `docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md`; durable role: `docs/DESIGN_CONTINUITY.md`; ledger: `docs/evidence/DESIGN_LEDGER.md`.

## Production
Website Placeholder V2.2 is live on `www.kymaean.com`; current production `main` baseline is `b80ec78cb63a82f8c6949ba49596179708e986d7`. The frozen Stage, integrated Threshold-K-as-K lockup, `Coming Soon`, corrected social card, accessibility behavior and no-analytics boundary remain unchanged.

## Active Website Sol refinement
Director-supplied live evidence exposed one responsive defect in tall computer-browser portrait windows: widths above the old 900px portrait breakpoint fell back to full-height `cover`, over-zooming the 16:9 Stage and suppressing amber/blue context. The authorized successor is branch `site/v2-2-tall-browser-crop-2026-09-15` from exact production main.

The candidate changes only `site/public/modes.css`: phones through 599 CSS px retain the existing 160vw / 54.9% treatment; portrait widths from 600px upward use continuous Stage width `calc(200vw - 240px)` and doorway-axis lockup `calc(56.125% - 7.35px)`. The rule is mathematically continuous at 599/600 and leaves landscape/wide rendering unchanged.

## Local recursive audit
Exact reference checks pass at 2048x1199 wide, 1235x647 mini-wide, 1227x1422 portrait, the Director-observed 1138x1354 tall-browser shape, 768x1024, 600x900, 599x900, 390x844 and 320x640: zero horizontal overflow, contained identity, exact 1672x941 Stage source, preserved left/center/right presence logic and doorway-axis relationship. 320x640 also passes 200% text, reduced motion with zero running animations, and forced colors with the Stage hidden and identity retained.

## Frozen cross-lane boundary
`PKT-STAGE-CORE-02` and `APP-SYN-01` remain untouched. This website crop correction creates no app UI, cast-size, state, palette, color-semantic, interaction, or final-brand authority.

**Exact next action:** commit/push the candidate with L-169 continuity, require exact-head repository workflows and Cloudflare hosted visual/byte verification, then promote under standing clean-recursive-audit authority only if the hosted pass remains clean; verify production afterward.
