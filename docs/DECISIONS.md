# Decisions

Newest first. Each entry: what was decided, by whom, and why.

## 2026-09-25 — Wordmark 02: Kymaean hand

- **Decision (Director).** The name is set in "Kymaean hand": cut lettering derived from the letter
  habits of the alphabet that passed through Kyme, built on the principle "everything is cut,
  nothing is drawn". Chosen over 12 other constructions across three rounds (boards preserved
  outside the repository); it was the only candidate that is both unmistakable and legible from
  480 px down to 90 px wide on the live stage.
- **System.** The Threshold K stays the mark: alone as the app icon and favicon (solid); beside the
  name only in the stacked lockup, preferably as a cut outline. The K is never set directly before the
  name. Two lights (amber and blue) is reserved for large moments; it blurs below about 150 px.
- **Release line.** Redrawn in the same hand. The homepage now loads no font (−12 KB), and the release
  line ships as an image so desktop keeps a largest-contentful-paint candidate. In high-contrast mode
  the drawn line gives way to real text in the system colours.
- **Source of truth.** `brand/wordmark/kymaean_wordmark.py`: geometry is generated with shapely
  (Linux, CI) into `geometry.json`; assembly into brand files and `index.html` has no dependencies.
  CI regenerates and fails on any difference.
- **Name check (first pass, not legal clearance).** No registered "Kymaean" mark found. Nearest:
  Kyma (sound-design software) and a pending "Kymabridge" (pharma SaaS). "Kymaean" was also the stock
  fool of the ancient joke book *Philogelos*. A proper trademark search is needed before launch.
- **Secrecy finding.** Searching "Kymaean" returns this repository's history and the public
  Ensemble-Project repository (Windows ARM64 app, `Kymaean.*` code names, pull requests). The codename
  does not hide the product. Flagged to the Director; no change made here.

## 2026-09-24 — Archival branch cleanup (one-time exception)

- **Authority.** One-time exception authorized by the Director, agreed with the Project side.
  Normal branch rules (AGENTS.md, Branches) are unchanged.
- **Before:** 176 branches besides `main`; 127 archive tags.
- **Retired: 170 branches.**
  - 25 were already safe: 20 fully merged into `main`, 4 identical to an existing archive tag,
    1 contained in an existing archive tag.
  - 145 had unique commits. Each tip was tagged `archive/branch/<original name>`, verified locally
    and again on GitHub, and only then deleted. Their status, recorded in each tag message:
    - 100 superseded: every changed file already exists in `main` history or archive tags;
    - 41 historical: exploration never integrated, preserved only by its tag;
    - 3 app lineage, cleared by the Project side (preserved by Ensemble-Project PR #275);
    - 1 obsolete: `renovation/w1-txt-corpus-coverage`, tooling for the retired docs corpus.
- **Kept: 6 branches with open pull requests** (list them with `gh pr list`). They await a
  Director decision on closing the pull requests.
- **Tags:** all 127 existing archive tags kept; 146 added (`archive/pre-renovation-2026-09-24`
  plus the 145 branch tags). Full map:
  `git for-each-ref refs/tags/archive/branch --format="%(refname:short) %(*objectname)"`.

## 2026-09-24 — App-design material leaves the Website

- The Project side audited all Website history (snapshot `43801c0b`, Q-ADMIN-05 source `846c60ee`,
  every branch). Q-ADMIN-05 was substantially complete; 38 further app-design source objects are
  preserved in Ensemble-Project PR #275 (candidate `78f6ad98`). Nothing app-related needs to stay
  in this repository's working tree.

## 2026-09-24 — Renovation 01

- **Ownership.** The Director assigned website design, implementation and repository organisation
  to Claude. ChatGPT works on the app in Ensemble-Project. Production changes still require the
  Director's approval.
- **Scope of the repository.** This repository now holds the website only. App design, design
  research, prototypes, character studies and the previous governance documents were removed from
  the working tree; everything removed is preserved at `archive/pre-renovation-2026-09-24`.
- **Secrecy.** Nothing about the product is disclosed until the app is finished and shipped.
- **Kept.** Threshold K, the KYMÆAN wordmark geometry and the stage image, unchanged.
- **Changed.**
  - The name now stands on the stage floor with a faint reflection. The previous placement
    collided with the arch and was cropped away on ultrawide screens.
  - The release line changed from "Coming Soon" to "In Rehearsal" (Director's choice) and now
    hangs above the arch.
  - A house-lights opening: the page starts dark, the lamps and then the room come up, the release
    line is revealed by the light and the name arrives on the floor. It plays once per session,
    can be skipped, and is off under reduced motion.
  - Added a self-hosted typeface (Josefin Sans 300), a themed 404 page, security headers with a
    strict CSP, and content-hashed assets cached immutably.
  - Removed unused files (`motion.js`, two unused stylesheets, the retired `stage-v2-2.webp`).
- **Measured (local build, 2026-09-24).** Lighthouse 100/100/100/100 on mobile and desktop;
  LCP 1.9 s mobile (simulated slow 4G) and 0.5 s desktop; CLS 0; axe: no violations at 1440 px,
  320 px and on the 404 page. An `<img>` covering the whole viewport was not reported as an LCP
  candidate in this build; making the release line present from the first frame fixed it.
