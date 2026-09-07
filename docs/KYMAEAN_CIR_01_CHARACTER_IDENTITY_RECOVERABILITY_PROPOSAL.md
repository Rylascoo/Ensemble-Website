<!-- D-R1-STATUS: HISTORICAL EVIDENCE -->

# KYMAEAN CIR-01 — CHARACTER IDENTITY RECOVERABILITY PROPOSAL

Status: DIRECTOR PROPOSAL FOR REVIEW / NON-RENDER IDENTITY-RECOVERABILITY CONTRACT / NO FINAL CHARACTER MEDIUM OR LABELING SYSTEM SELECTED

Date: 2026-09-04

Phase: Kymaean App + Website Design Synthesis — after SPR-R1 closed-Stage reduction pass

## 0. Purpose

SPR-R1B demonstrated that the default live Stage can remove the duplicate permanent Character portrait roster while preserving human primacy, Production/Scene continuity, Character-bounded Perspective, Watch posture, and Current Opportunity.

That reduction exposes a narrower unresolved design obligation:

> **How can every Character remain durably, accessibly and contextually identifiable when the living Stage no longer relies on a duplicate permanent roster?**

CIR-01 defines the minimum identity-recoverability contract.

It does not select:

- photorealism, illustration, 3D, silhouettes, or a final Character medium;
- permanent nameplates;
- a portrait roster;
- hover-only labels;
- creator-uploaded images;
- AI-generated identity assets;
- a final Character creation workflow;
- exact WinUI controls;
- a final accessible-control topology;
- a final Stage composition.

Authority basis:

- `CURRENT_STATE.md`;
- `docs/KYMAEAN_CHARACTER_REPRESENTATION_REQUIREMENTS_PROPOSAL_01.md`;
- `docs/KYMAEAN_CRV_01_CHARACTER_REPRESENTATION_VIABILITY_RESULT.md`;
- `docs/KYMAEAN_SPR_01_STAGE_PRESENCE_REDUCTION_PROPOSAL.md`;
- `docs/KYMAEAN_SPR_R1_STAGE_PRESENCE_REDUCTION_RESULT.md`;
- `docs/KYMAEAN_CHARACTER_BOUNDED_WATCH_PERFORM_CONTRACT_01.md`;
- current application authority at `Rylascoo/Ensemble-Project` main `7475a9397cff9063673908c666a729f0f3cd4525`, H1 Patch 0014.

Upstream laws:

> **Character != Performer.**

> **Character != Portrait.**

> **Identity is a redundant invariant bundle, not a single image.**

> **State decorates or contextualizes identity; state does not rewrite identity.**

> **Semantic persistence does not require visual duplication.**

> **Reduction is not loss when the living Production already carries the meaning.**

---

## 1. Core identity model

CIR separates six concepts that must not collapse into one another:

```text
Character entity identity
!=
creator-facing Character name
!=
visual representation / portrait
!=
current selection or focus
!=
Presentation Perspective
!=
Current Opportunity
```

A Character may be named Wren, currently be the active Presentation Perspective, and not hold Current Opportunity.

Another Character may hold Current Opportunity without becoming the perspective Character, creator-controlled Character, selected Character, or visually dominant identity.

Required law:

> **State may reference a Character; state does not define who that Character is.**

---

## 2. Recoverability requirement

A Character is **recoverable** when the creator can determine which enduring Character a present representation refers to without relying on one fragile channel.

CIR requires identity recoverability across:

- first encounter with the current Stage;
- repeated Scenes;
- changed pose, crop, scale, or viewpoint;
- reduced representation depth;
- narrow/adaptive layouts;
- focus and selection changes;
- Character-bounded Perspective changes;
- Current Opportunity changes;
- monochrome/high-contrast states;
- image-limited or image-unavailable states;
- screen-reader/assistive-technology traversal;
- static/quiescent representation.

Required law:

> **A Character must remain identifiable when any one non-essential visual cue disappears.**

---

## 3. Redundant identity bundle

CRV-01 already demonstrated that identity can survive reduced depiction depth when coherent invariants remain.

CIR therefore requires a redundant bundle rather than a permanent roster.

### 3.1 Programmatic / textual identity channel — REQUIRED

Every active Character representation must have a deterministic creator-facing textual/programmatic identity equivalent.

At minimum this means the system can expose the Character's current creator-facing name or equivalent human-readable identity label to:

- keyboard focus;
- touch/selection interaction;
- screen readers;
- reduced-detail/image-unavailable fallback;
- contextual references such as Perspective or Opportunity.

This requirement does **not** mean every Character name must be continuously printed beside every person.

It means visual minimalism may never make the identity inaccessible.

### 3.2 Visual identity channel — REQUIRED WHEN IMAGERY EXISTS

When a Character has a visual representation, it should preserve more than one coherent identity cue where the medium allows.

Possible invariant families remain open, including:

- silhouette / body proportion;
- facial structure;
- hair geometry;
- garment construction;
- creator-authored shape/motif;
- recurring non-state color accent;
- movement/gesture grammar that does not assert psychology;
- other authored identity cues.

Color alone is never sufficient.

A face alone is not sufficient for accessibility.

### 3.3 Engineering identity — NOT CREATOR-FACING PROVENANCE

The application may internally possess stable Character identity keys, but CIR does not authorize displaying engineering IDs, hashes, ContextPacket IDs, source hashes, or storage identifiers as ordinary identity UI.

Required law:

> **Creator-facing identity should remain human-readable without exposing engineering provenance.**

---

## 4. Continuous visibility versus recoverability

CIR distinguishes:

```text
identity must always be recoverable
!=
identity label must always be visibly printed
```

A full-time visible label is justified only when removing it would create material ambiguity in the current representation.

Possible valid identity-recovery behaviors may include, depending on future surface design:

- direct integrated name treatment near a Character;
- name shown on focus/selection;
- name shown when representation depth becomes too reduced for reliable visual distinction;
- semantic association between an accessible Character object and its living representation;
- a narrow-layout identity treatment that becomes more explicit as imagery compresses;
- a deliberate people/Character inspection route at application/task level when needed.

Rejected default:

- restoring a permanent duplicate portrait roster solely to solve identity recoverability.

---

## 5. Hover / pointer boundary

Hover may supplement identity disclosure but cannot be the only path.

Required law:

> **Any identity information available on hover must have an equivalent touch, keyboard and assistive-technology path.**

Do not make a Character's name or identity available only through:

- mouse hover;
- subtle visual tooltip with no focus equivalent;
- facial recognition;
- spatial memory;
- color.

---

## 6. Perspective identity

SPR-R1B strongly supported the separation:

```text
Perspective: Wren
Watch
```

CIR now makes the identity requirement explicit.

`Perspective: Wren` is a reference to the enduring Character Wren under the active disclosure state.

It must not imply:

- creator embodiment;
- Perform posture;
- account/profile ownership;
- Current Opportunity;
- Character knowledge beyond the actual Access/Context boundary.

Required law:

> **Perspective identifies whose disclosure boundary is active; it does not replace the Character's identity representation or convert the creator into that Character.**

A perspective reference must resolve to the same Character identity used elsewhere in the Stage.

---

## 7. Current Opportunity identity

Current Opportunity similarly references a Character without defining identity.

The UI must not require a single-letter token such as `C` to be the only way the creator knows who holds Opportunity.

`A / B / C` remain research aliases, not selected product-facing identity grammar.

Future Opportunity presentation must be able to resolve to a human-readable Character identity, directly or through an accessible associated representation.

Required law:

> **Opportunity may point to a Character; it must not reduce the Character to a turn token.**

---

## 8. Selection / focus boundary

Selected/focused Character and Character identity are separate.

Selection may make identity information more explicit, but identity must remain stable before, during, and after selection.

Do not encode selection by mutating the Character's core identity appearance into a different person/mode.

Selection/focus treatment must:

- have a defined semantic meaning;
- be keyboard/touch accessible;
- survive high contrast;
- not be mistaken for Current Opportunity, Perspective, emotion, or social dominance.

---

## 9. Rename / creator-authored identity changes

Creator-facing names may be editable under future product semantics.

CIR therefore does not define identity as name-only.

If a Character's creator-facing name changes legitimately:

- the underlying Character continuity remains the same Character;
- visual/contextual references should update coherently;
- history/current references should remain attributable to the same Character;
- the system should not require exposing internal IDs to explain continuity.

Exact rename/history UX is outside CIR scope.

Required law:

> **A name may identify a Character to the creator without being the entire identity model.**

---

## 10. Narrow / reduced-detail behavior

As the Stage loses physical space or visual detail, identity must become **more explicit semantically**, not less recoverable.

For example, a future narrow layout may choose one or more of:

- stronger textual naming;
- sequential Character focus;
- simplified but distinct visual invariants;
- accessible identity summaries;
- contextual naming at the current anchor.

CIR does not require simultaneous portrait/name display for all Characters.

It requires that reduction never force the creator to guess who a person is.

---

## 11. Image-unavailable / image-disabled fallback

The product model must survive without Character imagery.

When imagery is unavailable, the Stage may become less visually rich but must preserve:

- human-readable Character identity;
- Scene participation;
- Perspective reference;
- Opportunity reference;
- task/action attribution;
- accessibility traversal.

A fallback glyph/shape/avatar may supplement textual identity, but must not become the sole definition of the Character.

This extends CRV's result:

> **Rich depiction improves immediacy but is not required for persistent identity, relational presence, bounded perspective, or independent salience.**

---

## 12. Epistemic restraint

Identity cues cannot silently become psychological state.

Do not encode stable identity through cues that imply mutable private state such as:

- permanent 'anxious' expression;
- hostility/friendliness meter styling;
- inferred trust colors;
- emotion-specific portrait variants used as identity anchors;
- gaze-based attention certainty;
- body-language-based knowledge/intent status.

A Character representation may portray performance, but the identity system must not turn that portrayal into authoritative psychology.

Patch 0014 remains binding:

> **Visible portrayal != Observation / Knowledge / Belief / Intent authority.**

---

## 13. Accessibility contract

CIR requires that active Character identity be programmatically exposed wherever the Character is an interactive or meaningful Stage entity.

Exact control roles remain implementation-specific and unselected, but future WinUI translation must preserve:

- accessible Character name;
- predictable focus order;
- stable association between the visual representation and its accessible identity;
- explicit perspective identity when materially different;
- explicit Opportunity holder identity when active;
- no dependence on color, portrait recognition, animation, or position alone;
- equivalent identity access for pointer, touch, keyboard, and screen-reader use.

If a visual representation is decorative and a separate semantic element carries the identity, the relationship must remain clear and non-duplicative to assistive technology.

---

## 14. ARM64 / privacy / quiescence

Identity recoverability should be driven by deterministic local Character state and authored representation metadata.

CIR requires no:

- facial recognition;
- continuous identity inference;
- embedding comparison;
- gaze tracking;
- emotion analysis;
- camera access;
- background AI generation;
- continuous image regeneration;
- provider polling;
- persistent GPU/NPU work.

At rest, identity mapping should be quiescent.

If future creator-authored/generated imagery is added, privacy/consent/storage/model-processing rules require separate approval.

No Windows AI Foundry or NPU behavior is claimed by CIR-01.

---

## 15. Surface quarantine

CIR selects no final identity surface.

No inheritance rights for:

- the SPR photoreal cast;
- names Riven/Wren/Vale as defaults;
- A/B/C labels as product identity tokens;
- permanent nameplates;
- portrait chips;
- silhouette systems;
- any specific color association;
- exact focus ring;
- hover tooltip;
- avatar/glyph fallback;
- exact Perspective treatment;
- exact Opportunity treatment;
- any final Character medium.

> **Surface != law.**

---

## 16. CIR falsification criteria

A future identity system fails CIR if any of the following is true:

1. a Character becomes unidentifiable when their permanent roster portrait is removed;
2. identity depends on recognizing a face;
3. identity depends on color alone;
4. identity is available only on hover;
5. Perspective becomes a substitute for identity or implies embodiment;
6. Opportunity reduces the Character to a letter/turn token;
7. selection/focus visually rewrites Character identity;
8. narrow layout makes Characters ambiguous;
9. image-unavailable mode destroys Character attribution;
10. screen readers cannot recover the same Character identity referenced by visual state;
11. identity presentation leaks engineering IDs/provenance;
12. identity cues imply private psychology as authoritative state;
13. maintaining identity requires continuous AI/inference/rendering work.

---

## 17. Proposed first validation — CIR-V1

If the Director approves CIR-01, the smallest justified next action is **non-render**:

`CIR-V1 — Character Identity Recoverability Matrix`

It should exercise one Character set across at least these conceptual conditions:

1. full living Stage with no permanent roster;
2. reduced-detail representation;
3. narrow/sequential layout;
4. image-unavailable/textual fallback;
5. keyboard/screen-reader semantic traversal;
6. active Perspective referencing one Character while Opportunity references another;
7. focus/selection on a third Character.

For each condition, validate:

- who each Character is;
- how identity is recovered;
- whether identity survives removal of one cue;
- whether Perspective/Posture/Opportunity remain orthogonal;
- whether accessibility receives the same identity truth;
- whether any duplicate UI becomes necessary;
- whether any hidden state is inferred;
- whether the result remains deterministic and quiescent.

No render is authorized by CIR-01 itself.

---

## 18. Recursive audit order

`Director authorization -> SPR-R1B result -> Character Representation Requirements -> CRV-01 -> identity/entity distinction -> textual/programmatic recoverability -> visual invariants -> roster-removal law -> Perspective reference -> Opportunity reference -> selection/focus -> rename continuity -> narrow/reduced-detail -> image-unavailable fallback -> epistemic restraint -> accessibility -> ARM64/privacy/quiescence -> surface quarantine -> falsification criteria -> scope -> anti-churn`

Proposal audit corrections already incorporated:

1. did not restore a permanent roster;
2. did not require permanent visible labels;
3. made programmatic/textual identity recoverability mandatory;
4. separated identity from name-only dependence;
5. separated identity from Perspective, Opportunity, focus and creator agency;
6. rejected A/B/C research aliases as final identity grammar;
7. rejected hover-only identity access;
8. preserved image-unavailable operation;
9. preserved no-face-recognition/no-continuous-inference privacy direction;
10. kept engineering identity/provenance out of ordinary creator-facing UI;
11. preserved Patch 0014 epistemic restraint;
12. kept final Character medium and WinUI control topology open.

Final complete pass:

> **PASS — no remaining material identity/agency conflation, accessibility gap, roster-restoration drift, epistemic leak, quiescence concern, surface-selection leak, or worthwhile correction inside CIR-01 proposal scope.**

---

## 19. Director gate

Director decision requested:

> **Adopt CIR-01: every Character remains durably identifiable through a redundant identity bundle with a mandatory human-readable/programmatic identity channel and medium-appropriate visual invariants; identity remains distinct from name-only dependence, portrait, selection, Perspective, Posture and Current Opportunity; roster duplication is not required; hover/face/color/position cannot be sole identity channels; image-limited and assistive-technology states preserve the same Character truth; and identity recoverability requires no continuous AI or biometric inference.**

If approved, run exactly one non-render `CIR-V1 — Character Identity Recoverability Matrix`, recursively audit it, and stop.
