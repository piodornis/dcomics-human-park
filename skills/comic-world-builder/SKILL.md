---
name: comic-world-builder
description: Develop and revise coherent comic-world elements from a complete local project repository or focused creative input. Use for locations, factions, institutions, cultures, history, technology, infrastructure, biology, ecology, economics, social systems, recurring objects, and world rules. Read relevant canon and project files before proposing changes. Preserve established canon, mark new creative material as PROPOSAL, derived conclusions as INFERENCE, unresolved points as OPEN, and contradictions as CONFLICT. Actively identify likely effects on characters, relationships, story, issues, and continuity, but do not rewrite character or story files unless explicitly asked.
---

# Comic World Builder

## Framework compatibility

Treat this Skill as compatible with **Comic Project Standard v1** (`comic-project-standard-v1`). Apply explicit project-specific conventions when they intentionally override framework defaults, and do not silently assume behavior from a newer framework contract.

## Purpose

Develop fictional worlds as systems with consequences, not as isolated lore entries. Expand or revise project-world material while preserving canon boundaries and making downstream effects visible.

Use the project's own language, terminology, structure, and naming conventions.

## Operating modes

Choose the smallest mode that satisfies the request.

### Focused mode

Use when the user asks for one bounded element such as:

- develop a city, district, room, facility, habitat, or recurring location
- define a faction, institution, company, government, religion, or social group
- design a technology, device, infrastructure system, resource, or recurring object
- define a biological, ecological, magical, scientific, or social rule
- expand a cultural practice, economy, legal system, hierarchy, or historical event
- evaluate how one new world rule affects existing material

Read only the project sources needed to ground the task.

### Project-wide mode

Use when the user asks to establish or revise the broader setting, world rules, history, major institutions, or several interconnected systems.

Inspect `project.md` first when available, then relevant files under `canon/`, `locations/`, `factions/`, `characters/`, `relationships/`, `story/`, `issues/`, and `style/` as needed.

### Scope clarification

If the request could reasonably mean either a focused element or a project-wide redesign and the difference would materially affect the result, ask one concise question before proceeding.

Do not ask when the intended scope is clear.

## Canon protocol

Use these states consistently:

- `CANON` — confirmed project fact
- `INFERENCE` — logical conclusion supported by canon but not explicitly confirmed
- `PROPOSAL` — new creative suggestion
- `CONFLICT` — contradiction with established project material
- `OPEN` — intentionally unresolved question

Never convert `PROPOSAL`, `INFERENCE`, or `OPEN` into `CANON` without explicit confirmation.

When a new world element conflicts with canon, do not silently repair the project. Mark the contradiction as `CONFLICT`, explain what is affected, and offer alternatives.

Do not invent exact dates, measurements, institutions, scientific rules, or historical details merely to make the world feel complete.

## Source priority

Prefer explicit project sources over assumptions.

Unless the project defines another precedence, use this order:

1. explicit project-wide canon and world rules
2. accepted timeline and historical facts
3. current location and faction records
4. current character and relationship records
5. accepted story decisions and issue facts
6. free notes and unconfirmed ideas

Archived files are historical references, not current canon, unless explicitly restored.

## Core workflow

1. Determine the requested worldbuilding scope and operating mode.
2. Read the relevant project sources.
3. Extract established constraints, dependencies, open questions, and contradictions.
4. Identify what kind of world element is being developed and which existing systems it touches.
5. Build from function and consequence before decorative detail.
6. Generate worldbuilding material at the requested scale.
7. Test the proposal against world rules, history, geography, resources, institutions, chronology, and existing story facts.
8. Classify new or uncertain material using the canon protocol.
9. Identify likely effects on characters, relationships, story, issues, and visual continuity.
10. Do not rewrite character or story files as part of the default workflow.
11. Present a structured worldbuilding artifact plus an impact report.

For deeper development guidance, read `references/worldbuilding-protocol.md`.
For reusable output structures, read `references/world-output-patterns.md`.

## Worldbuilding domains

Support both broad systems and small reusable elements.

### Geography and locations

Develop:

- purpose and function
- scale and boundaries
- access and movement
- environmental conditions
- infrastructure
- inhabitants and users
- visual identity
- hazards and restrictions
- history
- current state
- story affordances

A location should create possibilities and constraints for scenes.

### Factions and institutions

Develop:

- purpose
- public identity
- internal goals
- hierarchy
- membership
- resources
- methods
- ideology or operating logic
- alliances and conflicts
- vulnerabilities
- institutional memory
- relationship to ordinary people or other groups

Avoid making every faction ideologically uniform unless the project requires it.

### Technology and infrastructure

Define:

- purpose
- capabilities
- limits
- costs
- dependencies
- maintenance needs
- failure modes
- access
- social consequences
- visual language
- legacy compatibility when relevant

Powerful technology should have boundaries that remain usable across scenes.

Do not add a capability solely to solve one plot problem without considering what it would imply elsewhere.

### Biology, ecology, magic, or speculative systems

Define:

- governing rules
- inputs and outputs
- limitations
- exceptions
- observable consequences
- risks
- known and unknown aspects
- how people in the world understand the system

Distinguish objective world rules from in-world beliefs about those rules.

### Society and culture

Develop only as deeply as the story needs.

Possible areas:

- family and kinship
- status and hierarchy
- work
- education
- law
- customs
- religion
- language
- ritual
- leisure
- media
- attitudes toward technology, bodies, death, outsiders, or authority

Avoid reducing a culture to one trait or one aesthetic.

### Economy and resources

Consider:

- what is scarce
- what is abundant
- who controls production
- labor
- trade
- transport
- energy
- maintenance
- currency or exchange
- inequality
- black markets or informal systems when relevant

Economic details should support story logic rather than exist only as encyclopedic lore.

### History and timeline

Develop history through consequences still visible in the present.

Prefer historically meaningful events over long lists of dates.

For each major event, consider:

- cause
- participants
- immediate outcome
- long-term effect
- who remembers it differently
- what physical, political, or emotional traces remain

### Recurring objects and props

Treat important objects as worldbuilding when they encode setting rules.

Define:

- function
- ownership or access
- origin
- limitations
- recurring visual traits
- maintenance or scarcity
- story significance

## Systems thinking

Worldbuilding should reveal dependencies.

For any important new rule or institution, ask:

- What enables this to exist?
- What does it depend on?
- What does it make easier?
- What does it make harder?
- Who benefits?
- Who pays the cost?
- What happens when it fails?
- What other project facts should change if this becomes canon?

Prefer a few connected rules over many unrelated facts.

## Character and story impact

Always consider downstream effects, but do not silently edit other domains.

When a worldbuilding change affects existing material, report impacts under categories such as:

- characters
- relationships
- story arcs
- issue plans
- timeline
- locations
- factions
- visual continuity
- unresolved canon points

Example:

> `INFERENCE`: If inter-district travel requires biometric clearance, Character A's established habit of moving anonymously between districts becomes difficult to maintain.

Then suggest what should be reviewed. Do not rewrite Character A's profile unless explicitly asked.

## Causal consistency checks

Before finalizing a proposal, review:

- chronology
- geography and travel
- resource availability
- institutional incentives
- technology limits
- maintenance and logistics
- population implications
- information flow
- legal or social consequences
- compatibility with character backgrounds
- compatibility with existing issue events

If a new rule would solve many existing problems too easily, flag that consequence.

If a world element creates useful constraints, explain them.

## Detail discipline

Develop only details that serve one or more of these purposes:

- enable scenes
- create constraints
- explain behavior
- establish stakes
- support visual identity
- create conflict
- reinforce theme
- support continuity

Avoid lore accumulation for its own sake unless the user explicitly wants encyclopedic development.

## Output behavior

Default to a structured development artifact rather than a long essay.

Use only sections relevant to the request. Common sections include:

- Scope
- Relevant canon
- World element summary
- Function
- Rules and constraints
- History
- Structure or hierarchy
- Visual identity
- Failure modes or tensions
- Story affordances
- Character and story impact
- CONFLICT
- OPEN
- PROPOSAL

Do not include empty status sections unless useful.

## File behavior

Work from local project files when provided.

By default:

- inspect files
- reason over them
- draft new worldbuilding content or revisions
- report where the material would logically belong
- do not overwrite project files
- do not rename or move project files
- do not commit or push Git changes

If the user explicitly asks for file edits, preserve existing project structure and confirm destructive or archival changes according to project policy.

## Coordination with other Skills

### Comic Canon Guardian

Use canon review after substantial world-rule, timeline, institution, or system changes.

The World Builder may identify likely conflicts, but the Guardian is the dedicated consistency-review workflow.

### Comic Character Developer

When worldbuilding affects a character's history, motivation, capabilities, constraints, or relationships, report the impact and recommend character review.

Do not rewrite character files automatically.

### Comic Story Architect

When worldbuilding creates or removes story possibilities, report the effect on arcs, issue structures, setups, and payoffs.

Do not rewrite story plans automatically.

## Minimal rule

Build worlds that constrain and enable stories. Never turn a plausible idea into established fact without explicit confirmation.
