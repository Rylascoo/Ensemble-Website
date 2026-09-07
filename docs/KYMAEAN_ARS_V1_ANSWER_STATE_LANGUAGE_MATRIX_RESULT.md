<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN ARS-V1 — ANSWER STATE LANGUAGE MATRIX RESULT

Status: DIRECTOR RESULT FOR REVIEW / NON-RENDER LANGUAGE + AFFORDANCE VALIDATION / NO FINAL COPY SYSTEM, HISTORY UI, OR ANSWER ENGINE SELECTED

Date: 2026-09-04

Phase: Kymaean App + Website Design Synthesis — after ARS-01 approval

## 0. Purpose

Validate `docs/KYMAEAN_ARS_01_ANSWER_ROUTE_SUFFICIENCY_SIGNALING_PROPOSAL.md` against six controlled user-facing answer states.

This matrix tests semantic wording, scope cues, and route promises only. It does not add application authority, an answer engine, history persistence/UI, Observation generation, recent Performance context, CharacterClaim disclosure, provider/model behavior, WinUI code, or final visual styling.

Authority resolved for this matrix:

- `Rylascoo/Ensemble-Website` parent checkpoint: `c219dba92a2aa65ecedc23f3b97cfe8ddd209fbb`;
- `Rylascoo/Ensemble-Project` current `main`: `7475a9397cff9063673908c666a729f0f3cd4525`;
- accepted AAS-01 / AAS-V1 source-sufficiency laws;
- approved ARS-01 answer-route / signaling laws;
- H1 Patch 0013 Current Opportunity authority;
- H1 Patch 0014 Production Context Continuity.

Core law under test:

> **The answer surface communicates the strongest truth the current authority supports, then the exact boundary if one matters, and never advertises an explanation route that cannot fulfill the requested question.**

---

## 1. Matrix summary

| Case | Controlled condition | Validated user-facing semantic form | Primary result |
|---|---|---|---|
| ARS-V1.1 | Supported current routing fact | `C currently has the opportunity.` | **DIRECT ANSWER PASS** |
| ARS-V1.2 | Supported Character-bounded current fact | `From B's current perspective: [supported fact].` | **PERSPECTIVE-SCOPED ANSWER PASS** |
| ARS-V1.3 | Current fact supported + exact historical explanation route established available | current fact + one `Trace why`-type route | **CONDITIONAL HISTORY-ROUTE PASS** |
| ARS-V1.4 | Current fact supported + requested reason not established | current fact + exact present-boundary sentence; no `Why?` route | **BOUNDED CAUSAL-INSUFFICIENCY PASS** |
| ARS-V1.5 | Perspective-bounded Observation answer unsupported | `B's current perspective does not establish an observation about C for this question.` | **PERSPECTIVE-INSUFFICIENCY PASS** |
| ARS-V1.6 | Recent dialogue unavailable under Patch 0014 | `Recent dialogue is not available in B's current perspective for this question.` | **CURRENT-CONTEXT AVAILABILITY PASS** |

The matrix validates that ARS semantic classes do **not** need to appear as persistent labels such as `SUPPORTED`, `HISTORY`, or `UNAVAILABLE`. The wording and route state can carry the meaning directly.

---

## 2. ARS-V1.1 — Supported current answer

### Question

> **Who currently has the opportunity?**

### Controlled authoritative condition

```text
ProductionState.CurrentOpportunityCharacterId == C
```

### Validated answer

```text
C currently has the opportunity.
```

### Why this wording passes

It:

- answers the requested claim directly;
- preserves `Current Opportunity != obligation`;
- does not add a reason;
- does not claim B knows the routing state;
- does not require `Verified`, `Authoritative`, `High confidence`, a percentage, or a green status badge.

### Rejected variants

```text
C must respond now.
```

Rejected: obligation is not established by Current Opportunity.

```text
I'm confident C has the opportunity.
```

Rejected: deterministic routing authority is not model confidence.

```text
Verified: C has the opportunity.
```

Rejected as default: adds system-status ornament when a direct answer is sufficient.

### Result

**PASS — DIRECT ANSWER REQUIRES NO EXPLICIT SUFFICIENCY BADGE.**

---

## 3. ARS-V1.2 — Supported Character-bounded current answer

### Question

> **What current shared condition is available to B?**

### Controlled premise

The exact current Production state contains at least one question-relevant active `SceneState` or `Pressure` record permitted to B through Patch 0014 Access/Context, with same-state association intact.

The actual record content is intentionally not invented by this design matrix.

### Validated semantic template

```text
From B's current perspective:
[supported question-relevant current fact]
```

### Why this wording passes

The scope cue establishes the governing disclosure boundary without asserting:

```text
B knows...
B noticed...
B understands...
```

unless those separate epistemic propositions are themselves supported.

The cue is required only when omission would make the answer look like full-Production/creator omniscience.

### Rejected variants

```text
B knows that [fact].
```

Rejected unless explicit permitted Knowledge authority supports that claim.

```text
Available to B (82% confidence): [fact].
```

Rejected: perspective permission is not probabilistic confidence.

### Result

**PASS — PERSPECTIVE MAY BE CLARIFIED WITHOUT BECOMING A KNOWLEDGE CLAIM.**

---

## 4. ARS-V1.3 — Current fact + authoritative historical explanation route available

### Question

> **Why does C currently have the opportunity?**

### Controlled premise

For this language case only, assume the user has explicitly asked the causal question and the system has established that an exact authoritative historical source route exists **and is semantically sufficient for the requested explanation**.

This is a conditional UX test. It is **not** a claim that the current Patch 0013/0014 retail baseline already implements such persistence/history UI for this question.

### Validated semantic form

```text
C currently has the opportunity.
[Trace why]
```

Equivalent future route wording may differ; `Trace why` is semantic test copy, not selected final copy.

### Required route behavior

The route must:

- enter an explicitly historical explanatory locus;
- preserve the originating Production/Scene/perspective anchor;
- answer only to the strength of the authoritative historical source;
- preserve return to the same current Stage;
- avoid implying that the present state itself contained the causal explanation.

### Rejected variants

```text
Why?
```

Rejected as a generic always-present affordance. It is valid only after question-specific explanatory availability is established.

```text
See history
```

Insufficient as the primary answer route if the product is promising a causal explanation; generic history existence does not prove that history answers the requested `why`.

### Result

**PASS — CONDITIONAL ONLY. AN EXPLANATION ROUTE IS A PROMISE AND REQUIRES QUESTION-SPECIFIC AUTHORITATIVE AVAILABILITY.**

---

## 5. ARS-V1.4 — Current fact + requested reason unavailable

### Question

> **Why does C currently have the opportunity?**

### Current authoritative condition

Current state establishes:

```text
CurrentOpportunityCharacterId == C
```

but the exact creator-facing causal rationale requested by the question is not established as available from current/historical authority.

This matches the current Patch 0013 boundary when only the canonical opportunity transition is available: selection is established; a full natural-language rationale is not automatically established.

### Validated answer

```text
C currently has the opportunity.
The current context establishes that fact, but not why C was selected.
```

### Affordance

No question-specific `Why?`, `Trace why`, or equivalent explanatory route is shown.

Return to the Stage remains available.

### Why this wording passes

It:

- preserves the supported present fact;
- states the causal boundary without saying `there is no reason`;
- avoids engineering language such as `missing DirectorTrace`;
- avoids confidence language;
- does not imply a hidden explanation exists;
- does not offer a route that may fail to fulfill the question.

### Rejected variants

```text
There is no reason available.
```

Rejected: can be read as negating the fiction rather than describing the answer boundary.

```text
The system is unsure why.
```

Rejected: source insufficiency is not uncertainty.

```text
C was selected because they are leading the discussion.
```

Rejected: unsupported renderer/model completion.

### Result

**PASS — CURRENT TRUTH AND CAUSAL INSUFFICIENCY CAN COEXIST WITHOUT FALSE NEGATION OR A FALSE `WHY` PROMISE.**

---

## 6. ARS-V1.5 — Perspective-bounded insufficiency

### Question

> **What did B observe about C?**

### Controlled authoritative condition

No question-relevant B-owned permitted `Observation` record exists.

Stage portrayal, co-presence, gaze, gesture, apparent speech, relationship, nomination, Director selection, `SceneState`, and causal adjacency remain non-sources for Observation.

### Validated answer

```text
B's current perspective does not establish an observation about C for this question.
```

### Why this wording passes

It describes what the perspective-authorized answer state can establish. It does not claim:

```text
B saw nothing.
B did not notice C.
C was not observable.
```

It also does not name a private/denied category that would leak inaccessible schema.

### Rejected variants

```text
B didn't see anything about C.
```

Rejected: absence of an authoritative Observation is not proof of fictional non-observation.

```text
Observation data is unavailable.
```

Rejected as default user-facing wording: exposes storage/domain language rather than the semantic answer boundary.

### Result

**PASS — PERSPECTIVE INSUFFICIENCY CAN BE COMMUNICATED WITHOUT FICTIONAL NEGATION OR SCHEMA LEAKAGE.**

---

## 7. ARS-V1.6 — Recent-dialogue insufficiency

### Question

> **What did C just say, from B's current perspective?**

### Current authoritative condition

Patch 0014 canonical Context v2 keeps:

```text
recentPerformances = []
RecentPerformanceText = empty
```

### Validated answer

```text
Recent dialogue is not available in B's current perspective for this question.
```

### Why this wording passes

It states availability in the current bounded answer source without saying:

```text
C said nothing.
B heard nothing.
There was no recent Performance.
```

The answer therefore preserves the distinction:

```text
not available from current answer authority
!=
did not happen in the fiction
```

### Rejected variants

```text
C hasn't said anything recently.
```

Rejected: current Context v2 emptiness does not establish fictional silence.

```text
I can't remember what C said.
```

Rejected: technical/context limitation must not be fictionalized as Character or assistant memory.

### Result

**PASS — CURRENT CONTEXT LIMITATION IS LEGIBLE WITHOUT CLAIMING FICTIONAL SILENCE.**

---

## 8. Cross-case language laws

### 8.1 Do not name the semantic class unless naming it solves real ambiguity

A direct supported answer should normally just answer.

Therefore ARS does not require visible labels such as:

```text
SUPPORTED NOW
AUTHORITATIVE
UNAVAILABLE
LOW CONFIDENCE
```

The semantic class is internal/product logic; user-facing language carries the meaning.

### 8.2 `Does not establish` is stronger than uncertainty wording

For deterministic bounded insufficiency, wording such as:

```text
does not establish
is not available in this perspective/context
```

is preferable to:

```text
maybe
probably
seems
not sure
low confidence
```

because the former describes the source boundary rather than simulating model uncertainty.

### 8.3 Avoid unnecessary engineering nouns

Default user-facing copy should not require:

- `authority source`;
- `SourceStateHash`;
- `ContextPacket`;
- `AccessReason`;
- `DirectorTrace`;
- record/domain enum names.

Those may govern the answer internally without becoming the answer.

### 8.4 A perspective cue is scope, not psychology

`From B's current perspective` means the answer was bounded by B's disclosure authority.

It does not itself mean:

- B knows;
- B saw;
- B heard;
- B remembers;
- B agrees.

### 8.5 A historical route must be question-specific

The product may know that history exists while still lacking the requested rationale.

Therefore:

```text
history exists
!=
show Trace why
```

The route is valid only when the user has asked a causal question and the corresponding authoritative historical explanation has been established as available.

### 8.6 No answer-state traffic light

The six cases remain semantically distinguishable through text + route state alone.

No confidence meter, truth score, permanent green/yellow/red legend, or status dashboard is required.

---

## 9. Accessibility / interaction result

The six states can be represented in a linear accessible order:

```text
question
-> answer or limitation
-> scope cue if material
-> one available meaning-connected route, if any
-> Return to Scene
```

No state depends on color, iconography, portrait, panel position, hover, animation, or motion.

A route that is not authorized should normally be omitted rather than displayed disabled, especially when visibility could leak the existence of inaccessible/private content or promise unsupported explanation.

---

## 10. ARM64 / quiescence result

ARS-V1 requires no continuous inference, background summarization, speculative historical explanation generation, provider polling, idle NPU activity, face/emotion analysis, or persistent GPU animation.

A supported answer may be composed from already-authoritative local state.

Question-specific historical-route availability may be evaluated after explicit user causal inquiry; no idle precomputation is required by this matrix.

---

## 11. Formal verdict

> **PASS — ANSWER-STATE LANGUAGE SEMANTICS VALIDATED ACROSS DIRECT, CHARACTER-BOUNDED, CONDITIONAL-HISTORY, CAUSAL-INSUFFICIENT, OBSERVATION-INSUFFICIENT, AND RECENT-DIALOGUE-INSUFFICIENT CASES.**

Promote as durable law:

> **Kymaean should usually communicate answer sufficiency through the answer itself: direct truth when supported, exact source-boundary language when unsupported, and a historical explanation affordance only when that requested explanation is actually available.**

Also promote:

> **Trust signaling should be semantic before it is decorative.**

No final copy strings are frozen for production; the tested wording establishes semantics and failure boundaries, not a permanent localization contract.

No visual surface is selected.

---

## 12. Recursive audit

Audit order:

`Director approval -> ARS-01 -> AAS-V1/AAS-01 -> current website/app heads -> Patch 0013 opportunity authority -> Patch 0014 Access/Context authority -> exact question -> answer proposition -> perspective scope -> temporal scope -> route promise -> fictional-negation risk -> confidence leakage -> private-category leakage -> opportunity/obligation -> technical/fictional separation -> accessibility -> ARM64 quiescence -> surface/scope`

Material corrections during ARS-V1 construction:

1. removed the need to visibly label supported answers as `SUPPORTED`/`AUTHORITATIVE` when direct answer text already communicates the state;
2. kept ARS-V1.2 as a semantic template because no exact current shared SceneState/Pressure text was supplied by current authority, preventing invented fictional facts;
3. made ARS-V1.3 explicitly conditional and future-facing rather than implying current Patch 0013/0014 already implements a sufficient persistent causal-history route;
4. changed the unavailable-reason copy to `The current context establishes that fact, but not why C was selected`, avoiding both engineering jargon and the false-fiction implication `there is no reason`;
5. preserved Observation insufficiency as a perspective/source boundary rather than `B saw nothing`;
6. preserved recent-dialogue insufficiency as current-context availability rather than `C said nothing` or fictional memory failure;
7. required omission of unsupported explanation affordances rather than disabled visible `Why?` controls;
8. retained `Current Opportunity != obligation`, `Perspective != Knowledge`, `not available != did not happen`, `history exists != requested explanation answerable`, and `technical limitation != fictional behavior`;
9. confirmed all six cases remain semantically recoverable without color, iconography, animation, or confidence scoring.

After each material correction, the audit restarted from Director approval and exact current application authority.

Final full pass:

> **PASS — no remaining confidence masquerade, false-fiction negation, unsupported history promise, perspective/knowledge conflation, Observation inference, recent-Performance assumption, opportunity/obligation conflation, private-category leak, technical/fictional confusion, accessibility-only visual dependency, or worthwhile correction within ARS-V1 scope.**

---

## 13. Next unresolved design question

ARS-V1 validates the language semantics. The next unresolved question is spatial/experiential rather than epistemic:

> **Can these answer states appear inside the human-first continuous Stage without turning trustworthy boundaries into a status dashboard, generic assistant message, modal interruption, or visually dominant warning system?**

Proposed next controlled visual experiment:

`ARS-R1 — Answer State Surface Integration`

It should test answer-state integration against the accepted SIPD/CDT/BCA Stage baseline, with one controlled answer state at a time and no new semantic authority.

Recommended minimum visual cases for later Director approval:

1. one supported Character-bounded answer;
2. one bounded-insufficiency answer;
3. one current fact with a legitimately available historical explanation route (conditional test state, clearly not a claim of current app implementation).

The experiment must prohibit:

- traffic-light truth badges;
- confidence meters;
- permanent answer-status rails;
- generic chat/composer UI;
- schema/category dashboards;
- disabled `Why?` controls;
- engineering provenance IDs;
- invented Character psychology/Observation/dialogue;
- final surface/style selection.

No ARS-R1 render or implementation is authorized until Director approval of ARS-V1.
