# Launch site plan

The teaser stays up until the app ships. At release, secrecy ends and this site becomes the
place that explains Kymaean and sends people to get it. This plan is what gets built ahead of
time, on a branch, so it is ready on launch day.

## Principle

The teaser becomes the first frame. Visitors land on the same stage and name they have seen for
months; scrolling carries them past the arch into the explanation. Nothing the site claims may
exceed what the shipped app does, as recorded in `Ensemble-Project`.

## Pages

| Page | Purpose | Needed by |
|---|---|---|
| `/` | Narrative home: stage → what Kymaean is → how it works → get it | Launch |
| `/privacy` | Privacy policy (what the app collects, stores, sends) | Store submission |
| `/support` | How to get help, contact, system requirements | Store submission |
| `/accessibility` | Accessibility statement for the site and the app | Launch |
| `/press` | Name, logo files, stage image, short description | Optional |

`/privacy` and `/support` must be live before the Microsoft Store submission, because Partner
Center asks for their URLs. They can publish without breaking secrecy if written generically,
or go live together with the launch.

## Inputs needed from Ensemble-Project

- Supported Windows versions and architectures (ARM64 only, or x64 as well).
- What leaves the device: remote AI providers, telemetry, crash reports; how credentials are kept.
- The product vocabulary that is safe to use publicly.
- The richest behaviour the release actually supports (so demos never overstate it).
- Store listing ID, name reservation, price.

## Technical direction

Stay framework-free while the site is one page. When the launch site grows past three pages,
move `site/` to Astro with static output, keeping the same Worker, headers and budgets: no
third-party requests, ≤ 30 KB of JavaScript on first view, Lighthouse 100.
