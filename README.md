# comic-story-framework

A reusable framework for developing comics with AI-assisted workflows and modular ChatGPT Skills.

The repository separates **general working logic** from **project-specific comic content**. Skills should be reusable across different comic projects, while characters, canon, stories, issues, locations, and visual references live in separate project repositories.

## Purpose

`comic-story-framework` is the source repository for reusable comic-development Skills, shared project schemas, and a starter project template.

The framework supports multiple creative entry points. A project may begin with a world, a character, a relationship, a story premise, or a more developed issue concept. The Skills are intended to converge those paths into one consistent project model rather than enforce one fixed creation order.

## Core principle

Keep **how work is done** separate from **what a specific comic contains**.

```text
comic-story-framework/
    reusable skills
    shared schemas
    project templates

comic-project/
    canon
    characters
    relationships
    locations
    factions
    story
    issues
    style
```

A reusable Skill defines a repeatable workflow. It should not embed the canon of a specific comic unless it is intentionally project-specific.

## Repository structure

```text
comic-story-framework/
├── README.md
├── skills/
│   ├── comic-character-developer/
│   ├── comic-canon-guardian/
│   ├── comic-story-architect/
│   ├── comic-world-builder/
│   ├── comic-issue-writer/
│   ├── comic-storyboard-director/
│   └── comic-continuity-reviewer/
├── schemas/
│   ├── project-structure.md
│   ├── canon-status.md
│   ├── character-schema.md
│   ├── relationship-schema.md
│   ├── issue-schema.md
│   └── archive-policy.md
└── templates/
    └── comic-project/
        ├── project.md
        ├── canon/
        ├── characters/
        ├── relationships/
        ├── locations/
        ├── factions/
        ├── story/
        ├── issues/
        ├── style/
        └── archive/
```

The structure may evolve as the framework is tested on real comic projects.

## Skill architecture

### Comic Character Developer

Creates and revises characters from character files, notes, visual references, or world/canon constraints. It checks biography, motivations, relationships, visual continuity, and downstream story impact. It can therefore be used **character-first**, **world-first**, and **relationship-first**.

### Comic World Builder

Develops locations, factions, institutions, technologies, cultures, history, ecology, infrastructure, and world rules. It reports impacts on characters and story without rewriting those files itself.

### Comic Canon Guardian

Checks whether claims, proposals, and revisions are compatible with the project's established canon and source-of-truth rules. It performs **canon consistency review**, while promotion to `CANON` remains a creator or explicitly authorized project decision. It is not responsible for detailed panel-to-panel continuity.

### Comic Story Architect

Develops series, volume, issue, character, and relationship arcs; A/B/C plots; setups and payoffs; beats; and scene proposals while preserving canon status.

### Comic Issue Writer

Turns an approved synopsis or outline into a comic script with pages, coarse panel structure, action, dialogue, captions, and sound effects.

### Comic Storyboard Director

Translates scripts or approved outlines into visual page and panel planning: staging, framing, pacing, composition, reading flow, and dialogue space.

### Comic Continuity Reviewer

Checks the **concrete execution** across scenes, pages, panels, issues, and visual references for narrative and visual continuity errors such as state, props, injuries, wardrobe, spatial layout, knowledge, and setup/payoff continuity.

## Shared canon states

All Skills use the same status model:

- `CANON` — confirmed project fact
- `INFERENCE` — logical conclusion derived from canon but not explicitly confirmed
- `PROPOSAL` — creative suggestion not yet accepted
- `CONFLICT` — incompatible statement or development
- `OPEN` — intentionally unresolved question or decision

A Skill must never silently promote `INFERENCE`, `PROPOSAL`, or `OPEN` to `CANON`, and must never silently resolve a `CONFLICT`.

## Multiple development paths

The framework is intentionally non-linear.

### World-first

Start with a setting or rough world idea:

```text
World idea
   ↓
Comic World Builder
   ↓
PROPOSAL / INFERENCE
   ↓
Canon Guardian review when useful
   ↓
Creator approval / status decision
   ↓
Character Developer
   ↓
Character PROPOSALs
   ↓
Canon Guardian review when useful
   ↓
Creator approval / status decision
   ↓
Story Architect
   ↓
Story PROPOSALs
   ↓
Canon Guardian review when useful
   ↓
Creator approval / scripting decision
   ↓
Issue Writer
   ↓
Storyboard Director
   ↓
Continuity Reviewer
```

The Character Developer should derive character proposals from world constraints such as institutions, social roles, technology, geography, history, scarcity, culture, and conflicts instead of inventing characters independently from the setting. The Canon Guardian may review compatibility, but it does not promote proposals to canon on the creator's behalf.

### Character-first

```text
Character idea / references
   ↓
Character Developer
   ↓
Character PROPOSALs
   ↓
Canon Guardian review when useful
   ↓
Creator approval / status decision
   ↓
World Builder and/or Story Architect
```

### Relationship-first

Start with a relationship, contrast, partnership, rivalry, family bond, or other interpersonal dynamic:

```text
Relationship idea / dynamic
   ↓
Character Developer
   ↓
Participant + relationship PROPOSALs
   ↓
Canon Guardian review when useful
   ↓
Creator approval / status decision
   ↓
Story Architect and/or World Builder
```

The Character Developer should derive the participating characters from the relationship's required roles, viewpoints, tensions, shared history, asymmetries, and emotional needs. Existing characters remain constraints rather than material to rewrite silently.

### Story-first

```text
Premise / story idea
   ↓
Story Architect
   ↓
Story PROPOSALs
   ↓
Canon Guardian review when useful
   ↓
Creator approval / status decision
   ↓
Character Developer + World Builder
```

These are entry paths, not rigid pipelines. Iteration between Skills is expected. A creative Skill may generate `PROPOSAL` or `INFERENCE` material, but only the creator or an explicitly authorized project workflow may promote it to `CANON`.

## Project repositories

Individual comics should live in separate repositories. A new project can begin from `templates/comic-project/`.

```text
my-comic/
├── project.md
├── canon/
├── characters/
├── relationships/
├── locations/
├── factions/
├── story/
├── issues/
├── style/
└── archive/
```

`project.md` should document project-specific conventions, including the preferred development entry point when useful and the project's threshold for when drafted story material becomes canon.

## Canon Guardian vs. Continuity Reviewer

Use the two review Skills for different questions:

```text
Canon Guardian
→ Is this statement, change, or proposal compatible with established project truth?

Continuity Reviewer
→ Is the concrete implementation consistent across scenes, pages, panels, and issues?
```

Examples:

- "Was Character A already employed by the agency at this date?" → Canon Guardian
- "The wrench moves from the right hand to the left hand between adjacent panels." → Continuity Reviewer

## Framework contract

The current compatibility target is **Comic Project Standard v1** (`comic-project-standard-v1`). Each Skill source declares this compatibility in its instructions. Project-specific conventions may intentionally override framework defaults, but a Skill must not silently assume behavior from a newer framework contract.

## Versioning and archive policy

Git is the primary version history for both the framework and individual comic projects.

Recommended principles:

- keep reusable Skills in this repository
- keep project-specific material in separate repositories
- review generated changes before committing them
- archive major superseded versions only when useful
- do not automatically commit or push unless explicitly requested
- treat `archive/` as historical reference, not current canon

See `schemas/archive-policy.md` for the detailed archive policy.

## Skill source vs. installed Skill

The editable Skill folders in this repository are the **source versions**. Package and install them into ChatGPT as needed.

```text
Repository source
      ↓
Validate / package
      ↓
Install in ChatGPT
```

When a Skill changes, update the source here first, then package and reinstall the updated Skill.

## Design guidelines

Skills in this framework should:

- remain focused on one responsibility
- avoid embedding project-specific canon
- preserve existing project structure where practical
- use the shared five-state canon model
- report downstream effects without silently rewriting another Skill's domain
- ask for confirmation before destructive or archival changes
- produce outputs that are easy to review in Git
- use shared schemas whenever consistency matters
- preserve the project's language and terminology

## Current status

The first complete core workflow is implemented:

1. `comic-character-developer`
2. `comic-world-builder`
3. `comic-canon-guardian`
4. `comic-story-architect`
5. `comic-issue-writer`
6. `comic-storyboard-director`
7. `comic-continuity-reviewer`

The next phase is end-to-end testing on one or more real comic projects and refinement based on observed workflow gaps. A later visual-production layer may be added after the text/storyboard workflow is stable.

## License

Add the appropriate license for your intended use before publishing or distributing the framework.
