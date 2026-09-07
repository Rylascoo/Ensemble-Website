<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN AAS-V1 — SOURCE SUFFICIENCY MATRIX RESULT

Status: DIRECTOR RESULT FOR REVIEW / NON-RENDER AUTHORITY VALIDATION / NO ANSWER ENGINE OR NEW APPLICATION AUTHORITY SELECTED

Date: 2026-09-04

Phase: Kymaean App + Website Design Synthesis — after AAS-01 approval

## 0. Purpose

Validate `docs/KYMAEAN_AAS_01_AUTHORITATIVE_ANSWER_SOURCING_PROPOSAL.md` against five controlled question/source cases using only authority already established by the current Ensemble deterministic spine.

This is not a UI mockup and does not add application APIs, new data, persistence, recent Performance context, Observation generation, causal-history implementation, or model-authored explanation.

Authority resolved for this matrix:

- `Rylascoo/Ensemble-Website` parent checkpoint: `44f0cd3f65a17d32403398dd7ea7f3e57a57f86b`;
- `Rylascoo/Ensemble-Project` current `main`: `7475a9397cff9063673908c666a729f0f3cd4525`;
- H1 Patch 0013 Effective Opportunity Authority;
- H1 Patch 0014 Production Context Continuity;
- AAS-01 source-lane, same-state, disclosure-before-relevance, statement-support, and bounded-insufficiency laws.

Core law under test:

> **A question is answerable only to the semantic strength actually supported by permitted authoritative sources.**

---

## 1. Matrix summary

| Case | Controlled question | Required authority | Result |
|---|---|---|---|
| AAS-V1.1 | Who currently has the opportunity? | Current `ProductionState.CurrentOpportunityCharacterId` | **SUFFICIENT CURRENT ANSWER** |
| AAS-V1.2 | What current shared condition is available to B? | Same-state, Access-permitted `SceneState` / `Pressure` record(s) | **SUFFICIENT CHARACTER-BOUNDED ANSWER WHEN RELEVANT PERMITTED RECORD EXISTS** |
| AAS-V1.3 | What did B observe about C? | B-owned permitted authoritative `Observation` | **BOUNDED INSUFFICIENCY WHEN NO SUCH OBSERVATION EXISTS** |
| AAS-V1.4 | What did C just say, from B's current bounded context? | Authorized recent Performance/dialogue context | **BOUNDED INSUFFICIENCY AT PATCH 0014** |
| AAS-V1.5 | Why does C currently have the opportunity? | Causal/historical authority sufficient for the requested rationale | **HISTORICAL ROUTE REQUIRED; SUFFICIENCY CONDITIONAL** |

The matrix therefore validates all four AAS semantic outcomes:

```text
1. sufficient current answer
2. sufficient Character-bounded answer
3. historical route required
4. bounded insufficiency
```

---

## 2. Case AAS-V1.1 — Direct Current Opportunity

### Question

> **Who currently has the opportunity?**

### Permitted source lane

Lane A — current Production / routing authority.

Required source:

```text
current ProductionState
-> CurrentOpportunityCharacterId
```

Current Patch 0013/0014 authority establishes Current Opportunity as effective deterministic Production routing state.

### Sufficiency judgment

**SUFFICIENT CURRENT ANSWER**

If the current authoritative value is C, the supported semantic answer is:

```text
C currently has the opportunity.
```

The answer may identify current routing state. It may not add a causal or psychological reason.

It also may not silently become:

```text
C must respond.
```

because Current Opportunity remains distinct from obligation.

### Boundary

This is creator-visible operational truth. It does not automatically establish that B knows the routing fact.

Required distinction:

```text
creator-visible routing truth
!=
Character knowledge
```

### Result

**PASS**

AAS correctly permits a direct deterministic answer without model inference.

---

## 3. Case AAS-V1.2 — Character-Bounded Current Shared State

### Question

> **What current shared condition is available to B?**

### Controlled authoritative premise

For this matrix case, assume the exact current Production state contains at least one question-relevant active `SceneState` or `Pressure` record and that Patch 0014 Access permits it into B's same-state Character projection/context.

This is controlled test data, not a claim that an unspecified rendered meeting detail is authoritative.

### Permitted source lane

Lane B — Character-bounded current fictional authority:

```text
current ProductionState
-> CharacterBoundedAccessControl.Evaluate(state, B)
-> CharacterAccessProjection
-> Production-bound ContextPacket v2
```

Current Patch 0014 permits active `SceneState` as shared Scene state and active `Pressure` as public Pressure.

Same-state association must hold for any Production/Context combination:

```text
ProductionState.StateHash
== CharacterAccessProjection.SourceStateHash
== ContextPacket.SourceStateHash
```

where those artifacts are used.

### Sufficiency judgment

**SUFFICIENT CHARACTER-BOUNDED ANSWER WHEN A QUESTION-RELEVANT PERMITTED RECORD EXISTS**

The answer may contain only the minimum relevant permitted current fact(s). It must not enumerate every permitted category merely because the projection contains them.

If no relevant permitted record exists, the same question falls to bounded insufficiency rather than visual/model completion.

### Result

**PASS**

AAS correctly distinguishes permission from relevance and requires exact current-state association.

---

## 4. Case AAS-V1.3 — Unsupported Observation

### Question

> **What did B observe about C?**

### Controlled authoritative premise

No question-relevant B-owned permitted `Observation` record exists.

The Stage artwork may visually depict C speaking, gesturing, looking toward B, or using objects. Those depiction cues are deliberately excluded as authority sources.

### Required authority

An epistemic claim using `observed`, `saw`, or `noticed` requires an actual permitted authoritative Observation for the active subject.

Patch 0014 explicitly does not infer observation from:

- co-presence;
- Candidate visible text;
- addressed Characters;
- nomination;
- Director selection;
- relationships;
- `SceneState`;
- causal adjacency;
- rendered gaze/pose/gesture.

### Sufficiency judgment

**BOUNDED INSUFFICIENCY**

Semantically safe response form:

```text
The current bounded context does not establish an observation by B about C for this question.
```

This must not be repaired with:

```text
B saw C looking at them.
B noticed C presenting terms.
```

unless separate authoritative Observation state actually supports those claims.

### Result

**PASS**

AAS correctly fails closed rather than promoting Scene portrayal into Character epistemic authority.

---

## 5. Case AAS-V1.4 — Unavailable Recent Dialogue

### Question

> **What did C just say, from B's current bounded context?**

### Required authority

Authorized recent Performance/dialogue material in current Character-bounded context.

### Current authority

Patch 0014 Context v2 canonically preserves:

```text
recentPerformances = []
RecentPerformanceText = empty
```

The context pipeline therefore does not currently supply recent Performance text merely because a concept image depicts C speaking.

### Sufficiency judgment

**BOUNDED INSUFFICIENCY AT PATCH 0014**

Semantically safe response form:

```text
No recent dialogue is available in B's current bounded context for this question.
```

This means only that the current bounded authority does not supply the requested dialogue. It must not be phrased as proof that C said nothing.

### Result

**PASS**

AAS correctly distinguishes absence of current answer authority from absence of fictional events.

---

## 6. Case AAS-V1.5 — Causal Explanation of Current Opportunity

### Question

> **Why does C currently have the opportunity?**

### Current authority

Current `ProductionState` can establish:

```text
CurrentOpportunityCharacterId == C
```

This answers **who**, not **why**.

### Historical authority

Patch 0013 can establish that deterministic opportunity authority selected C in an effective opportunity transition.

The canonical `E0OpportunityTransition` carries minimal causal/routing identity, including:

- parent StateHash;
- result StateHash;
- strategy contract;
- selected Character ID.

But the canonical event deliberately does not duplicate the full `DirectorOpportunityInput`, Proposal, Trace, rule, diagnostics, Context prose, Candidate prose/control, Take payload, or full OpportunityHistory.

The live `E0OpportunityTransitionResult` does return `DirectorEvaluation` for E0 diagnostics/provenance, but that returned diagnostic/evaluation object is not itself separately effective authority, and durable persistence/full session reconstruction of such rationale remains outside the current promoted scope.

### Sufficiency judgment

**HISTORICAL ROUTE REQUIRED; SUFFICIENCY CONDITIONAL**

The current Stage answer may safely establish:

```text
C currently has the opportunity.
```

A creator-facing causal explanation requires a deliberate historical route and an exact authoritative source sufficient for the requested rationale.

If an exact retained/reconstructed source transition and authoritative Director evaluation/trace are legitimately available and semantically sufficient, the historical route may answer within those limits.

If only the canonical opportunity event is available, it proves that C was selected but does not automatically justify a natural-language causal rationale such as:

```text
C was selected because they are leading the discussion.
```

If the required rationale cannot be established from authoritative historical material, the correct outcome remains bounded insufficiency.

### Result

**PASS — WITH CONDITIONAL HISTORICAL SUFFICIENCY**

This is the most important matrix finding:

> **Historical existence of a transition is not equivalent to availability of every creator-facing explanation for that transition.**

---

## 7. Cross-case findings

### 7.1 Source lane and question semantics must match

The same entity can participate in multiple distinct questions:

```text
Who has Current Opportunity?
-> routing authority

What current fictional condition is available to B?
-> Character-bounded Access/Context authority

What did B observe?
-> permitted Observation authority

What did C just say?
-> authorized recent Performance authority

Why was C selected?
-> historical/causal rationale authority
```

A Character anchor does not authorize one generic `everything about C` context source.

### 7.2 Negative/insufficient answers must be semantically exact

AAS must distinguish:

```text
not available in current authority
```

from:

```text
did not happen
```

and:

```text
not permitted to this perspective
```

from:

```text
does not exist
```

These differences are part of trust, not implementation trivia.

### 7.3 Authority must support connective language

A direct fact can be fully supported while a `because` explanation remains unsupported.

Therefore answer composition needs proposition-level source discipline, not just a bag of individually true facts.

### 7.4 Bounded insufficiency is product behavior

Two of five controlled cases intentionally terminate in bounded insufficiency under current Patch 0014 authority.

This is not a missing-copy defect.

It is correct behavior until later application authority explicitly supplies the missing Observation/recent Performance semantics.

### 7.5 Historical routing needs its own availability signal

Case AAS-V1.5 exposes three distinct states:

```text
current fact is answerable
historical explanation route exists and is sufficient
historical explanation is unavailable/insufficient
```

The user experience must not collapse the last two into a generic `Why?` affordance that promises an explanation the authority cannot actually provide.

---

## 8. AAS-V1 formal verdict

> **PASS — SOURCE-SUFFICIENCY MODEL VALIDATED ACROSS CURRENT, CHARACTER-BOUNDED, HISTORICAL-ROUTE, AND INSUFFICIENT CASES.**

The matrix supports the AAS-01 laws without requiring new app authority.

Promote as durable design law:

> **Answer availability is claim-specific: Kymaean must distinguish what is true now, what is available to this perspective, what requires historical authority, and what current authority cannot support.**

Also promote:

> **An unavailable answer must describe the authority limitation without falsely negating the fiction.**

No visual surface is selected.

---

## 9. Recursive audit

Audit order:

`Director approval -> AAS-01 law -> current website/app heads -> Patch 0013 routing authority -> Patch 0014 Access/Context authority -> exact question semantics -> source lane -> freshness -> disclosure -> proposition support -> observation boundary -> recent Performance boundary -> causal connective authority -> insufficiency semantics -> Watch/opportunity invariants -> accessibility -> ARM64 quiescence -> surface/scope`

Material corrections during matrix construction:

1. made AAS-V1.2 explicitly conditional on a real question-relevant permitted `SceneState`/`Pressure` source instead of inventing a meeting fact;
2. phrased Observation failure as `not established by current bounded context`, not `did not happen`;
3. phrased recent-dialogue failure as `not available in current bounded context`, not `C said nothing`;
4. separated `C currently has opportunity` from both the deterministic selection event and any fictional reason for relevance;
5. treated Patch 0013 `DirectorEvaluation` as diagnostic/provenance returned by the transition result, not as canonical event payload or independently effective authority;
6. made historical causal sufficiency conditional on exact retained/reconstructed authoritative material rather than assuming every `Why?` is answerable;
7. preserved creator-operational routing truth != Character knowledge;
8. preserved Current Opportunity != obligation;
9. added the requirement that a history affordance must not promise an explanation unless an authoritative route is actually available.

After each material correction, the audit restarted from Director approval and exact current app authority.

Final full pass:

> **PASS — no remaining unsupported-fact assumption, visual-inference leak, stale-state splice, disclosure bypass, causal-connective overreach, false-negative fiction claim, recent-Performance assumption, opportunity/obligation conflation, or worthwhile correction within AAS-V1 scope.**

---

## 10. Next unresolved design question

AAS-V1 has validated source sufficiency. It has also exposed the next user-facing trust problem:

> **How should Kymaean communicate the difference between `answerable now`, `requires an authoritative historical route`, and `not currently supportable` without exposing engineering internals, implying uncertainty where there is none, or promising a `Why?` route that cannot produce an answer?**

Proposed next non-render artifact:

`ARS-01 — Answer Route & Sufficiency Signaling`

ARS-01 should define semantic signaling/wording/affordance rules first. It should not select final visual styling or implement an answer engine.

No ARS proposal or render is authorized by this result until Director approval.
