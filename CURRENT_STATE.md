<!-- D-R1-STATUS: ACTIVE LAW -->

# Ensemble Website - Current State

Updated: 2026-09-17

## Authority
Design/website authority: `Rylascoo/Ensemble-Website`; engineering/product truth: `Rylascoo/Ensemble-Project/CURRENT_STATE.md`. Bootstrap: `AGENTS.md`; workflow: `docs/KYMAEAN_VISUAL_DESIGN_WORKFLOW_AUTHORITY_01.md`; durable role: `docs/DESIGN_CONTINUITY.md`; ledger: `docs/evidence/DESIGN_LEDGER.md`.

## Director rollback
L-203 records the Director decision to undo the Bellweather production website update and return to concept-first website work. Draft PR #104 is closed unmerged; its branch-local L-201/L-202 never became `main` authority.

The exact rollback target is the pre-Bellweather V2.2 `site/public/**` tree at `538fa349e046041e2759748d54fda176ac6a9749`, parent of PR #102's production merge. The rollback changes only the six public paths introduced/modified by PR #102 and preserves the frozen Stage and all other V2.2 production assets.

## Cross-surface boundary
L-196 remains unchanged: Bellweather is website-focused. A future app-specific study requires separate explicit opening and remains limited to Home/entry; Productions, Stage, Settings, global chrome and functional task/empty-state surfaces remain excluded.

## Publication maintenance
The pre-existing apex redirect quirk remains separate maintenance debt and is not part of this rollback.

## Frozen boundary
Do not build another production mascot integration from prior studies by default. Prior Bellweather/PERSON/WORLD/temporal work remains evidence, not a mandated implementation. After restoration, the website returns to a fresh non-production concept study covering homepage intent, Bellweather's role if any, visual hierarchy, mystery and interaction grammar.

**Exact next action:** complete exact-head/Cloudflare validation of the rollback, fresh-check `main`, merge if clean, verify the live site exactly matches the restored V2.2 public tree, then begin one isolated concept proposal and stop for Director review before any production candidate.
