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
| Wordmark | `brand/kymaean-wordmark-*.svg` | "Kymaean hand", cut letters. Generated; see Lettering. |
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

## Lettering

**Everything is cut, nothing is drawn.** The name and the release line are lettering, not type.
They come from `brand/wordmark/kymaean_wordmark.py`:

- **Source.** Letter habits of the alphabet that reached Italy through Kyme: a splayed M, a leaning
  N, crossbars that share one slope. Kyme shapes the construction, never the ornament: no Greek
  letters, keys, columns or inscription pastiche.
- **Construction.** Each stroke is a chisel cut that widens slightly toward its outer ends; joints
  keep plain width and close with a bevel; ends on the cap or base line are cut flush; horizontals
  are lighter so every stroke reads equal. Every letter in KYMÆAN is a straight stroke, which is why
  the name can be cut this way.
- **Spacing.** Optical: each pair's row-by-row whitespace is solved to the same target.
- **Release line.** Same hand, heavier stroke because it is set small; ships as
  `assets/img/release.svg` so it is the page's first contentful image.

**The mark system.** The Threshold K alone is the app icon and favicon (solid; it holds down to
16 px). Beside the name it appears only in the stacked lockup, preferably cut as an outline so it
rhymes with the letters (`brand/kymaean-lockup-stacked-cut-*.svg`). Never set the K immediately
before the name: it reads "K KYMÆAN".

**Two lights** (amber and blue) is an expression for large moments only. It fails below about
150 px, where the colours blur, so the everyday name is always one colour.

Type: the homepage loads no font. **Josefin Sans 300** (SIL OFL) is used only for sentences, such as
the 404 page.

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
Changing it means editing the release skeletons in the generator, the text in `index.html`
(screen-reader text, `<title>`, descriptions), and re-rendering the social card.
