<!-- D-R1-STATUS: ACTIVE LAW -->

# Ensemble / Kymaean - APPUI-01 Fresh-Chat Handoff

Status: `PHASE C ACTIVE / APPUI-01 ITERATIVE SCREEN-FIRST / WINDOWS 11 ARM64`
Date: 2026-09-14

Recover live authority through `AGENTS.md` and exact-ref `CURRENT_STATE.md`; this handoff is convenience only. At creation, active serial Design head is `7c14e7d60ad70c0545324e0c6bf35bb288f4fab6`, Website `main` is `5d698484bfb8a8b65b4b9acc429cf3713a522f9b`, and Engineering `main` is `57ec145c09e701e5d62907ae75046f38b5cbe285`. Verify rather than assume.

## Director correction
The current product-design target is a **Microsoft Windows 11 desktop app on ARM64 intended for the Microsoft Store**. Do not design this as a phone/mobile app. The recent mobile-looking chat concept is not product-platform authority and should not be used as the app-shell model.

The Director explicitly ended the weeks-long artwork-first/convergence-first sequence: human artwork is not required for the current app design, and the app should now be made visually good and distinctive through real screens. We are allowed to figure out the design as we go. Existing design research constrains obvious regressions; it must not become a reason to avoid making screens. Pivot evidence SHA-256 `4b21d11345aed8a049f95ae1b40115a3b9650fef32a554d7789765d61a34b9c3`.

CHARART-01 returned one valid first image (SHA-256 `4b793a5bf265d932e581d5b34fd05fa9ed132c3b6d0b2623a26a3c7b3363d6ba`, 1672x941, 3,129,723 bytes), consuming its attempt, but it was not scored, not adopted, and not preserved as a master. CHARART-01 is Director-terminated and must not resume unless explicitly reopened.

## Active work
`APPUI-01 - Windows 11 ARM64 Working App Visual Prototype` is iterative, not a frozen-candidate gate. Make coherent full-window desktop mockups/prototypes, review them as compositions, and revise. Do not wait for final palette/type/artwork/identity completion. Provisional visual choices are allowed when clearly treated as working choices.

First useful surface set:
- Production / Scene overview;
- live Stage workspace;
- selected Character / state inspector;
- Performance / causal-history strip or adjacent history surface.

Use `docs/KYMAEAN_APP_INFORMATION_RELATIONSHIP_ARCHITECTURE_PROPOSAL_01.md`, `docs/KYMAEAN_APP_SHELL_NAVIGATION_GRAMMAR_PROPOSAL_01.md`, `docs/KYMAEAN_APP_TASK_FIRST_LOW_FIDELITY_INTERACTION_PROTOTYPE_01.md`, and `docs/evidence/APP_SYN_01_DESIGN_SOL_WHOLE_SYSTEM_VIEW_01.json` as historical design inputs only. Do not replay them as mandatory gates. Fresh-read current Product/Engineering authority whenever a screen would otherwise invent semantics.

## Preserved constraints
`PKT-STAGE-CORE-02` remains exact Stage authority; compose around it rather than silently redesigning it. CPS-B remains canonical Character presence, but portraits are optional. APPICON E06 remains the app-icon design-master envelope around exact C0. DUR-01 remains PASS evidence. CLR F2/F1 is still unselected: explore color provisionally in mockups without claiming a final palette. Preserve keyboard/focus/state distinction, reduced-motion/static truth, high-contrast intent, privacy/perspective boundaries, and no invented authority semantics.

## Platform boundary
Design for a resizable Windows 11 desktop experience with keyboard/mouse first-class and touch compatibility where natural. Native WinUI/XAML implementation, Windows accessibility validation, ARM64 runtime/performance, MSIX/package identity, WACK/Store certification and Partner Center remain Engineering/outside-lane authority.

## Working rhythm
Prefer one or two substantial app-screen compositions over another abstract framework. Show enough UI to expose hierarchy, density, navigation, Stage adjacency, Character presence, inspector behavior and history placement. Then use Director reaction to improve the next pass. Stop only for a genuinely consequential product/taste decision or an outside-lane semantic dependency.
