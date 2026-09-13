# Continuity Review Protocol

## Contents

- [1. Establish authority and scope](#1-establish-authority-and-scope)
- [2. Build a continuity ledger](#2-build-a-continuity-ledger)
- [3. Review in causal order](#3-review-in-causal-order)
- [4. Check character continuity](#4-check-character-continuity)
- [5. Check relationship continuity](#5-check-relationship-continuity)
- [6. Check timeline continuity](#6-check-timeline-continuity)
- [7. Check object and environment continuity](#7-check-object-and-environment-continuity)
- [8. Check visual continuity](#8-check-visual-continuity)
- [9. Check dialogue continuity](#9-check-dialogue-continuity)
- [10. Check setup/payoff continuity](#10-check-setuppayoff-continuity)
- [11. Classify certainty](#11-classify-certainty)
- [12. Classify severity](#12-classify-severity)
- [13. Suggest minimal repairs](#13-suggest-minimal-repairs)
- [14. Do not conflate review with revision](#14-do-not-conflate-review-with-revision)

## 1. Establish authority and scope

Identify which files represent the current project state. Prefer live project files over `archive/`. Respect project-defined precedence when synopsis, outline, script, storyboard, and continuity notes differ.

If precedence is unspecified, report discrepancies instead of guessing which file wins.

## 2. Build a continuity ledger

For the reviewed scope, track only material details that can persist or change.

Useful ledger fields:

| Entity | Attribute | Source | State | Effective point | Expected persistence |
|---|---|---|---|---|---|
| Character A | left-hand injury | Issue 2 p8 | injured | after p8 | until healed |
| Prop X | possession | Issue 2 p10 | held by B | after p10 | until transferred |

Do not expose the full internal ledger unless it helps the user. Use it to reason consistently.

## 3. Review in causal order

Prefer chronological or reading order rather than filename order.

Check:

1. incoming state
2. scene changes
3. outgoing state
4. next appearance

For non-linear stories, distinguish story order from chronological order.

## 4. Check character continuity

Review:

- physical condition
- knowledge
- goals
- emotional state when explicitly established
- promises and obligations
- inventory and equipment
- costume state
- location
- relationships

Do not report normal emotional variability as an error.

## 5. Check relationship continuity

Track relationship state changes such as:

- trust gained or lost
- authority shifts
- secrets revealed
- betrayals
- alliances
- promises
- unresolved conflicts

Compare dialogue and behavior to the most recent established relationship state.

## 6. Check timeline continuity

Look for:

- impossible travel time
- reversed event order
- inconsistent ages or durations
- healing that occurs too quickly without explanation
- repeated "first" events
- overlapping presence in incompatible locations
- day/night mismatches

Use `OPEN` when timing is underspecified rather than manufacturing exact dates.

## 7. Check object and environment continuity

Track meaningful props and environmental state:

- possession
- damage
- destruction
- repair
- opening/closing
- activation state
- placement
- depletion

Ignore trivial background-object variation unless it affects comprehension or story logic.

## 8. Check visual continuity

When visual references exist, compare stable design anchors and scene-specific state.

Stable anchors may include:

- silhouette
- major markings
- permanent scars
- identification labels
- prosthetics
- recurring equipment

Scene-specific states may include:

- dirt
- blood
- temporary damage
- wet clothing
- carried props
- lighting condition

Distinguish intentional stylistic variation from continuity-breaking change.

## 9. Check dialogue continuity

Look for statements that reveal impossible knowledge, contradict previous facts, misname entities, or reset a relationship/event as though it had not happened.

Different wording is not a continuity error.

## 10. Check setup/payoff continuity

Maintain a light registry of important setups.

Useful states:

- introduced
- reinforced
- transformed
- paid off
- intentionally unresolved

Flag orphaned setups only when the reviewed scope or project plan indicates a payoff should already have occurred.

## 11. Classify certainty

Use:

- confirmed discrepancy
- likely discrepancy
- ambiguous/open

A strong review is conservative. Prefer fewer well-supported findings over speculative noise.

## 12. Classify severity

Use:

- BLOCKING
- MAJOR
- MINOR
- NOTE

Severity reflects reader/story impact, not how easy a fix is.

## 13. Suggest minimal repairs

Prefer the smallest correction that restores continuity while preserving approved intent.

If multiple fixes are possible, present options and note which upstream area each would affect.

## 14. Do not conflate review with revision

Standard continuity review ends with findings and correction directions.

Only enter revision mode after an explicit request.
