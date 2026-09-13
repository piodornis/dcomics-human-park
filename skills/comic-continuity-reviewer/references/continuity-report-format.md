# Continuity Report Format

Use this format for substantial reviews. Adapt it for smaller focused checks.

```markdown
# Continuity Review — [scope]

## Summary

- Scope reviewed: ...
- Sources reviewed: ...
- Overall status: Clear / Needs attention / Blocking issues found
- Findings: X blocking, X major, X minor, X notes

## Priority Findings

### [BLOCKING] C-001 — Short title

**Category:** Timeline / Character / Visual / Prop / Relationship / World / Setup-Payoff

**Affected:** Character, issue, scene, prop, etc.

**Evidence:**
- Source A: ...
- Source B: ...

**Why this conflicts:**
...

**Correction direction:**
...

**Canon status:** CONFLICT / OPEN / INFERENCE

## Minor Findings

### [MINOR] C-002 — Short title
...

## Open / Ambiguous Items

- Item that cannot be decided from available sources.

## Continuity State Changes

Optional concise list of important outgoing states for the next issue or scene.

## Recommended Handoffs

- Canon Guardian: ...
- Issue Writer: ...
- Storyboard Director: ...
```

## Finding IDs

Use stable IDs within one report:

- `C-001`
- `C-002`
- `C-003`

Do not imply that IDs are globally permanent unless the project adopts that convention.

## Small focused review

For one page or scene, a compact table is acceptable:

| Severity | Category | Finding | Evidence | Suggested direction |
|---|---|---|---|---|

Follow the table with `OPEN` items if needed.

## Clean review

When no material issues are found:

```markdown
## Result
No material continuity conflicts found in the reviewed scope.

## Open items
- ...

## Continuity reminders
- ...
```

Do not invent findings to make the report appear more useful.
