# Comic Project Standard v1 — Issue Schema

## Contents

- [Design goals](#design-goals)
- [Recommended location](#recommended-location)
- [Issue directory naming](#issue-directory-naming)
- [`synopsis.md`](#synopsismd)
- [`outline.md`](#outlinemd)
- [A-, B-, and C-Plots](#a--b--and-c-plots)
- [Character movement](#character-movement)
- [Relationship movement](#relationship-movement)
- [Setups and payoffs](#setups-and-payoffs)
- [`script.md`](#scriptmd)
- [`storyboard.md`](#storyboardmd)
- [`continuity-notes.md`](#continuity-notesmd)
- [Status handling](#status-handling)
- [Issue lifecycle](#issue-lifecycle)
- [Handoff between Skills](#handoff-between-skills)
- [Issue-level source of truth](#issue-level-source-of-truth)
- [Change impact check](#change-impact-check)
- [Compatibility requirements for Skills](#compatibility-requirements-for-skills)
- [Version](#version)

This document defines the recommended structure for issue-, chapter-, episode-, or installment-level records used by projects compatible with the `comic-story-framework`.

The goal is to separate high-level story planning from the concrete execution of a single installment while preserving continuity, traceability, and clean handoffs between Skills.

## Design goals

An issue record should:

- capture the dramatic purpose of a single installment
- connect the issue to larger story, character, and relationship arcs
- distinguish planned content from established canon
- support iterative development from synopsis to script and storyboard
- keep continuity-sensitive information easy to review
- allow different projects to use different levels of detail
- avoid mixing project-wide canon with issue-specific execution

## Recommended location

```text
issues/
└── issue-001/
    ├── synopsis.md
    ├── outline.md
    ├── script.md
    ├── storyboard.md
    └── continuity-notes.md
```

Not every file is required.

Create only the files that support the current production workflow.

## Issue directory naming

Use a stable sortable naming convention.

Recommended:

```text
issue-001/
issue-002/
issue-003/
```

Alternative project-specific conventions are allowed, for example:

```text
chapter-01/
episode-01/
volume-01-issue-01/
```

The project should document deviations in `project.md`.

## `synopsis.md`

Use `synopsis.md` for a compact summary of what the installment is about.

Recommended structure:

```markdown
# Issue 001 — Working Title

## Status
Draft / Planned / Approved / Published

## Purpose

Why this issue exists in the larger story.

## Synopsis

Short prose summary of the installment.

## Main Conflict

...

## Primary Characters

- ...

## Relevant Arcs

- Story arc:
- Character arc:
- Relationship arc:

## End State

What has materially changed by the end of the issue.

## Open Questions

- ...
```

The synopsis should be readable without the full script.

## `outline.md`

Use `outline.md` for the structural breakdown of the issue.

Recommended structure:

```markdown
# Issue 001 — Outline

## Issue Goal

...

## A-Plot

...

## B-Plot

...

## C-Plot

...

## Beat Structure

### Beat 1 — Opening state
...

### Beat 2 — Inciting change
...

### Beat 3 — Escalation
...

### Beat 4 — Turning point
...

### Beat 5 — Climax
...

### Beat 6 — Resolution / Cliffhanger
...

## Character Movement

### Character A
Start:
Change:
End:

## Relationship Movement

### Character A ↔ Character B
Start:
Change:
End:

## Setups

- ...

## Payoffs

- ...

## Open Story Questions

- ...
```

The exact number of beats is flexible.

Do not force every issue into the same beat count.

## A-, B-, and C-Plots

Use plot labels when parallel storylines exist.

### A-Plot

The main dramatic line of the issue.

### B-Plot

A secondary line that supports, contrasts, or complicates the A-Plot.

### C-Plot

A smaller recurring or setup-oriented line.

Do not create B- or C-Plots simply to fill a template.

## Character movement

Each important character should end the issue in a meaningfully different state when appropriate.

Possible changes:

- new information
- changed motivation
- damaged trust
- increased commitment
- changed status
- new fear
- new responsibility
- physical consequence
- changed relationship

Not every character must change in every issue.

## Relationship movement

When an issue materially changes a relationship, record:

- state at the beginning
- event or pressure that changes it
- state at the end

Example:

```markdown
### A ↔ B

Start:
Professional distrust.

Change:
A relies on B during a crisis.

End:
Trust remains limited, but competence is no longer questioned.
```

## Setups and payoffs

A setup introduces information, an object, behavior, promise, problem, image, or question that is intended to matter later.

A payoff resolves or transforms an earlier setup.

Recommended notation:

```markdown
## Setups

- S-001: Character A hides the damaged key.
- S-002: The emergency generator makes an irregular sound.

## Payoffs

- P-001 → S-014 from Issue 002: The missing badge reveals the infiltrator.
```

Project-specific IDs are optional but useful for long-running stories.

## `script.md`

Use `script.md` for the issue's written comic script.

The exact script format is project-specific.

A compatible script should make at least these elements identifiable:

- page
- panel
- location
- active characters
- action
- dialogue
- captions
- sound effects
- continuity-sensitive visual information

Example:

```markdown
# Page 1

## Panel 1

**Location:** Maintenance corridor

**Characters:** B-21

**Action:** B-21 kneels beside an open service panel.

**B-21:** "..."

**SFX:** CLANK
```

The Story Architect should generally stop before writing full script dialogue unless explicitly requested.

The Issue Writer may produce or revise `script.md`.

## `storyboard.md`

Use `storyboard.md` for panel-level visual planning.

Possible fields:

```markdown
# Page 1

## Panel 1

- Shot: Wide
- Camera: Slight high angle
- Focus: Character A entering the room
- Background: Damaged control wall
- Dialogue space: upper right
- Visual purpose: establish isolation
```

The Storyboard Director may produce or revise this file.

The storyboard should preserve story intent rather than silently rewriting the issue.

## `continuity-notes.md`

Use this file for issue-specific continuity observations.

Recommended structure:

```markdown
# Issue 001 — Continuity Notes

## Incoming continuity

- ...

## New established facts

- ...

## Character state changes

- ...

## Relationship state changes

- ...

## Visual continuity

- ...

## Timeline effects

- ...

## Conflicts

- ...

## Open items

- ...
```

The Continuity Reviewer and Canon Guardian may use this file as a review surface.

## Status handling

Apply the shared canon-status model.

Important distinction:

A planned event in `outline.md` is normally `PROPOSAL` until accepted according to the project's workflow.

A scripted event is not automatically `CANON` merely because it appears in a draft script.

Projects should define when an issue becomes canon, for example:

- when outline is approved
- when script is approved
- when issue is finalized
- when issue is published

Document this in `project.md`.

## Issue lifecycle

Recommended lifecycle:

```text
idea
  ↓
synopsis
  ↓
outline
  ↓
canon review
  ↓
script
  ↓
continuity review
  ↓
storyboard
  ↓
final review
  ↓
approved / published
```

Projects may use a different order.

## Handoff between Skills

### Story Architect

Reads:

- project canon
- characters
- relationships
- story arcs

Produces or revises:

- synopsis
- outline
- beat structure
- arc movement
- setups and payoffs

Should not silently rewrite established canon.

### Canon Guardian

Reads issue files and compares them with:

- canon
- timeline
- characters
- relationships
- earlier issues

Produces a review report.

Read-only by default.

### Issue Writer

Uses an approved synopsis or outline to create or revise the script.

Should preserve the issue's dramatic intent unless asked to restructure it.

### Storyboard Director

Uses the script or approved outline to plan pages and panels.

Should not invent major story changes without marking them as proposals.

### Continuity Reviewer

Checks issue execution for:

- character state
- props
- injuries
- clothing
- location state
- timeline
- relationship state
- setups and payoffs

## Issue-level source of truth

Within an issue:

- `synopsis.md` explains purpose and summary
- `outline.md` is the main structural plan
- `script.md` is the detailed written execution
- `storyboard.md` is the visual execution plan
- `continuity-notes.md` records continuity impact

When these files disagree, the project workflow should define precedence.

Until that precedence is explicit, a Skill should report the discrepancy instead of guessing.

## Change impact check

When an issue changes substantially, review possible effects on:

- master story arc
- character arcs
- relationship arcs
- timeline
- future issue setups
- previous issue payoffs
- visual continuity
- world rules
- unresolved story questions

## Compatibility requirements for Skills

A reusable issue-aware Skill should:

- preserve the project's issue naming convention
- respect the project's canon threshold
- distinguish planning from established canon
- identify which issue file it is using as the current authority
- avoid rewriting unrelated files
- report downstream impacts of substantial changes
- preserve accepted story intent across handoffs
- follow the shared canon-status model

## Version

Standard version: `v1`
