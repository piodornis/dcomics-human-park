# Comic Project Standard v1 — Canon Status

## Contents

- [Status model](#status-model)
- [CANON](#canon)
- [INFERENCE](#inference)
- [PROPOSAL](#proposal)
- [CONFLICT](#conflict)
- [OPEN](#open)
- [Promotion rules](#promotion-rules)
- [Demotion and revision](#demotion-and-revision)
- [Status precedence](#status-precedence)
- [Recommended output pattern](#recommended-output-pattern)
- [Writing to project files](#writing-to-project-files)
- [Cross-skill behavior](#cross-skill-behavior)
- [Example](#example)
- [Minimal rule](#minimal-rule)
- [Version](#version)

This document defines the shared status model used by Skills in the `comic-story-framework`.

Its purpose is to prevent creative suggestions, deductions, unresolved questions, and contradictions from being silently treated as established project facts.

## Status model

Use exactly these five primary states:

- `CANON`
- `INFERENCE`
- `PROPOSAL`
- `CONFLICT`
- `OPEN`

## CANON

A confirmed project fact.

Use `CANON` when the information has been explicitly established by the creator or is already part of the accepted project source of truth.

Examples:

```markdown
CANON:
B-21 is an older maintenance bot.
```

```markdown
CANON:
The city is inaccessible during the winter season.
```

A Skill must not alter established canon silently.

If a requested change would overwrite or invalidate existing canon, report the conflict before treating the new information as canon.

## INFERENCE

A logical conclusion derived from existing canon, but not explicitly confirmed.

Use `INFERENCE` when the conclusion is strongly supported by existing material but has not been formally established.

Example:

```markdown
INFERENCE:
Because Character A avoids the laboratory after the accident,
they may associate the location with guilt or fear.
```

An inference must remain distinguishable from canon.

Do not write an inference back into authoritative project files as a confirmed fact unless the user accepts it.

## PROPOSAL

A new creative suggestion.

Use `PROPOSAL` for ideas that extend, reinterpret, or develop the project but are not yet accepted.

Examples:

```markdown
PROPOSAL:
Character A and Character B knew each other before the main story.
```

```markdown
PROPOSAL:
The abandoned station could become the setting of Issue 4.
```

A proposal may be detailed and well-supported without becoming canon automatically.

## CONFLICT

A contradiction with existing canon or with another authoritative project source.

Use `CONFLICT` when two statements cannot both be true without revision, clarification, or a change in interpretation.

Example:

```markdown
CONFLICT:
The timeline places the evacuation before Character C was activated,
but the character profile states that Character C witnessed it.
```

A conflict report should identify:

1. the conflicting statements
2. the source of each statement
3. why they conflict
4. possible resolution options
5. whether resolving the conflict would change canon

A Skill should not resolve a canon conflict silently.

## OPEN

An intentionally unresolved question or undecided project point.

Use `OPEN` when the project explicitly leaves something undecided.

Examples:

```markdown
OPEN:
The exact year of B-21's activation has not been established.
```

```markdown
OPEN:
It is not yet decided whether the antagonist survives Issue 6.
```

A Skill may propose answers to an open point, but those answers remain `PROPOSAL` until accepted.

## Promotion rules

Status changes should be explicit.

Recommended flow:

```text
OPEN
  │
  ├──> PROPOSAL
  │       │
  │       └──> CANON
  │
  └──> CANON

INFERENCE
  │
  └──> CANON

CONFLICT
  │
  └──> requires resolution before CANON is changed
```

Only the user or an explicitly authorized project workflow may promote content to `CANON`.

Skills may recommend a promotion, but should not assume approval.

## Demotion and revision

Existing canon may be revised.

When the user intentionally changes established canon:

1. identify the old canon statement
2. identify affected files or story elements
3. mark resulting contradictions as `CONFLICT`
4. prepare the revised canon
5. update dependent material only after confirmation when the change is substantial
6. preserve prior history through Git and, when desired, project archives

A deliberate canon revision is not an error. The purpose of the framework is to make its consequences visible.

## Status precedence

When several states apply, use the most informative state for the current task.

General guidance:

- established accepted fact → `CANON`
- logical but unconfirmed deduction → `INFERENCE`
- new creative idea → `PROPOSAL`
- contradiction → `CONFLICT`
- unresolved question → `OPEN`

`CONFLICT` takes precedence when an otherwise plausible statement contradicts established canon.

Example:

A new idea may begin as `PROPOSAL`, but if it contradicts an existing fact, report it as a `CONFLICT` and explain the proposed change.

## Recommended output pattern

When a Skill proposes or analyzes project changes, use a compact structure like:

```markdown
## CANON
- Existing confirmed facts relevant to the task.

## INFERENCE
- Conclusions supported by canon but not yet confirmed.

## PROPOSAL
- New creative options.

## CONFLICT
- Contradictions that require resolution.

## OPEN
- Questions that remain undecided.
```

Do not include empty sections unless the output format requires them.

## Writing to project files

When updating authoritative project files:

- write confirmed information as normal project content
- preserve explicit `OPEN` items when the project uses them
- do not insert speculative material as fact
- keep proposals outside authoritative canon sections until accepted
- use review notes or change summaries for temporary `INFERENCE`, `PROPOSAL`, and `CONFLICT` content when appropriate

The labels are primarily a reasoning and review protocol. A project does not need to prefix every sentence in every file with a status label.

## Cross-skill behavior

All reusable Skills in the framework should follow these rules:

### Character Developer
May create `INFERENCE` and `PROPOSAL` content when developing a character. Must report `CONFLICT` when a requested character change contradicts established canon.

### Canon Guardian
Primarily identifies `CANON`, `CONFLICT`, `INFERENCE`, and `OPEN`. It may suggest `PROPOSAL` resolutions but must not apply them automatically.

### Story Architect
May freely generate `PROPOSAL` content, but must distinguish it from established canon and surface conflicts with existing project facts.

### Issue Writer
May elaborate accepted story plans while preserving the status of unresolved or proposed material.

### Continuity Reviewer
Should treat established canon as the baseline and report inconsistencies as `CONFLICT`.

## Example

Given:

```markdown
CANON:
Mara has never left the orbital station.

PROPOSAL:
In Issue 3, Mara remembers standing on the surface of Mars.
```

The correct analysis is:

```markdown
CONFLICT:
The proposed memory implies that Mara has previously been on Mars,
which contradicts the established fact that she has never left the station.

Possible resolutions:
1. Change the memory to a simulation.
2. Revise the existing canon.
3. Give the memory to another character.
4. Establish that Mara's belief about her past is unreliable.
```

The Skill must not silently choose one of these options.

## Minimal rule

When uncertain, follow this principle:

> Never convert possibility into fact without explicit confirmation.

## Version

Standard version: `v1`
