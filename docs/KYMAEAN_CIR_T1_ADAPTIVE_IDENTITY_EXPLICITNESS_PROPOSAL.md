# KYMAEAN CIR-T1 — ADAPTIVE IDENTITY EXPLICITNESS PROPOSAL

Status: DIRECTOR PROPOSAL FOR REVIEW / NON-RENDER TEMPORAL IDENTITY-DISCLOSURE CONTRACT / NO FINAL LABELING, MOTION, OR CHARACTER SURFACE SELECTED

Date: 2026-09-04

Phase: Kymaean App + Website Design Synthesis — after CIR-R1 first-use identity discoverability

## 0. Purpose

CIR-V1 established that Character identity remains recoverable without a permanent roster and that semantic explicitness should increase as visual certainty decreases.

CIR-R1 then proved that direct names can make a no-roster Stage understandable on first use, but it also exposed two risks:

1. first-use labels can accidentally become permanent Stage clutter;
2. identity recovery can drift into invented personality/professional summaries rather than simply identifying the Character.

CIR-T1 defines when identity should become more explicit, when it may recede, and what must remain recoverable throughout.

CIR-T1 does not select:

- permanent nameplates;
- floating label geometry;
- hover behavior;
- animation/fade timing;
- exact focus treatment;
- final Character medium;
- final Opportunity treatment;
- final Perspective treatment;
- final WinUI control topology;
- onboarding implementation;
- a render.

## 1. Governing synthesis

> **Identity explicitness should adapt to ambiguity; Character identity itself must remain stable.**

And:

> **Identity recovery should reveal who the person is, not summarize what kind of person the system thinks they are.**

Therefore identity presentation is allowed to change in visibility or textual explicitness as context changes, but the Character entity, name association, programmatic identity and stable authored visual invariants do not mutate merely because the UI becomes more or less explicit.

## 2. Explicitness states

CIR-T1 defines conceptual states, not implementation enums.

### E0 — ESTABLISHED / LOW AMBIGUITY

Use when the Character set is already reliably distinguishable in the current Stage and no state/task has made identity ambiguous.

Requirements:

- living Character representations remain primary;
- human-readable/programmatic identity remains available;
- continuously printed names are not required if removal creates no material ambiguity;
- no permanent roster is restored merely for reassurance.

### E1 — FIRST ENCOUNTER / IDENTITY INTRODUCTION

Use when a Character is newly encountered in the current Production/Scene context or the creator does not yet have a reliable visual association.

Requirements:

- make the Character's human-readable identity directly discoverable;
- association between name and living representation must be unambiguous;
- do not add personality, profession, psychology, intent, knowledge or other invented descriptor material merely to make the name memorable;
- Perspective/Opportunity/focus may be present but remain separate references.

### E2 — RE-IDENTIFICATION / AMBIGUITY INCREASE

Use when ambiguity rises because of changed pose, crop, viewpoint, representation depth, layout, visual similarity, occlusion, Scene transition or another legitimate presentation change.

Requirements:

- increase textual/programmatic identity explicitness only as much as needed;
- identity recovery must not depend on remembering prior spatial position;
- avoid biometric/inference mechanisms;
- do not treat re-identification as a new Character or reset of continuity.

### E3 — FOCUS / CURRENT ANCHOR

Use when the creator deliberately focuses, selects, inspects or invokes context from one Character.

Requirements:

- focused Character identity may become more explicit;
- focus state must remain distinct from identity itself;
- focus styling must not imply Opportunity, Perspective, Observation, emotion or social dominance;
- when focus leaves, identity can return to E0 if ambiguity is low.

### E4 — STATE REFERENCE REQUIRES IDENTITY

Use when Perspective, Current Opportunity, task attribution, dialogue attribution or another authoritative state references a Character.

Requirements:

- the state reference resolves to a human-readable Character identity;
- `Perspective: Wren` must not become `(You)`;
- Opportunity must not reduce Vale to `C` or another token;
- state references must not substitute for the Character's own identity channel.

### E5 — REDUCED / NARROW / IMAGE-LIMITED / ASSISTIVE

Use when visual identity confidence decreases substantially or imagery is unavailable.

Requirements:

- semantic identity becomes more explicit rather than less;
- textual/programmatic identity may become primary;
- no dependence on face recognition, color, motion, exact position or simultaneous wide geometry;
- accessibility receives the same stable Character truth as visual interaction.

## 3. Recession law

Identity explicitness may recede only when all of the following remain true:

1. the creator can still recover who the Character is without guessing;
2. programmatic/human-readable identity remains available;
3. no current Perspective/Opportunity/focus/task reference becomes ambiguous;
4. narrow/image-limited/accessibility paths remain intact;
5. recession does not depend on a timer alone if ambiguity remains materially high.

Required law:

> **Labels may recede; recoverability may not.**

The contract therefore rejects arbitrary 'show once, then disappear forever' behavior.

## 4. Explicitness trigger law

More visible identity is justified by ambiguity or task need, not by generic interface decoration.

Valid trigger families include:

- first encounter;
- representation-depth reduction;
- changed crop/viewpoint;
- narrow layout;
- image unavailable;
- deliberate focus/selection;
- state reference whose target would otherwise be unclear;
- accessibility traversal;
- two or more Characters becoming visually confusable.

Invalid trigger families include:

- model confidence score;
- inferred user confusion from camera/eye tracking;
- facial-recognition uncertainty;
- emotion inference;
- background AI deciding a person is 'important';
- Opportunity alone causing the Character to receive personality emphasis or cinematic dominance.

## 5. Identity-content budget

Default creator-facing identity content is the minimum authoritative material needed to answer:

> **Who is this Character?**

Usually that means the current creator-facing Character name or equivalent human-readable identity.

CIR-T1 does not authorize the renderer/UI to append:

- personality labels;
- profession/archetype summaries;
- psychological adjectives;
- intent or motivation;
- knowledge/Observation claims;
- relationship judgments;
- trust/affinity scores;
- generated biography fragments.

If future product semantics deliberately expose any such information, it belongs to a separate bounded task/context contract and must use actual authority.

Required law:

> **Identity disclosure is not Character summarization.**

## 6. Perspective / Opportunity / focus orthogonality

The following state remains valid simultaneously:

```text
Riven = focused
Wren = active Presentation Perspective
Vale = Current Opportunity
Watch = Creator Posture
```

CIR-T1 requires that identity explicitness for any one Character may increase due to current need without transferring or conflating those states.

Examples:

- focusing Riven may reveal `Riven`; it does not make Riven the Perspective Character;
- `Perspective: Wren` may remain explicit even if Wren's local name label has receded;
- `Current Opportunity: Vale` may identify Vale directly even if Vale is not selected;
- Watch remains creator posture and does not attach ownership to Wren.

## 7. Opportunity identity correction

CIR-R1 showed the failure of retaining `C` as the visible Opportunity identity while also naming the Character Vale.

Required correction:

> **Product-facing state references should resolve to human-readable Character identity, not require research-alias translation.**

`A/B/C` may remain internal research notation in documents/tests but gain no product-facing inheritance rights.

## 8. Marketing / onboarding boundary

CIR-R1 also reintroduced product-thesis copy into the active Stage.

CIR-T1 freezes:

> **Active Stage identity support does not require product-thesis or marketing narration.**

If first-use onboarding/help is needed, it must be a deliberately invoked or clearly bounded application-level experience rather than permanent Stage copy pretending to be current Production information.

## 9. Interaction and motion boundary

CIR-T1 does not require animation.

A future implementation may use static, focus-triggered, or brief transition behavior, but:

- identity truth must remain available without motion;
- reduced-motion users receive equivalent discoverability;
- name visibility cannot rely on fleeting animation;
- motion may not imply emotion, speaking status or Opportunity;
- no idle pulsing/glowing is justified.

## 10. Accessibility contract

A future implementation must preserve:

- stable accessible Character name/equivalent;
- deterministic association between visible Character and accessible identity;
- explicit state-reference target when Perspective/Opportunity/focus differs;
- predictable focus order;
- pointer/touch/keyboard/assistive equivalence;
- no hover-only identity;
- no dependence on color/portrait/position/motion;
- no accidental duplicate announcements caused by redundant visual + semantic identity elements.

Actual WinUI roles, AutomationProperties and narrator/screen-reader behavior remain implementation-stage work and are not validated by this proposal.

## 11. ARM64 / privacy / quiescence

Adaptive explicitness should be deterministic UI behavior derived from already-authoritative local state and presentation conditions.

It requires no:

- facial recognition;
- gaze tracking;
- confusion detection;
- biometric matching;
- image embeddings;
- emotion analysis;
- camera access;
- continuous AI inference;
- background generation;
- persistent GPU/NPU activity.

At rest, no additional compute is needed merely to decide whether a name should remain visible.

## 12. Surface quarantine

No inheritance rights for:

- CIR-R1 photoreal cast or office;
- Riven/Wren/Vale defaults;
- floating dark name cards;
- connector dots/leader lines;
- personality descriptor copy;
- `C` Opportunity token;
- eye icon for Watch;
- marketing phrase;
- fade animation;
- hover tooltip;
- exact timing rules;
- exact typography/palette;
- any final Character medium.

> **Surface != law.**

## 13. CIR-T1 falsification criteria

A future adaptive identity system fails if:

1. labels recede while identity becomes materially ambiguous;
2. first-use discoverability requires a permanent roster;
3. labels become personality/profession summaries;
4. re-identification requires facial recognition or biometric inference;
5. Opportunity uses only a token like `C` when a human-readable identity exists;
6. Perspective becomes creator embodiment;
7. focus changes who the Character appears to be;
8. narrow/image-limited modes become less explicit rather than more;
9. accessibility receives weaker identity truth than sighted pointer use;
10. motion is required to understand identity;
11. Stage marketing is used as identity scaffolding;
12. adaptive behavior requires continuous AI/GPU/NPU work;
13. surface choices are promoted as product law from this proposal.

## 14. Proposed first validation — CIR-T1V1

If approved, the smallest justified next action is **non-render**:

`CIR-T1V1 — Adaptive Identity Explicitness State Matrix`

Validate at least:

1. first encounter -> explicit naming;
2. established low-ambiguity Stage -> names may recede;
3. deliberate focus on one Character -> local re-explicitness;
4. Perspective on another Character -> separate explicit state reference;
5. Current Opportunity on a third Character -> human-readable state reference;
6. narrow/reduced-detail layout -> broader re-explicitness;
7. image-unavailable / assistive state -> textual/programmatic identity primary;
8. return to full low-ambiguity Stage -> reversible recession without identity loss.

For each case audit:

- who is identifiable;
- why explicitness is increased/reduced;
- what single cue may disappear safely;
- whether state references remain orthogonal;
- whether any psychology/marketing/provenance leaks in;
- accessibility equivalence;
- deterministic quiescence.

No render is authorized by CIR-T1 itself.

## 15. Recursive audit

Audit order:

`Director authorization -> CIR-R1 result -> CIR-V1 -> first-use explicitness -> recession law -> ambiguity triggers -> identity-content budget -> Perspective/Posture -> Opportunity correction -> focus -> narrow/image-limited -> accessibility -> marketing boundary -> motion/reduced-motion -> Patch 0014 epistemic restraint -> ARM64/privacy/quiescence -> surface quarantine -> falsification -> anti-churn`

Corrections already incorporated:

1. did not promote permanent visible nameplates;
2. did not restore a roster;
3. separated name discovery from Character summarization;
4. corrected visible Opportunity identity away from research-token dependence;
5. kept Perspective/Posture/focus/Opportunity orthogonal;
6. did not make elapsed time alone sufficient to hide identity;
7. did not require animation or hover;
8. kept marketing/onboarding outside active Stage truth;
9. preserved image-unavailable and assistive behavior;
10. required no biometric/continuous-AI inference;
11. kept final WinUI and Character surface open.

Final complete pass:

> **PASS — no remaining material roster-restoration drift, permanent-nameplate assumption, identity/psychology conflation, state-reference collision, accessibility gap, timer-only recession error, marketing leak, quiescence concern, or surface-selection leak inside CIR-T1 proposal scope.**

## 16. Director gate

Director decision requested:

> **Adopt CIR-T1: identity explicitness increases when ambiguity or task need rises and may recede only while Character identity remains unambiguously and accessibly recoverable; first-use identity support reveals who the Character is without personality/professional summarization; Perspective, Opportunity, focus and Posture remain independent references; product-facing Opportunity resolves to human-readable Character identity rather than A/B/C tokens; reduced/narrow/image-unavailable/assistive states become more semantically explicit; and adaptive identity behavior requires no biometric or continuous-AI inference.**

If approved, run exactly one non-render `CIR-T1V1 — Adaptive Identity Explicitness State Matrix`, recursively audit it, and stop.
