# KYMAEAN CONTINUOUS WORKSPACE — GRAYSCALE WIREFRAME 01

Status: DIRECTOR PROPOSAL FOR REVIEW / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Phase: Kymaean App + Website Design Synthesis — structural interaction validation

## Purpose

Create the first concrete low-fidelity wireframe sequence for the accepted principle:

> **Stable Production, fluid focus.**

This artifact tests one continuous creator session without selecting final visual identity, typography, palette, material system, artwork, portrait system, motion language, exact WinUI controls, final Studio/Stage/Archive labels, final Production terminology, final Character Context taxonomy, or final Take/rehearsal/branch UX.

The wireframes are intentionally monochrome and schematic. Their job is to test hierarchy, continuity, disclosure, authority, accessibility, adaptive behavior, and causal comprehension.

---

## 1. Prototype success condition

The sequence succeeds only if the creator can say:

> **I stayed inside one Production. I understood what was happening, followed why it mattered, changed my relationship to the scene, saw what became effective, and returned to the same world with different possibilities.**

It fails if the experience reads as a tour through separate modules.

---

## 2. Persistent shell invariants

Across every frame, preserve only the minimum anchors needed to prevent semantic disorientation:

- current Production identity;
- current Scene identity when a Scene exists;
- current-versus-history status when history is being inspected;
- active Presentation Perspective when disclosure differs;
- authority/effect status when material is provisional or effective;
- Back as navigation history only;
- blocking capability status only when materially relevant.

Everything else may enter or leave focus.

The wireframe intentionally does **not** require a permanent left rail, top tabs, card grid, ribbon, timeline, chat column, or inspector pane.

---

## 3. Frame A — Present / Watch

Primary question:

> **Who is here, what is happening, and what matters now?**

```text
┌──────────────────────────────────────────────────────────────────────┐
│  [Production]                     [Scene]         [Perspective/status]│
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                         PRIMARY HUMAN FIELD                          │
│                                                                      │
│             [Character A]      [Character B]                         │
│                       \        /                                     │
│                        \      /                                      │
│                        [Character C]                                  │
│                                                                      │
│                 current relational/action focus                      │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│  current utterance / action / observed cue                           │
├──────────────────────────────────────────────────────────────────────┤
│ [Inspect context]   [Intervene]   [Take perspective]   [More…]       │
└──────────────────────────────────────────────────────────────────────┘
```

Requirements:

- people and their relationship dominate the primary surface;
- transcript/action detail supports the scene rather than replacing it;
- creator commands are visible but subordinate;
- no full Studio-style metadata wall is present;
- no history summary is visible unless the current scene itself requires one;
- human identity must remain discernible without depending on a fixed photoreal portrait.

O0 regression benchmark:

> **Refined Stage — the people are the scene; software chrome supports them.**

---

## 4. Frame B — Context expansion without leaving the present

Trigger examples:

- inspect a Character;
- inspect a pressure;
- inspect a relationship;
- inspect why a condition matters now.

```text
┌──────────────────────────────────────────────────────────────────────┐
│  [Production]                     [Scene]         [Perspective/status]│
├─────────────────────────────────────────────────┬────────────────────┤
│                                                 │ CONTEXT            │
│               PRIMARY HUMAN FIELD               │                    │
│                                                 │ selected person /  │
│      [A]             [B]                        │ relationship /     │
│             [C]                                 │ pressure           │
│                                                 │                    │
│      present action remains legible             │ relevant current   │
│                                                 │ conditions         │
│                                                 │                    │
│                                                 │ [Why?] [History]   │
├─────────────────────────────────────────────────┴────────────────────┤
│ [Return focus]                task-relevant creator commands          │
└──────────────────────────────────────────────────────────────────────┘
```

Requirements:

- context is adjacent meaning, not a destination;
- selected-object identity is preserved;
- the present remains visible on wide layouts but need not remain side-by-side on narrow layouts;
- the inspector must explain why surfaced information is relevant;
- creator-only information must disappear when bounded perspective forbids it.

This is where historical Studio insight is reused without restoring Studio as a mandatory root tab.

---

## 5. Frame C — Causal trace / historical focus

Trigger:

> **Why is this true now?**

```text
┌──────────────────────────────────────────────────────────────────────┐
│ [Back] [Production] [Scene]      HISTORICAL FOCUS      [Current →]   │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  CURRENT CONDITION                                                   │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │ selected present condition / relationship / unresolved pressure│  │
│  └────────────────────────────────────────────────────────────────┘  │
│                              ▲                                       │
│                              │ consequence                           │
│  EFFECTIVE PRIOR EVENT       │                                       │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │ accepted event / performance consequence                       │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                              ▲                                       │
│                              │ relevant prior condition              │
│  PRIOR CONTEXT                                                        │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│ [Return to current condition]       [Inspect related consequence]    │
└──────────────────────────────────────────────────────────────────────┘
```

Requirements:

- historical inspection is unmistakably historical;
- current authoritative Production remains a retained destination;
- chronology is secondary to causal explanation;
- Back means prior focus, not undo;
- no historical item becomes mutable current state merely because it is selected;
- causal history may show multiple contributing events if product truth later requires it; this wireframe does not freeze a one-parent model.

O0 regression benchmark:

> **Refined Archive — history answers what changed and why it matters now.**

---

## 6. Frame D — Character-bounded perspective

Trigger:

> **Experience the current Production through one Character's permitted disclosure boundary.**

```text
┌──────────────────────────────────────────────────────────────────────┐
│ [Production] [Scene]      PERSPECTIVE: CHARACTER       [Exit view]   │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                     SAME PRIMARY HUMAN FIELD                         │
│                                                                      │
│         what this perspective can perceive / access                  │
│                                                                      │
│              unavailable creator-only context omitted                │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│ AVAILABLE TO THIS PERSPECTIVE                                        │
│ relevant cues / memories / known information only where product      │
│ authority supports them                                              │
├──────────────────────────────────────────────────────────────────────┤
│ [Act/perform if allowed]                    [Return to creator view]  │
└──────────────────────────────────────────────────────────────────────┘
```

Requirements:

- same Production identity and Scene identity remain legible;
- disclosure changes, not reality;
- privileged creator inspectors close or redact rather than leak;
- the UI must not imply unsupported certainty about private mind;
- perspective state is programmatically exposed for assistive technology;
- exiting bounded perspective restores the prior creator focus when possible.

O0 regression benchmark:

> **Take a Seat / Character View — perspective should feel lived, not like a cosmetic filter.**

---

## 7. Frame E — Provisional performance / creator authority boundary

Purpose:

Test the distinction:

```text
PERFORMANCE MATERIAL ≠ AUTOMATICALLY EFFECTIVE HISTORY
```

```text
┌──────────────────────────────────────────────────────────────────────┐
│ [Production] [Scene]               PROVISIONAL MATERIAL              │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                   performance / take under review                    │
│                                                                      │
│        people and performed action remain the primary content        │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│ STATUS: not yet effective in authoritative history                   │
│                                                                      │
│ [Review consequence]      [Accept/effect]*      [Reject/retain]*      │
└──────────────────────────────────────────────────────────────────────┘
```

`*` These command labels are placeholders for interaction testing only. Final Take/accept/reject/rehearsal semantics remain governed by `Rylascoo/Ensemble-Project` and are not frozen here.

Requirements:

- provisional status must be understandable without color;
- technical capability failure must never masquerade as fictional rejection;
- the user cannot confuse preview/rehearsal material with effective Production history;
- this state must degrade truthfully when AI capability is unavailable.

---

## 8. Frame F — Consequence recognition

Immediately after an accepted/effective boundary, show the smallest useful explanation of what changed.

```text
┌──────────────────────────────────────────────────────────────────────┐
│ [Production] [Scene]             EFFECTIVE CONSEQUENCE               │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ WHAT CHANGED                                                        │
│ ┌────────────────────────────────────────────────────────────────┐   │
│ │ concise changed condition / relationship / access / pressure   │   │
│ └────────────────────────────────────────────────────────────────┘   │
│                                                                      │
│ STILL IN MOTION / UNRESOLVED                                         │
│ ┌────────────────────────────────────────────────────────────────┐   │
│ │ consequence that remains active or incomplete                  │   │
│ └────────────────────────────────────────────────────────────────┘   │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│ [Trace why]                                  [Return to present]     │
└──────────────────────────────────────────────────────────────────────┘
```

`What Changed` and `Still in Motion` are historical benchmark language, not selected final copy.

Requirements:

- consequence is expressed as changed present/future condition, not celebration animation;
- no artificial requirement that every accepted event produce a dramatic visible change;
- unchanged dimensions may remain unstated;
- causal explanation can be inspected but should not trap the user in history.

---

## 9. Frame G — Return to changed present

This is the decisive frame.

```text
┌──────────────────────────────────────────────────────────────────────┐
│  [Production]                     [Scene]         [Perspective/status]│
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                         PRIMARY HUMAN FIELD                          │
│                                                                      │
│             [Character A]      [Character B]                         │
│                       \        /                                     │
│                        \      /                                      │
│                        [Character C]                                  │
│                                                                      │
│         same persistent people / altered current relationship        │
│                                                                      │
├──────────────────────────────────────────────────────────────────────┤
│ CURRENT CONDITION: changed consequence is now part of the present    │
├──────────────────────────────────────────────────────────────────────┤
│ [Continue]   [Inspect what changed]   [Direct]   [Take perspective]  │
└──────────────────────────────────────────────────────────────────────┘
```

Success feeling:

> **I am back in the same world, but it is different because of what happened.**

Requirements:

- same Production and Character identities persist;
- change is semantically legible without requiring animation;
- current possibility is visibly affected where consequence warrants it;
- the interface does not dump the user onto an Archive/summary page;
- next action emerges from the changed present.

---

## 10. Adaptive layout translation

The semantic sequence must survive window width changes.

### Wide

May use:

```text
[scope/context] [primary human field] [contextual inspector]
```

Only when the adjacent pane genuinely improves comprehension.

### Medium

Prefer:

```text
[scope/context]
[primary human field]
[context drawer / temporary detail]
```

The primary field remains dominant.

### Narrow

Prefer sequential focus:

```text
CURRENT PRESENT
   ↓ inspect
CONTEXT DETAIL
   ↓ back
CURRENT PRESENT
```

Requirements:

- no essential meaning depends on simultaneous panes;
- focus return is deterministic;
- history/perspective/provisional status remain explicit in text/semantics;
- touch targets have keyboard equivalents;
- the complete causal session remains possible in one window.

---

## 11. Keyboard / assistive-technology traversal

Minimum semantic traversal order:

1. application/scope navigation;
2. Production + Scene identity;
3. perspective/current-history/effect status when active;
4. primary human field or equivalent structured participant/action content;
5. selected contextual content;
6. task commands;
7. secondary help/diagnostics.

When an inspector closes or historical focus ends, focus returns to the invoking object or a meaningful successor.

No state distinction may rely solely on:

- color;
- glow;
- portrait treatment;
- spatial distance;
- animation;
- multi-pane simultaneity.

---

## 12. ARM64 / battery implications

This wireframe intentionally requires no continuous computation.

The UI can remain semantically complete while idle with:

- no graph physics;
- no ambient relationship animation;
- no continuous timeline movement;
- no polling for unchanged state;
- no idle AI inference;
- no persistent NPU/GPU work.

Richness may later be added only if it becomes fully quiescent when nothing changes.

---

## 13. Recursive audit corrections

The first wireframe pass produced material corrections and was restarted after each one.

Corrections:

1. removed a permanent three-column layout that would have made Studio/Stage/Archive semantics spatially fixed;
2. removed a permanent timeline from the shell because it made history an incumbent destination;
3. replaced a transcript-dominant live view with a human-field-dominant hierarchy;
4. made historical focus explicitly labeled and added a direct return-to-current affordance;
5. removed creator-only inspector persistence from Character-bounded perspective;
6. made provisional/effective status text-semantic rather than badge-color dependent;
7. separated technical capability failure from fictional or creator rejection state;
8. removed the assumption that every accepted event produces a dramatic consequence card;
9. ensured narrow layout can complete the same causal session sequentially;
10. required Frame G to restore selected Production/Scene/Character continuity rather than return to a generic workspace root.

Final recursive pass:

```text
product truth                    PASS
authority                        PASS
scope                            PASS
user model                       PASS
information architecture         PASS
O0 experiential continuity       PASS
accessibility                    PASS
Windows-native feasibility       PASS
ARM64/battery suitability        PASS
privacy/disclosure               PASS
implementation simplicity        PASS
distinctiveness                  PASS
surface inheritance              PASS
evidence quality                 PASS
contradictions                   PASS
open decisions preserved         PASS
```

No material correction or worthwhile structural improvement remains in this proposal pass.

---

## 14. Director gate

Approve or reject the structural wireframe thesis:

> **Kymaean's first concrete app prototype should be one persistent, human-centered Production workspace whose structure transforms according to present attention, context, causal inspection, bounded perspective, provisional/effective authority, consequence, and return to the changed present—without turning those concepts into permanent navigation silos.**

If approved, the next justified design question is no longer basic information architecture.

It becomes:

> **What visual-system grammar can make these structural states unmistakably Kymaean while preserving human primacy, Windows-native usability, accessibility, quiescent ARM64 behavior, and the project's surface-quarantine laws?**

That is the boundary where visual-system exploration may begin. No production XAML/C# is authorized by this artifact.
