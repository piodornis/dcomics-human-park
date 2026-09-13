# Worldbuilding Protocol

## Contents

- [1. Establish the baseline](#1-establish-the-baseline)
- [2. Identify the worldbuilding function](#2-identify-the-worldbuilding-function)
- [3. Build from constraints](#3-build-from-constraints)
- [4. Separate objective reality from in-world belief](#4-separate-objective-reality-from-in-world-belief)
- [5. Model consequences](#5-model-consequences)
- [6. Test for scale errors](#6-test-for-scale-errors)
- [7. Test for loopholes](#7-test-for-loopholes)
- [8. Preserve contradictions that are intentional](#8-preserve-contradictions-that-are-intentional)
- [9. Create story affordances](#9-create-story-affordances)
- [10. Produce an impact map](#10-produce-an-impact-map)

Use this protocol for complex world-development tasks.

## 1. Establish the baseline

Before inventing new material, identify:

- established facts
- current world rules
- relevant history
- affected locations and factions
- known character dependencies
- story events that rely on the current world state
- open canon questions

Do not fill gaps automatically.

## 2. Identify the worldbuilding function

Ask what the new element must do for the project.

Possible functions:

- create a setting for recurring scenes
- explain a character's background
- create a source of conflict
- impose a limitation
- make a plot event possible
- make a plot event costly
- distinguish a culture or faction
- provide visual identity
- connect existing canon elements

If the user gives an aesthetic idea with no function, preserve the aesthetic and propose functional consequences rather than inventing a large system immediately.

## 3. Build from constraints

Define constraints before abundance.

For systems, establish:

1. what the system does
2. what it cannot do
3. what it costs
4. what it depends on
5. how it fails
6. who can access it
7. what changes if it becomes common

This is especially important for technology, magic, transport, surveillance, medicine, energy, communication, and weapons.

## 4. Separate objective reality from in-world belief

A project may contain:

- actual world rules
- scientific theories
- propaganda
- religion
- superstition
- institutional doctrine
- character misunderstanding

Do not collapse these into one truth layer.

Example:

```markdown
CANON:
The reactor becomes unstable under sustained magnetic interference.

CANON — in-world belief:
Operators are taught that instability is caused by contamination.

OPEN:
It is not yet established whether the operator manual is deliberately misleading.
```

## 5. Model consequences

For each important proposal, trace at least first-order consequences and, when relevant, second-order consequences.

Example:

```text
PROPOSAL:
Long-distance transport is extremely expensive.

First-order:
Most people rarely leave their region.

Second-order:
Regional dialects and institutions remain unusually distinct.

Story impact:
A character who has traveled widely becomes exceptional and potentially suspicious.
```

Do not turn inferred consequences into canon automatically.

## 6. Test for scale errors

Ask whether a local rule accidentally implies a global change.

Examples:

- a cheap cure changes healthcare everywhere
- perfect translation changes diplomacy and language barriers
- easy teleportation changes geography, warfare, logistics, and trade
- ubiquitous surveillance changes crime, privacy, and rebellion
- abundant energy changes infrastructure and economics

If a proposal has broad implications, surface them explicitly.

## 7. Test for loopholes

Look for obvious workarounds that would undermine established stakes.

If a system can solve a major recurring problem, ask why characters or institutions do not already use it.

Possible valid answers:

- cost
- scarcity
- risk
- law
- maintenance
- knowledge
- access
- ethics
- incompatibility
- time
- political control

Do not invent a limitation unless it fits the project; mark it as `PROPOSAL`.

## 8. Preserve contradictions that are intentional

Not every contradiction in the world is a canon error.

Institutions may be hypocritical. Cultures may hold incompatible values. Characters may believe false things. Laws may contradict practice.

A true `CONFLICT` is a contradiction between authoritative project facts that cannot both remain true under the current interpretation.

## 9. Create story affordances

Good worldbuilding creates actions characters can take.

For a location, ask:

- what can happen here that cannot happen elsewhere?
- what obstacles exist?
- what resources exist?
- who controls access?
- what visual opportunities recur?

For a faction, ask:

- what can they offer?
- what can they threaten?
- what do they need?
- what internal fracture can create drama?

For technology, ask:

- what problem does it solve?
- what new problem does it create?

## 10. Produce an impact map

For substantial changes, finish with an impact map.

Example:

```markdown
## Impact Map

### Characters
- Character A: background should be reviewed.

### Relationships
- A/B power balance may change because B now controls access to transport.

### Story
- Issue 4 escape plan becomes easier and may lose tension.

### Timeline
- No known effect.

### Canon
- Existing world rule about border isolation requires review.
```

This is a review list, not permission to rewrite those files.
