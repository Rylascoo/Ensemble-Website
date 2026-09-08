ENSEMBLE WEBSITE / KYMAEAN — WEBSITE UPDATE PLANE

Status: ACTIVE NON-DEPLOYABLE CHANGE / RELEASE RECORD BOUNDARY
Created: 2026-09-08

PURPOSE
`updates/` is the non-deployable change-management plane for the Kymaean public website.

It holds website change packets, release notes, migration notes and deployment records. It must never become a second copy of executable website source.

SOURCE OF TRUTH
- Deployable website source/configuration: `../site/` only.
- Website/design intelligence and governance: `../intelligence/` plus the established `../docs/` / `../tools/` authority surfaces.
- Product/backend implementation: `Rylascoo/Ensemble-Project`.

CHANGE LIFECYCLE
1. Start from current `main` on a scoped branch such as `site/<work-package>`.
2. Record a change packet here when the work needs durable scope, release or deployment accounting.
3. Implement executable/public changes only under `site/`.
4. Run repository-boundary, site-specific and any implementation-required validation.
5. Merge the audited change back to `main`.
6. When deployment is authorized and performed, record the exact deployed commit, Cloudflare project/environment and material release notes here.

BOUNDARIES
- Files in `updates/` are not served by Cloudflare.
- Do not import or copy code from `updates/` into the running site at build time.
- Do not use this directory to bypass `site/` publication review.
- Do not place secrets, API tokens, credentials or environment values here.

SUBDIRECTORIES
Create scoped subdirectories only when the first real record requires them. Do not manufacture empty `pending/` or `released/` hierarchies before there is a real update to track.
