# KYMAEAN AAS-01 — AUTHORITATIVE ANSWER SOURCING PROPOSAL

Status: DIRECTOR PROPOSAL FOR REVIEW / NON-RENDER AUTHORITY-SOURCING CONTRACT / NO ANSWER ENGINE OR NEW APP AUTHORITY SELECTED

Date: 2026-09-03

Phase: Kymaean App + Website Design Synthesis — after BCA-V1 composition validation

## 0. Purpose

Define how a Kymaean contextual question is grounded in exact current authority before any user-facing answer is composed.

AAS-01 exists because BCA-V1 validated the `one question -> one answer -> minimum basis` composition, but the renderer invented plausible answer facts from the visible meeting scene.

The design problem is now not panel layout. It is trust:

> **Which authoritative sources may support a requested answer, how is freshness/disclosure proven, and what happens when those sources are insufficient?**

AAS-01 does not add application APIs, persistence, a provenance UI, an LLM answer engine, new Character domains, new Observation semantics, recent Performance context, a new Director strategy, or causal-history implementation.

Authority basis:

- `CURRENT_STATE.md`;
- `docs/KYMAEAN_BCA_01_BOUNDED_CONTEXT_ANSWER_PROPOSAL.md`;
- `docs/KYMAEAN_BCA_V1_ONE_QUESTION_ONE_ANSWER_RESULT.md`;
- `docs/KYMAEAN_CDT_01_CONTEXT_DISCLOSURE_TRANSITION_PROPOSAL.md`;
- `docs/KYMAEAN_APP_ARCHITECTURE_TO_VISUAL_REQUIREMENTS_PATCH_0014_ADDENDUM_01.md`;
- `Rylascoo/Ensemble-Project` current `main` `7475a9397cff9063673908c666a729f0f3cd4525`;
- H1 Patch 0013 effective-opportunity authority;
- H1 Patch 0014 Production Context Continuity.

---

## 1. Core law

The authoritative answer path is:

```text
creator question
    -> identify semantic claim requested
        -> identify permitted source lane(s)
            -> prove current-state / historical association
                -> apply disclosure authority
                    -> test semantic sufficiency
                        -> sufficient?
                           yes -> compose minimum supported answer
                           no  -> state bounded insufficiency truthfully
```

Required laws:

> **Models, renderers, imagery, and plausible narrative completion are never authority sources.**

> **A true fact and another true fact do not authorize a causal `because` between them.**

> **No answer may be more specific, more certain, more causal, or more epistemically privileged than its source authority.**

---

## 2. Authority is not one undifferentiated pool

AAS distinguishes source lanes by semantic job. These are design responsibilities, not new storage enums.

### Lane A — Current Production / routing authority

Examples of current operational authority include, where present in current `ProductionState`:

- Production/Scene identity;
- roster/Character identity;
- `CurrentOpportunityCharacterId`;
- current Production records and their lifecycle/protection/domain state;
- current StateHash identity.

This lane may support creator-operational statements such as:

- `C currently holds Current Opportunity.`

It does **not** automatically mean the Character represented by the active Presentation Perspective knows that fact.

Required distinction:

```text
creator-visible system/routing truth
!=
Character knowledge
```

If an answer is explicitly framed as `information available to B`, raw Production material must not bypass Character-bounded Access.

### Lane B — Character-bounded current fictional authority

For a Character-bounded answer, the preferred current fictional source is the same Access-before-Context pipeline already implemented by Patch 0014:

```text
current ProductionState
-> CharacterBoundedAccessControl.Evaluate(...)
-> CharacterAccessEvaluation / CharacterAccessProjection
-> Production-bound DeterministicContextComposer
-> ContextPacket v2
```

Current Patch 0014 permits:

- active `SceneState` as shared Scene state;
- active `Pressure` as public Pressure;
- Constitution, Disposition, Circumstance, Observation, Knowledge, Belief, Suspicion, Memory, Goal, and Relationship only when owned by the active subject;

and denies:

- active `HistoricalTruth`;
- active `UnresolvedProposition`;
- active `WorldState`;
- other-owned Character material;
- active `CharacterClaim` for every Character while disclosure remains deferred;
- inactive records according to lifecycle precedence.

Lane B is the authority for statements of the form:

> `This is available to B now.`

It must not be replaced by visual interpretation of the Stage.

### Lane C — Historical / causal authority

Historical explanation is a separate route.

Potential authoritative historical sources already exist in the deterministic spine, including where retained and applicable:

- `E0CausalCommit`;
- `E0OpportunityTransition`;
- `E0OpportunityHistory`;
- causal StateHash parent/result association;
- accepted Take/Performance/consequence authority already owned by earlier patches.

However, existence of a historical event does not mean every natural-language rationale is stored.

Patch 0013's canonical `E0OpportunityTransition` records only:

- contract version;
- parent StateHash;
- result StateHash;
- strategy contract;
- selected Character ID.

It intentionally does **not** embed the full Director trace, Context prose, Candidate prose/control, or diagnostics.

Therefore:

```text
event proves that C was selected
!=
event necessarily proves a creator-facing semantic reason for why C was selected
```

A causal `Why?` answer may require an explicitly retained/reconstructed authoritative source chain and, where the requested rationale is not actually represented by that authority, may still be insufficient.

### Lane D — Technical capability / product-operation authority

Technical questions such as why a feature/action is unavailable must be sourced from actual capability/product state, not fictional context.

Examples may later include:

- feature readiness;
- hardware compatibility;
- model/capability availability;
- creator posture/action eligibility.

This lane is operational and must not be fictionalized as Character behavior or dramatic state.

### Non-source — visual/model inference

The following may influence presentation but never establish answer truth:

- generated Character appearance;
- gaze;
- facial expression;
- pose;
- apparent speaking/listening;
- environmental text invented by a renderer;
- visual salience;
- an LLM's plausible narrative completion;
- a renderer's own explanatory copy.

Required law:

> **Representation can depict; authority must establish.**

---

## 3. Same-state freshness law

Current answers must not splice facts from different Production states.

Patch 0014 already provides exact current source association:

- `CharacterAccessProjection.SourceStateHash` associates a Production-backed projection with the exact source Production state;
- Context v2 carries the same `SourceStateHash` in canonical structured bytes and Context/trace metadata;
- `SourceStateHash` is engineering association metadata, not fictional knowledge and not Character-facing rendered prose.

For a CURRENT answer that combines Lane A and Lane B information, AAS requires conceptually:

```text
current ProductionState.StateHash
== CharacterAccessProjection.SourceStateHash
== ContextPacket.SourceStateHash
```

where those artifacts are used.

If association is stale, missing where required, or foreign:

> **do not compose the answer from that material.**

Do not silently mix:

- an old ContextPacket;
- a new Current Opportunity;
- a previous Scene;
- a new Production record set.

This is answer-level continuation of Patch 0014's source-proof boundary.

---

## 4. Disclosure precedes relevance

AAS does not search all known Production data and then redact afterward.

For Character-bounded fictional content:

```text
source authority
-> Access decision/projection
-> question relevance
-> answer
```

not:

```text
all Production knowledge
-> answer draft
-> redact private material afterward
```

Required law:

> **Access constrains the candidate source set before answer composition.**

This prevents a model from indirectly leaking denied facts through summaries, causal connective language, omissions, or `unknown` category names.

---

## 5. Statement-level support law

Every material proposition in a bounded answer must be attributable internally to sufficient authority.

This does not require showing engineering provenance IDs to the user.

The answer composer must not introduce unsupported semantic operations between individually supported facts.

### 5.1 Causal claims

Words such as:

- because;
- therefore;
- led to;
- resulted in;
- caused;
- as a consequence;

require actual causal authority.

Two co-current facts are not enough.

Example:

```text
SUPPORTED:
C currently holds Current Opportunity.
A revised agreement is currently operative.

NOT AUTOMATICALLY SUPPORTED:
C holds Current Opportunity because the revised agreement is operative.
```

unless an authoritative causal source establishes that relation.

### 5.2 Epistemic claims

Words such as:

- knows;
- saw;
- heard;
- noticed;
- remembers;
- believes;
- suspects;
- understands;

require the corresponding permitted authoritative domain/state.

Appearance or co-presence is insufficient.

### 5.3 Intent / psychology claims

Words such as:

- wants;
- intends;
- trusts;
- fears;
- agrees;
- is confident;
- is skeptical;
- is ready;

require explicit authoritative subjective state that is permitted to the active perspective.

Do not derive them from expression/pose.

### 5.4 Modal / action claims

Words such as:

- can;
- cannot;
- must;
- may;
- is required to;

require actual action/capability/authority state.

Current Opportunity must never become `C must respond` unless separate authority explicitly says so.

### 5.5 Temporal claims

Words such as:

- now;
- earlier;
- still;
- no longer;
- before;
- after;

must respect the current/historical locus and actual state/event association.

---

## 6. Sufficiency outcomes

AAS recognizes four semantic outcomes. These are not implementation enums.

### Outcome 1 — Sufficient current answer

The current permitted authority directly supports the requested claim.

Example design case:

```text
Question: Who currently has the opportunity?
Source: current ProductionState.CurrentOpportunityCharacterId
Answer: C currently has the opportunity.
```

Any non-obligation language must remain separately grounded in the known opportunity semantics.

### Outcome 2 — Sufficient Character-bounded answer

The current same-state Access/Context projection contains question-relevant permitted material.

Example design case:

```text
Question: What current shared condition is available to B?
Source: same-state permitted SceneState / Pressure records
Answer: compose only from those relevant permitted records.
```

### Outcome 3 — Historical route required

The requested question asks why a current truth became true and current state alone does not contain the causal explanation.

The current answer should preserve what is known now and offer deliberate causal trace only if authoritative history is actually available.

Example:

```text
Current authority:
C currently holds Current Opportunity.

Question:
Why did C receive it?

Action:
enter causal trace if the required source chain/rationale is available.
```

Do not append speculative history to the current answer.

### Outcome 4 — Bounded insufficiency

The required claim is not established by permitted current or available historical/technical authority.

Correct response is a truthful limitation, for example in semantic form:

```text
The current authoritative context establishes that C has the opportunity,
but it does not provide an additional supported reason for that assignment here.
```

Exact wording remains open.

Required law:

> **Insufficient authority is an answer state, not an invitation to hallucinate.**

---

## 7. Current Opportunity case — authoritative correction

BCA-V1 asked:

> `Why is C currently relevant?`

The controlled render answered with invented meeting semantics.

AAS-01 narrows the authority correctly.

Current Patch 0013/0014 can support, depending on exact available state:

```text
CurrentOpportunityCharacterId == C
```

and an effective opportunity transition can prove that the deterministic opportunity authority selected C at that transition.

What current canonical Production state does **not** itself contain is a free-form semantic reason such as:

- `C is leading the discussion`;
- `C is presenting terms`;
- `C is relevant because next steps are being discussed`.

The opportunity transition event also intentionally omits the full Director Trace/diagnostic explanation.

Therefore the design must distinguish:

```text
WHO has current opportunity
from
WHY the system selected them
from
WHY they matter fictionally in the Scene
```

Those are not interchangeable questions and may require different authority lanes.

---

## 8. Observation/recent-Performance boundary

AAS inherits current Patch 0014 limits unchanged.

### Observation

No Character observation may be inferred from:

- co-presence;
- visible Candidate text;
- addressed Characters;
- nomination;
- Director selection;
- relationship;
- SceneState;
- causal adjacency;
- rendered gaze/gesture/pose.

If a permitted authoritative Observation record exists for the active subject, it may be used according to Access/Context authority.

Otherwise an observation claim is unsupported.

### Recent Performance

Canonical Context v2 currently keeps:

```text
recentPerformances = []
RecentPerformanceText = empty
```

Therefore questions such as `What did C just say?` are not answerable from current Context v2 merely because a concept render visually depicts C speaking.

Future accepted-Performance context may later extend this boundary through separate app authority.

### CharacterClaim / recall

CharacterClaim disclosure and current recall remain deferred.

Do not source `B remembers...` from the mere existence of a claim.

---

## 9. Internal proof versus user-facing presentation

AAS requires source discipline internally but does not require dumping engineering provenance into the fictional surface.

Do not render:

- raw `SourceStateHash`;
- ContextPacketId;
- record hash;
- commit hash;
- internal AccessReason;
- model/provider trace;

as Character-facing fictional prose merely to prove trustworthiness.

Creator-facing deep diagnostics/provenance may be designed later as a separate technical/specialist surface.

Required principle:

> **Provenance can govern an answer without becoming the answer.**

---

## 10. Deterministic-first answer composition

At this checkpoint, AAS favors deterministic composition from already-authoritative local state.

No generative model is required to answer when the supporting facts and bounded response can be rendered deterministically.

A future model-assisted explanation layer may be considered separately only if it preserves proposition-level authority and degrades truthfully.

A model may never be treated as the source of fictional truth merely because its prose is coherent.

No background answer generation, speculative summary cache, provider polling, or idle NPU inference is required.

---

## 11. Failure behavior

Fail closed when:

- required source state is stale/foreign;
- active perspective cannot access the needed material;
- source association cannot be proven where required;
- the requested causal relation is not represented by authority;
- a Character epistemic/subjective claim lacks permitted support;
- recent Performance is requested but unavailable under current authority;
- an expected technical capability is unavailable;
- the only support is visual/model inference.

Failure must not:

- change Production truth;
- consume Current Opportunity;
- change Watch/Perform posture;
- widen Presentation Perspective;
- invent a fallback explanation;
- convert technical inability into fictional behavior.

---

## 12. Accessibility and trust communication

Bounded sufficiency/insufficiency must be understandable without relying on:

- color;
- panel geometry;
- portrait;
- animation;
- visual salience.

A user should be able to determine semantically:

- what question was asked;
- what answer is supported;
- whether the answer is current or historical;
- whether more explanation is unavailable or requires a history route;
- how to return to the Stage.

Do not use ambiguous low-confidence language such as `probably`, `seems`, or `likely` to disguise missing authority in a deterministic bounded-context surface.

---

## 13. ARM64 / quiescence contract

AAS is intentionally compatible with the project's low-idle-cost direction.

Preferred implementation characteristics for later engineering review:

- operate from already-materialized current Production/Access/Context state where possible;
- no continuous inference;
- no proactive answer generation for every Character/anchor;
- no face/emotion analysis;
- no relationship scoring;
- no provider polling;
- no persistent GPU/NPU work;
- no speculative historical reconstruction until explicitly requested.

This proposal itself authorizes no implementation.

---

## 14. Controlled validation proposal

If AAS-01 is approved, do **not** immediately generate another UI image.

The smallest justified validation is a non-render source matrix:

`AAS-V1 — Source Sufficiency Matrix`

Use exact current app authority and test at least these controlled cases:

### Case A — direct routing fact

```text
Question: Who currently has Current Opportunity?
Expected source: current ProductionState
Expected outcome: sufficient current answer
```

### Case B — Character-bounded current fact

```text
Question: What current shared condition is available to B?
Expected source: same-state CharacterAccessProjection / Context v2 permitted SceneState or Pressure
Expected outcome: sufficient only for relevant permitted records
```

### Case C — unsupported observation

```text
Question: Did B observe C's gesture?
Expected source: permitted Observation record required
Expected outcome without such record: bounded insufficiency
```

### Case D — unavailable recent dialogue

```text
Question: What did C just say?
Expected source: recent Performance context
Current Patch 0014 outcome: bounded insufficiency because canonical recentPerformances is empty
```

### Case E — causal reason for Current Opportunity

```text
Question: Why did C receive Current Opportunity?
Current state can establish: C has Current Opportunity
Historical event can establish: deterministic opportunity authority selected C
Expected outcome: historical route required; semantic rationale is sufficient only if the required authoritative causal/Director source is actually available
```

The matrix must identify for each case:

- requested proposition;
- allowed source lane;
- freshness/state-association requirement;
- disclosure requirement;
- available authoritative evidence;
- unsupported inference temptations;
- sufficiency outcome;
- minimal truthful answer shape;
- whether a history/technical route is warranted.

Stop after the matrix and recursive audit. No render or implementation automatically follows.

---

## 15. Surface quarantine

AAS selects no visual surface.

No inheritance rights arise from BCA/CDT/SIPD's:

- photoreal office/cast;
- exact answer panel;
- white cards;
- portrait chips;
- green/orange/blue state treatments;
- generic productivity shell;
- exact labels or icons.

This is an authority-composition checkpoint, not a visual-style checkpoint.

---

## 16. Recursive audit

Audit order:

`Director authorization -> BCA-V1 result -> current app main -> Patch 0013 opportunity authority -> Patch 0014 Access/Context source proof -> source-lane separation -> same-state freshness -> Access-before-relevance -> statement-level support -> causal/epistemic/modal/temporal claim gates -> sufficiency outcomes -> observation/recent Performance/CharacterClaim boundaries -> current/history separation -> internal proof vs user-facing presentation -> deterministic-first composition -> failure behavior -> accessibility -> ARM64 quiescence -> validation sufficiency -> surface quarantine -> scope`

Material corrections made during construction:

1. separated creator-operational Production authority from Character-bounded fictional authority;
2. made Access-before-Context the source filter for B-bounded fictional claims rather than a post-answer redaction step;
3. required same-StateHash association when current Production facts and Context v2 material are combined;
4. distinguished `C has Current Opportunity` from any semantic explanation of why C has it;
5. recognized that Patch 0013's opportunity event proves selected Character/causal transition but intentionally omits full Director rationale;
6. prohibited causal connective language from being inferred merely because two current facts are both true;
7. made epistemic, psychological, modal, and temporal language require matching authority;
8. elevated bounded insufficiency into a valid answer outcome;
9. kept current answers separate from deliberate causal trace/history;
10. prohibited raw hashes/packet IDs from leaking into Character-facing prose while retaining them as internal freshness/proof constraints;
11. kept deterministic local composition as the default and generative inference non-required;
12. selected a non-render Source Sufficiency Matrix as the next validation because the unresolved question is authority, not surface.

After each material correction, audit restarted from Director authorization and current application authority.

Final complete pass:

> **PASS — no remaining material source-lane conflation, stale-state splice, Access bypass, unsupported causal connective, epistemic/private-mind inference, opportunity-reason conflation, recent-Performance assumption, CharacterClaim/recall leak, provenance-presentation leak, generative-authority assumption, accessibility defect, quiescence concern, surface-inheritance leak, or worthwhile correction inside AAS-01 proposal scope.**

---

## 17. Director gate

Director decision requested:

> **Adopt AAS-01: every contextual answer is grounded only in permitted authoritative source lanes with same-state freshness where applicable; each material proposition must be semantically supported; causal, epistemic, psychological, modal and temporal language require matching authority; and insufficient authority produces a truthful bounded-insufficiency answer rather than model/renderer completion.**

If approved, the next smallest justified action is exactly one non-render:

`AAS-V1 — Source Sufficiency Matrix`

Then audit and stop.

No answer engine, new Core API, new persistence layer, Observation system, recent-Performance context, Director strategy change, causal-history implementation, WinUI implementation, AI inference pipeline, or website implementation is authorized by this proposal.
