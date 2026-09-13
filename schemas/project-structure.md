# Comic Project Standard v1 — Project Structure

## Contents

- [Design goals](#design-goals)
- [Recommended repository structure](#recommended-repository-structure)
- [Root file: `project.md`](#root-file-projectmd)
- [`canon/`](#canon)
- [`characters/`](#characters)
- [`relationships/`](#relationships)
- [`locations/`](#locations)
- [`factions/`](#factions)
- [`story/`](#story)
- [`issues/`](#issues)
- [`style/`](#style)
- [`archive/`](#archive)
- [Path discovery](#path-discovery)
- [Source-of-truth principle](#source-of-truth-principle)
- [Git workflow](#git-workflow)
- [Compatibility requirement for framework Skills](#compatibility-requirement-for-framework-skills)
- [Version](#version)

This document defines the recommended repository structure for comic projects that use the `comic-story-framework`.

The goal is to provide a predictable, project-agnostic layout that reusable Skills can understand without embedding project-specific canon or assumptions.

## Design goals

The project structure should:

- separate canon, characters, relationships, story, issues, and style
- be readable and maintainable without AI tooling
- work well with Git versioning
- support incremental growth from a small idea to a large series
- allow Skills to locate relevant project information consistently
- avoid duplicating the same fact across multiple files where possible
- keep project-specific knowledge outside reusable Skills

## Recommended repository structure

```text
comic-project/
├── project.md
├── canon/
│   ├── series-bible.md
│   ├── timeline.md
│   ├── glossary.md
│   └── world-rules.md
├── characters/
├── relationships/
├── locations/
├── factions/
├── story/
├── issues/
├── style/
└── archive/
```

Not every project needs every directory immediately. Empty directories may be added when they become relevant.

## Root file: `project.md`

`project.md` is the entry point for the comic project.

It should contain project-level information such as:

- project title
- working title, if different
- language
- genre
- tone
- format
- intended audience, if relevant
- current project phase
- optional development entry point: `world-first`, `character-first`, `relationship-first`, `story-first`, or `mixed`
- paths used by the project
- project-specific deviations from this standard
- status of the canon
- optional notes about visual or narrative direction

Example:

```markdown
# Project

## Title
Project X

## Language
German

## Format
Comic series

## Status
Development

## Development entry point
relationship-first

## Canon policy
Use the shared status model:
CANON, INFERENCE, PROPOSAL, CONFLICT, OPEN
```

## `canon/`

Contains project-wide facts and rules that apply across characters, locations, relationships, and stories.

Recommended files:

### `canon/series-bible.md`

High-level source of truth for the fictional setting and series.

Typical contents:

- premise
- major themes
- setting
- central conflicts
- established world facts
- important historical context
- project-wide narrative constraints

### `canon/timeline.md`

Chronological reference for confirmed events.

Use relative chronology when exact dates are not yet established.

Avoid inventing exact dates only to make the timeline appear complete.

### `canon/glossary.md`

Definitions of recurring terms, technologies, factions, locations, titles, concepts, and in-world language.

### `canon/world-rules.md`

Rules that define how the fictional world functions.

Examples:

- technology limits
- political structures
- magic systems
- biological rules
- social rules
- economic constraints
- rules for artificial intelligence
- travel or communication limitations

## `characters/`

Contains character-specific information.

Recommended pattern:

```text
characters/
└── character-id-or-name/
    ├── profile.md
    └── references/
```

`profile.md` is the current working character record.

Possible additional files may be introduced when the character becomes complex enough, for example:

```text
characters/
└── character-id/
    ├── profile.md
    ├── history.md
    ├── motivations.md
    └── references/
```

Do not split a character into many files unless it improves clarity.

Visual reference images, character sheets, costume references, and similar material should live under `references/` or another clearly documented project-specific asset path.

## `relationships/`

Contains relationships that are important enough to require their own source of truth.

Recommended filename pattern:

```text
relationships/character-a__character-b.md
```

A relationship file may contain:

- relationship status
- shared history
- current dynamic
- mutual values
- points of conflict
- what each character wants from the other
- what each character misunderstands about the other
- development phases
- key scenes
- unresolved questions

Character profiles may summarize relationships, but the dedicated relationship file should be preferred when the relationship becomes substantial.

## `locations/`

Contains reusable location records.

Typical contents:

- physical description
- function
- atmosphere
- inhabitants or users
- historical relevance
- recurring visual details
- known story events
- restrictions or hazards

## `factions/`

Contains groups, institutions, organizations, species, teams, companies, governments, or other collective actors.

Typical contents:

- purpose
- hierarchy
- ideology
- resources
- important members
- alliances
- conflicts
- history

## `story/`

Contains story-level planning that is broader than a single issue.

Recommended contents may include:

```text
story/
├── master-arc.md
├── character-arcs.md
├── unresolved-setups.md
└── chronology.md
```

Possible uses:

- overall series arc
- season or volume arcs
- major turning points
- character development arcs
- setups and payoffs
- unresolved narrative threads
- story chronology

Do not use `story/` as a replacement for established canon. A planned event is not automatically canon unless the project's canon policy says otherwise.

## `issues/`

Contains issue-, chapter-, episode-, or installment-specific material.

Recommended pattern:

```text
issues/
└── issue-001/
    ├── synopsis.md
    ├── outline.md
    ├── script.md
    ├── storyboard.md
    └── continuity-notes.md
```

Only create the files needed for the project's current workflow.

Possible issue-level artifacts:

- synopsis
- scene list
- beat sheet
- script
- dialogue pass
- storyboard description
- page breakdown
- continuity report
- revision notes

## `style/`

Contains project-specific creative direction.

Recommended contents may include:

```text
style/
├── visual-style.md
├── dialogue-style.md
├── storytelling-rules.md
└── lettering-notes.md
```

This directory should describe the project's style, not the generic behavior of reusable Skills.

Examples:

- visual language
- palette logic
- panel density
- recurring framing rules
- dialogue conventions
- humor style
- narration rules
- prohibited visual or tonal choices

## `archive/`

Contains superseded project files that should remain accessible outside Git history.

Archiving is optional when Git history alone is sufficient.

Recommended principles:

- never archive or replace a current file silently
- request confirmation before moving an older version into the archive
- retain clear filenames or metadata that identify the superseded version
- prefer Git history as the authoritative change record
- use `archive/` when an old version needs to remain directly browsable

Possible pattern:

```text
archive/
├── characters/
├── relationships/
├── story/
└── issues/
```

## Path discovery

Reusable Skills should not assume that every project follows this structure perfectly.

When working with a project:

1. inspect `project.md` first, if available
2. respect project-specific path overrides
3. prefer existing structure over forcing a migration
4. ask before restructuring files
5. use this standard as the default only when no project-specific convention exists

## Source-of-truth principle

Avoid storing the same detailed information in several places.

Prefer:

- character facts in character files
- relationship detail in relationship files
- global world rules in `canon/`
- story plans in `story/`
- issue execution in `issues/`
- project-specific creative direction in `style/`

Summaries and cross-references are allowed, but Skills should identify which file is authoritative for the relevant fact.

## Git workflow

Recommended workflow:

```text
inspect current files
        ↓
prepare proposed changes
        ↓
review canon impact
        ↓
request confirmation when required
        ↓
write/update project files
        ↓
review diff
        ↓
commit
        ↓
push if explicitly requested
```

Skills must not assume permission to commit, push, delete, move, or archive files unless the user explicitly authorizes those actions.

## Compatibility requirement for framework Skills

A reusable Skill designed for `comic-story-framework` should:

- remain independent of any specific comic title
- discover project content through this structure or `project.md`
- state which project areas it reads
- state which project areas it may modify
- distinguish read-only checks from write operations
- avoid changing unrelated project files
- preserve the project's chosen language and terminology
- follow the shared canon-status model

## Version

Standard version: `v1`

This document is intentionally conservative. New directories or schemas should only be added when repeated real-world use shows that they are necessary.
