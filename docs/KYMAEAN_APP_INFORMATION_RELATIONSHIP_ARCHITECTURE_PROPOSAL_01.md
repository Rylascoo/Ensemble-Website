<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN APP INFORMATION RELATIONSHIP ARCHITECTURE — PROPOSAL 01

Status: DIRECTOR PROPOSAL FOR REVIEW / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Phase: Kymaean App + Website Design Synthesis — post-recovery app information/interaction architecture

Current basis:

- `docs/KYMAEAN_EXPERIENCE_ONTOLOGY_SYNTHESIS_01.md`
- `docs/KYMAEAN_APP_WEBSITE_DESIGN_SYNTHESIS_BLUEPRINT_01.md`
- `Rylascoo/Ensemble-Project/CURRENT_STATE.md`
- `Rylascoo/Ensemble-Project/docs/blueprint/CREATOR_ONTOLOGY_EXTENSIBILITY_GUARD.md`

This document proposes an information-relationship architecture for the future Kymaean app. It does not select final labels, navigation chrome, visual identity, detailed layout, animation, XAML, C#, final creator ontology, Take/branch/rehearsal UX, Character Context disclosure UX, or Presentation Perspective switching UX.

---

## 1. The design problem

The recovered experience ontology establishes three strongly related experiential orientations:

1. **current possibility** — what could happen under present conditions;
2. **present performance** — what is happening now and whose agency is salient;
3. **causal history** — what happened, what became authoritative, what changed, and what remains unresolved.

These must be understandable as one continuous Production rather than three unrelated applications.

At the same time, the app must not:

- freeze `Studio`, `Stage`, or `Archive` as final navigation merely because they are useful conceptual ancestors;
- expose engine/storage ontology as default creator vocabulary;
- treat Watch / Direct / Perform / Write as mutually exclusive products or mandatory tabs;
- treat Creator/Production, Audience, and Character perspectives as cosmetic view themes;
- imply that unaccepted performance or uncommitted proposals are authoritative history;
- make AI availability a prerequisite for basic state inspection and creator control.

The architecture question is therefore:

> **How can one Production remain continuously legible while the user's attention moves among possibility, present performance, and causal history?**

---

## 2. Authority map

### VALIDATED / FROZEN PRODUCT AUTHORITY

The proposal must preserve:

- creator authority;
- persistent Character identity independent of Performer assignment;
- the seven-part creative cycle `CAST -> WORLD -> KNOWLEDGE -> PRESSURE -> SCENE -> PERFORMANCE -> CONSEQUENCE`;
- Production/Creator, Audience, and Character disclosure as projections over one authoritative Production;
- deterministic Access Control before context relevance/composition;
- probabilistic proposal versus deterministic authority separation;
- accepted performance preservation;
- causal and attributable consequence;
- graceful degradation that preserves correctness;
- local sovereignty over complete Production state and credentials.

### APPROVED BUT NOT CURRENT EXECUTABLE AUTHORITY

Patch 0012 architecture establishes an intended atomic causal-commit boundary, but current application authority does not establish Patch 0012 implementation/runtime behavior.

Design may therefore respect the semantic boundary:

> accepted Performance and retained Approved consequences become effective together or neither does

without presenting that architecture as already implemented product behavior.

### STRONG DIRECTION / OPEN DESIGN GUARD

Creator-facing dramatic language must remain extensible.

> **Keep authority semantics precise; keep creative semantics open.**

UI labels may be projections over authoritative data and are not automatically engine enums or one-to-one storage categories.

### OPEN DESIGN

Still open:

- final Production/Studio terminology;
- final app shell and navigation;
- dominant creator posture;
- final Stage composition;
- final Archive presentation;
- final Presentation Perspective switching;
- final Character Context disclosure;
- final Take/branch/rehearsal UX;
- final transcript prominence;
- visual identity and artwork system.

---

## 3. Architecture thesis: one Production, three coupled information orientations

The app should treat the Production as the persistent scope.

Within that scope, the creator may orient toward:

```text
POSSIBILITY CONTEXT
what conditions, people, relationships, knowledge, pressures and options exist now
        │
        ▼
PRESENT PERFORMANCE
what is happening now under those conditions
        │
        ▼
CAUSAL HISTORY
what became authoritative, what changed, and what remains unresolved
        │
        └──────────────► changes future possibility
```

These are **information orientations**, not final user-facing mode names.

The architecture should allow the user's focus to move among them while preserving a stable sense that all three belong to the same Production and causal continuity.

### Consequence

The app should not require a hard application-level mode switch merely to inspect why the current scene is the way it is or what a prior event changed.

### Constraint

The app also should not flatten all three into one dense screen. Their information density, interaction authority, and temporal purpose differ.

The proposed relationship is therefore:

> **persistent Production context + focusable information orientation + progressively disclosed adjacent context**

This is a structural rule, not a pixel-layout prescription.

---

## 4. Persistent continuity anchors

Certain information should remain conceptually stable while focus moves among possibility, present performance, and history.

### 4.1 Production identity

The user must always be able to determine which persistent creative reality they are affecting or inspecting.

The exact public term remains open.

### 4.2 Current Scene context

When a Scene is active, the app must preserve awareness of the current bounded circumstance even while the user inspects history or surrounding conditions.

History inspection should not silently change the active Scene.

### 4.3 Character / roster continuity

Characters remain the same persistent creative entities across setup, performance, and history.

A change in representation, focus, performer assignment, or temporal orientation must not imply a new Character identity.

### 4.4 Current Presentation Perspective

The active disclosure projection must remain legible whenever it materially constrains what can be shown.

Perspective is semantic state, not decoration.

### 4.5 Authority/effect status

The user must be able to distinguish, in accessible human language, among information that is conceptually:

- current authoritative state;
- proposed/draft/non-effective material;
- accepted historical performance;
- rejected or otherwise non-effective alternatives where later UX exposes them;
- unresolved rather than established.

This does not require exposing internal enum names.

### 4.6 Capability availability

When a requested function depends on an unavailable AI/provider/local capability, the app must communicate the capability limitation without converting technical failure into fictional state.

The Production itself remains inspectable and safely editable to the extent supported without that capability.

---

## 5. Transition contracts

The information architecture should communicate causal boundaries by behavior rather than by constant engineering exposition.

### 5.1 Possibility -> Present Performance

This transition means that a bounded present circumstance becomes the focus of active performance.

The UI should preserve enough context to answer:

- who is present;
- what current conditions matter;
- what pressure or opportunity is salient;
- whose agency is currently relevant;
- which disclosure perspective is active.

It must not imply that every creator-authored possibility is already canonical fact.

### 5.2 Present Performance -> Causal History

A generated or human Performance is not automatically history merely because it appeared on screen.

The design must preserve a legible boundary between provisional performance activity and effective accepted history.

Where current or future Take semantics are shown, the interface should distinguish accepted/effective history from rejected, cancelled, partial, or alternate material without requiring users to understand internal commit machinery.

### 5.3 Causal History -> Future Possibility

History matters because consequences change future conditions.

The interface should allow a creator to understand, when useful:

```text
what happened
    ↓
what changed
    ↓
what is now possible / constrained / unresolved
```

This relationship is more important than a generic chronological timeline.

A historical event that produced no durable state mutation may still remain historically true as accepted performance texture; the UI should not imply that every accepted moment must become a permanent editable field.

### 5.4 History inspection while Present Performance remains current

Inspecting prior history must not silently move the Production backward or replace current authority with a historical snapshot.

The app should preserve a clear return path to the live/current context.

### 5.5 Creator intervention during Present Performance

Direction or other creator intervention must remain distinct from secretly writing a Character's required action.

Higher-authority changes should be explicit and reviewable where the eventual authority design requires it.

The final Intervene taxonomy remains open.

---

## 6. Creator postures intersect the architecture; they do not define it

Watch / Direct / Perform / Write describe how the creator relates to the same Production.

They should influence available actions and emphasis without requiring four separate product silos.

| Posture | Possibility context | Present performance | Causal history |
| --- | --- | --- | --- |
| Watch | mostly ambient/inspectable | primary focus | available for explanation/continuity |
| Direct | editable/intervenable within authority | guidance/attention actions | prior causes available for informed direction |
| Perform | character-bounded relevant context | creator temporarily acts as Performer | bounded history/memory as permitted for that Character |
| Write | conditions and alternatives inspectable | takes/performance material inspectable | continuity, consequences and future rehearsal/branch concepts become more prominent |

This table describes relationships only.

It does **not** freeze final controls, branch semantics, or the amount of guidance supplied in Perform/Take a Seat.

---

## 7. Presentation Perspective intersects every information orientation

Presentation Perspective is orthogonal to possibility/performance/history.

A useful conceptual matrix is:

```text
                         POSSIBILITY   PERFORMANCE   HISTORY
Creator / Production        yes            yes         yes
Audience                    bounded        bounded     bounded
Character                   bounded        bounded     bounded
```

`bounded` means the visible information must respect the applicable disclosure/access contract; it does not mean every orientation exposes identical content.

### Design requirements

- Changing perspective must not mutate Production truth.
- Audience history must not reveal creator-only truth merely because it exists in authoritative state.
- Character perspective must not become omniscient because the human creator is occupying it.
- Moving to a more revealing perspective should be deliberate enough to avoid accidental spoilers.
- Essential perspective state must be programmatically exposed to assistive technology.

The exact switching control remains open.

---

## 8. Ambient, inspectable, and explicit information

To avoid both clutter and hidden authority, information should be allocated by interaction importance.

### AMBIENT

Information that usually remains legible without opening a specialist surface:

- current Production identity;
- active Scene identity/state when applicable;
- current participants/roster at a useful summary level;
- current Presentation Perspective when it affects disclosure;
- current attention/opportunity when relevant to the live experience;
- whether the user is viewing current versus historical material;
- blocking capability/failure state when it prevents a requested action.

### INSPECTABLE

Information available through progressive disclosure when the creator asks why, what changed, or what is relevant:

- consequence detail;
- causal provenance;
- relationship development;
- relevant knowledge/belief/memory projections where permitted;
- unresolved propositions and pressures;
- prior accepted performances;
- provider/model/cost/diagnostic detail when eventually supported and useful to advanced creators.

### EXPLICIT / HIGH-CONSEQUENCE ACTIONS

Actions that should not occur invisibly:

- changes that establish or alter authoritative reality at a high authority level;
- perspective changes that intentionally reveal more privileged information when spoiler risk exists;
- accepting/rejecting/promoting performance material where final Take/rehearsal UX requires explicit creator action;
- recasting/provider changes at performance boundaries;
- future branch/canon/retcon operations if and when those semantics are approved;
- disclosure to external providers where product policy eventually requires explicit user awareness/control.

This allocation is a proposal and should be validated before implementation.

---

## 9. Information persistence across orientation changes

The app should preserve continuity through stable semantic identity rather than by keeping every panel visually present.

At minimum, transitions should preserve references to:

- the same Production;
- the same persistent Characters;
- the active/current Scene when one exists;
- current Presentation Perspective;
- authoritative current-state identity;
- selected historical event or inspected cause when temporarily looking backward;
- the user's safe return point to current context.

Temporary UI focus, open inspectors, and visual arrangement need not become Production data.

---

## 10. Relationship and state communication

R0 and Blueprint 0.1 both warn against false precision.

### Prefer

- semantic descriptions of change;
- relational grouping and structure;
- evidence of what changed;
- explicit unresolved status where appropriate;
- state comparison when causality otherwise becomes unclear.

### Avoid by default

- psychological meters;
- fake confidence gauges;
- numeric relationship scores presented as truth;
- generic AI activity indicators as substitutes for causal state;
- causal diagrams on every surface;
- visual effects that imply consequence without actual state change.

Internal bounded signals may later support orchestration, but they should not automatically become creator-facing psychology.

---

## 11. History architecture: causal first, chronological second

Archive/history should eventually answer more than "what was said?"

The information relationship should support questions such as:

- What happened?
- What became authoritative?
- What changed because of it?
- Who or what was affected?
- What remains unresolved?
- What later state traces back to this event?

Chronological ordering remains useful, but chronology alone is insufficient.

The historical O0 phrases `What Changed` and `Still in Motion` remain useful design evidence, not frozen labels.

History must also respect Presentation Perspective.

---

## 12. Possibility architecture: conditions, not configuration machinery

The possibility-facing experience should help the creator shape usable dramatic conditions without making the product feel like an agent graph or schema editor.

It should support human-readable projections of:

- people and relationships;
- current/world circumstances;
- knowledge/disclosure boundaries;
- pressures and goals;
- Scene setup;
- relevant possibilities/uncertainties;
- performer assignment as secondary casting infrastructure.

The precise internal ontology remains governed by application authority and the Creator Ontology Extensibility Guard.

A new creator-authored dramatic concept must not require a new top-level UI mode merely because it is semantically novel.

---

## 13. Present-performance architecture: social presence over machinery

The live experience should prioritize:

- who is present;
- who is salient;
- what is happening;
- what changed in response;
- anticipation of what may happen next.

Provider/model identity, diagnostics, and deep state should remain secondary unless deliberately inspected.

Current Attention may influence presentation but cannot become narrative authority or imply obligation to respond.

Silence, refusal, redirection, and nonverbal action must remain representable as agency.

The final Stage layout remains open.

---

## 14. Graceful degradation architecture

The information architecture must remain coherent when AI generation or a local/remote capability is unavailable.

### The app should still permit, as supported by authoritative implementation:

- opening and inspecting locally owned Production state;
- navigating existing causal history;
- viewing Character/world/relationship information appropriate to the active perspective;
- creator-authored editing of supported state;
- reviewing existing accepted performances and consequences;
- changing settings/capability choices that do not require unavailable inference.

### The app must not

- invent fictional responses to mask provider failure;
- turn a timeout/refusal into Character behavior;
- fabricate consequence when performance did not become accepted history;
- imply NPU/local execution when no such execution was verified;
- run constant background inference to maintain ambience.

A capability limitation should reduce available automation, not corrupt creative truth.

---

## 15. Accessibility architecture

Accessibility is part of information semantics.

### Required

- every orientation has a clear programmatic heading/landmark structure;
- keyboard users can move between current context, adjacent context, and inspectors without losing focus origin;
- perspective state is announced semantically;
- current versus historical status is available without color alone;
- accepted/effective versus proposed/non-effective material is distinguishable without animation or color alone;
- relationship/spatial structure has textual or semantic equivalents;
- character identity never depends solely on portrait recognition;
- causal history can be traversed in a meaningful reading order;
- reduced-motion mode preserves every state transition meaning;
- high-contrast mode preserves state and authority distinctions;
- scalable text does not require spatial precision to remain understandable;
- touch targets and pointer interactions have keyboard equivalents.

### Design implication

If a relationship can only be understood by where two shapes sit on a canvas, the information architecture is incomplete.

---

## 16. Windows-native / ARM64 / battery feasibility

This proposal is intentionally compatible with a quiescent, event-driven Windows UI.

### Prefer

- state-driven view updates;
- virtualized history lists/trees where scale requires them;
- lazy loading of deep history/provenance;
- progressive disclosure instead of permanently rendering all relationships;
- lightweight semantic transitions whose meaning survives when animation is disabled;
- cached local projections where appropriate to implementation authority;
- user-triggered inference rather than idle inference for purely decorative state.

### Avoid

- continuous graph physics;
- permanent particle/ambient simulations;
- always-running GPU canvases;
- background NPU activity solely to animate or summarize the interface;
- polling loops for state that can be event-driven;
- web-app assumptions that fight native focus, accessibility, windowing, or power behavior.

No claim is made that final WinUI, NPU, or Windows AI implementation has been validated.

---

## 17. Website relationship

This artifact governs future **app** information relationships.

The website should not copy the app shell literally.

However, the public product narrative may later borrow the same causal comprehension sequence:

```text
conditions / people
    -> performance
    -> consequence
    -> continuity / changed future possibility
```

The website must remain truthful about what is implemented and validated at the time of publication.

---

## 18. Architectures rejected at this gate

The following are rejected as current default assumptions, not necessarily forbidden forever:

### Three rigid top-level modes

Treating possibility, performance, and history as isolated apps would weaken continuity and encourage duplicate context.

### Chat-thread-first architecture

A transcript may remain important, but message chronology is not the product ontology and cannot carry the full causal/relationship model by itself.

### Dashboard-first architecture

Exposing every state, metric, relationship, provider, and consequence simultaneously would prioritize machinery over creative presence.

### Always-visible causal graph

A causal graph may become a useful advanced inspector, but making it the default risks turning a creative environment into systems analysis.

### Posture-as-navigation

Watch / Direct / Perform / Write are creator relationships to one engine, not automatically primary destinations.

### Perspective-as-theme

Creator/Audience/Character perspective has disclosure authority and cannot be reduced to cosmetic presentation.

### Animation-dependent continuity

Causality and identity must remain legible when motion is reduced or disabled.

---

## 19. Validation/prototyping strategy

No production XAML/C# is required to test this architecture.

The next validation should use low-cost structural prototypes that deliberately avoid visual-style selection.

Required scenarios:

1. **New/quiet Production** — little or no history; creator establishes possibility.
2. **Active Scene** — current performance is primary while relevant context remains inspectable.
3. **Accepted performance with consequence** — user can understand what became history and what changed.
4. **Accepted performance with no durable mutation** — history remains true without implying every detail became durable state.
5. **Rejected/cancelled/alternate material** — clearly non-effective where exposed.
6. **Inspect history during an active Scene** — user can understand the past and return to current context without changing authority.
7. **Character-bounded Perform posture** — the creator can act without receiving omniscient Production disclosure.
8. **Audience perspective** — unrevealed Production truth remains hidden.
9. **Capability unavailable** — core Production inspection remains coherent and technical failure does not become fiction.
10. **Keyboard/screen-reader traversal** — current, adjacent, and historical context remain semantically navigable.
11. **Reduced-motion/high-contrast** — all state relationships remain understandable.

Evaluation questions:

- Can users tell what is current, proposed, historical, and unresolved?
- Can they understand that history changed future conditions without reading engine terminology?
- Can they inspect the past without feeling that the Production moved backward?
- Can they distinguish Character identity from Performer/provider identity?
- Can they understand the active disclosure perspective?
- Does the architecture remain useful when generation is unavailable?
- Does any surface imply more authority or implementation than the product actually has?

---

## 20. Open decisions deliberately preserved

This proposal does not decide:

- final user-facing names for possibility/performance/history functions;
- whether Studio/Stage/Archive remain public labels;
- exact navigation control type;
- default landing surface for new or existing Productions;
- exact app shell geometry;
- transcript prominence;
- exact relationship visualization;
- final intervention taxonomy;
- Character Context disclosure density;
- exact perspective-switching control;
- final Take/branch/rehearsal interactions;
- visual identity, palette, type, material, portrait/artwork system;
- motion language;
- final website composition;
- production implementation.

---

## 21. Recursive audit

Audit sequence:

`product truth -> frozen authority -> approved/unimplemented boundary -> open ontology -> Production continuity -> possibility/performance/history relationship -> creator postures -> Presentation Perspective -> authority/effect status -> history causality -> graceful degradation -> accessibility -> Windows-native feasibility -> ARM64/battery -> website truth -> implementation simplicity -> surface inheritance -> contradictions -> unsupported claims -> open decisions`

### Pass 1

Material correction:

- Rejected an initial three-mode interpretation and made Production the persistent scope with focusable information orientations instead.

Restarted.

### Pass 2

Material correction:

- Added persistent Presentation Perspective as an orthogonal semantic anchor rather than embedding it inside the live-performance function.

Restarted.

### Pass 3

Material correction:

- Added explicit authority/effect-status semantics so provisional performance, accepted history, unresolved information, and future alternate material cannot visually collapse.

Restarted.

### Pass 4

Material correction:

- Separated accepted historical texture from durable projected state so the UI does not imply every true performance detail becomes a permanent field.

Restarted.

### Pass 5

Material correction:

- Added capability-unavailable behavior and removed any architectural dependency on continuous inference or animated ambience.

Restarted.

### Pass 6

Material correction:

- Added an explicit rejection of posture-as-navigation and perspective-as-theme to prevent future mockups from reintroducing the recovered ontology drift.

Restarted.

### Pass 7

No material correction or worthwhile improvement found within the bounded information-relationship architecture scope.

Result:

> **PASS FOR DIRECTOR REVIEW**

---

## 22. Director decision gate

This proposal recommends the following architecture principle:

> **One persistent Production context, with possibility, present performance, and causal history as connected focusable information orientations; creator posture and Presentation Perspective intersect them orthogonally rather than becoming separate products or navigation silos.**

If approved, the next smallest unresolved design question is not visual styling. It is:

> **What minimal shell/navigation grammar can express this relationship clearly on Windows without prematurely fixing final labels or component aesthetics?**

A subsequent artifact could address that question with low-fidelity structural alternatives only.

Stop at this Director-review gate.
