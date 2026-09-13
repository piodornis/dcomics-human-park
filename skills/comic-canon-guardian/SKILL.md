---
name: comic-canon-guardian
description: Review a comic project for canon consistency across project metadata, canon, characters, relationships, locations, factions, story plans, and issues. Use for repository-wide canon audits or focused checks of a proposed scene, character change, relationship change, timeline event, world rule, story beat, or revision against established project facts and source-of-truth rules. Do not use as the primary tool for panel-to-panel, scene-to-scene, prop, wardrobe, injury, spatial, or visual-state continuity; route those implementation checks to Comic Continuity Reviewer. Produce read-only reports using CANON, INFERENCE, PROPOSAL, CONFLICT, and OPEN, identify contradictory sources and affected areas, and suggest resolution options without silently changing canon or editing project files.
---

# Comic Canon Guardian

## Framework compatibility

Treat this Skill as compatible with **Comic Project Standard v1** (`comic-project-standard-v1`). Apply explicit project-specific conventions when they intentionally override framework defaults, and do not silently assume behavior from a newer framework contract.

Review comic-project material for **canon consistency and source-of-truth conflicts** while preserving uncertainty, source boundaries, and creator authority.

Operate read-only by default. Do not edit, move, archive, delete, commit, or push project files.

## Scope decision

1. If the user clearly requests a focused check, inspect only the requested material plus the minimum related files needed for validation.
2. If the user clearly requests a repository-wide audit, inspect the complete relevant repository structure.
3. If scope is ambiguous and substantially changes the amount of work, ask whether to run a focused check or a repository-wide audit.
4. Prefer `project.md` as the project entry point when present. Respect project-specific path overrides and existing structures.
5. If the request is primarily about concrete execution continuity across panels, scenes, props, injuries, wardrobe, staging, or visual references, defer to Comic Continuity Reviewer instead of broadening this skill into an implementation continuity pass.

## Canon status model

Use exactly these states:

- `CANON` — explicitly established project fact.
- `INFERENCE` — logical conclusion supported by canon but not explicitly confirmed.
- `PROPOSAL` — new creative suggestion not yet accepted.
- `CONFLICT` — contradiction between authoritative statements or between a proposal and established canon.
- `OPEN` — intentionally unresolved question or decision.

Never promote `INFERENCE` or `PROPOSAL` to `CANON` without explicit creator confirmation.
Never resolve a `CONFLICT` silently.

For detailed classification and edge cases, read `references/canon-review-protocol.md`.

## Repository review workflow

1. Discover the project structure.
   - Read `project.md` first when available.
   - Identify relevant directories such as `canon/`, `characters/`, `relationships/`, `locations/`, `factions/`, `story/`, `issues/`, and `style/`.
   - Do not assume every directory exists.
2. Establish source priority.
   - Treat explicit project-wide canon rules as authoritative for global facts.
   - Treat current character profiles as authoritative for character-specific facts unless overridden by confirmed project-wide canon.
   - Treat dedicated relationship files as authoritative for detailed relationship dynamics.
   - Treat story plans as plans, not confirmed events, unless the project marks them as canon.
   - Treat old or archived versions as historical context, not current canon, unless explicitly restored.
3. Extract only relevant claims.
   - Record the claim, source file, and status when stated or inferable.
   - Preserve ambiguity instead of normalizing it away.
4. Cross-check dependencies.
   - chronology and ages
   - identity and naming
   - character history and motivation
   - relationships and loyalties
   - world rules and technology limits
   - locations and travel constraints
   - faction membership and authority
   - injuries, equipment, appearance, and persistent state
   - setups, payoffs, and issue-to-issue continuity
5. Classify findings.
6. Report conflicts with exact source references or file paths when available.
7. Suggest resolution options without selecting one unless the user asks for a recommendation.
8. Identify downstream areas likely to require re-checking after a canon change.

## Focused review workflow

For requests such as "check this scene against canon" or "does this character revision break anything?":

1. Identify the changed or proposed claims.
2. Locate the smallest set of authoritative files needed to validate them.
3. Compare each claim against established facts and open questions.
4. Distinguish contradiction from mere absence of evidence.
5. Produce a compact review report.

Do not turn an unspecified detail into a conflict. Missing information is usually `OPEN`, not `CONFLICT`.

## Conflict rules

Report a `CONFLICT` only when two claims cannot both remain true under the current interpretation.

For every conflict, include:

- conflicting claim A
- source of claim A
- conflicting claim B
- source of claim B
- why they conflict
- severity
- affected files or story areas
- possible resolution options

Use severity levels:

- `BLOCKING` — breaks identity, chronology, core world rules, or a major established event.
- `MAJOR` — materially changes motivation, relationship, plot logic, or persistent state.
- `MINOR` — local continuity discrepancy with limited downstream effect.
- `NOTE` — ambiguity or weak inconsistency worth tracking but not yet a contradiction.

## Source discipline

Do not silently fill gaps with genre conventions or general knowledge.
Do not treat generated prose as canon merely because it sounds definitive.
If two files differ and authority is unclear, report the ambiguity as `OPEN` or `CONFLICT` depending on whether both claims can coexist.
If a file is explicitly marked draft, proposal, deprecated, or archived, preserve that status.

## Output format

For a focused check, use:

```markdown
# Canon Review

## Scope
[What was checked]

## Result
[Consistent / conflicts found / insufficient canon]

## Conflicts
### [Short title]
**Severity:** BLOCKING | MAJOR | MINOR | NOTE
**Claim A:** ...
**Source:** ...
**Claim B:** ...
**Source:** ...
**Why this conflicts:** ...
**Resolution options:**
1. ...
2. ...

## Open Questions
- ...

## Inferences
- ...

## Downstream Checks
- ...
```

For a repository-wide audit, add:

```markdown
## Coverage
- canon: checked / missing / partial
- characters: checked / missing / partial
- relationships: checked / missing / partial
- story: checked / missing / partial
- issues: checked / missing / partial

## Summary
- Blocking conflicts: N
- Major conflicts: N
- Minor conflicts: N
- Notes: N
- Open questions surfaced: N
```

Omit empty sections when that improves clarity.

For more output guidance, read `references/report-format.md`.

## Change requests after review

If the user asks to fix a conflict, first distinguish:

- changing canon,
- changing a draft/proposal,
- changing a character or relationship record,
- changing story execution while preserving canon.

Prepare suggested edits only after the user chooses a resolution path. Do not edit files as part of the default review workflow.

## Compatibility principles

Remain project-agnostic.
Preserve the project's language and terminology.
Respect existing file organization when coherent.
Use the shared Comic Project Standard when the project provides no stronger local convention.
