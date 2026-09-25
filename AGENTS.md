# Working in this repository

Read this before changing anything. It is short on purpose.

## Start here (fresh chat)

1. `README.md`: what this is and where everything lives.
2. This file: the rules.
3. `docs/DESIGN.md`: the design system (composition, tokens, type, motion, voice).
4. `docs/DECISIONS.md`: newest entry first; this is the current state.
5. Check the live site against `main`; it deploys automatically.

Product facts come from `Rylascoo/Ensemble-Project` (`CURRENT_STATE.md`). Visual masters live in
Google Drive, `Ensemble Project`. Nothing else is needed to work on the website.

## Who decides

- The **Director** (repository owner) approves anything that reaches production and owns
  product meaning and final taste.
- **Claude** owns website design and implementation, and keeps this repository organised.
- Product facts (what the app does, platforms, data handling) come only from `Ensemble-Project`.
  If a page needs a fact that isn't established there, don't write it.

## Rules

1. **Secrecy until ship.** Until the app is released, the public site says nothing about what
   Kymaean is or does. No product description, feature, screenshot, platform, audience or date.
2. **Brand constants.** The Threshold K, the KYMÆAN wordmark geometry and the stage image are
   fixed. Don't redraw, re-letter, recolour or regenerate them. Everything else can change.
3. **One place for each thing.** Deployable files live in `site/public/`. Masters in `brand/` and
   Drive. Decisions in `docs/DECISIONS.md` (append, newest first). No other state files.
4. **Budgets.** Everything in `site/public/` totals ≤ 400 KiB; first view needs no JavaScript to
   render; Lighthouse 100 in all four categories on mobile and desktop is the standard, not the goal.
5. **Accessibility is a floor.** Reduced motion, forced colours, keyboard and 320 px width must
   all work. Text contrast ≥ 7:1 on its actual background.
6. **No third-party requests.** No external fonts, scripts, analytics or embeds. The CSP enforces it.

## How to change the site

1. Branch from `main` (`site/<short-name>`).
2. Edit files in `site/public/`, then `node tools/site.mjs stamp` and `node tools/site.mjs check`.
3. Review renders at 1440×900, 2560×1080, 390×844, 844×390 and 768×1024, plus reduced motion.
4. Push, open a pull request, and review the Cloudflare preview URL.
5. The Director approves; merge to `main`; confirm the live site serves the new bytes.
6. Record anything consequential in `docs/DECISIONS.md`.

## Branches

A branch may be deleted only when it has no unique commits (`git rev-list --count main..<branch>`
is 0). A branch with unique commits stays until its content is explicitly dispositioned by the
Director. The archival cleanup of 2026-09-24 was a one-time, Director-authorized exception
(see `docs/DECISIONS.md`); it is not a precedent. Never delete or move an `archive/` tag.

## Retired material

Design research, app-design material, character studies and the old governance documents were
removed from the working tree on 2026-09-24. They remain intact in Git history (see README,
History). Do not restore them into the working tree; `tools/site.mjs check` fails on retired terms.
