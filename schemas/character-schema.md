# Comic Project Standard v1 — Character Schema

## Contents

- [Design goals](#design-goals)
- [Recommended location](#recommended-location)
- [Required minimum fields](#required-minimum-fields)
- [Recommended `profile.md` structure](#recommended-profilemd-structure)
- [Identity and naming](#identity-and-naming)
- [Short profile](#short-profile)
- [Appearance](#appearance)
- [Background](#background)
- [Core traits](#core-traits)
- [Motivations](#motivations)
- [Strengths and weaknesses](#strengths-and-weaknesses)
- [Relationships](#relationships)
- [Narrative function](#narrative-function)
- [Dialogue and voice](#dialogue-and-voice)
- [Visual continuity notes](#visual-continuity-notes)
- [Open canon points](#open-canon-points)
- [Change workflow](#change-workflow)
- [Character revision impact check](#character-revision-impact-check)
- [Visual references](#visual-references)
- [Notes and unstructured input](#notes-and-unstructured-input)
- [Source-of-truth principle](#source-of-truth-principle)
- [Compatibility requirement for Skills](#compatibility-requirement-for-skills)
- [Version](#version)

This document defines the recommended structure for character records used by projects compatible with the `comic-story-framework`.

The purpose of the schema is to make character information easy to review, version, compare, and use across multiple Skills without forcing every project into an overly rigid template.

## Design goals

A character record should:

- provide one clear source of truth for the current character state
- separate confirmed facts from unresolved questions and proposals
- support both concise and highly developed characters
- remain readable without AI tooling
- allow visual references and free-form notes to be attached
- support continuity checks across story, relationships, and canon
- avoid duplicating detailed relationship or world information unnecessarily

## Recommended location

```text
characters/
└── character-id-or-name/
    ├── profile.md
    └── references/
```

Additional files may be introduced when a character becomes complex enough to benefit from them.

Examples:

```text
characters/
└── character-id/
    ├── profile.md
    ├── history.md
    ├── motivations.md
    └── references/
```

Use a single `profile.md` by default. Split content only when this improves clarity.

## Required minimum fields

A useful character record should contain at least:

- identifier or name
- current role or function
- short profile
- core traits
- motivations
- strengths
- weaknesses or conflict potential
- relationships summary
- current narrative function
- open questions

Projects may add or remove sections when appropriate.

## Recommended `profile.md` structure

```markdown
# Character Name or ID

> **Status:** Current working profile
> **Canon state:** CANON / mixed / draft
> **Last revised:** optional

## Identity

| Field | Value |
|---|---|
| Name / ID | |
| Role | |
| Age / generation / model | |
| Pronouns | |
| Affiliation | |
| Current status | |

## Short Profile

Concise overview of who this character is and why they matter.

## Appearance

Key visual traits that should remain consistent.

## Background

Confirmed personal history relevant to the current story.

## Core Traits

| Trait | Expression |
|---|---|
| | |

## Motivations

### Primary motivation
...

### Secondary motivations
...

### Fears / pressures
...

## Strengths

- ...

## Weaknesses and Conflict Potential

- ...

## Relationships

Short summaries only. Use dedicated relationship files for complex relationships.

## Narrative Function

What this character contributes to the story structurally or thematically.

## Typical Behavior

- ...

## Typical Dialogue / Voice

- ...

## Visual Continuity Notes

- ...

## Open Canon Points

- ...
```

The exact headings may be adapted to the project, but reusable Skills should be able to map the local structure to these conceptual fields.

## Identity and naming

Use the project’s own naming conventions.

For characters with non-human identifiers, codenames, model numbers, ranks, or aliases, preserve those forms consistently.

Example:

```markdown
| Name / ID | B-21 |
| Role | Maintenance and safety bot |
```

If a character has multiple names or identities, distinguish them clearly.

## Short profile

The short profile should answer:

- who is this character?
- what is their current function?
- what makes them distinct?
- what tension or role makes them narratively useful?

Keep this section compact enough to be used as fast context by other Skills.

## Appearance

Record only details that matter for continuity or storytelling.

Useful fields may include:

- build
- height or relative scale
- face
- hair
- skin or surface material
- colors
- clothing
- markings
- scars
- damage
- accessories
- recurring equipment
- posture
- visual silhouette

Avoid writing image-generation prompts directly into the character profile unless the project intentionally uses that format.

Detailed visual prompts may live in `references/` or in a dedicated visual guide.

## Background

The background section should distinguish:

- confirmed history
- uncertain memories
- disputed events
- unresolved dates
- proposed additions

Do not convert gaps into facts.

If exact chronology is unknown, use relative chronology instead of inventing dates.

## Core traits

Traits should describe behavior, not only adjectives.

Prefer:

```markdown
| Skeptical | Distrusts new solutions until they prove reliable over time. |
```

instead of:

```markdown
| Skeptical | Very skeptical. |
```

A small number of well-defined traits is usually more useful than a long undifferentiated list.

## Motivations

Motivations should explain what drives decisions.

Recommended categories:

- primary motivation
- secondary motivation
- fear
- obligation
- desire
- unresolved need
- moral boundary

Motivations may conflict with each other.

Example:

```markdown
### Primary motivation
Protect the people assigned to their care.

### Internal conflict
Wants to respect procedure but increasingly believes that procedure is failing those people.
```

## Strengths and weaknesses

Strengths and weaknesses should be actionable in scenes.

Good weaknesses:

- avoids asking for help
- confuses control with safety
- prioritizes short-term rescue over long-term consequences
- overestimates their ability to remain emotionally detached

Avoid weaknesses that are merely disguised strengths unless the project intentionally uses them that way.

## Relationships

A character profile should contain concise relationship summaries.

Example:

```markdown
## Relationships

### Character B
Respects Character B's experience but resents their caution.
```

If the relationship is narratively important or develops across multiple phases, create a dedicated relationship file under `relationships/`.

The dedicated relationship file should become the primary source for relationship detail.

## Narrative function

This section explains the character's role in the story beyond biography.

Possible functions:

- protagonist
- antagonist
- foil
- mentor
- witness
- emotional anchor
- thematic counterpoint
- comic relief
- bridge between factions
- unreliable source of information

A character may fulfill several functions.

## Dialogue and voice

Record stable patterns rather than isolated example lines.

Possible dimensions:

- sentence length
- vocabulary
- formality
- humor
- emotional directness
- recurring phrases
- what the character avoids saying
- how their speech changes under stress

Sample quotes may be added when useful.

## Visual continuity notes

Use this section for recurring visual details that should be preserved across scenes and image generation.

Examples:

- always wears the same damaged glove
- left eye is artificial
- jacket remains oversized
- identification mark is visible on the right side
- damage from Issue 4 persists afterward

Temporary story-state details should include context or time range.

## Open canon points

Use this section for unresolved character-specific questions.

Example:

```markdown
## Open Canon Points

- exact birthplace
- identity of former mentor
- whether the character knows the truth about the accident
```

These items have status `OPEN`.

Any answer generated by a Skill remains `PROPOSAL` until accepted.

## Change workflow

When revising a character:

1. inspect the current profile
2. inspect relevant canon, relationship, and story files
3. identify requested changes
4. classify affected information using the canon-status model
5. check background, motivation, relationships, and narrative function for consequences
6. report conflicts
7. prepare a revised profile
8. summarize changes
9. archive or replace the previous version only after confirmation when required by project policy

## Character revision impact check

A substantial character change should trigger checks against:

- background history
- motivations
- fears
- strengths and weaknesses
- relationships
- story role
- timeline
- current or planned issue events
- visual continuity
- unresolved canon points

A Skill should not assume that changing one trait is isolated from the rest of the character.

## Visual references

Reference images may live under:

```text
characters/<character>/references/
```

Recommended filenames:

```text
front-view.png
side-view.png
expression-sheet.png
costume-a.png
equipment-reference.png
```

Projects may use different naming conventions.

Visual references should be treated as evidence for appearance, not automatically for biography or personality unless the project explicitly says so.

## Notes and unstructured input

Free-form notes may be used as input to a Character Developer Skill.

The Skill should:

- extract useful facts
- classify them by status
- avoid silently promoting uncertain notes to canon
- integrate accepted material into the correct profile sections
- preserve ambiguity when the notes are ambiguous

## Source-of-truth principle

For a character:

- `profile.md` is the default current source of truth
- dedicated relationship files are authoritative for detailed relationship dynamics
- `canon/` overrides contradictory character assumptions when it contains an established project-wide rule
- story plans remain proposals unless promoted according to project policy
- Git history records how the character changed over time

## Compatibility requirement for Skills

A reusable Character-related Skill should:

- accept Markdown profiles, images, character sheets, and free-form notes
- preserve the project language
- respect existing headings when practical
- not force this exact template when the project already has a coherent structure
- detect missing or conflicting information
- clearly distinguish CANON, INFERENCE, PROPOSAL, CONFLICT, and OPEN
- ask before destructive replacement or archive operations
- report downstream impacts of major character revisions

## Version

Standard version: `v1`
