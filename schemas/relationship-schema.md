# Comic Project Standard v1 — Relationship Schema

## Contents

- [Design goals](#design-goals)
- [Recommended location](#recommended-location)
- [When to create a dedicated relationship file](#when-to-create-a-dedicated-relationship-file)
- [Recommended structure](#recommended-structure)
- [Relationship summary](#relationship-summary)
- [Core dynamic](#core-dynamic)
- [Two-perspective rule](#two-perspective-rule)
- [Shared values and differences](#shared-values-and-differences)
- [Shared history](#shared-history)
- [Development phases](#development-phases)
- [Conflict design](#conflict-design)
- [Loyalty and attachment](#loyalty-and-attachment)
- [Power balance](#power-balance)
- [Communication pattern](#communication-pattern)
- [Running gags and recurring behavior](#running-gags-and-recurring-behavior)
- [Key scenes](#key-scenes)
- [Narrative function](#narrative-function)
- [Synchronization with character files](#synchronization-with-character-files)
- [Canon-state handling](#canon-state-handling)
- [Relationship revision impact check](#relationship-revision-impact-check)
- [Compatibility requirement for Skills](#compatibility-requirement-for-skills)
- [Version](#version)

This document defines the recommended structure for relationship records used by projects compatible with the `comic-story-framework`.

A relationship file is intended for relationships that are narratively important enough to deserve their own source of truth.

## Design goals

A relationship record should:

- describe the relationship as a dynamic system rather than a static label
- preserve both characters' perspectives
- track development over time
- connect emotional, practical, thematic, and narrative dimensions
- support continuity checks
- prevent contradictory relationship descriptions across character files
- distinguish established relationship facts from proposals and unresolved questions

## Recommended location

```text
relationships/
└── character-a__character-b.md
```

Use a stable filename convention.

Examples:

```text
relationships/b-21__b-73.md
relationships/mara__jonas.md
relationships/ada__the-council.md
```

The filename should not imply directionality unless the relationship itself is directional.

## When to create a dedicated relationship file

Create one when:

- the relationship changes meaningfully over time
- both perspectives matter
- it drives important story decisions
- it contains recurring conflict
- it carries thematic weight
- several issues or scenes depend on it
- character profiles would otherwise duplicate substantial information

Simple or incidental relationships may remain as summaries in character profiles.

## Recommended structure

```markdown
# Character A ↔ Character B

> **Status:** Current working relationship profile
> **Canon state:** CANON / mixed / draft

## Relationship Summary

Short description of the current relationship.

## Core Dynamic

One or two sentences describing the underlying tension or bond.

## Shared Values

- ...

## Fundamental Differences

- ...

## Character A's Perspective

### What A values in B
...

### What A dislikes or distrusts in B
...

### What A misunderstands about B
...

### What A needs from B
...

## Character B's Perspective

### What B values in A
...

### What B dislikes or distrusts in A
...

### What B misunderstands about A
...

### What B needs from A
...

## Shared History

Confirmed events that shaped the relationship.

## Development Phases

### Phase 1 — ...
...

### Phase 2 — ...
...

## Sources of Conflict

- ...

## Sources of Loyalty / Attachment

- ...

## Power Balance

Describe authority, dependency, leverage, vulnerability, or asymmetry.

## Communication Pattern

Describe how they speak, argue, cooperate, avoid, or repair conflict.

## Recurring Behaviors / Running Gags

- ...

## Key Scenes

- ...

## Narrative Function

Explain what this relationship contributes to the story.

## Open Canon Points

- ...
```

Projects may adapt the headings, but reusable Skills should preserve the same conceptual structure.

## Relationship summary

The summary should describe the relationship in its current state.

Examples:

```markdown
They are professional rivals who increasingly rely on each other.
```

```markdown
They are siblings with strong loyalty but incompatible ideas of responsibility.
```

Avoid reducing a complex relationship to a single label if that label hides the important tension.

## Core dynamic

The core dynamic is the relationship's central engine.

Useful patterns include:

- trust vs control
- duty vs affection
- old generation vs new generation
- admiration mixed with resentment
- dependency without emotional honesty
- loyalty under ideological conflict
- protection that becomes control
- rivalry that reveals mutual respect

A strong core dynamic should generate scenes naturally.

## Two-perspective rule

Always preserve both perspectives.

Do not write:

```markdown
A distrusts B.
```

and assume the relationship is fully described.

Prefer:

```markdown
A distrusts B because B improvises too freely.

B sees A as dependable but overly cautious.
```

The relationship may be asymmetrical.

One character may care more, understand more, hold more power, or misread the other more severely.

## Shared values and differences

Relationships become more useful when conflict is not based only on opposition.

Record:

- what both want
- where their methods differ
- what they agree on but interpret differently

Example:

```markdown
Shared value:
Both want to protect vulnerable people.

Difference:
A trusts procedure; B trusts immediate practical judgment.
```

This structure creates durable conflict without requiring one side to be irrational.

## Shared history

Record only confirmed events.

If the past is not yet established, keep it `OPEN` or `PROPOSAL`.

Do not invent a long shared history merely because the present relationship suggests one.

## Development phases

Use phases when the relationship changes over time.

Example:

```markdown
### Phase 1 — Functional cooperation
They work together because their tasks overlap.

### Phase 2 — Professional friction
Their methods clash repeatedly.

### Phase 3 — Earned respect
Each recognizes the other's competence.

### Phase 4 — Personal loyalty
They begin protecting each other beyond formal obligation.
```

Phases may be tied to issue numbers, arcs, or relative chronology.

Avoid assigning exact dates unless they are established.

## Conflict design

Sources of conflict may include:

- values
- methods
- loyalty
- secrets
- hierarchy
- jealousy
- fear
- trauma
- ideology
- misunderstanding
- resource competition
- incompatible goals
- timing

For each major conflict, prefer explaining why both sides make sense from their own perspective.

## Loyalty and attachment

Record how care or loyalty is shown.

Characters do not need to express attachment verbally.

Possible signals:

- repairs
- protection
- sharing information
- taking risks
- covering for mistakes
- making space for vulnerability
- remembering preferences
- defending the other in public
- challenging the other in private

These details are often more useful than abstract declarations such as "they are close."

## Power balance

Relationships may involve several forms of power:

- formal authority
- physical power
- technical competence
- social leverage
- emotional dependence
- access to information
- institutional status
- moral influence

Power may shift over time.

A relationship does not need to be equal to be narratively balanced.

## Communication pattern

Describe interaction behavior.

Examples:

- formal in public, direct in private
- uses humor to avoid vulnerability
- rarely argues, but silently withholds cooperation
- one character overexplains while the other answers in fragments
- conflict is repaired through action rather than apology

This section is especially useful for dialogue and scene-writing Skills.

## Running gags and recurring behavior

Recurring patterns can create continuity and emotional texture.

Examples:

- repeated disagreement over tools
- correcting each other's terminology
- silent exchange of equipment
- one character predicts the other's objections
- ritualized argument before cooperation

A running gag should not flatten the relationship into comedy if the relationship also carries serious stakes.

## Key scenes

Record scenes that establish or transform the relationship.

Each key scene may include:

```markdown
### Scene title

**Status:** CANON / PROPOSAL

**Function:** What changes here?

**Setup:** ...

**Turning point:** ...

**Aftereffect:** ...
```

Do not treat a proposed scene as established history until accepted.

## Narrative function

Explain what the relationship contributes beyond the two characters.

Examples:

- embodies a thematic conflict
- connects two factions
- exposes different moral systems
- creates comic relief under tension
- humanizes an otherwise distant character
- drives a betrayal arc
- demonstrates generational change

## Synchronization with character files

Dedicated relationship files should be the detailed source of truth.

Character profiles should contain concise summaries.

When the relationship changes:

1. update the dedicated relationship file
2. identify whether either character summary must change
3. identify whether motivations or arcs are affected
4. check story and timeline dependencies
5. report conflicts before applying broad revisions

Do not maintain two independent detailed versions of the same relationship.

## Canon-state handling

Apply the shared status model.

Examples:

```markdown
CANON:
A and B currently work together.

INFERENCE:
A's repeated maintenance of B's equipment suggests growing attachment.

PROPOSAL:
Their first major disagreement could occur during Issue 2.

OPEN:
It is not yet established whether they knew each other before the main story.

CONFLICT:
Issue 1 shows them meeting for the first time, while the current relationship draft says they worked together years earlier.
```

## Relationship revision impact check

A major relationship change should trigger review of:

- both character profiles
- motivations
- loyalties
- faction relationships
- character arcs
- story beats
- issue scripts
- timeline
- key scenes
- dialogue dynamics

A relationship change may affect one character more strongly than the other.

## Compatibility requirement for Skills

A reusable relationship-aware Skill should:

- preserve both viewpoints
- avoid assuming symmetry
- distinguish current state from historical development
- distinguish shared values from points of conflict
- treat key scenes as proposals unless established
- synchronize summaries without duplicating the full relationship
- report downstream story impacts
- follow the shared canon-status model

## Version

Standard version: `v1`
