# Comic Project Standard v1 — Archive Policy

## Contents

- [Design goals](#design-goals)
- [Core rule](#core-rule)
- [Git first](#git-first)
- [When to use `archive/`](#when-to-use-archive)
- [When not to archive](#when-not-to-archive)
- [Recommended archive structure](#recommended-archive-structure)
- [Recommended filename pattern](#recommended-filename-pattern)
- [Archival metadata](#archival-metadata)
- [Canon status of archived material](#canon-status-of-archived-material)
- [Character revisions](#character-revisions)
- [Relationship revisions](#relationship-revisions)
- [Story and issue revisions](#story-and-issue-revisions)
- [Branches vs. archive](#branches-vs-archive)
- [Destructive operations](#destructive-operations)
- [Archive proposals](#archive-proposals)
- [Archive review](#archive-review)
- [Search behavior](#search-behavior)
- [Restoration workflow](#restoration-workflow)
- [Source-of-truth rule](#source-of-truth-rule)
- [Compatibility requirements for Skills](#compatibility-requirements-for-skills)
- [Version](#version)

This document defines the recommended archival behavior for projects compatible with the `comic-story-framework`.

The archive exists to preserve directly browsable superseded material when Git history alone is not sufficient for the project's workflow.

Git remains the primary version-history mechanism.

## Design goals

The archive policy should:

- prevent silent loss of earlier creative states
- keep the current working tree understandable
- avoid unnecessary duplication
- preserve important superseded versions when useful
- require explicit confirmation before destructive or archival operations
- work consistently across characters, relationships, story, and issues

## Core rule

> Never archive, replace, move, or delete a current project file silently.

A Skill may prepare an archival plan, but it should only perform the archival action after explicit user approval when the action changes the project structure or removes the current version from its existing location.

## Git first

Use Git as the authoritative history of changes.

Preferred workflow:

```text
current file
    ↓
proposed revision
    ↓
review diff
    ↓
accept revision
    ↓
commit
```

The archive is supplementary.

Do not create an archived copy of every minor edit.

## When to use `archive/`

Archive a superseded version when one or more of the following apply:

- the old version remains useful for creative comparison
- the old version represents a major conceptual branch
- the user explicitly asks to preserve it outside Git history
- the file is being replaced by a substantially different structure
- the project needs human-browsable historical snapshots
- the old material may be mined later for discarded ideas

## When not to archive

Do not archive automatically for:

- typo fixes
- formatting changes
- minor wording improvements
- metadata corrections
- small continuity fixes
- routine iterative edits already captured by Git

## Recommended archive structure

```text
archive/
├── characters/
├── relationships/
├── canon/
├── story/
├── issues/
├── locations/
├── factions/
└── style/
```

Mirror the live project structure only as needed.

Do not create empty archive directories without a reason.

## Recommended filename pattern

Use filenames that remain understandable without Git metadata.

Recommended pattern:

```text
<original-name>__archived-YYYY-MM-DD__<reason>.md
```

Example:

```text
b-21-profile__archived-2026-09-12__pre-redesign.md
```

If the project avoids dates or uses relative chronology, a sequential version is acceptable:

```text
b-21-profile__v1.md
b-21-profile__v2.md
```

Projects should choose one convention and document it in `project.md`.

## Archival metadata

An archived file should ideally begin with a short metadata note.

Example:

```markdown
> **Archived:** 2026-09-12
> **Superseded by:** `characters/b-21/profile.md`
> **Reason:** Major character redesign
> **Status:** Historical reference, not current canon
```

This prevents archived content from being mistaken for the current source of truth.

## Canon status of archived material

Archived material is not automatically current canon.

By default:

```text
archive = historical project state
```

A current canon file always takes precedence over an archived version.

If an archived idea is later restored, it must be re-evaluated against the current project state.

## Character revisions

For major character revisions:

1. inspect the current profile
2. prepare the revised profile
3. summarize meaningful changes
4. identify canon and relationship impact
5. ask whether the previous profile should be archived if project policy requires confirmation
6. archive the superseded file if approved
7. place the revised file in the live character path
8. review Git diff
9. commit only when requested or when the user's workflow explicitly authorizes it

## Relationship revisions

When a relationship is substantially reworked:

- archive only the detailed relationship file if needed
- do not archive both character summaries merely because the relationship file changed
- update character summaries separately
- preserve old relationship versions only when they remain creatively useful

## Story and issue revisions

Consider archiving when:

- an entire issue premise is replaced
- a major arc is abandoned
- a script undergoes a structural rewrite
- an alternate ending is intentionally preserved
- a discarded branch may be revisited later

Do not archive every outline iteration.

## Branches vs. archive

Use Git branches when exploring an alternative that may continue evolving independently.

Use `archive/` when preserving a superseded snapshot inside the project.

Rule of thumb:

```text
still evolving alternative → Git branch

finished or discarded historical version → archive
```

## Destructive operations

The following actions require explicit confirmation unless the user has already granted a clear broader instruction:

- deleting a file
- replacing a current file without preserving recoverability
- moving a current file into `archive/`
- renaming canonical files in ways that may break references
- removing image references
- overwriting a current profile with a substantially different version

Skills should state what will happen before performing the operation.

## Archive proposals

A Skill may output:

```markdown
## Archive Proposal

Current file:
`characters/b-21/profile.md`

Reason:
Major rewrite changes motivation, background, and relationships.

Suggested archive path:
`archive/characters/b-21/profile__archived-2026-09-12__pre-rewrite.md`

Action:
Awaiting confirmation.
```

This is preferred over silently moving files.

## Archive review

Archived files should not normally be included in routine canon checks.

A Canon Guardian should:

- ignore `archive/` by default
- inspect it only when requested
- use it when tracing historical changes
- never treat archived content as current canon unless explicitly restored

## Search behavior

When a Skill searches a project:

1. prefer live project files
2. exclude `archive/` by default
3. include archived files only for historical comparison, restoration, or explicit user request

This prevents obsolete material from contaminating current reasoning.

## Restoration workflow

When restoring archived material:

1. inspect the archived file
2. compare it with current canon
3. classify contradictions as `CONFLICT`
4. extract reusable elements
5. treat restored ideas as `PROPOSAL` until approved
6. update current files only after confirmation

Do not restore archived content wholesale without review.

## Source-of-truth rule

The archive is never the primary source of truth for current project state.

Precedence:

```text
current live files
    ↓
project-defined canonical authority
    ↓
Git history
    ↓
archive snapshots
```

Git history and archive snapshots serve different purposes and may both be useful.

## Compatibility requirements for Skills

A reusable Skill should:

- ignore archived files during normal project reasoning unless needed
- never treat archived content as current canon by default
- ask before moving live files into the archive
- preserve traceability between archived and replacement files
- avoid generating unnecessary archive copies
- prefer Git for ordinary version history
- follow project-specific archive conventions when documented

## Version

Standard version: `v1`
