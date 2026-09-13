# Story Architecture Protocol

## Contents

1. Context extraction
2. Scale selection
3. Causal story construction
4. Multi-thread planning
5. Character and relationship arcs
6. Setup and payoff management
7. Conflict handling
8. Revision workflow

## 1. Context extraction

Before proposing structure, identify:

- confirmed premise and world constraints
- current timeline position
- participating characters
- each relevant character's motivation and limitations
- important relationships
- active story questions
- prior setups
- known planned outcomes
- unresolved canon points

Do not treat every file equally. Distinguish current authoritative records from notes, drafts, and abandoned ideas.

## 2. Scale selection

Choose the planning scale requested by the user.

### Series / volume

Focus on large changes in story state. Do not overspecify scenes too early.

### Multi-issue arc

Define what each issue contributes to the larger movement. Each installment should alter pressure, knowledge, relationships, capability, or goals.

### Single issue

Define a complete dramatic movement while preserving links to the larger story.

### Character or relationship arc

Track internal or interpersonal state change across existing story structure.

## 3. Causal story construction

Build chains in the form:

```text
constraint or desire
    -> choice
    -> consequence
    -> new pressure
    -> harder choice
```

Prefer this over disconnected event lists.

For major turns, test whether removing the previous beat would break the next one. If not, causality may be weak.

## 4. Multi-thread planning

When using A/B/C plots, track each thread separately before interleaving them.

Example:

```text
A: rescue operation
A1 -> A2 -> A3 -> A4

B: conflict between two crew members
B1 -> B2 -> B3

C: mysterious equipment failure
C1 -> C2
```

Then identify intersections:

```text
A2 causes B2
B3 complicates A4
C2 becomes setup for next issue
```

Avoid secondary threads that could be removed without changing character, theme, tension, or future story.

## 5. Character and relationship arcs

### Character arc check

For each meaningful phase, record:

- state before
- pressure
- choice
- cost
- insight, denial, or reinforcement
- state after

Do not require explicit self-awareness for an arc to occur.

### Relationship arc check

For both participants, record:

- perception of the other
- level of trust
- dependency
- unresolved grievance or need
- power balance
- what changes after key scenes

Relationship development may be asymmetric.

## 6. Setup and payoff management

Track setup/payoff pairs explicitly when they matter to long-form continuity.

Recommended fields:

```markdown
### Setup
**Status:** PROPOSAL
**Introduced:** Issue 2
**Element:** Character hides a damaged access card.
**Visibility:** Low but legible.

### Payoff
**Planned:** Issue 5
**Function:** The card proves prior access to the restricted area.
**Dependencies:** Character must still possess it; no earlier scene may establish its destruction.
```

Flag orphaned setups and unsupported payoffs.

## 7. Conflict handling

When an attractive story move contradicts canon:

1. identify the exact contradiction
2. preserve the desired dramatic function
3. propose alternatives that achieve a similar function without conflict
4. optionally propose a deliberate canon revision as a separate option
5. never assume which option the creator chooses

Example:

```markdown
CONFLICT:
The proposed confrontation requires A to know the location of the bunker,
but current canon states A has never learned it.

PROPOSAL A:
Let B reveal the location under pressure.

PROPOSAL B:
Move the confrontation to a location A already knows.

PROPOSAL C — canon revision:
Establish an earlier scene in which A discovers the bunker.
```

## 8. Revision workflow

When restructuring existing story material:

1. preserve accepted goals and constraints
2. identify what is not working
3. distinguish structural problems from taste preferences
4. propose the minimum viable changes first
5. show downstream consequences
6. keep rejected or superseded ideas out of canon unless explicitly archived or retained as alternatives

Useful revision targets include:

- slow escalation
- repeated beats
- weak causality
- passive protagonist
- unsupported reversal
- unresolved setup
- overloaded issue
- character arc that changes without sufficient pressure
- climax that does not answer the story's central question
