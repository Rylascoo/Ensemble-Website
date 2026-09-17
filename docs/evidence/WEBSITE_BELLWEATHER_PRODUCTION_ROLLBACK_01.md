<!-- D-R1-STATUS: ACTIVE LAW -->

# Kymaean Website — Bellweather Production Rollback 01

Status: DIRECTOR-ORDERED PRODUCTION ROLLBACK / PRE-BELLWEATHER V2.2 RESTORE
Date: 2026-09-17

## Director decision

After reviewing the live Bellweather integration and the follow-on cadence candidate, the Director ordered the latest Bellweather website update undone and requested a return to concept-first design work before any further production change.

Draft PR #104 is closed unmerged and must remain historical evidence only. Its branch-local L-201/L-202 entries never became `main` authority.

## Exact rollback target

The authoritative pre-Bellweather public tree is `main@538fa349e046041e2759748d54fda176ac6a9749`, the parent of PR #102's production merge `d51d43e89bddc7178a4d3fd366f9e8a54ead2753`.
The rollback restores only `site/public/**` from that exact commit. Expected public delta from current production is therefore exactly:
- remove `bellweather-person.webp`;
- remove `bellweather-presence.webp`;
- restore `index.html`;
- restore `styles.css`;
- restore `modes.css`;
- restore `motion.js`.

All other production assets remain byte-identical, including the frozen Stage, wordmark assets, social card, icons, atmosphere stylesheet and headers.

## Design consequence

This rollback does not reject Bellweather as a concept or erase prior research. It rejects the current production expression as the next public answer. Existing mascot/person/world/temporal evidence remains historical design evidence, not an instruction to rebuild the same experience.
The next website program is concept-first and non-production. It should revisit what the homepage is trying to communicate, the role of Bellweather (if any), visual hierarchy, interaction grammar, pacing and mystery before implementation constraints are allowed to harden the answer.

No new production website implementation is authorized by this rollback beyond restoring the exact pre-Bellweather V2.2 public tree.

## Publication gate

Require exact-head repository checks and Cloudflare build, fresh-main race check, merge, exact-main checks, then direct live byte/header/no-analytics/browser verification against the restored ten-file V2.2 public tree.

**Result:** rollback is authorized; concept exploration resumes only after the live restoration is verified.
