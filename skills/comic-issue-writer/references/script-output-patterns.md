# Script Output Patterns

## Contents

- [Default full-issue format](#default-full-issue-format)
- [Scene-oriented planning before panelization](#scene-oriented-planning-before-panelization)
- [Revision output](#revision-output)
- [Proposal separation](#proposal-separation)
- [Blocking conflict pattern](#blocking-conflict-pattern)
- [Balloon-conscious dialogue](#balloon-conscious-dialogue)
- [Captions](#captions)
- [SFX](#sfx)
- [Page-turn note](#page-turn-note)

## Default full-issue format

```markdown
# Issue 001 — Working Title

> **Script status:** Draft
> **Basis:** `outline.md`

## Page 1

### Panel 1
**Location:** ...
**Characters:** ...
**Action:** ...

**CHARACTER A:** ...

**CAPTION:** ...

**SFX:** ...

### Panel 2
**Action:** ...

**CHARACTER B:** ...
```

Omit empty metadata fields.

## Scene-oriented planning before panelization

Use this only as an intermediate step when needed:

```markdown
## Scene 1 — Service corridor

**Purpose:** Establish the disagreement.
**Entering state:** A and B are cooperating uneasily.
**Turn:** The repair method fails.
**Exit state:** A must accept B's help.
```

Then convert the accepted scene map into page-and-panel script form.

## Revision output

When revising an existing script, provide the revised script and then a compact summary:

```markdown
## Revision Summary
- Tightened dialogue on pages 2–3.
- Moved the reveal to the page turn between pages 5 and 6.
- Preserved the accepted ending.
- OPEN: source of the alarm remains undefined.
```

## Proposal separation

If a better result requires a major deviation, keep it outside the main accepted draft:

```markdown
## PROPOSAL — Alternate Beat

Instead of resolving the confrontation on page 8, delay the reveal until page 10.

**Benefit:** ...
**Cost:** ...
**Affected material:** ...
```

## Blocking conflict pattern

```markdown
## CONFLICT — Cannot draft this beat cleanly

**Outline says:** ...
**Canon says:** ...
**Why this conflicts:** ...

Possible resolutions:
1. ...
2. ...
3. ...
```

## Balloon-conscious dialogue

Prefer:

```markdown
**A:** I checked it twice.

**B:** Then check what you assumed.
```

over unnecessarily long exposition in a single balloon.

## Captions

Use captions intentionally for:

- location/time transitions
- narration
- internal narration when the project uses it
- information that cannot be conveyed efficiently through visible action or dialogue

Do not use captions merely to restate the panel.

## SFX

Use concise readable effects and preserve the project's language/style conventions.

Examples:

```markdown
**SFX:** KLANG
**SFX:** HSSSS
**SFX:** klick
```

## Page-turn note

When the reveal depends on the page turn, a compact production note is acceptable:

```markdown
> **Page-turn intent:** Do not reveal the figure before the next page.
```

This is structural guidance, not detailed camera direction.
