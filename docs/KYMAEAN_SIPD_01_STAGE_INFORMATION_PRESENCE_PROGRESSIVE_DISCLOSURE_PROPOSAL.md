# KYMAEAN SIPD-01 — STAGE INFORMATION PRESENCE & PROGRESSIVE DISCLOSURE PROPOSAL

Status: DIRECTOR PROPOSAL FOR REVIEW / NON-RENDER INFORMATION-PRESENCE ARCHITECTURE / NO UI SURFACE OR IMPLEMENTATION SELECTED

Phase: Kymaean App + Website Design Synthesis — after CRV-01 representation viability and TCV-01 temporal continuity

## 0. Purpose

Define what information belongs persistently in Kymaean's live present-performance workspace, what should appear contextually, and what should remain progressive/on-demand.

This proposal does **not** redesign the accepted shell/navigation architecture. It specializes existing authority:

> **persistent Production context + focusable information orientation + progressively disclosed adjacent context**

for the live Stage/present-performance orientation.

It does not select final labels, panel positions, WinUI controls, typography, palette, material, portrait medium, exact Stage composition, final Character Context taxonomy, transcript architecture, Take/rehearsal UX, branch/history UX, or production implementation.

Authority basis:

- `CURRENT_STATE.md`;
- `docs/KYMAEAN_APP_INFORMATION_RELATIONSHIP_ARCHITECTURE_PROPOSAL_01.md`;
- `docs/KYMAEAN_APP_SHELL_NAVIGATION_GRAMMAR_PROPOSAL_01.md`;
- `docs/KYMAEAN_CONTINUOUS_WORKSPACE_WIREFRAME_PROPOSAL_01.md`;
- `docs/KYMAEAN_VISUAL_SYSTEM_GRAMMAR_PROPOSAL_01.md`;
- `docs/KYMAEAN_CHARACTER_BOUNDED_WATCH_PERFORM_CONTRACT_01.md`;
- `docs/KYMAEAN_CHARACTER_REPRESENTATION_REQUIREMENTS_PROPOSAL_01.md`;
- `docs/KYMAEAN_CRV_01_CHARACTER_REPRESENTATION_VIABILITY_RESULT.md`;
- `docs/KYMAEAN_TCV_01_TEMPORAL_CHARACTER_CONTINUITY_RESULT.md`;
- current application authority at `Rylascoo/Ensemble-Project` main `7475a9397cff9063673908c666a729f0f3cd4525`, H1 Patch 0014 — E0 Production Context Continuity.

Durable laws:

> **Stable Production, fluid focus.**

> **Human signal over system ornament.**

> **Relationship organizes the living Production; editorial hierarchy explains only what the relationship cannot responsibly carry alone.**

> **Relationship and current evidence share the burden of making the changed present understandable.**

> **Bounded disclosure is subtractive.**

> **Surface != law.**

---

## 1. Design problem

Recent architecture-grounded renders repeatedly became dense because several legitimate information classes were shown simultaneously:

- people / relational field;
- current opportunity;
- bounded evidence;
- current authoritative facts;
- transcript / recent Performance;
- creator commands;
- causal trace/history;
- capability/technical detail.

Each class may be useful. Their simultaneous presence is not therefore justified.

The design question is:

> **What must the creator know without asking in order to understand and safely act in the live Production, and what should Kymaean reveal only when the creator follows meaning into deeper context?**

The answer must avoid both failure modes:

```text
TOO LITTLE
-> current reality / disclosure / agency becomes ambiguous

TOO MUCH
-> people become illustrations inside a dashboard
```

---

## 2. Core presence rule

Information earns persistent presence on the live Stage only when removing it would create one of these material failures:

1. **scope ambiguity** — the creator cannot tell which Production/Scene they are in;
2. **disclosure ambiguity** — the creator cannot tell that the active perspective limits what may be shown;
3. **agency ambiguity** — the creator cannot tell whose opportunity/agency is currently relevant or what posture they are in when that affects available actions;
4. **authority ambiguity** — provisional/historical/non-effective material could be mistaken for current effective truth;
5. **blocking capability ambiguity** — a requested action is unavailable and the reason materially affects the task;
6. **current-action ambiguity** — the creator cannot understand the immediate human situation without the information.

Everything else should default toward contextual or on-demand disclosure.

Required principle:

> **Importance does not imply permanence.**

---

## 3. Five-layer Stage information model

The Stage should be designed as five semantic layers. These are information-presence responsibilities, not literal stacked panels or storage enums.

### L0 — Persistent continuity anchors

Smallest stable semantic frame required to preserve one Production.

Candidate responsibilities:

- Production identity;
- active Scene identity/state when a Scene exists;
- active Presentation Perspective when it materially constrains disclosure;
- current-versus-historical locus when ambiguity is possible;
- creator posture when it materially changes available agency;
- blocking capability state only when it blocks/degrades the current task.

Constraint:

> **The anchor region must not become a status dashboard.**

### L1 — Living human field

The primary Stage.

Responsibilities:

- specific people presently relevant to the Scene;
- relationship/current interaction as composition;
- present human action/attention where legitimately represented;
- current opportunity/salience when materially relevant;
- changed relational organization after consequence.

Programmatic/accessibility equivalents must expose the same essential facts without depending on portrait recognition, spatial arrangement, color or motion.

Required priority:

```text
PEOPLE / HUMAN PRESENCE
-> RELATIONSHIP + CURRENT ACTION
-> RELEVANT CURRENT CONSEQUENCE / POSSIBILITY
```

No permanent roster sidebar is required merely because Character identity is important. Identity may participate directly in the living field, with compact supporting identity where necessary.

### L2 — Contextual current evidence

Trustworthy present information that helps explain the current field without becoming permanent exposition.

Possible content, when legitimately available under the active perspective:

- current authoritative facts relevant to the selected person/action/condition;
- observable/received evidence where the Character-bounded contract permits it;
- unresolved current condition when it materially affects the immediate situation;
- local authority/effect status where confusion is plausible.

This layer should normally be:

- invoked by selecting/focusing a person, condition, opportunity, statement or current fact;
- shown because a state transition creates immediate ambiguity;
- dismissible/reversible without changing Production truth.

The experimental evidence classes `Observed / Heard-Received / Established-Available / Unknown` remain semantic research categories, not a mandatory permanent four-section panel.

Required boundary:

> **Evidence may explain what is available now; it must not summarize private psychology.**

### L3 — Task/agency layer

Commands and inputs appear because the creator is doing something, not because every possible command deserves permanent chrome.

Examples:

- Watch: minimal/non-portrayal command presence;
- Direct: creator intervention commands become locally available around the relevant Scene/entity/task;
- Perform: bounded performance-input region appears persistently **while Perform is active**, because creator agency has materially changed;
- Write: writing/analysis tools may become primary within their eventual approved task surface, without becoming default live-Stage furniture.

A posture change may reconfigure L3 without changing L0-L2 Production truth or disclosure authority.

### L4 — Deep explanation / specialist context

Information that answers deeper questions and should not compete with the live Stage by default:

- causal trace / why-is-this-true-now history;
- detailed consequence provenance;
- prior accepted Performance/history where later UX supports it;
- relationship development history;
- deep Character/context detail where permitted;
- rejected/alternate material if future Take/rehearsal semantics expose it;
- provider/model/cost/diagnostic detail;
- advanced authority metadata;
- technical capability diagnostics.

L4 may occupy a side inspector, detail page, overlay or sequential focus depending on density/window width. Exact Windows control choice remains open.

---

## 4. Information-class allocation

### 4.1 Production identity

**Default:** PERSISTENT.

Why:

The creator must always know which persistent creative reality they are affecting or inspecting.

Presence should remain quiet and stable rather than decorative.

### 4.2 Current Scene

**Default:** PERSISTENT when a Scene is active.

Why:

Current circumstance must remain recoverable while inspecting adjacent context.

Historical inspection must not silently replace the active Scene.

### 4.3 Character identity / participants

**Default:** PERSISTENT AS THE HUMAN FIELD, not necessarily as a separate roster panel.

Why:

People are the primary experiential substrate of present performance.

Supporting compact identity may appear when scale/density/accessibility requires it, but Character identity should not default to dossier cards.

### 4.4 Presentation Perspective

**Default:** PERSISTENT/AMBIENT whenever disclosure differs materially from Creator/Production visibility.

Why:

Perspective is authority state, not decoration.

Character-bounded/Audience presentation must never leave the creator guessing why information is absent.

Subtractive rule:

- inaccessible information is removed/withheld;
- creator-only content is not left visible-but-dimmed;
- the UI must not disclose the existence of inaccessible private material merely to populate an `Unknown` bucket unless that existence is itself legitimately known.

### 4.5 Creator posture

**Default:** AMBIENT when it changes agency; otherwise need not dominate the Stage.

Why:

Watch versus Perform must be semantically explicit because agency differs.

Do not require four permanent posture tabs.

### 4.6 Current Opportunity / salience

**Default:** AMBIENT/PERSISTENT WHILE MATERIALLY ACTIVE, but visually quiet.

Why:

Current Opportunity can affect anticipation and available agency, and it must remain independent from perspective and obligation.

Required semantics:

```text
Current Opportunity = C
!=
C must respond
!=
C wants to act
```

The relational field should carry as much salience as possible; explicit status clarifies rather than substitutes for composition.

### 4.7 Current authoritative facts / changed-present evidence

**Default:** CONTEXTUAL.

Why:

TCV-01 shows current evidence is essential to causal continuity, but not every current fact deserves permanent display.

Surface the smallest fact set necessary to understand the selected/current situation. Deeper state remains inspectable.

Examples of legitimate present evidence may include, if available under perspective:

- a revised agreement is operative;
- a constraint currently applies or no longer applies;
- a current condition exists;
- an available action/opportunity changed.

Do not automatically narrate `what changed / why it changed` on the Stage.

### 4.8 Character-bounded evidence

**Default:** CONTEXTUAL / ON-DEMAND, with local evidence cues only when immediate action would otherwise be ambiguous.

Why:

A permanent evidence dashboard competes with the human field and encourages explanatory synthesis.

When opened, evidence must respect Access before Context and Patch 0014's no-inferred-observation law.

Do not infer observation from:

- co-presence;
- visible Candidate text;
- addressed Characters;
- nomination;
- Director selection;
- relationships;
- SceneState;
- causal adjacency.

### 4.9 Recent Performance / transcript

**Default:** PROGRESSIVE / ON-DEMAND.

Why:

- VSG hierarchy places supporting language below people/relationship/current consequence;
- repeated renders became transcript-heavy when it remained permanently visible;
- current Patch 0014 canonical Context v2 keeps `recentPerformances = []` and `RecentPerformanceText` empty;
- therefore a permanent transcript cannot be treated as required by current bounded-Context architecture.

Future design may permit a compact relevant utterance/action near the current human focus when supported by authoritative data, but full Performance history should default toward inspectable/history context rather than permanent Stage furniture.

This proposal does not decide where future canonical recent Performance comes from.

### 4.10 Creator commands

**Default:** CONTEXTUAL TO POSTURE + TASK.

Why:

Commands should follow what the creator is doing.

Do not keep a universal command ribbon visible.

Special case:

- Perform input remains available while Perform posture is active because creator agency has explicitly changed.
- Watch must not expose Character portrayal controls.

### 4.11 Authority/effect status

**Default:** LOCAL/PERSISTENT ONLY WHERE CONFUSION IS MATERIAL.

Examples:

- candidate/non-effective material being reviewed;
- historical focus;
- effective current fact alongside a provisional alternative;
- pending explicit creator decision where later Take semantics require one.

Do not plaster `effective` labels onto ordinary current facts whose authority is otherwise unambiguous.

### 4.12 Causal trace / history

**Default:** ON-DEMAND SEMANTIC TRANSITION.

Why:

History answers `Why is this true now?`, not `What should permanently occupy the Stage?`

Entry should originate from a current person/fact/consequence/event when possible.

While open:

- historical locus is explicit;
- current Production remains retained;
- privileged disclosure remains bounded by perspective;
- Back/return-current restores the prior current focus;
- inspecting history does not mutate current state.

TEO-style minimal earlier/later comparison may be used inside causal trace when it materially improves observability. It is not mandatory Stage structure.

### 4.13 Capability state

**Default:** ABSENT WHEN HEALTHY; AMBIENT WHEN DEGRADED/BLOCKING; DEEP DETAIL ON DEMAND.

Why:

Capability affects task availability, not Production existence.

Do not turn provider/NPU/model status into permanent theatrical chrome.

Technical failure is never fictional state and never causal history.

### 4.14 Provider/model/cost/diagnostics

**Default:** DEEP ON-DEMAND.

Why:

Provider/model identity is secondary to Character identity and present dramatic meaning.

No current evidence authorizes persistent Windows AI/NPU telemetry or claims of local/NPU execution.

---

## 5. Progressive-disclosure triggers

Information may expand for four justified reasons.

### Trigger A — user asks/follows meaning

Examples:

- select a Character;
- inspect current evidence;
- ask why a condition is true;
- inspect a consequence;
- open history;
- inspect capability detail.

This is the preferred trigger.

### Trigger B — task requires agency

Examples:

- enter Perform -> performance input appears;
- enter a creator intervention task -> relevant commands/context appear.

The additional surface exists because the creator's job changed.

### Trigger C — state changed and omission would mislead

Examples:

- perspective becomes Character-bounded;
- current versus historical locus changes;
- provisional material appears beside effective current state;
- requested AI capability becomes unavailable.

Only the smallest corrective status should surface automatically.

### Trigger D — selected current fact requires evidence to act safely

A compact contextual explanation may surface if an action would otherwise encourage the creator to treat unsupported inference as authority.

This is an exception, not permission for constant AI-authored explanation.

---

## 6. Collapse / return laws

Progressive disclosure must preserve continuity when it closes.

Required:

- return focus to the invoking person/fact/opportunity or a meaningful successor;
- preserve same Production and Scene identity;
- preserve Presentation Perspective unless the creator explicitly changed it;
- preserve current/historical locus correctly;
- closing an inspector never changes Production truth;
- closing history does not undo/revert anything;
- collapsed information leaves a discoverable path to reopen it.

Back remains navigation, not causal mutation.

---

## 7. Wide / medium / narrow allocation

Semantic presence must not depend on a wide three-column layout.

### Wide

May show:

- L0 anchors;
- L1 human field;
- one currently relevant L2/L4 inspector adjacent to it;
- posture/task commands where active.

Do not open multiple competing inspectors merely because space exists.

### Medium

Prefer:

- dominant L1 field;
- one collapsible contextual surface;
- commands colocated with the task.

### Narrow

Prefer sequential focus:

```text
live Stage
-> context/evidence detail
-> return
```

No essential meaning may require simultaneous columns.

---

## 8. Character-bounded SIPD contract

Character-bounded perspective is the strictest test of information presence.

The Stage should feel intentionally complete despite having **less information**.

Required ordering:

1. derive/obey active disclosure authority;
2. form the living human field from legitimately available current material;
3. expose only current evidence legitimately available under that authority;
4. expose task actions permitted by posture;
5. make deeper bounded context progressive;
6. omit privileged information entirely.

Never do:

```text
show privileged creator information
+
label it `Director View`
```

inside a Character-bounded surface.

Never infer knowledge/observation/private mind merely to fill a contextual panel.

Required principle:

> **A bounded Stage should become quieter, not emptier-with-placeholders.**

---

## 9. Present evidence versus history allocation

TCV-01 establishes the boundary:

### Stage may show current evidence

When relevant and available:

- current condition;
- current authoritative fact;
- current opportunity;
- current constraint/affordance;
- current effective relationship/state consequence.

### Stage should not automatically show historical explanation

- previous state;
- change event sequence;
- causal chain;
- `What Changed` summary;
- thematic narration such as `A different now`;
- permanent before/after comparison.

### History/causal trace may show

- relevant prior condition;
- effective event;
- retained consequence;
- resulting current state;
- minimal earlier/later comparison when needed.

Required principle:

> **The current Stage presents what is true now; causal trace explains why.**

---

## 10. Information-density budgets — qualitative, not numeric

Do not introduce arbitrary card/character counts or pixel quotas as product law.

Use qualitative budgets:

### Persistent budget

Only enough information to preserve:

- scope;
- human situation;
- disclosure/agency truth;
- immediately relevant salience;
- blocking status.

### Contextual budget

One coherent adjacent question at a time, such as:

- `What is available to B here?`
- `Why is this condition true?`
- `What did this consequence affect?`

Avoid opening unrelated evidence + history + diagnostics + Character dossier simultaneously.

### Deep budget

Depth is allowed when deliberately entered. Density may rise because the user chose analysis/history/diagnostics, but the surface must still preserve reading order, perspective authority and return path.

---

## 11. Accessibility contract

Progressive disclosure cannot hide meaning from assistive technology.

Required:

- L0 anchors have programmatic names/state;
- current people/participants and Current Opportunity have semantic equivalents;
- perspective and posture are announced when they change;
- contextual surfaces announce relationship to the invoking item;
- focus enters expanded content predictably and returns safely;
- collapsed content remains discoverable;
- current/historical and provisional/effective distinctions are not color-only;
- causal trace has meaningful reading order;
- narrow/adaptive layouts preserve the same semantics;
- reduced motion does not remove disclosure-transition meaning;
- Character identity does not depend on face/position/color alone.

Progressive disclosure is a visual-density strategy, not an excuse to remove semantic access.

---

## 12. ARM64 / battery / implementation implications

SIPD is intentionally compatible with a quiescent, event-driven Windows application.

Prefer later implementation patterns such as:

- derive view state from authoritative Production + navigation/session state;
- instantiate deep inspectors on demand;
- virtualize/lazy-load long history when required;
- recompute only affected local view projections after state change;
- preserve cached static Character representation where appropriate;
- use state-triggered, brief, optional motion;
- do no decorative idle inference.

Avoid baseline dependence on:

- continuous graph/layout physics;
- always-live transcript processing;
- background summarization to keep contextual panels populated;
- persistent provider polling;
- background NPU inference for ambience;
- continuous face/emotion analysis;
- permanent GPU-heavy relationship canvases.

When Production state and user focus do not change, Stage rendering should be computationally quiescent.

No Windows App SDK/Windows AI API selection is made by this proposal.

---

## 13. State-management boundary

SIPD state must not be confused with Production authority.

Navigation/session view state may include:

- selected Character/fact/event;
- open inspector;
- expanded/collapsed context;
- current scroll/focus location;
- local pane mode;
- transient filter/sort;
- safe return point.

These do not create causal history or alter Production StateHash merely because the UI changed.

Production-derived semantic state may include, according to current/future authority:

- current Scene;
- current participants;
- current opportunity;
- effective current conditions;
- disclosure/access projection;
- accepted/effective causal state.

Implementation must preserve this boundary.

---

## 14. What SIPD explicitly rejects

Do not default the live Stage to:

- permanent Character dossier rail;
- permanent evidence taxonomy panel;
- permanent transcript/chat window;
- permanent causal timeline;
- permanent `What Changed` panel;
- permanent relationship meters;
- permanent Tension/Progress/Risk meters;
- permanent provider/model telemetry;
- multiple simultaneous inspectors;
- universal action ribbon;
- creator-only content dimmed inside bounded perspective;
- AI-generated psychological summaries;
- perpetual animation as a substitute for changing Production state.

This is not minimalism for its own sake.

It is information authority and human-priority discipline.

---

## 15. First SIPD falsification packet

If the Director approves this proposal, the next smallest justified visual experiment is one **controlled information-presence study**, not a final Stage design.

Working name:

`SIPD-V1 — Live Stage Presence Test`

Use one architecture-correct semantic state:

- same P0 / S0 / A / B / C;
- Character-Bounded Watch;
- Current Opportunity = C;
- response not required;
- one already-effective changed current condition;
- no Perform controls;
- no private-mind inference;
- no permanent transcript;
- no permanent evidence dashboard;
- no history panel;
- no provider diagnostics;
- no thematic narration.

Required persistent/ambient information only:

- Production + Scene continuity;
- active bounded perspective;
- Watch posture only if needed to prevent agency ambiguity;
- people/relational field;
- C's Current Opportunity with non-obligation semantics;
- smallest current fact/evidence cue needed to understand the changed present.

Allow exactly one user-invoked contextual evidence expansion in a second state if necessary to test progressive disclosure.

Falsification questions:

1. Does the live Stage remain understandable before any inspector opens?
2. Are people still the first read?
3. Is B-bounded disclosure legible without a permanent evidence dashboard?
4. Is C's opportunity legible without becoming a game turn?
5. Is the changed present understandable with only the smallest legitimate current evidence?
6. Can deeper evidence be reached without leaving the Production mentally?
7. Does closing the context surface restore the human field cleanly?
8. Does the design remain meaningful in narrow/single-surface layout?
9. Does it avoid depending on a transcript, timeline or narration?
10. Does the design remain plausible as an event-driven, quiescent ARM64 UI?

Stop after first unrefined presence/expanded-context evidence and critique. No automatic refinement chain.

---

## 16. Recursive audit

Audit order:

`Director authorization -> information-relationship architecture -> shell grammar -> continuous workspace -> visual hierarchy -> Watch/Perform contract -> CRV identity -> TCV changed-present -> Patch 0014 disclosure authority -> opportunity semantics -> causal-history boundary -> transcript authority -> adaptive layout -> accessibility -> state management -> ARM64 quiescence -> anti-churn -> scope`

Material corrections made during audit:

1. treated SIPD as specialization of the existing shell, not a new navigation architecture;
2. made `importance != permanence` explicit;
3. removed the assumption that Character identity requires a permanent roster rail;
4. kept Current Opportunity ambient only while materially active and explicitly non-obligatory;
5. moved current authoritative facts to contextual presence rather than a permanent state dashboard;
6. moved Character-bounded evidence to progressive disclosure rather than a permanent four-section panel;
7. prohibited `Unknown` UI from revealing private categories whose existence is not legitimately available;
8. moved transcript/recent Performance to progressive disclosure by default and preserved Patch 0014's current `recentPerformances = []` boundary;
9. kept posture-specific commands contextual, with Perform input as the justified persistent exception while Perform is active;
10. moved causal trace/history fully on demand and preserved TEO comparison only as an optional history resource;
11. made capability status absent when healthy, ambient only when blocking/degraded, with diagnostics on demand;
12. prevented wide layouts from opening multiple inspectors merely because space exists;
13. required bounded perspective to become quieter through subtraction rather than show privileged placeholders;
14. separated navigation/session disclosure state from Production authority;
15. prohibited background summarization/polling/inference to populate idle panels;
16. preserved accessibility discoverability despite visual collapse;
17. constrained the next render to a single information-presence falsification rather than broad Stage refinement.

After each material correction, the audit restarted from upstream authority.

Final complete pass:

> **PASS — no remaining material contradiction, disclosure leak, persistent-density overreach, transcript/history overclaim, perspective/posture conflation, accessibility gap, quiescence conflict, or worthwhile correction within SIPD-01 scope.**

---

## 17. Director gate

Director decision requested:

> **Accept SIPD-01: the live Stage keeps only continuity anchors, the living human field, materially active opportunity/agency truth, and the smallest current evidence necessary to avoid ambiguity; evidence detail, transcript/Performance history, causal trace, diagnostics and most commands are progressively disclosed according to task and perspective.**

If approved, the next smallest justified action is:

> **Generate SIPD-V1 — Live Stage Presence Test as one controlled unrefined information-presence experiment, critique it, and stop before refinement or implementation.**

No final Stage layout, transcript architecture, Character Context taxonomy, history UX, WinUI control mapping, production XAML/C#, or final visual surface is authorized by this proposal.
