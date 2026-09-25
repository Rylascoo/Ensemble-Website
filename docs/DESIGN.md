# Design system

## Idea

The site is a stage before the performance. The visitor arrives in a dark house, the lights come
up, and the only thing standing on the stage is the name. The page should feel like a premiere
that hasn't opened yet: theatrical without theatre props, mysterious without being vague about
what it is — a release notice.

## Fixed elements

| Element | Source | Notes |
|---|---|---|
| Threshold K | `brand/threshold-k-*.svg` | Symbol and first letter of the wordmark. |
| Wordmark | `brand/kymaean-wordmark-*.svg` | Custom monoline letters, `KYMÆAN`. Geometry is final. |
| Stage | `site/public/assets/img/stage.webp` | 1672×941. See provenance below. |

Stage provenance: encoded from a 1672×941 PNG, SHA-256 `5234c02b0b9d076964b6cec465b253cc37e89bac37328d89d6fd978fefea36fa`
(2,467,967 bytes); the WebP is SHA-256 `8e7c0bf3cbbe1f466f77d70d59d4310ff6d5c6a97f9e1741d35bf21a7d18e2a8`.
Known limit: on screens wider than ~1700 CSS px the image is upscaled and softens. A higher-resolution
master is being located; when found it goes to Drive and a new WebP is encoded from it.

## Tokens

| Token | Value | Use |
|---|---|---|
| `--void` | `#000000` | Page background. Matches the image's own edge pixels, so there is no seam. |
| `--ink` | `#ddd5c7` | Wordmark and primary text. Warm ivory, lit by the amber lamp. |
| `--ink-2` | `#c4bbad` | Release line and secondary text. 11.1:1 on black; 9.7:1 on the stage floor. |

Type: **Josefin Sans 300** (SIL OFL), self-hosted. Chosen because it shares the wordmark's
monoline stroke and pointed apexes, so the release line reads as part of the same identity.
Release line: uppercase, tracking 0.44em, `clamp(.78rem, .6rem + .5vw, 1.2rem)`.

## Composition

A single `.frame` has the stage image's exact aspect ratio and covers the viewport. Every element
is positioned in percentages of that frame, so it lands on the same spot of the stage at any size.

```
 ┌──────────────────────────────────────────┐
 │               IN REHEARSAL               │  ← hangs above the arch crown (14%)
 │  amber             ╭──╮            blue  │
 │   lamp             │  │            lamp  │
 │                    │  │                  │
 │ ═══════════════════╧══╧════════════════  │  ← stage rim (~60%)
 │                 KYMÆAN                   │  ← stands on the floor (63.2%)
 │                 (reflection)             │
 │ ──────────────────────────────────────── │  ← apron (~80%)
 └──────────────────────────────────────────┘
```

- **Portrait:** the whole stage stays in view at 190vw wide (165vw on tablets), centred slightly
  low; the image fades into the black house above and below.
- **Short landscape** (phones on their side): the release line moves under the name and the
  reflection is dropped, because the field above the arch is too shallow.
- **Ultrawide:** the release line clamps to the top of the viewport.

## Motion

One choreographed moment: house lights. A black layer over the page opens at the amber lamp,
then the blue lamp, then the room; the release line is revealed by the light and the name arrives
on the floor (1.5 s). It plays once per browser session; any key, click, scroll or touch skips to
the end. Reduced motion shows the final frame immediately. Nothing else moves.

## Voice

Release notices, not marketing. Short, declarative, theatrical vocabulary used literally
("In Rehearsal", "This part of the house isn't open yet"). No exclamation marks, no superlatives,
no description of the product before launch.

Alternatives to "In Rehearsal" considered: Coming Soon (previous), Opening Soon, Curtain Soon.
Changing it means editing `index.html` (visible text, `<title>`, descriptions), `tools/card.html`
and re-rendering the social card.
