# KYMAEAN — HERO METHOD 02 NEUTRAL GEOMETRY SCAFFOLD FORMAT 01

Status: **MECHANISM-NEUTRAL TOOLING SPECIFICATION / NO CANDIDATE SCAFFOLD AUTHORIZED**  
Date: 2026-09-06

## Purpose

Define a deterministic, auditable scaffold **format** for future Method 02 construction work without instantiating any candidate-specific geometry.

This document does not authorize Candidate 04, choose a visual direction, create a candidate scaffold, transfer a scaffold to a renderer, or generate artwork.

## Core law

A Neutral Geometry Scaffold may encode **relational composition only**.

It must not carry aesthetic authorship, identity assignment, style, narrative interpretation or brand geometry.

## Coordinate system

Use normalized source-artboard coordinates:

- origin `(0,0)` = top-left;
- width = `1.0`;
- height = `1.0`;
- all points/boxes/paths expressed in normalized coordinates before export;
- source-artboard pixel dimensions recorded separately;
- deterministic rounding: maximum four decimal places.

This keeps the same structural record portable across source resolutions without selecting a rendering resolution.

## Allowed primitive classes

A future candidate-specific scaffold may use only these primitive classes unless later separately approved:

1. `figure_region`
   - approximate human bounding region;
   - optional major body-axis line;
   - anonymous labels only: `A`, `B`.

2. `critical_contact`
   - point or short segment where a physical/spatial relation is causally necessary;
   - may identify relationship type only structurally, e.g. `support`, `reach`, `occlusion`, `shared-boundary`.

3. `condition_path`
   - contour/centerline/boundary describing the shared condition;
   - may distinguish `baseline_witness` from `changed_segment` only as construction metadata.

4. `baseline_witness_region`
   - bounded area containing visible geometric evidence needed to recover baseline organization.

5. `negative_space_region`
   - bounded area required to remain structurally unoccupied for causal/readability reasons.

6. `occlusion_order`
   - pairwise front/behind relation only where causally necessary.

7. `responsive_boundary`
   - fixed Harness-derived crop/identity boundaries generated from the declared source-artboard dimensions.

## Explicitly excluded information

A scaffold must not encode or imply:

- final color or palette;
- material identity or surface finish;
- lighting;
- texture;
- clothing style;
- facial features;
- hair style beyond a generic figure silhouette needed for non-overlap;
- ethnicity, race, age coding beyond broad adult/non-child geometry if required by an already-approved candidate specification;
- historical period;
- named artistic style;
- symbolic props;
- narrative captions intended for artwork;
- emotion, gaze meaning, knowledge, belief, memory, intention or motive;
- Threshold K or O3 geometry;
- brand colors or logo placement;
- decorative composition marks;
- arrows/labels intended to survive into final artwork.

## Scaffold record schema

A future scaffold record should use the following mechanism-neutral structure:

```json
{
  "format": "kymaean.hero.method02.neutral-scaffold/1",
  "source_artboard": {
    "width": 0,
    "height": 0
  },
  "figures": [],
  "critical_contacts": [],
  "condition_paths": [],
  "baseline_witness_regions": [],
  "negative_space_regions": [],
  "occlusion_order": [],
  "responsive_boundaries": []
}
```

Zeros/empty arrays above are schema placeholders, not a candidate geometry.

## Primitive field conventions

### Figure region

```json
{
  "id": "A",
  "type": "figure_region",
  "bbox": [0, 0, 0, 0],
  "body_axis": [[0, 0], [0, 0]]
}
```

### Critical contact

```json
{
  "id": "contact-1",
  "type": "critical_contact",
  "relation": "support",
  "geometry": [[0, 0], [0, 0]],
  "participants": ["A", "condition-1"]
}
```

Allowed `relation` values are structural only and may be extended prospectively if a later Director-approved method revision requires another externally visible physical relation.

### Condition path

```json
{
  "id": "condition-1",
  "type": "condition_path",
  "role": "baseline_witness",
  "points": []
}
```

`role` may be `baseline_witness`, `changed_segment` or `continuity_path`.

### Region

```json
{
  "id": "region-1",
  "type": "baseline_witness_region",
  "polygon": []
}
```

## Responsive boundary generation

Responsive boundaries are not hand-drawn to favor a candidate.

They must be derived deterministically from:

- declared source-artboard dimensions;
- fixed desktop frame `1280 x 720`, `object-fit: cover`, `object-position:50% 50%`;
- fixed mobile artwork frame `390 x 488`, `object-fit: cover`, `object-position:72% 50%`;
- fixed desktop identity/copy geometry from Harness 01.

A future tool may visualize these windows, but it must not move them.

## Scaffold audit

Before any future scaffold can enter a Director review package, verify:

1. every primitive is from an allowed class;
2. every coordinate is normalized and deterministic;
3. no aesthetic variable is encoded;
4. no private-state/narrative claim is encoded;
5. no brand geometry is encoded;
6. responsive boundaries were calculated, not artistically adjusted;
7. every candidate-specific primitive traces to an already-authorized construction record;
8. no unnecessary primitive exists solely to make the scaffold look like finished art.

Any violation -> scaffold is invalid and must be corrected before review.

## Reference-transfer boundary

Method 02 approval does not authorize renderer transfer.

If a later execution package proposes using one candidate-specific scaffold as a structural reference, that package must separately approve:

- exact scaffold bytes/file;
- transfer mechanism;
- intended geometry-only variable;
- any available reference-strength setting;
- leakage detection;
- disposition if scaffold/diagram artifacts survive.

Default remains:

**visible scaffold/diagram artifacts in returned artwork = candidate failure, not a free reroll.**

## Current boundary

This file defines format/tooling only.

No specific visual direction, Candidate 04 construction, candidate-specific scaffold, reference transfer, renderer packet, Round 04 or image generation is authorized.
