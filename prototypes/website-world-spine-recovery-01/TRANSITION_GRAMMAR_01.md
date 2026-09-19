# Website World Spine — Transition Grammar 01

Status: **NON-PRODUCTION TRANSITION STUDY / VISUAL LANGUAGE ONLY**

Parent study: `prototypes/website-world-spine-recovery-01/index.html`

## Core problem

The recovered V0 Site Spine contains useful narrative order, but its historical execution reads as assembled sections. The new world-spine study fixes section hierarchy, but it still needs a transition language that proves the page is one continuous world rather than a stack of themed modules.

The transitions should therefore reuse visible matter from the outgoing state as the structural origin of the incoming state.

No transition may depend on:
- app UI;
- product state names;
- mascot presence;
- a literal portal;
- full-screen loading/interstitial tricks;
- decorative particles;
- generic parallax for its own sake.

## T1 — STAGE → PLACE

**Carrier:** the Stage horizon.

The hero does not simply fade out. As the visitor leaves the opening frame, the broad Stage geometry darkens and loses photographic detail while one horizontal light/contact line remains. That line becomes the first structural rule of the next section.

Meaning:
the website has not left the Stage; it has abstracted it.

Avoid:
- abrupt black cut;
- image shrinking into a card;
- hero screenshot becoming a product panel.

Reduced motion:
the hero ends with the same horizon line already aligned to the next section.

## T2 — PLACE → PERSPECTIVE

**Carrier:** one continuous field dividing into multiple apertures.

The single shared field develops vertical occlusion/masking boundaries. The result is three partial views of the same environment, not three independent cards.

Meaning:
different availability does not require different worlds.

Avoid:
- three bordered cards entering separately;
- carousel affordances;
- arrows or connector diagrams;
- different images implying separate scenes.

Reduced motion:
show the already-divided shared field with continuous background alignment.

## T3 — PERSPECTIVE → CONSEQUENCE

**Carrier:** the central division becomes a causal/material scar.

One aperture boundary acquires physical weight. The line widens irregularly, picks up restrained oxidized-copper warmth, and the surrounding surface changes from deep slate to limestone beginning at that disturbance rather than via a global theme fade.

Meaning:
what changes the world should deform what follows.

This is the strongest transition in the system and should be the clearest material transformation.

Avoid:
- white flash;
- generic dark/light mode crossfade;
- warm color flooding the page;
- timeline animation.

Reduced motion:
the limestone field begins with the scar already crossing its upper edge, visibly inherited from the prior section.

## T4 — CONSEQUENCE → PARTICIPATION

**Carrier:** the scar resolves into a spatial axis.

As the limestone sequence completes, the scar narrows into a neutral axis/void. The limestone recedes around that axis, revealing a dark shared scene at its center. Peripheral relational positions emerge from distance, not from card containers.

Meaning:
the changed field becomes a place one can relate to.

Avoid:
- four equal option cards;
- labeled product modes;
- radial menu UI;
- CTA-like colored nodes.

Reduced motion:
show the dark spatial field immediately after the limestone section with one aligned vertical axis preserving continuity.

## T5 — PARTICIPATION → IDENTITY RETURN

**Carrier:** the central scene simplifies rather than expands.

Peripheral spatial evidence recedes first. The center remains, then loses descriptive detail until only proportion, negative space and the neutral identity field survive. The KYMÆAN mark returns into that cleared field.

Meaning:
the website can widen conceptually without making the brand louder.

Avoid:
- feature-summary grid;
- oversized conversion CTA;
- explosive logo reveal;
- replaying the hero image.

Reduced motion:
final identity section begins with the same center alignment as the prior scene.

## Motion law

Motion should expose continuity, not provide entertainment.

Preferred:
- slow spatial continuity;
- masking/occlusion;
- material inheritance;
- restrained scale change;
- opacity only when paired with structural continuity.

Do not use:
- spring/bounce;
- constant floating objects;
- autoplay narrative performance;
- high-frequency scroll effects;
- scroll-jacking.

The user always owns scroll position.

## Responsive law

Mobile must preserve **transition cause**, not mimic desktop geometry.

Examples:
- T2 may become stacked apertures, but a shared background registration must prove they belong to one scene.
- T3 scar may move diagonally/vertically as needed, but must visibly originate from the preceding division.
- T4 peripheral relations may distribute above/below the center rather than four corners.
- T5 identity return preserves center alignment.

Do not shrink desktop transition compositions wholesale.

## Accessibility law

Every state must read completely with motion removed.

`prefers-reduced-motion`:
- no scroll-timeline animation;
- no meaning hidden behind intermediate motion;
- inherited carriers appear statically at section boundaries.

Forced colors:
- decorative imagery/material fields may disappear;
- section order, headings and semantic text remain legible;
- carriers should fall back to system-color borders rather than vanish when they aid structure.

## Current recommendation

Advance **T3 Perspective → Consequence** as the first transition to stress-test visually.

Reason:
it is the most distinctive inherited Kymaean grammar, links Quiet Stage to Mineral Theater, and directly tests whether the website can feel causally continuous instead of thematically sectioned.

Do not build all transitions into production code. First prove T3 in isolation, then T1/T2/T4/T5.
