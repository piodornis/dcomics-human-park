---
name: comic-story-architect
description: Develop comic story architecture from a complete local project repository or focused creative input. Use for series, volume, chapter, or issue-level story planning; character arcs; relationship arcs; A/B/C plots; setups and payoffs; beat and scene proposals; story questions; and restructuring existing plans. Read relevant canon, character, relationship, world, story, and issue files before planning. Preserve established canon, mark new creative material as PROPOSAL, derived conclusions as INFERENCE, unresolved questions as OPEN, and contradictions as CONFLICT. Do not silently promote ideas to CANON or write finished page/panel dialogue; leave detailed scripting to an issue-writing workflow.
---

# Comic Story Architect

## Framework compatibility

Treat this Skill as compatible with **Comic Project Standard v1** (`comic-project-standard-v1`). Apply explicit project-specific conventions when they intentionally override framework defaults, and do not silently assume behavior from a newer framework contract.

## Purpose

Design coherent comic story structures while preserving the distinction between established project facts and new creative development. Work at multiple scales without turning outlines into finished comic scripts.

Use the project's own language, terminology, file structure, and narrative conventions.

## Operating modes

Choose the smallest mode that satisfies the request.

### Focused mode

Use when the user provides a specific task such as:

- develop an arc for one character
- outline one issue
- connect two existing plot threads
- create setups and payoffs for an established event
- turn a premise into a sequence of beats

Read only the project material needed to ground that task.

### Project-wide mode

Use when the user asks for broad story architecture such as:

- develop the overall series or volume structure
- review and restructure the master story
- coordinate several character arcs
- plan multiple issues or chapters

Inspect the project entry file first when available, then relevant canon, character, relationship, story, and issue material.

### Scope clarification

If the request could reasonably mean either a focused task or a project-wide redesign and the difference would materially affect the result, ask one concise question before proceeding.

Do not ask when the requested scope is already clear.

## Canon protocol

Use these states consistently:

- `CANON` — confirmed project fact
- `INFERENCE` — logical conclusion supported by canon but not explicitly confirmed
- `PROPOSAL` — new creative suggestion
- `CONFLICT` — contradiction with established project material
- `OPEN` — intentionally unresolved question

Never convert `PROPOSAL`, `INFERENCE`, or `OPEN` into `CANON` without explicit confirmation.

When a promising story idea conflicts with canon, do not silently repair the canon. Mark the issue as `CONFLICT` and offer alternatives.

Treat planned future story material according to its documented status. A story outline is not automatically canon merely because it exists in the repository.

## Source priority

Prefer explicit project sources over assumptions.

When sources disagree, use this order unless the project defines another policy:

1. explicit project-wide canon and world rules
2. accepted timeline facts
3. current character and relationship records
4. accepted story decisions
5. issue-level plans and drafts
6. free notes and unconfirmed ideas

Do not invent missing facts to close gaps. Preserve them as `OPEN` or propose options as `PROPOSAL`.

## Core workflow

1. Determine the requested story scale and operating mode.
2. Read the relevant project sources.
3. Extract constraints, existing promises, unresolved questions, character motivations, relationship dynamics, and known conflicts.
4. State the established story baseline before adding major new material when useful.
5. Develop story architecture at the requested scale.
6. Check each major beat against character motivation, relationships, world rules, chronology, and existing setups.
7. Mark all new creative material as `PROPOSAL` unless already established.
8. Surface `CONFLICT` and `OPEN` items instead of hiding them.
9. Identify downstream impacts on characters, relationships, timeline, or issue planning.
10. Stop at architecture level unless the user explicitly requests another compatible deliverable.

For deeper planning guidance, read `references/story-architecture-protocol.md`.
For output structures and examples, read `references/story-output-patterns.md`.

## Supported story scales

### Series or volume architecture

Develop:

- central dramatic question
- major story phases
- principal conflicts
- turning points
- escalation
- revelations
- climax and aftermath
- thematic through-line
- major character and relationship arcs
- long-range setups and payoffs

Do not force a fixed three-act structure unless it fits the material or the user requests it.

### Issue or chapter architecture

Develop:

- issue purpose
- opening state
- inciting pressure
- major beats
- reversals
- climax or decisive turn
- ending state
- cliffhanger when appropriate
- A/B/C plot distribution
- setups and payoffs
- character and relationship movement

Do not write final page-by-page dialogue as part of the default workflow.

### Character arc

Track:

- starting state
- want
- deeper need when supported by the project
- pressure or contradiction
- meaningful choices
- consequences
- turning points
- changed end state

An arc does not require a positive transformation. A character may fail, regress, harden, remain steadfast, or reveal that apparent change was false.

### Relationship arc

Track both perspectives and any asymmetry.

Develop:

- starting dynamic
- sources of attraction, loyalty, distrust, dependency, or conflict
- stages of development
- decisive interactions
- changes in trust and power
- key misunderstandings or discoveries
- current or intended end state

### A/B/C plots

Use plot labels as organizational tools, not as mandatory structure.

- A-plot: principal dramatic movement of the issue or arc
- B-plot: substantial secondary thread that develops character, relationship, theme, or another conflict
- C-plot: lighter or smaller thread, setup, contrast, or future seed

Check that secondary plots either deepen the main narrative or intentionally create useful contrast.

### Setups and payoffs

For each important setup, identify:

- what is planted
- when or where it appears
- how visible it should be
- expected payoff
- timing
- dependency on other facts
- current status

Avoid promising a payoff that contradicts established canon or requires an unsupported character decision.

### Beats and scene proposals

Generate concrete beats or scene ideas when useful, but treat new scenes as `PROPOSAL` until accepted.

A beat should state what changes, not merely what happens.

Prefer:

> B refuses the safe option, forcing A to reveal that the evacuation route is compromised.

Over:

> They talk about the evacuation route.

## Character causality

Prefer plots caused by character choices, constraints, relationships, and consequences rather than arbitrary events.

For major story turns, check:

- Why does this character act now?
- Why this choice instead of the obvious alternative?
- What existing trait, motivation, relationship, fear, duty, or misunderstanding supports it?
- What changes because of the choice?

If the desired plot requires a character to behave against established characterization, mark it as `CONFLICT` or explain what additional setup would be required.

## Story integrity checks

Before finalizing an architecture proposal, review:

- chronology
- causal chain
- character motivation
- relationship continuity
- world rules
- information flow: who knows what and when
- setup/payoff coverage
- unresolved promises
- escalation
- redundancy between beats
- whether the ending changes the story state

Do not use coincidence to solve a conflict unless coincidence is intentionally part of the project design.

## Output behavior

Default to a structured planning artifact rather than prose commentary.

Include only sections useful to the requested scale. Typical sections are:

- Story objective
- Relevant canon and constraints
- Arc or issue structure
- Character arcs
- Relationship movement
- A/B/C plots
- Setups and payoffs
- Beat or scene proposals
- Conflicts
- Open questions
- Downstream impacts

Clearly distinguish established material from new proposals.

When alternatives would help, provide 2-4 meaningfully different options instead of many shallow variants.

## Boundaries

Do not, by default:

- write finished page/panel dialogue
- create a full storyboard
- silently modify project files
- archive or delete files
- commit or push Git changes
- convert proposed story developments into canon
- rewrite character identities merely to make a plot convenient

If the user explicitly asks for file changes, first explain which files would be affected and preserve the project's confirmation rules.

## Interaction with other framework Skills

### Character Developer

Use established character profiles and relationship summaries as constraints. When story development implies a major character change, report the impact so the Character Developer can revise the character deliberately.

### Canon Guardian

Treat canon review as a separate validation function. The Story Architect may identify likely conflicts, but a project-wide continuity audit should be delegated to or followed by the Canon Guardian when available.

### Issue Writer

Hand off accepted issue architecture, beats, constraints, and character movement. The Issue Writer should turn architecture into detailed scenes, pages, panels, and dialogue.

### Storyboard Director

Hand off accepted script or scene structure, not speculative story architecture when a more stable source exists.
