<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN ARS-01 — ANSWER ROUTE & SUFFICIENCY SIGNALING PROPOSAL

Status: DIRECTOR PROPOSAL FOR REVIEW / NON-RENDER ANSWER-STATE COMMUNICATION CONTRACT / NO ANSWER ENGINE, HISTORY UI, OR FINAL VISUAL SIGNALING SELECTED

Date: 2026-09-04

Phase: Kymaean App + Website Design Synthesis — after AAS-V1 source-sufficiency validation

## 0. Purpose

Define how Kymaean communicates the result of authoritative answer sourcing without exposing engineering internals, inventing uncertainty, falsely negating the fiction, or promising a historical explanation that current authority cannot actually provide.

AAS-V1 established four source-sufficiency outcomes:

```text
1. sufficient current answer
2. sufficient Character-bounded answer
3. historical route required
4. bounded insufficiency
```

ARS-01 addresses the user-facing semantic layer immediately after that sourcing decision.

It does not add:

- application APIs;
- a new answer engine;
- a new history/provenance store;
- Observation generation;
- recent Performance context;
- CharacterClaim disclosure;
- a causal-history implementation;
- a final visual status system;
- WinUI code;
- provider/model/NPU behavior.

Authority basis:

- `CURRENT_STATE.md`;
- `docs/KYMAEAN_AAS_01_AUTHORITATIVE_ANSWER_SOURCING_PROPOSAL.md`;
- `docs/KYMAEAN_AAS_V1_SOURCE_SUFFICIENCY_MATRIX_RESULT.md`;
- `docs/KYMAEAN_BCA_01_BOUNDED_CONTEXT_ANSWER_PROPOSAL.md`;
- `docs/KYMAEAN_BCA_V1_ONE_QUESTION_ONE_ANSWER_RESULT.md`;
- `docs/KYMAEAN_CDT_01_CONTEXT_DISCLOSURE_TRANSITION_PROPOSAL.md`;
- current `Rylascoo/Ensemble-Project` authority through H1 Patch 0014.

---

## 1. Core communication law

The answer surface must communicate **what the authority can support**, not how confident an AI feels.

Required law:

> **Deterministic authority boundaries must not be presented as probabilistic confidence.**

Therefore Kymaean must not translate a source result such as `unsupported under current authority` into ambiguous language such as:

- `probably`;
- `maybe`;
- `I think`;
- `seems`;
- `low confidence`;
- a confidence meter.

The product instead communicates one of three primary user-facing conditions:

```text
SUPPORTED NOW
HISTORY REQUIRED / AVAILABLE
NOT CURRENTLY SUPPORTABLE
```

Character-bounded answers remain a supported-now condition with an explicit perspective scope when that scope matters.

These are semantic communication classes, not proposed implementation enums or persistent UI badges.

---

## 2. Primary signaling principle

> **State the supported truth first; state the boundary second; offer only a route that authority can justify.**

Default sequence:

```text
question
-> supported answer OR precise limitation
-> minimum scope/boundary cue if needed
-> at most one meaning-connected next route
-> return to Stage
```

Do not start with a system-status banner if the question can be answered directly.

Do not make the user decode an icon/color before reading the answer.

Do not convert every answer into a provenance dashboard.

---

## 3. Condition A — Supported now

### 3.1 Current creator-operational answer

When current Production/routing authority directly supports the requested claim, answer directly.

Controlled AAS-V1 case:

```text
Question:
Who currently has the opportunity?

Supported answer if CurrentOpportunityCharacterId == C:
C currently has the opportunity.
```

No `verified`, `high confidence`, or green success badge is semantically required.

Do not add:

```text
C must respond.
```

unless separate obligation authority exists.

### 3.2 Character-bounded current answer

When the answer is scoped to a Character perspective, make the perspective legible without turning it into a disclaimer wall.

Preferred semantic framing:

```text
From B's current perspective
[direct supported answer]
```

or an equivalent compact accessible scope cue.

Avoid wording such as:

```text
B knows that...
```

unless the specific knowledge claim itself is authoritatively supported.

A perspective scope marker tells the user **which disclosure boundary governs the answer**. It does not itself assert Character knowledge.

### 3.3 Supporting basis

If BCA minimum sufficiency requires supporting basis, include only the smallest question-relevant authoritative basis.

Do not expose:

- `SourceStateHash`;
- ContextPacketId;
- internal AccessReason;
- record hashes;
- commit hashes;
- provider/model trace.

Required principle:

> **Provenance governs the answer; it does not need to dominate the answer surface.**

---

## 4. Condition B — Historical explanation required

A current answer can be sufficient for `what is true now` while insufficient for `why it became true`.

Example:

```text
Current authority:
C currently has the opportunity.

Question:
Why does C currently have the opportunity?
```

ARS must not silently append a causal explanation from co-current facts, visual cues, or plausible narrative completion.

### 4.1 Current fact first

If current authority supports the present fact, preserve it:

```text
C currently has the opportunity.
```

Then communicate the temporal boundary:

```text
The current context does not establish why.
```

Exact wording remains open, but the semantics must distinguish current fact from historical explanation.

### 4.2 A question-specific `Why?` route requires authoritative availability

A `Why?`, `See why`, `Trace why`, or equivalent explanation affordance creates a promise: the product can meaningfully pursue the requested causal explanation.

Required law:

> **Do not offer a question-specific historical explanation action unless an authoritative route for that requested explanation is established as available.**

The existence of a history container, StateHash chain, or opportunity transition event alone is not enough if the requested rationale is absent from that authority.

Patch 0013 is the controlled example:

```text
canonical E0OpportunityTransition
proves selected Character + transition identity

but

canonical event does not carry the full Director input / trace / natural-language rationale
```

Therefore:

```text
transition exists
!=
creator-facing Why? is necessarily answerable
```

### 4.3 When history is authoritative and sufficient

If a legitimate historical source route is known to support the requested explanation, one meaning-connected route may appear.

Conceptually:

```text
C currently has the opportunity.
[Trace why]
```

The route label must communicate historical explanation rather than generic browsing.

Exact copy is not selected by ARS-01.

### 4.4 When historical sufficiency is not established

Do not show a `Why?` affordance merely because history exists somewhere.

Safe semantic outcome:

```text
C currently has the opportunity.
The current authoritative context does not establish a supported reason for that assignment here.
```

This does not mean no reason exists in the fiction.

It means the currently available authority cannot support the requested explanation.

If a generic History surface is independently useful and later authorized, its label must remain neutral and must not imply it contains the answer to this particular question.

---

## 5. Condition C — Not currently supportable

Bounded insufficiency is not an error state by default. It is a truthful answer boundary.

Required law:

> **Describe the authority limitation without converting it into a fictional negation.**

### 5.1 Missing current answer authority

Preferred semantic pattern:

```text
The current context does not establish an answer to that question.
```

Do not transform this into:

```text
That did not happen.
```

unless authoritative state actually establishes non-occurrence.

### 5.2 Character-perspective limitation

If the question is explicitly scoped to B and the permitted B projection cannot support it:

```text
B's current perspective does not provide an answer to that question.
```

This phrasing does not confirm that inaccessible private content exists.

Do not use:

```text
C's private reasoning is hidden from B.
```

unless the existence of that category is itself legitimately known and intentionally exposed.

### 5.3 Unsupported Observation

Controlled AAS-V1 case:

```text
Question:
What did B observe about C?

No question-relevant permitted B-owned Observation exists.
```

Safe semantic form:

```text
B's current context does not establish an observation about C for this question.
```

Do not substitute rendered gaze, pose, gesture, co-presence, or apparent speaking/listening.

### 5.4 Unavailable recent dialogue

Controlled Patch 0014 case:

```text
recentPerformances = []
RecentPerformanceText = empty
```

Safe semantic form:

```text
Recent dialogue is not available in B's current bounded context for this question.
```

This must remain distinct from:

```text
C said nothing.
```

---

## 6. Permission, absence, and insufficiency must not collapse

ARS preserves the following distinctions:

```text
not available in current authority
!=
did not happen

not permitted to this perspective
!=
does not exist

historical route not established
!=
no history exists

current answer insufficient
!=
low confidence

technical feature unavailable
!=
fictional Character refusal
```

These differences must survive final copy, accessibility output, and any future model-assisted layer.

---

## 7. Technical/capability limitations are operational, not fictional

If an answer/action cannot proceed because of product capability state, communicate that as technical/product state.

Do not fictionalize it.

Conceptually:

```text
This explanation is not available with the current capability state.
```

not:

```text
B cannot remember.
C refuses to explain.
The Scene does not allow it.
```

Exact readiness/hardware wording is deferred until actual Windows/AI capability contracts are authorized and implemented.

ARS-01 does not introduce or claim `AIFeatureReadyState` behavior in the current application baseline.

---

## 8. Route-affordance law

A contextual answer surface should normally expose at most one primary meaning-connected continuation beyond return.

Examples of legitimate future semantic routes may include:

```text
Trace why
Inspect current opportunity
Return to Scene
```

but only when the active answer/source state justifies them.

Reject as default:

```text
Ask anything about C
Explore more
Related details
See all context
Why?  [when no answerable historical route is established]
```

Required principle:

> **The next action follows the meaning of the answer, not the existence of more data.**

---

## 9. Do not create a traffic-light answer system

ARS-01 does not authorize permanent visual states such as:

- green = authoritative;
- yellow = uncertain;
- red = unavailable;
- confidence percentages;
- certainty meters;
- truth scores;
- provenance scores.

Reason:

- deterministic support is not probabilistic confidence;
- color-only status fails accessibility;
- a strong visual status system would compete with the human-first Stage;
- `unavailable` can mean several semantically distinct things that one red state would collapse.

Preferred hierarchy:

```text
1. exact answer/limitation language
2. compact scope or temporal cue when necessary
3. route availability
4. optional redundant icon/color later, never sole meaning
```

No final visual treatment is selected.

---

## 10. Scope cues

Scope cues exist only to prevent ambiguity.

Potential semantic scopes:

```text
Current
From B's current perspective
History
Technical / capability
```

These are not required to appear as permanent chips or tabs.

Use a scope cue only when the answer could otherwise be misunderstood as belonging to a different perspective, temporal locus, or authority lane.

Required law:

> **Scope clarification is contextual; it is not another permanent metadata rail.**

---

## 11. Return behavior

ARS inherits CDT:

```text
LIVE STAGE
-> question / contextual disclosure
-> answer / route state
-> Back / dismiss
-> SAME LIVE STAGE
```

Answer sufficiency signaling does not:

- mutate Production;
- consume Current Opportunity;
- change Presentation Perspective;
- enter Perform;
- create a Performance;
- establish fictional truth;
- widen disclosure authority.

If the user enters a causal-history route, the inspection locus may change to history, but the originating Production/Scene/perspective anchor and return path remain preserved.

---

## 12. Accessibility contract

Every answer state must be understandable through semantic text/programmatic structure without depending on:

- color;
- icon shape;
- portrait;
- animation;
- panel position;
- visual salience;
- hover-only explanation.

Assistive technology must be able to recover:

1. the exact question;
2. the direct supported answer or exact limitation;
3. the active perspective/temporal scope when material;
4. whether a historical explanation route is actually available;
5. the one next action, if any;
6. the return action.

Focus order must follow that semantic order.

When a route is unavailable, disabled-but-visible controls should not leak the existence of private or unsupported content. Omission is preferred unless the user has explicitly requested the unavailable operation and needs an explanation.

---

## 13. ARM64 / quiescence contract

ARS signaling must not require continuous inference or proactive answer-route prediction.

Preferred later implementation characteristics:

- derive answer state from already-authoritative local data when possible;
- determine route availability deterministically from existing authority metadata/source associations where possible;
- if determining historical sufficiency requires deeper work, perform it only on explicit user action rather than idle precomputation;
- no background summarization;
- no speculative `Why?` generation;
- no provider polling;
- no idle NPU inference;
- no face/emotion analysis;
- no persistent GPU animation.

A UI affordance must not promise more than the system has actually established merely to avoid a later check.

---

## 14. Controlled wording matrix

The following examples define semantics, not final copy.

| Authority condition | Safe semantic communication | Must not imply |
|---|---|---|
| Current routing fact supported | `C currently has the opportunity.` | `C must respond.` |
| B-bounded current fact supported | `From B's current perspective: [supported fact].` | `B knows [fact]` unless Knowledge authority exists |
| Current fact supported; historical explanation proven available | current fact + one historical explanation route | current state itself contains the causal reason |
| Current fact supported; requested reason not established | `C currently has the opportunity. The current authoritative context does not establish a supported reason here.` | `there is no reason` |
| Observation unsupported | `B's current context does not establish an observation for this question.` | `B saw nothing` |
| Recent dialogue unavailable | `Recent dialogue is not available in B's current bounded context for this question.` | `C said nothing` |
| Perspective cannot support requested private/other-owned fact | `B's current perspective does not provide an answer to that question.` | existence/content of denied material |
| Technical capability unavailable | explicit operational limitation | fictional refusal/psychology |

---

## 15. Falsification tests

ARS-01 fails if any proposed answer state:

1. uses confidence language to disguise missing authority;
2. makes `not available` mean `did not happen`;
3. exposes denied-category existence merely to explain omission;
4. offers `Why?` when the requested historical explanation is not authoritatively available;
5. turns a historical transition into an unsupported natural-language rationale;
6. turns Current Opportunity into obligation;
7. turns perspective scope into a Knowledge claim;
8. renders engineering hashes/IDs as fictional evidence;
9. makes technical capability failure look like Character behavior;
10. uses color/iconography as the sole distinction;
11. creates a permanent answer-status dashboard;
12. changes Production/perspective/posture merely by answering;
13. requires idle AI/NPU work to keep answer states ready.

---

## 16. Recursive audit

Audit order:

`Director approval -> AAS-V1 result -> AAS-01 -> BCA/CDT/SIPD contracts -> current app head -> Patch 0013 opportunity authority -> Patch 0014 Access/Context authority -> answer semantics -> scope wording -> history availability promise -> insufficiency wording -> private-category leakage -> opportunity/obligation -> perspective/knowledge distinction -> technical/fictional separation -> accessibility -> ARM64 quiescence -> surface/scope`

Material corrections made during ARS-01 construction:

1. separated `historical route exists` from `requested explanation is answerable`;
2. prohibited question-specific `Why?` affordances unless authoritative explanation availability is established;
3. made current fact appear before historical-boundary language so a `why` failure does not hide what is actually known;
4. split perspective limitation wording from generic current insufficiency to avoid confusing disclosure with nonexistence;
5. removed confidence/traffic-light semantics because deterministic insufficiency is not probability;
6. prohibited disabled/visible private-content controls that could leak inaccessible category existence;
7. preserved `B perspective` as a disclosure scope rather than claiming `B knows`;
8. separated technical capability limitation from fictional behavior;
9. required route actions to follow answer meaning rather than generic entity browsing;
10. preserved explicit-user-action historical checks over idle precomputation for ARM64 quiescence.

After each material correction, audit restarted from AAS-V1 and current application authority.

Final full pass:

> **PASS — no remaining false-fiction negation, confidence masquerade, perspective/knowledge conflation, unsupported `Why?` promise, private-category leak, opportunity/obligation conflation, technical/fictional confusion, accessibility-only visual dependency, or worthwhile correction within ARS-01 scope.**

---

## 17. Director gate

Director decision requested:

> **Adopt ARS-01: Kymaean states supported truth directly, describes insufficiency as an authority boundary rather than uncertainty or fictional negation, and offers a historical explanation action only when that requested explanation is authoritatively available. Perspective, temporal locus, and technical capability are clarified only when needed and never collapsed into one generic status system.**

If approved, the next smallest justified action is a non-render controlled validation:

`ARS-V1 — Answer State Language Matrix`

It should test exact wording/affordance semantics for:

1. supported current answer;
2. supported Character-bounded answer;
3. current fact + authoritative history route available;
4. current fact + requested reason unavailable;
5. perspective-bounded insufficiency;
6. recent-dialogue insufficiency.

No final copy, visual badge/color system, history UI, answer engine, observation/recent-Performance implementation, WinUI code, or website implementation is authorized by ARS-01.
