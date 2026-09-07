<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN APP SHELL + NAVIGATION GRAMMAR — PROPOSAL 01

Status: DIRECTOR PROPOSAL FOR REVIEW / NO PRODUCTION IMPLEMENTATION AUTHORIZED

Phase: Kymaean App + Website Design Synthesis — shell/navigation architecture after accepted information-relationship model

Current basis:

- `docs/KYMAEAN_EXPERIENCE_ONTOLOGY_SYNTHESIS_01.md`
- `docs/KYMAEAN_APP_INFORMATION_RELATIONSHIP_ARCHITECTURE_PROPOSAL_01.md`
- `docs/KYMAEAN_APP_WEBSITE_DESIGN_SYNTHESIS_BLUEPRINT_01.md`
- `Rylascoo/Ensemble-Project/CURRENT_STATE.md`
- `Rylascoo/Ensemble-Project/docs/blueprint/CREATOR_ONTOLOGY_EXTENSIBILITY_GUARD.md`
- current Microsoft Windows app navigation guidance, used only as native-feasibility evidence

This proposal defines the smallest shell/navigation grammar capable of expressing one persistent Production, current possibility, present performance, causal history, creator posture, and Presentation Perspective without freezing final labels, visual styling, detailed component layout, or production implementation.

It does not select final `Studio` / `Stage` / `Archive` labels, final Production terminology, Character Context disclosure UX, Take/branch/rehearsal UX, app icon, typography, palette, material system, animation language, or exact WinUI control composition.

---

## 1. Accepted upstream basis

The accepted information-relationship architecture establishes:

> **one persistent Production context + focusable information orientation + progressively disclosed adjacent context**

The Production remains the user's persistent creative scope.

Within it, the user's attention may orient toward:

- **current possibility** — relevant conditions, people, relationships, knowledge, pressures, options and Scene setup;
- **present performance** — what is happening now and whose agency is salient;
- **causal history** — what became authoritative, what changed, what remains unresolved and what later possibility follows from it.

These are connected information orientations, not three independent applications and not automatically three top-level navigation destinations.

Creator postures — Watch / Direct / Perform / Write — intersect this structure but do not define four product silos.

Presentation Perspective — Creator/Production, Audience, Character-bounded — is an orthogonal disclosure state over the same authoritative Production.

---

## 2. Shell thesis

The smallest coherent shell is:

```text
APPLICATION SCOPE
    │
    ├── Production selection / lifecycle
    │
    ▼
PERSISTENT PRODUCTION SHELL
    │
    ├── stable identity + current-context anchors
    ├── one primary work surface
    ├── contextual adjacent-information inspector
    ├── contextual command layer
    └── explicit semantic status when authority/perspective/capability matters
```

The core rule is:

> **Navigate between durable scopes; transition within one Production by following meaning.**

The shell should use conventional Windows navigation only for destinations that are genuinely durable destinations.

Possibility, performance and history should not become global menu items merely because they are easy to label.

---

## 3. Navigation hierarchy

The proposal uses four levels of navigation responsibility.

### LEVEL 0 — Application / Production scope

Purpose:

- enter a Production;
- create/open/switch Productions when supported;
- reach app-level settings, help, diagnostics or account/provider configuration where appropriate;
- leave the current Production deliberately.

This is durable navigation because the user is changing application scope or persistent creative object.

Potential implementation pattern later:

- standard Windows top-level navigation framework such as `NavigationView` may be appropriate;
- exact left/top/compact presentation remains open;
- custom navigation should not be invented unless standard controls prove insufficient.

No final menu labels are selected here.

### LEVEL 1 — Persistent Production workspace

Once inside a Production, the user should perceive one continuous workspace.

The shell should preserve stable semantic anchors such as:

- Production identity;
- current Scene when one exists;
- current Presentation Perspective when disclosure differs;
- current-versus-history state;
- blocking capability status when relevant.

The workspace may substantially change its content composition as focus changes, but it should not feel as though the user opened another application.

### LEVEL 2 — Meaningful focus transitions

Possibility, present performance and causal history are reached through contextual transitions such as:

- inspect the conditions relevant to this Scene;
- return to what is happening now;
- show what changed because of this accepted event;
- trace why this current condition exists;
- inspect what remains unresolved;
- inspect a Character's permitted context;
- return from historical inspection to current state.

These are semantic transitions, not necessarily menu navigation.

The final wording remains open.

### LEVEL 3 — Inspectors and transient command surfaces

Secondary/deep information should appear through appropriately dismissible or persistent contextual surfaces rather than forcing global navigation.

Examples of information class, not final controls:

- causal provenance;
- consequence detail;
- relationship development;
- allowed Character context;
- provider/model/cost diagnostics;
- capability detail;
- advanced authority metadata;
- alternate/rejected material if future Take UX exposes it.

Potential Windows-native host patterns may include side panes, details views, dialogs, teaching surfaces, context menus, command bars or dedicated detail pages depending on density and task duration.

No specific control is frozen by this document.

---

## 4. Stable shell regions

The shell needs semantic regions, not a permanent fixed pixel layout.

### 4.1 Scope / identity region

Must make the current persistent creative scope understandable.

Possible responsibilities:

- Kymaean/app identity at appropriate level;
- current Production identity;
- Production switch/exit affordance;
- navigation back/forward where meaningful;
- app-level commands that should not masquerade as creative state.

Constraint:

The title area must not become a crowded status dashboard.

### 4.2 Context anchor region

Must communicate the minimum context needed to understand the primary surface.

Depending on the current task, this may include:

- active Scene;
- current roster/participants at summary level;
- current Presentation Perspective;
- current-versus-historical state;
- current attention/opportunity when materially relevant.

Constraint:

Only information whose absence would create semantic ambiguity belongs here persistently.

### 4.3 Primary work surface

The center of attention.

Its composition changes depending on what the creator is doing, but it remains inside the same Production workspace.

It may support:

- experiencing current performance;
- shaping relevant possibility;
- reviewing accepted causal history;
- writing/rehearsal work when later semantics permit;
- bounded Character performance.

The primary work surface should never require permanent simultaneous display of every orientation.

### 4.4 Contextual inspector region

Purpose:

Show adjacent meaning without replacing the user's current task.

Examples:

- why this condition exists;
- what an accepted event changed;
- relevant Character/context detail;
- unresolved pressure;
- causal lineage;
- history excerpt;
- advanced diagnostics.

The inspector should preserve a clear semantic relationship to the selected entity/event/state.

Constraint:

An inspector is not a dumping ground for every field that does not fit the primary surface.

### 4.5 Command region

Commands should follow the current task and selected object.

Examples of command classes:

- creator direction/intervention;
- edit supported conditions;
- inspect context;
- accept/reject/review performance material where future Take UX authorizes it;
- perspective changes;
- performer/provider configuration;
- export or history actions.

Avoid a universal command ribbon containing every possible operation.

### 4.6 Semantic status region

Status must be visible when it affects truth, disclosure, user expectation or capability.

Examples:

- viewing historical rather than current state;
- Character-bounded perspective active;
- material is proposed/non-effective rather than authoritative;
- AI/provider capability unavailable for a requested operation;
- operation awaiting explicit creator decision where later semantics require it.

This region may be distributed across the shell rather than one literal status bar.

---

## 5. The Production workspace should be current-state biased

The shell should normally preserve a clear understanding of the **current authoritative Production**.

Historical inspection is important, but history should not silently become current state.

When the creator moves into historical focus:

- the shell should state that historical material is being inspected;
- the active/current Production context remains retained;
- back/return-current behavior should be predictable;
- commands that mutate current state must not appear to operate on a historical snapshot unless future branch/retcon semantics explicitly authorize that behavior.

This prevents one of the largest conceptual risks in a causal product: confusing inspection with time travel or mutation.

---

## 6. Back navigation grammar

Back should mean navigation history, not undo.

Required distinction:

```text
BACK
returns to prior location/focus

UNDO / REVERT / RETCON / BRANCH
changes creative or historical state under future approved semantics
```

The shell must not overload the Windows back affordance to alter Production truth.

Examples of valid Back behavior:

- close deep history inspection and return to the prior current-performance focus;
- return from Character detail to the selected Scene;
- return from app-level settings to the Production workspace;
- return from a secondary Production page to its parent destination.

Examples of invalid Back behavior:

- reject an accepted Take;
- undo a consequence;
- rewind authoritative history;
- change Presentation Perspective merely because a prior page used another perspective.

This preserves Windows navigation expectations and Kymaean's causal authority semantics simultaneously.

---

## 7. Presentation Perspective grammar

Perspective is not top-level navigation.

It is semantic disclosure state.

The shell should therefore represent perspective as a stateful control/status relationship, not as three separate application areas.

Requirements:

- current perspective is discoverable when it affects disclosure;
- perspective changes are deliberate;
- movement toward more privileged disclosure should avoid accidental spoilers;
- switching perspective does not mutate Production truth;
- Character-bounded perspective must not silently leak creator-only information through persistent inspectors or history surfaces;
- assistive technology must receive the active perspective semantically.

The exact control remains open.

A segmented selector, menu, command or other standard pattern may later be evaluated; none is selected here.

---

## 8. Creator posture grammar

Watch / Direct / Perform / Write should influence emphasis, available commands and disclosure of tools without becoming four permanent shell tabs by default.

### Watch

- minimal command chrome;
- current performance dominant;
- adjacent causality/history available without forcing inspection.

### Direct

- creator authority/intervention actions become more available;
- relevant possibility context can surface without replacing the performance context unnecessarily.

### Perform

- Character-bounded context and creator-as-Performer actions become primary;
- privileged creator-only information must recede according to disclosure authority.

### Write

- structured possibility/history/take analysis may gain prominence;
- alternate/rehearsal workflows remain deferred until semantics are approved.

The posture may be inferred from the task or entered through explicit actions depending on later design.

This proposal does not require a global posture switch.

---

## 9. Focus-transition grammar

The architecture should prefer object/meaning-linked transitions over arbitrary page changes.

### Possibility -> Performance

The creator should retain enough of the relevant setup to understand the Scene without carrying the entire setup UI into the live experience.

### Performance -> History

The creator should be able to inspect when/why the displayed material became effective history where that distinction matters.

### History -> Possibility

The creator should be able to follow consequence forward into current conditions and unresolved possibilities.

### Current -> Cause

From a current state element, the creator may inspect the accepted event(s) or prior conditions that explain it when causal provenance is available.

### Cause -> Current

Returning should restore the prior current focus rather than dropping the creator at a generic workspace root.

### Character -> Related context

Character identity should remain stable as the user moves among present action, relationship/context detail, and causal history.

These transitions should preserve selected-object identity wherever possible.

---

## 10. Navigation-state versus Production-state boundary

Not all shell state belongs in the Production.

### Navigation/session state may include

- selected entity/event;
- current inspector;
- current scroll/focus location;
- shell pane open/closed state;
- navigation history;
- local window size/layout mode;
- transient filters/sorts unless later product semantics say otherwise.

### Production authority includes only product-defined creative state

Navigation must not silently create causal history.

Likewise, opening a history event, expanding a Character inspector, changing a sort order or resizing a pane must not affect Production StateHash/causal authority merely because the UI changed.

This separation supports deterministic state management and keeps UI interaction cheap on ARM64.

---

## 11. Multi-window boundary

This proposal does not require multi-window behavior.

Future Windows-native design may evaluate secondary windows for genuinely long-lived parallel tasks, but the baseline should remain complete in one window.

Do not require separate windows for:

- history;
- Character context;
- possibility setup;
- diagnostics.

Reasons:

- simpler focus/navigation semantics;
- lower implementation complexity;
- better accessibility predictability;
- less state synchronization burden;
- lower risk of confusing two views of one authoritative Production.

Multi-window becomes justified only when a concrete creator workflow demonstrates a durable benefit.

---

## 12. Adaptive Windows behavior

The semantic hierarchy must survive different window widths.

### Wide window

May support:

- persistent navigation pane if needed;
- primary work surface plus adjacent inspector;
- richer contextual anchoring.

### Medium window

May collapse secondary navigation/inspector affordances while retaining the same information structure.

### Narrow window

Should prioritize one primary surface at a time and move inspectors/details into sequential navigation or overlays.

No essential meaning may depend on a simultaneous multi-column layout.

This makes the grammar compatible with Windows `NavigationView` adaptive patterns without requiring the final shell to use a specific pane mode.

---

## 13. Keyboard and accessibility navigation grammar

The shell must have a predictable semantic order independent of visual experimentation.

A baseline reading/focus hierarchy should remain logically expressible as:

1. application/scope navigation;
2. Production/context identity;
3. primary work surface;
4. contextual inspector when open;
5. task commands;
6. status/help detail.

Exact visual order may differ when accessibility semantics remain coherent.

Requirements:

- keyboard users can reach every durable destination without traversing decorative content;
- focus returns to the invoking element or meaningful successor when an inspector/dialog closes;
- Back has consistent semantics;
- current/historical state and Presentation Perspective are programmatically exposed;
- navigation selection does not rely on color alone;
- collapsed/adaptive navigation remains discoverable to screen readers;
- touch targets have keyboard equivalents;
- history and causal relationships have a meaningful reading order;
- reduced motion does not alter navigation meaning;
- scaling does not force hidden horizontal spatial relationships to carry essential semantics.

---

## 14. Quiescent rendering and ARM64/battery implications

The shell is deliberately compatible with near-zero idle work.

Navigation and state presentation should be driven by explicit state changes and user interaction.

Avoid baseline dependence on:

- continuous ambient animation;
- graph physics;
- constant relationship recomputation for decoration;
- polling to update non-changing status;
- idle AI inference;
- background NPU work merely to make the shell feel alive;
- permanently rendered high-cost canvases.

When nothing changes, the shell should be visually and computationally quiescent.

Causal continuity is conveyed through semantic state and user-triggered inspection, not through perpetual animation.

---

## 15. Graceful capability degradation in the shell

AI capability belongs in task availability, not navigation existence.

If a provider/local model/NPU feature is unavailable:

- the Production shell still opens;
- existing state/history remains navigable;
- existing Character and relationship data remains inspectable subject to perspective;
- deterministic editing functions remain available where supported;
- unavailable inference actions become disabled/unavailable with truthful explanation;
- the shell does not invent fictional Character output to hide failure;
- capability failure does not become causal history.

This preserves one stable mental model across capable and degraded states.

---

## 16. Windows-native feasibility note

Current Microsoft Windows app guidance emphasizes:

- simple, clear, consistent navigation;
- adaptive use of top/left navigation structures;
- standard `NavigationView` for many multi-page WinUI applications;
- conventional Back behavior based on navigation history.

This proposal is intentionally compatible with those expectations.

It does **not** yet freeze:

- `NavigationView` as the mandatory final root control;
- a `Frame` topology;
- left versus top navigation;
- exact page routing;
- custom title-bar behavior;
- multi-window use;
- specific Windows App SDK version-dependent APIs.

Those belong to implementation translation after design approval and API verification.

---

## 17. What should NOT become top-level navigation by default

The audit strongly rejects promoting the following into permanent primary nav solely because they are important concepts:

- Possibility / Performance / History;
- Studio / Stage / Archive;
- Watch / Direct / Perform / Write;
- Creator / Audience / Character perspective;
- Cast / World / Knowledge / Pressure / Scene / Performance / Consequence;
- Providers / models;
- relationship types;
- engine authority categories.

Some may later earn durable destinations through workflow evidence.

Importance is not the same thing as navigation level.

---

## 18. Minimal conceptual shell map

A compact model:

```text
┌────────────────────────────────────────────────────────────┐
│ APPLICATION / PRODUCTION SCOPE                             │
│ durable navigation only                                    │
├────────────────────────────────────────────────────────────┤
│ PRODUCTION CONTEXT                                         │
│ identity · Scene · perspective · current/history status    │
├────────────────────────────────────────────────────────────┤
│                                                            │
│                  PRIMARY WORK SURFACE                      │
│                                                            │
│    focus follows creator task and causal relationships     │
│                                                            │
├───────────────────────────────────────┬────────────────────┤
│ CONTEXTUAL COMMANDS                   │ OPTIONAL INSPECTOR │
│ relevant to current task/object       │ adjacent meaning   │
└───────────────────────────────────────┴────────────────────┘
```

This is semantic topology, not a layout mockup.

On narrower windows, the inspector may become sequential/overlay content while preserving the same relationship.

---

## 19. Candidate shell principle for Director review

> **Stable Production, fluid focus.**

Meaning:

- the persistent creative reality remains legible;
- navigation changes durable scope;
- focus transitions follow causal/relational meaning;
- adjacent information is inspectable rather than permanently exposed;
- posture and perspective alter relationship/disclosure rather than fragmenting the product;
- current authority remains distinguishable from history and proposal;
- the shell remains coherent without AI and quiescent when idle.

This phrase is an internal design shorthand, not public branding.

---

## 20. Recursive audit

Audit sequence:

`product truth -> accepted ontology -> accepted information architecture -> authority/state boundary -> navigation hierarchy -> creator postures -> Presentation Perspective -> possibility/performance/history transitions -> current/history distinction -> back semantics -> accessibility -> Windows-native convention -> adaptive behavior -> ARM64/battery -> graceful degradation -> implementation simplicity -> ontology openness -> visual neutrality -> contradictions -> open decisions`

### Pass 1

Material correction:

- Initial shell model risked turning possibility/performance/history into primary navigation destinations.
- Corrected to durable-scope navigation plus semantic focus transitions inside one Production workspace.

Restarted.

### Pass 2

Material correction:

- Back navigation was initially underspecified and could be confused with undo/revert/retcon.
- Added explicit navigation-history versus causal-state mutation boundary.

Restarted.

### Pass 3

Material correction:

- Presentation Perspective risked appearing as a page category.
- Reframed as persistent disclosure state intersecting every information orientation.

Restarted.

### Pass 4

Material correction:

- Shell regions risked becoming a fixed desktop layout.
- Reframed them as semantic regions with adaptive narrow-window behavior.

Restarted.

### Pass 5

Material correction:

- Multi-window could have been inferred as desirable for history/context.
- Explicitly made one-window completeness the baseline and deferred multi-window until workflow evidence exists.

Restarted.

### Pass 6

Material correction:

- Capability state was initially treated as a secondary status concern.
- Elevated blocking capability state when it affects a requested action while preserving navigation and local inspection without AI.

Restarted.

### Pass 7

Material correction:

- Windows `NavigationView` guidance could be misread as selecting a final root control.
- Clarified that current Microsoft guidance is feasibility evidence only; exact WinUI topology remains unselected.

Restarted.

### Pass 8

No material correction or worthwhile simplification found within current scope.

Result:

> **PASS FOR DIRECTOR REVIEW**

---

## 21. Explicit open decisions preserved

Not selected:

- final primary navigation destinations;
- final `Studio` / `Stage` / `Archive` naming;
- exact Production term;
- exact root navigation control;
- left versus top navigation;
- exact title-bar treatment;
- exact Scene/header/context composition;
- inspector docking/overlay behavior;
- exact perspective control;
- explicit versus inferred creator posture controls;
- Character Context UI;
- Take/branch/rehearsal UI;
- multi-window behavior;
- visual styling;
- typography;
- palette;
- iconography;
- motion treatment;
- production XAML/C#.

---

## 22. Smallest unresolved question after this proposal

If this shell grammar is accepted, the next highest-leverage design question is:

> **What task-first low-fidelity interaction prototype should test “Stable Production, fluid focus” before visual styling begins?**

That prototype should test comprehension and navigation relationships using neutral structure, not branded aesthetics.

It should prove or falsify:

- whether users understand one persistent Production;
- whether current versus historical state remains clear;
- whether contextual transitions are discoverable without top-level mode tabs;
- whether Presentation Perspective remains understandable without dominating navigation;
- whether Watch/Direct/Perform/Write can coexist without posture silos;
- whether keyboard/back behavior remains predictable.

---

## 23. Stop gate

Stop here.

Do not automatically create wireframes, visual mockups, XAML, C#, brand artwork, or website implementation.

Current gate:

> **Director review of `docs/KYMAEAN_APP_SHELL_NAVIGATION_GRAMMAR_PROPOSAL_01.md`.**

Anti-churn law:

> **evidence -> smallest unresolved question -> recursive audit -> one justified next action -> stop**
