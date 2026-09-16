# Comic Project

## Project identity

- **Title:** Human Park
- **Language:** Deutsch
- **Format:** Comic-Serie (Hefte)
- **Status:** Development
- **Bereits veröffentlicht/entworfen:** Human Park Nr. 1 – „Fünf Exemplare“, Human Park Nr. 2 – „Artgerechte Haltung“

## Development entry point

`mixed` — Projekt startete mit ausgearbeiteten Charakteren (character-first) und bringt gleichzeitig erhebliches Weltwissen/Story-Kanon mit (world-first-Anteile, siehe `canon/series-bible.md`).

## Project premise

Fünf Menschen (Mara, Jun, Salim, Liv, David) werden in intakten Kryokammern auf der verlassenen Erde gefunden und auf den Mars gebracht, wo eine KI-Gesellschaft mit eigener Verwaltung, Rechtsprechung und Wissensinfrastruktur existiert. Sie werden in einer Schutzanlage untergebracht, die sich schrittweise zum „Human Park“ entwickelt — einer Mischung aus Gefängnis, Zoo und Forschungsstation. Die Wissens-KI Modulia begleitet ihren Fall und entdeckt zunehmend Widersprüche im eigenen System — bis eine alte Aufnahme beweist, dass sie die fünf Menschen bereits vor den Ereignissen der Serie kannte und ihre Erinnerung bereits einmal zuvor verloren hat.

Vollständige Kanon-Zusammenfassung: `canon/series-bible.md`. Chronologie: `canon/timeline.md`. Begriffe: `canon/glossary.md`.

## Canon policy

Use the shared framework states:

- `CANON`
- `INFERENCE`
- `PROPOSAL`
- `CONFLICT`
- `OPEN`

### Canon threshold

Define when drafted material becomes canon for this project. Example: only after explicit creator approval. Canon Guardian may review compatibility, but review alone does not promote a `PROPOSAL` or `INFERENCE` to `CANON`.

## Paths

- Canon: `canon/`
- Characters: [Charakterübersicht](characters/README.md), Profile unter `characters/<id>/profile.md`; zugehörige Designakten unter `design/characters/<id>/design.md` und Bilder unter `references/`.
- Relationships: `relationships/`
- Locations: `locations/`
- Factions: `factions/`
- Story: `story/`
- Issues: `issues/`
- Style: `style/`
- Archive: `archive/`

## Work overview

See [work-status.md](work-status.md) for next actions, pending decisions, handoffs and links to unresolved conflicts. It is a project-specific coordination index, not a source of narrative canon or visual approval. Consult the linked domain records before resuming work; update the relevant entries after meaningful progress, decisions or handoffs.

## Project-specific conventions

Document deviations from the framework here rather than forcing generic Skills to guess.

- **`canon/conflicts.md`** (project-specific addition, not part of the standard schema): central index of all open/resolved `CONFLICT` entries, one line each, linking to the full write-up wherever it actually lives. Any Skill that finds or resolves a conflict should update this index.

## Framework reference

Reusable Skills, shared schemas, and the project template are maintained in the separate framework repository, not vendored into this project:

```
/Users/ralphdornis/Documents/GitHub/comic-framework-story
```

Compatibility target: `comic-project-standard-v1`.

## Production planning

Ausgabe 1 erprobt `comic-production-standard-v0.1-draft`. Einstieg: [production-project.md](production-project.md). Physische Seiten, Panelbudgets und Werbereservierungen liegen unter `production/issues/`; Originalskript und Kanon bleiben Story-owned. Der erste Plan vom 2026-09-16 ist DRAFT; Format, Umfang und Adaption sind noch nicht angenommen.

## Bildungsanspruch und redaktionelle Vertiefung

Autorenwunsch vom 2026-09-16: Human Park soll aktuelle Kenntnisse über LLMs, Agentic Development, KI allgemein, Modellkollaps und weitere Theorien vermitteln. Im redaktionellen Teil verweist das Heft auf vertiefende Informationen im Web oder in einer App. Reale Fachinformationen, Forschungshypothesen und die Fiktion werden klar getrennt. [Strategieentwurf](knowledge/README.md), [Hinweis für Heft 1](editorial/issue-001/wissen-hinter-der-geschichte.md). Das bestehende Kanonglossar bleibt der fiktiven Welt vorbehalten; Plattform und öffentliche Adresse sind noch offen.
