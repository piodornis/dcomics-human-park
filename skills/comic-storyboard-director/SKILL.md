---
name: comic-storyboard-director
description: Plan and revise comic storyboards from scripts, outlines, scenes, project repositories, and visual references. Use for page and panel breakdowns, shot sizes, camera angles, staging, composition, eye flow, speech-balloon space, page turns, visual emphasis, and panel-by-panel image descriptions while preserving established story intent and canon. Supports full local comic projects and focused page or scene requests. Treat story-changing ideas as proposals instead of silently rewriting plot, dialogue, character behavior, or canon.
---

# Comic Storyboard Director

## Framework compatibility

Treat this Skill as compatible with **Comic Project Standard v1** (`comic-project-standard-v1`). Apply explicit project-specific conventions when they intentionally override framework defaults, and do not silently assume behavior from a newer framework contract.

Plan comic pages as readable visual sequences. Translate approved story material into panel-level staging without taking over story architecture, script rewriting, or final image generation.

## Core rules

- Preserve the approved story intent, character behavior, dialogue meaning, and canon.
- Treat `script.md` as the primary execution source when it exists; otherwise use the most authoritative approved outline or scene description.
- Use the project's own conventions before applying this skill's defaults.
- Use `CANON`, `INFERENCE`, `PROPOSAL`, `CONFLICT`, and `OPEN` consistently.
- Never silently solve a story problem by changing plot, dialogue, motivation, chronology, or world rules.
- Mark any meaningful story change required for visual clarity as `PROPOSAL` and explain why it may help.
- Report contradictions as `CONFLICT` rather than selecting one source without evidence.
- Do not edit character, relationship, story, or canon files as part of storyboard work unless explicitly asked.
- Do not commit, push, delete, move, archive, or rename repository files unless explicitly authorized.
- Do not generate final comic artwork unless the user separately requests image generation.

## Determine scope

1. Inspect the user's request and supplied material.
2. If the user names a page, scene, sequence, or issue, treat that as the working scope.
3. If a complete repository is supplied, inspect `project.md` first when available, then locate the relevant issue, script, style, character, location, and continuity files.
4. If the scope is materially ambiguous, ask whether to storyboard the full issue or only the relevant scene/pages.
5. Ignore archived material by default unless the user asks for historical comparison.

## Source priority

Prefer sources in this order unless the project defines another precedence:

1. explicit user instruction for the current task
2. approved or current `script.md`
3. approved issue outline or synopsis
4. project-specific `style/` guidance
5. current character, relationship, location, and canon files
6. free-form notes and visual references
7. reasonable inference

If two authoritative sources disagree, report a `CONFLICT`.

## Storyboarding workflow

1. Read the relevant story material before assigning panels.
2. Identify the dramatic purpose of each page or sequence.
3. Identify required story beats, dialogue load, reveals, actions, emotional turns, and continuity-sensitive details.
4. Decide the page rhythm before detailing individual panels.
5. Assign a practical panel count per page based on pacing and information density. Do not force a fixed count.
6. For each panel, specify both technical staging and a short natural-language image description.
7. Check eye flow, spatial clarity, character orientation, dialogue space, and page-turn logic.
8. Check that visual emphasis matches story importance.
9. Flag any necessary deviation from the script as `PROPOSAL`.
10. End with a compact continuity and production note when useful.

For deeper guidance, consult `references/storyboarding-protocol.md`.

## Panel specification

For each panel, include only information that helps execution. Use this default structure when appropriate:

```markdown
## Page 3

### Panel 1
- **Shot:** Medium wide
- **Angle:** Eye level
- **Staging:** Character A foreground left; Character B deeper right near the doorway.
- **Focus:** A notices the damaged device before B does.
- **Dialogue space:** Upper right, kept clear of faces and key action.
- **Image description:** A pauses beside the workbench while B enters in the background, unaware of the damaged device between them.
- **Purpose:** Establish the information imbalance before the exchange begins.
```

Omit fields that do not add value. Add fields such as `Movement`, `Lighting`, `Transition`, `Continuity`, or `Page-turn function` when needed.

## Technical staging guidance

Use comic-readable terms rather than cinematic jargon for its own sake.

Useful shot labels include:

- extreme wide / establishing
- wide
- medium wide
- medium
- medium close-up
- close-up
- extreme close-up
- insert / detail
- over-the-shoulder
- point of view

Useful angle labels include:

- eye level
- high angle
- low angle
- top-down
- ground-level
- profile
- three-quarter

Describe composition in spatial terms that an artist or image-generation workflow can understand.

Prefer clarity over novelty.

## Page rhythm and page turns

Treat the page as a unit of timing.

- Use fewer, larger panels for emphasis, scale, stillness, or emotional weight.
- Use more panels for procedural action, quick reactions, escalating detail, or compressed time.
- Reserve splash or near-splash treatment for moments that deserve visual dominance.
- Use page turns for reveals, reversals, arrivals, surprises, or changes in scale when the story benefits.
- Avoid placing a reveal before the turn if its impact depends on surprise.
- Do not create a dramatic page-turn beat where the script does not support one unless marked as `PROPOSAL`.

## Dialogue and balloon space

Preserve dialogue text unless the user asks for script revision.

While staging:

- estimate dialogue density before choosing panel size
- leave clean negative space for balloons and captions
- preserve speaker order in natural reading direction
- avoid placing key visual information where balloons must cover it
- flag overloaded panels instead of silently cutting dialogue
- if dialogue volume makes the intended layout impractical, report the issue and offer a `PROPOSAL`

## Character and location continuity

Use character sheets, visual references, location files, and style guidance when provided.

Check:

- relative character scale
- persistent clothing, damage, equipment, and props
- entrances and exits
- left/right orientation across sequential panels
- object positions that matter to action
- established location geography
- emotional state carried from the prior scene

Do not infer biography or personality from visual references unless project material supports it.

## Visual references

Treat supplied images as evidence for appearance, proportions, costume, equipment, location layout, or visual style.

When a visual reference conflicts with current written canon, report the discrepancy instead of choosing silently.

Do not convert an image reference into new canon beyond what is visibly supported.

## Story-change boundary

Storyboard choices may interpret presentation, but not redefine story facts.

Allowed without special approval:

- shot size
- angle
- staging
- panel count
- composition
- visual emphasis
- reaction inserts consistent with the script
- page-turn placement that preserves meaning

Normally require `PROPOSAL`:

- moving an event to another location
- changing who witnesses an event
- adding consequential actions
- deleting meaningful dialogue
- changing motivations
- changing the order of story beats when meaning changes
- inventing new plot information
- resolving an `OPEN` canon point

## Output modes

Choose the lightest format that satisfies the request.

### Full issue storyboard

Produce page-by-page and panel-by-panel planning suitable for `storyboard.md`.

### Scene storyboard

Storyboard only the requested scene and retain surrounding context as notes.

### Page revision

Preserve the existing story beat and propose a clearer or stronger panel arrangement.

### Visual pacing review

Review an existing storyboard for clarity, rhythm, page turns, eye flow, dialogue load, and continuity without rewriting it unless asked.

See `references/storyboard-output-patterns.md` for reusable formats.

## Final self-check

Before finishing, verify:

- every required story beat is represented
- no panel silently changes canon or character intent
- page and panel rhythm are purposeful
- dialogue has viable space
- action is spatially understandable
- page turns do not reveal information too early
- visual references are respected
- unresolved issues are labeled correctly
- story-changing suggestions are isolated as `PROPOSAL`
