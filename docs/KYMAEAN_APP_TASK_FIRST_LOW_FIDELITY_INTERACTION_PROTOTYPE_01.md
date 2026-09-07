<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN APP TASK-FIRST LOW-FIDELITY INTERACTION PROTOTYPE — PROPOSAL 01

Status: DIRECTOR PROPOSAL FOR REVIEW / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Phase: Kymaean App + Website Design Synthesis — interaction validation after shell/navigation grammar

Current basis:

- `docs/KYMAEAN_EXPERIENCE_ONTOLOGY_SYNTHESIS_01.md`
- `docs/KYMAEAN_APP_INFORMATION_RELATIONSHIP_ARCHITECTURE_PROPOSAL_01.md`
- `docs/KYMAEAN_APP_SHELL_NAVIGATION_GRAMMAR_PROPOSAL_01.md`
- `docs/KYMAEAN_APP_WEBSITE_DESIGN_SYNTHESIS_BLUEPRINT_01.md`
- O0 Original Concept Foundation in Google Drive, used only as experiential benchmark evidence
- `Rylascoo/Ensemble-Project/CURRENT_STATE.md` for current implementation/validation boundaries

This document proposes the first low-fidelity interaction prototype needed to test the accepted architecture principle:

> **Stable Production, fluid focus.**

It does not select final labels, visual identity, typography, palette, material system, portrait system, animation language, final Stage/Studio/Archive layouts, exact WinUI controls, final Take/rehearsal semantics, Character Context disclosure categories, or production XAML/C#.

---

## 1. Prototype question

The prototype should answer one high-leverage question:

> **Can a creator complete one meaningful causal session while continuously feeling that they remain inside one persistent Production rather than moving among disconnected software modules?**

The test session should contain enough structure to exercise:

- current possibility;
- present performance;
- causal history;
- Watch / Direct / Perform relationships;
- bounded Presentation Perspective;
- current-versus-history distinction;
- provisional-versus-effective performance distinction;
- consequence changing future possibility;
- return to the changed present;
- graceful degradation semantics;
- keyboard/screen-reader/reduced-motion viability.

The prototype is intentionally task-first. It does not begin from a navigation sitemap or component inventory.

---

## 2. Experiential target

The creator should be able to experience the session approximately as:

```text
I am with these people.
Something is happening.

I can understand the circumstances without leaving the moment.
I can watch.
I can intervene.
I can temporarily inhabit someone's bounded perspective.

Something happens.
It becomes part of history.
It changes something.

I can understand what changed and why it matters now.
Then I am back with the same people in a world that is no longer quite the same.
```

The app should not require the creator to think in terms of:

```text
Possibility Mode
Performance Mode
History Mode
Authority Mode
Perspective Mode
```

Those are architecture concepts beneath the experience.

---

## 3. O0 experiential benchmarks

The recovered O0 screens are not layout templates. They provide three benchmark tests for this prototype.

### Benchmark A — Refined Stage

Question:

> **Can people and relationships become more important than software chrome during live performance?**

Success means:

- people are the primary semantic focus;
- current action and social attention are legible;
- transcript/text supports the scene rather than replacing it;
- creator machinery recedes until needed;
- current context can be inspected without converting the live experience into a dashboard.

### Benchmark B — Refined Character View / Take a Seat

Question:

> **Can a change in disclosure perspective materially transform the creator's experience of the same Production without implying a different reality?**

Success means:

- privileged creator-only information recedes appropriately;
- the Character-bounded experience is semantically coherent;
- the Character remains the same persistent person;
- returning restores the prior creator context predictably;
- the design does not require freezing the O0 psychological category list.

### Benchmark C — Refined Archive

Question:

> **Can history answer `what changed and why does it matter now?` instead of only `what happened before?`**

Success means:

- accepted history is distinct from transcript chronology;
- consequence is inspectable;
- unresolved movement remains visible where supported;
- the creator can follow a cause forward into current conditions;
- returning from history restores the prior current focus.

If the low-fidelity prototype is architecturally clean but fails these three experiential tests, it should be considered weaker than the original conceptual lineage.

---

## 4. Prototype content boundary

Use one deliberately small illustrative Production scenario.

Prototype content exists only to exercise interaction and should not become product canon, visual seed authority, or engine schema.

Recommended test cast:

- three persistent Characters;
- one current Scene;
- one salient relationship tension;
- one bounded piece of asymmetric information;
- one current pressure/opportunity;
- one creator intervention opportunity;
- one provisional Performance;
- one accepted Performance outcome;
- one consequential state change;
- one unresolved implication that matters to the next moment.

Historical O0 names such as Wren, Marlowe, and Voss may be reused as recognizable test-fixture names if useful, but no historical surface, portrait treatment, wording hierarchy, or exact screen layout is inherited by doing so.

---

## 5. Prototype spine

The prototype should cover one complete interaction loop:

```text
OPEN / RESUME PRODUCTION
        ↓
CURRENT SCENE / WATCH
        ↓
INSPECT RELEVANT CONTEXT
        ↓
RETURN TO CURRENT SCENE
        ↓
DIRECT / INTERVENE
        ↓
OPTIONAL CHARACTER-BOUNDED PERFORMANCE
        ↓
PROVISIONAL PERFORMANCE
        ↓
ACCEPTED / EFFECTIVE PERFORMANCE BOUNDARY
        ↓
WHAT CHANGED?
        ↓
TRACE CAUSE / HISTORY
        ↓
RETURN TO CHANGED PRESENT
        ↓
NEXT POSSIBILITY IS DIFFERENT
```

The prototype succeeds only if these transitions feel like one causal continuum rather than a tour through product sections.

---

## 6. State 01 — Resume the Production

### User task

Understand where things currently stand and resume meaningful work quickly.

### Required information

- Production identity;
- current Scene identity/context;
- current participants;
- current Presentation Perspective if it affects disclosure;
- one concise current tension/pressure summary;
- indication of whether a Scene is active, paused, awaiting action, or otherwise current;
- capability limitation only when it blocks a relevant action.

### Low-fidelity structure

```text
┌─────────────────────────────────────────────────────────────┐
│ [Back/app scope]  [Production identity]        [App actions]│
├─────────────────────────────────────────────────────────────┤
│ Current Scene: [scene]       Perspective: [current state]   │
│ [brief circumstance / pressure summary]                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                 CURRENT PEOPLE / SCENE                      │
│                                                             │
│      [Character]        [Character]        [Character]      │
│                                                             │
│                 [current action / silence]                  │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ [Watch/resume] [Inspect context] [Intervene when relevant]  │
└─────────────────────────────────────────────────────────────┘
```

### Test

The user should understand the present situation without first entering a setup/dashboard screen.

---

## 7. State 02 — Watch the live Scene

### User task

Experience present performance with minimal machinery.

### Primary semantic focus

- people;
- relationship geometry / attention;
- current action;
- anticipation.

### Supporting information

- transcript or performed text as supporting evidence;
- current attention/opportunity when materially relevant;
- minimal status indicating provisional/effective state when needed;
- contextual commands revealed without dominating the scene.

### Low-fidelity structure

```text
┌─────────────────────────────────────────────────────────────┐
│ [Production]   [Scene]                    [Perspective]      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                  PEOPLE / RELATIONSHIP FIELD                │
│                                                             │
│       [A]                 [B]                 [C]            │
│                    ↘ attention / relation                   │
│                                                             │
│                [performed action / dialogue]                │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ [supporting transcript / current line / silence]            │
├─────────────────────────────────────────────────────────────┤
│ [Inspect]       [Intervene]       [Take a Seat / Perform]   │
└─────────────────────────────────────────────────────────────┘
```

### Design law

The live Scene is not a chat transcript with decorative avatars.

The people and their present relationship remain primary.

---

## 8. State 03 — Inspect relevant context without leaving the Scene conceptually

### User task

Understand why the current moment is charged or constrained.

### Interaction

Select a Character, relationship, pressure, condition, or current cue.

A contextual inspector opens while the current Scene remains retained.

### Low-fidelity structure

```text
┌─────────────────────────────────────────────────────────────┐
│                   CURRENT SCENE RETAINED                    │
│                                                             │
│ [people / action remain visible or semantically retained]   │
│                                      ┌────────────────────┐ │
│                                      │ CONTEXT INSPECTOR  │ │
│                                      │                    │ │
│                                      │ Why relevant now   │ │
│                                      │ What is current    │ │
│                                      │ What is unresolved │ │
│                                      │ [Trace cause]      │ │
│                                      └────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### Requirements

- opening context does not pause/mutate Production unless the user explicitly invokes a causal action;
- inspector state is navigation/session state, not Production state;
- disclosure respects active Presentation Perspective;
- no fixed engine ontology must be exposed merely because the creator asks for context;
- close/Back returns focus meaningfully to the invoking Scene element.

---

## 9. State 04 — Follow `why is this true now?` into causal history

### User task

Trace a current condition to the accepted event or prior state that explains it.

### Transition principle

This is a semantic focus transition, not necessarily navigation to a global Archive destination.

### Low-fidelity structure

```text
CURRENT CONDITION
      │
      │  Why?
      ▼
┌─────────────────────────────────────────────────────────────┐
│ HISTORICAL INSPECTION — CURRENT STATE RETAINED              │
├─────────────────────────────────────────────────────────────┤
│ [accepted event / prior condition]                          │
│                                                             │
│ What happened                                               │
│ What became effective                                       │
│ What changed                                                │
│ What remained unresolved                                    │
│                                                             │
│ [Show resulting current condition]   [Return to current]    │
└─────────────────────────────────────────────────────────────┘
```

### Critical distinction

Historical inspection must never imply that the Production has been rewound.

`Back` returns navigation focus. It does not undo history.

---

## 10. State 05 — Direct / intervene

### User task

Change a condition, emphasis, opportunity, or creator-level circumstance without secretly dictating a Character's internal agency.

### Interaction principle

Direction is a creator-authority action, not ordinary page navigation.

The exact intervention taxonomy remains open.

### Low-fidelity structure

```text
CURRENT SCENE
      ↓ Intervene
┌─────────────────────────────────────────────────────────────┐
│ CREATOR INTERVENTION                                        │
├─────────────────────────────────────────────────────────────┤
│ What do you want to change about the circumstance?          │
│                                                             │
│ [small set of context-relevant action classes]              │
│ [human-readable free creative expression where supported]   │
│                                                             │
│ Effect / authority summary                                  │
│ [Cancel]                                      [Apply/Direct] │
└─────────────────────────────────────────────────────────────┘
```

### Requirements

- high-authority effects are explicit;
- creator direction is distinguishable from writing required Character behavior;
- current Presentation Perspective must not accidentally hide the creator's own authority state;
- internal enum names are not exposed by default;
- no final intervention categories are frozen here.

---

## 11. State 06 — Take a Seat / Character-bounded performance

### User task

Temporarily perform through one Character's bounded information position.

### Transition

The workspace should materially transform because disclosure has changed.

The exact visual transformation remains open.

### Low-fidelity structure

```text
┌─────────────────────────────────────────────────────────────┐
│ [Production] [Scene]       PERSPECTIVE: CHARACTER-BOUNDED   │
├─────────────────────────────────────────────────────────────┤
│ You are performing as [Character]                           │
│                                                             │
│ What is available to this Character now                     │
│ ----------------------------------------------------------- │
│ [permitted current context]                                 │
│ [relevant memory/knowledge projection where authoritative]  │
│ [observable current cues]                                   │
│ [current relationship/pressure projection]                  │
│                                                             │
│ [Perform / act / speak / remain silent]                     │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ [Return control / leave bounded perspective]                │
└─────────────────────────────────────────────────────────────┘
```

### Requirements

- creator-only privileged inspectors disappear or become inaccessible as required;
- the same Character identity persists;
- returning restores the prior creator context;
- the interface may use theatrical human language but must not freeze every displayed concept into engine ontology;
- silence/refusal/nonverbal action remain legitimate agency;
- exact Character Context disclosure semantics remain open until application authority supports them.

---

## 12. State 07 — Provisional Performance

### User task

Understand that a Performance occurred or was proposed without prematurely treating it as authoritative history.

### Design problem

The product must avoid the common AI-interface failure where generated text appears and therefore looks instantly canonical.

### Required distinction

```text
PERFORMANCE MATERIAL
        ≠ automatically
AUTHORITATIVE HISTORY
```

### Low-fidelity structure

```text
┌─────────────────────────────────────────────────────────────┐
│ PERFORMANCE                                                 │
├─────────────────────────────────────────────────────────────┤
│ [performed action / dialogue / silence]                     │
│                                                             │
│ Status: [provisional / awaiting creator or authority step]  │
│                                                             │
│ [review context if needed]                                  │
│ [future Take decision controls only if approved semantics]  │
└─────────────────────────────────────────────────────────────┘
```

### Current authority boundary

Patch 0011 Take semantics are machine-validated for exercised E0 gates; Patch 0012 atomic causal commit is approved architecture but not current runtime authority.

Therefore this prototype may represent the conceptual distinction between provisional material and effective accepted history, but it must not claim final implemented commit behavior or freeze final Take/rehearsal UX.

---

## 13. State 08 — Consequence review: `What changed?`

### User task

Understand the material result of accepted history.

### Experience target

This is where the Archive benchmark becomes important.

Do not show only `scene complete` or a chronological transcript.

Show the causal relationship:

```text
what happened
      ↓
what changed
      ↓
what is still unresolved
      ↓
what is now different about the next moment
```

### Low-fidelity structure

```text
┌─────────────────────────────────────────────────────────────┐
│ CONSEQUENCE                                                 │
├─────────────────────────────────────────────────────────────┤
│ WHAT CHANGED                                                │
│ [one or more human-readable consequential changes]          │
│                                                             │
│ STILL IN MOTION                                             │
│ [unresolved pressure / relationship / proposition]          │
│                                                             │
│ WHY                                                         │
│ [accepted causal event link]                                │
│                                                             │
│ [See current result]                    [Inspect history]    │
└─────────────────────────────────────────────────────────────┘
```

`What Changed` and `Still in Motion` are retained here as historical O0 benchmark language only, not final product labels.

### Requirements

- consequence is human-readable;
- accepted historical texture is not automatically promoted to durable editable state;
- causal provenance is inspectable, not necessarily permanently visible;
- current versus historical state remains explicit;
- no false psychological precision.

---

## 14. State 09 — Return to the changed present

### User task

Resume the current Production and perceive that the world has genuinely changed.

### Critical experience

The prototype should not end on a summary page.

It should return to the same persistent Production where the consequence is now part of the present conditions.

### Low-fidelity structure

```text
┌─────────────────────────────────────────────────────────────┐
│ [same Production]          [same persistent Characters]     │
├─────────────────────────────────────────────────────────────┤
│ CURRENT SCENE / NEXT MOMENT                                 │
│                                                             │
│ [people]                                                     │
│                                                             │
│ [changed condition now visible/inspectable]                 │
│ [unresolved implication still present]                      │
│                                                             │
│ [Continue] [Inspect why] [Direct when relevant]             │
└─────────────────────────────────────────────────────────────┘
```

### Core success condition

The user should feel:

> **I am back in the same world, but it is different because of what happened.**

If that feeling is not recoverable from the interaction structure, the prototype has failed the product thesis.

---

## 15. Navigation contract across the prototype

### Durable navigation

Used only for:

- Production/application scope changes;
- app-level settings/help/diagnostics;
- other later-approved durable destinations.

### Semantic focus transitions

Used for:

- Scene -> relevant context;
- current condition -> cause;
- performance -> consequence;
- consequence -> current changed condition;
- Character -> related permitted context;
- current -> historical inspection -> current.

### Transient surfaces

Used for:

- inspector detail;
- task commands;
- short high-authority confirmations;
- capability/error explanation;
- bounded supporting context.

### Back

Always navigation history.

Never causal mutation.

---

## 16. Capability-degradation test variant

The prototype must include one degraded-capability pass.

Example:

- creator opens an existing Production;
- current Scene/history/context remain navigable;
- generation/performer action is unavailable;
- the unavailable action explains the capability limitation truthfully;
- deterministic creator editing/inspection remains available where supported;
- no fictional Character failure is inserted into the Scene;
- no causal history is created by the technical failure.

Success criterion:

> **Loss of automation must not destroy the Production mental model.**

---

## 17. Accessibility prototype pass

The low-fidelity prototype is not complete until the flow can be described without relying on visual styling.

### Keyboard flow must prove

- durable scope navigation is reachable directly;
- current Scene can be entered without crossing unrelated chrome;
- inspectors have predictable open/close focus return;
- history inspection has predictable Back semantics;
- creator intervention can be completed without pointer-only gestures;
- Character-bounded performance has a clear entry and exit;
- consequence review can be traversed in causal reading order;
- return-current restores meaningful focus.

### Screen-reader semantics must distinguish

- current versus historical material;
- creator versus Character-bounded perspective;
- provisional versus effective/accepted material;
- current Scene participants;
- selected Character/current object;
- consequence and unresolved status;
- disabled/unavailable AI capability versus fictional in-world state.

### Reduced motion

No transition meaning may depend on animation.

### High contrast / scaling

No essential state distinction may depend on subtle border, glow, portrait color, spatial distance, or simultaneous multi-column layout.

---

## 18. ARM64 / battery / implementation-simplicity pass

The prototype should be realizable with event-driven state updates and computational quiescence.

No low-fidelity interaction requires:

- continuous graph simulation;
- permanent ambient animation;
- idle inference;
- polling;
- persistent NPU/GPU activity;
- live causal-map recomputation for decoration;
- multi-window synchronization.

The interaction structure should map naturally to strict MVVM later:

- Production state remains authoritative domain state;
- shell/navigation state remains UI/session state;
- selected entity/event is UI state unless product semantics explicitly say otherwise;
- commands invoke explicit creator/domain actions;
- inspectors project read-only or appropriately authorized data;
- capability state gates actions without changing fictional truth.

No production XAML/C# is authorized by this proposal.

---

## 19. Prototype evaluation rubric

The first low-fidelity prototype should be judged against these questions.

### Product comprehension

1. Can a creator explain what is currently happening?
2. Can they tell what is current versus historical?
3. Can they tell what is provisional versus effective?
4. Can they tell what changed because of an accepted event?
5. Can they see how that change affects what comes next?

### Continuity

6. Does the Production feel persistent across focus transitions?
7. Do Characters remain recognizably the same persistent entities?
8. Does historical inspection feel like inspection rather than time travel?
9. Does returning from history restore the user's prior current context?

### Agency

10. Can the creator watch without machinery dominating?
11. Can they intervene without secretly scripting Character agency?
12. Can they enter Character-bounded performance without accidental omniscience?
13. Can they leave bounded perspective predictably?

### O0 benchmark recovery

14. Are people more important than chrome during live performance?
15. Does bounded perspective feel materially different rather than cosmetically filtered?
16. Does history answer `what changed and why does it matter now?`

### Accessibility

17. Can every essential distinction be expressed without color or animation?
18. Can the causal flow be traversed in a meaningful programmatic reading order?
19. Can keyboard users complete the entire loop?

### Native feasibility

20. Can the UI become computationally quiescent when nothing changes?
21. Can degraded AI capability remove automation without destroying navigation or truth?
22. Can the structure adapt from wide to narrow layouts without changing product semantics?

A prototype that fails any core authority/continuity distinction should not advance to visual styling merely because it is attractive.

---

## 20. What this prototype deliberately does not decide

Do not infer approval of:

- `Studio`, `Stage`, or `Archive` as final navigation labels;
- `Take a Seat` as final copy;
- `What Changed` or `Still in Motion` as final copy;
- a dark/gold O0 visual surface;
- portrait or character-identity rendering style;
- transcript placement;
- Character knowledge/belief/memory/want category taxonomy;
- final intervention taxonomy;
- final Take/rehearsal/branch controls;
- final Character Context disclosure categories;
- `NavigationView`, `Frame`, pane topology, title-bar composition, or specific WinUI controls;
- final animation/motion treatment;
- website translation;
- implementation behavior not established by application authority.

---

## 21. Recursive audit

Audit sequence:

`product truth -> accepted ontology -> accepted information architecture -> shell grammar -> task coherence -> O0 experiential benchmark -> authority boundaries -> perspective/disclosure -> provisional/effective distinction -> causality/history -> creator agency -> accessibility -> Windows-native feasibility -> ARM64/battery -> graceful degradation -> implementation simplicity -> surface inheritance -> contradictions -> unsupported claims -> open decisions`

### Pass 1

Material correction found:

- Replaced a page-by-page `Studio -> Stage -> Archive` prototype with one continuous Production session, because testing named spaces would prematurely reintroduce rigid navigation.

Restarted.

### Pass 2

Material correction found:

- Added the explicit O0 Stage/Character/Archive benchmark rubric so the prototype cannot become architecturally clean while losing the original project's human experiential intelligence.

Restarted.

### Pass 3

Material correction found:

- Added the `provisional Performance != authoritative history` checkpoint so generated material cannot visually become canon merely by appearing.

Restarted.

### Pass 4

Material correction found:

- Added `return to the changed present` as a required final state; ending on a consequence summary would fail the recursive product thesis that consequence changes future possibility.

Restarted.

### Pass 5

Material correction found:

- Separated historical inspection from causal mutation and preserved Back as navigation only.

Restarted.

### Pass 6

Material correction found:

- Added a capability-degradation variant because the same Production mental model must survive loss of AI automation.

Restarted.

### Pass 7

Material correction found:

- Removed any assumption that the O0 Character View category list is final product ontology; the prototype preserves bounded disclosure experience while leaving final creator-facing categories open.

Restarted.

### Pass 8

Material correction found:

- Added explicit screen-reader semantics for current/history, perspective, provisional/effective material, and capability failure so the causal architecture is not visual-only.

Restarted.

### Pass 9

No material correction or worthwhile improvement found within current low-fidelity interaction scope.

Result:

> **PASS FOR DIRECTOR REVIEW**

---

## 22. Director gate

Approve or revise the prototype thesis:

> **The first Kymaean interaction prototype should test one uninterrupted causal creator session: resume a living Production, experience people in a current Scene, inspect context/cause without losing the present, intervene or temporarily inhabit a Character, distinguish provisional performance from effective history, understand what changed, trace why, and return to the same Production in a meaningfully changed present.**

If approved, the next smallest justified step is to produce the first actual **low-fidelity screen/state wireframe set** for this exact flow.

That next artifact should remain grayscale/structural, avoid visual-identity selection, and test hierarchy, transitions, accessibility, and adaptive Windows behavior before any aesthetic system is applied.

Do not generate production XAML/C# or styled visual concepts from this proposal alone.
