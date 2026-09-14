# Human Park — Arbeitsstand

Stand: 2026-09-14. Zentrale Arbeitsübersicht; kein Ersatz für Kanon, Designakten oder Konfliktberichte.

## Einstieg und nächster Schritt

Earth-Referenzen und Fundanlagen-Entwürfe sind im Repo übernommen. Raumskizze V2 ergänzt einen ehemaligen sechsten Stellplatz bei fünf vorhandenen Kammern; EXPLORATION / PROPOSAL. Nächster konkreter Schritt: **W-03 — Raumfolge, Leerplatz und Transportmaßstab abstimmen.** Commit und Push dieser Übernahme sind noch ausstehend.

Vor Wiederaufnahme [project.md](project.md), [design-project.md](design-project.md) und die Quellen des gewählten Eintrags lesen. Diese Übersicht beschreibt den geprüften Stand, keine laufenden Hintergrundaufträge.

## Nächste Arbeiten

W-01 und W-02 sind abgeschlossen; W-03 und W-04 führen Earth weiter. Weitere Stränge sind unabhängig davon aufgeführt. Zuständigkeiten bezeichnen Arbeitsrollen, keine gestarteten Agenten.

| ID | Arbeitsstand | Nächster Schritt / Ergebnis | Zuständigkeit | Quelle / Abhängigkeit |
|---|---|---|---|---|
| W-03 | Zur Abstimmung | Raumfolge, seitliche Wartung und Kammerplätze abstimmen. Kammerhülle, Transportmittel, Wendefläche und Türöffnungen zusammen prüfen. | Autor / Environment Designer; Story bei neuen Fakten | [Serienfaden](story/die-sechste-kryokammer.md), [Transportfunktion](issues/issue-002/script.md). Skizze ist nicht maßstäblich. |
| W-04 | Nach W-03 | Kryoraum als Innenansicht und Gegenansicht aus derselben Geometrie entwickeln. | Comic Environment Designer | Ein abgestimmter Grundriss ist Voraussetzung; keine sechste Person voraussetzen. |
| W-05 | Zur späteren Entscheidung | Zeitpunkt des ersten Hinweises auf die sechste Kammer und mögliche Einbindung in Heft 3, Beat 5, wählen. | Autor / Comic Story Architect | [Heft-3-Outline](issues/issue-003/outline.md), [Serienfaden](story/die-sechste-kryokammer.md). Bisher PROPOSAL. |
| W-06 | Offen, eigener Strang | Modulias Raumstudie: Maße/Kameras und Gestaltung am Original 01 weiter abgleichen; anschließend Nutzungsszene mit Modulia und B-73 prüfen. | Environment Designer / Character Designer | [Designrecord](design/environments/modulia-workspace/design.md), [Raumstudie](design/environments/modulia-workspace/geometry/raumstudie-v1/README.md), [Review](design/environments/modulia-workspace/reviews/environment-review-2026-09-14.md). Studie bleibt PROPOSAL / EXPLORATION. |
| W-07 | Modulare Frachter- und Beladungsentwürfe übernommen | Gesamtansicht mit gelben Türen, Container mit Haltevorrichtungen und drei alternative Beladungen SELECTED. Kryoeinbau EXPLORATION: Maßstab mit Earth-Kammerhülle, Entnahmeweg, Sicherung oberer Boxen und redundante Versorgung prüfen; B-21s Zugang/Versteck offen. | Environment Designer / Story | [Raumschiff-Designrecord](design/environments/biological-cargo-spacecraft/design.md), [Bildbestand](design/environments/biological-cargo-spacecraft/references/README.md). Tatsächliche Zuglänge OPEN. |
| W-08 | Offen, eigener Strang | Mars: Zugangshub aus Gegenrichtung, Wasserzellen im Detail und Pflanzenmaßstab neben Figuren testen. | Environment Designer / Style Director | [Mars-Designrecord](design/environments/mars/design.md). Kein finaler Lageplan, Bildstatus EXPLORATION. |

## Entscheidungen und bewusst offene Rätsel

Offene Fragen sind nicht automatisch Fehler oder Aufgaben, die sofort gelöst werden müssen.

| ID | Gegenstand | Behandlung | Maßgebliche Quelle |
|---|---|---|---|
| D-01 | Zugangsgeschichte, Tiefe, ursprünglicher Eingang und Verbindung zum Wartungsbereich | Vor konkreter Ortsausarbeitung entscheiden oder sichtbar als PROPOSAL belassen. | [Raumkonzept](<design/environments/earth-discovery-facility/references/plan/raumkonzept-v2.md>), [Story-Handoff](story/die-sechste-kryokammer.md) |
| D-02 | Inhalt, Verbleib und Vorgeschichte der sechsten Kammer; Wissen der Figuren | Bewusst OPEN halten. Fehlende Kammer bestätigt keine fehlende Person. | [Serienfaden](story/die-sechste-kryokammer.md), [Kanon](canon/series-bible.md) |
| D-03 | B-73s Entscheidung und weiterer Verlauf der Protokolllücke | Im Zuge der Heftplanung behandeln, nicht aus einem Design ableiten. | [Heft 3](issues/issue-003/synopsis.md) |
| D-04 | Große Vergessen, alte Aufnahme und Ursache der Kryokonservierung | Bewusst offene Serienmysterien; keine automatische Auflösung. | [Series Bible](canon/series-bible.md), [Timeline](canon/timeline.md) |

## Widersprüche und Designbefunde

Zentraler Index bestätigter narrativer Konflikte: **[canon/conflicts.md](canon/conflicts.md)**. Vollständige Befunde bleiben in ihren Fachdateien; diese Übersicht dupliziert keine Konfliktanalyse.

| ID | Verweis | Nächster Umgang |
|---|---|---|
| C-01 | [Offener Konflikt #1](canon/conflicts.md): Funktionsklassen-Doktrin und Wetter-/Unterhaltungs-KI-Präzedenzfälle; Details in [world-rules.md](canon/world-rules.md) | Story-/Autorenentscheidung bei Wiederaufnahme des Governance-Strangs. Bis dahin nicht als gesicherte Doktrin verwenden. |
| C-02 | [Designreview Modulias Arbeitsplatz](design/environments/modulia-workspace/reviews/environment-review-2026-09-14.md) und [anschließende Raumstudie](design/environments/modulia-workspace/geometry/raumstudie-v1/README.md) | Frühere Bildabweichungen gegen den späteren Studienstand prüfen. Fehlende Maße oder unterschiedliche Entwürfe nicht pauschal als Kanonwiderspruch behandeln; siehe W-06. |

## Earth-Artefakte im Repo

Die frühere externe Entwurfsserie ist mit relativen Links, Vorversionen und Promptprotokollen übernommen. Aktueller Status: [Earth-Designrecord](design/environments/earth/design.md), [Fundanlage](design/environments/earth-discovery-facility/design.md), [Stilleitfaden v0.3](design/styles/human-park-earth/style.md). Herkunft und Datei-Hashes: [Importmanifest](design/environments/earth/intake-manifest.json).

Aktuelle Raumskizze: [V2](design/environments/earth-discovery-facility/references/plan/fundanlage-raumskizze-v2.png), EXPLORATION; fünf vorhandene Kammern und ein leerer ehemaliger sechster Platz. Position und Spuren bleiben PROPOSAL. Zugang V2 bleibt SELECTED.

Die ausgewählten Bilder und drei angenommenen Regeln bestätigen keine neue Zugangsgeschichte, keine finale Raumgeometrie und keinen projektweiten Human-Park-Style-Pack. Detailstatus und Scope bei der Übernahme in den jeweiligen Designakten festhalten.

## Zuletzt abgeschlossen

| ID | Ergebnis | Nachweis |
|---|---|---|
| W-01 | Raumskizze V2 erstellt und visuell geprüft: fünf vorhandene Kammern, ein leerer ehemaliger sechster Platz; keine zusätzliche Person. Auswahl und Raumgeometrie bleiben offen. | [Designrecord](design/environments/earth-discovery-facility/design.md) |
| W-02 | Earth-Referenzen, Vorversionen, Stilregeln und Prompts ins Repo übernommen, Designakten angelegt und verknüpft. | [Earth](design/environments/earth/design.md), [Leitfaden](design/styles/human-park-earth/style.md) |
| E-01 | Frühere sechste Kryokammer als CANON ergänzt; fünf Gefundene bleiben unverändert. Wissensstand, Inhalt und Verbleib bleiben OPEN. | [Series Bible](canon/series-bible.md), [Timeline](canon/timeline.md), [Glossar](canon/glossary.md) |
| E-02 | Story-Faden angelegt und Heftnotizen ergänzt; möglicher Archivhinweis in Heft 3 bleibt PROPOSAL. Veröffentlichte Originalskripte nicht verändert. | [Serienfaden](story/die-sechste-kryokammer.md), [Heft-1-Notizen](issues/issue-001/continuity-notes.md), [Heft-3-Outline](issues/issue-003/outline.md) |
| E-03 | Arbeitsübersicht angelegt und ihre Funktion als Projektkonvention in project.md verlinkt. | [Projektkonventionen](project.md) |

## Pflege dieser Übersicht

- Bei Wiederaufnahme zuerst den gewählten Eintrag und seine Quellen prüfen. Neuere Fachakten haben Vorrang vor einer veralteten Zusammenfassung.
- Nach einem relevanten Arbeitsschritt, einer Entscheidung, Pause oder Übergabe: betroffene Zeile, nächsten konkreten Schritt, Abhängigkeit und Quellenverweis aktualisieren.
- Stabile IDs erhalten. Abgeschlossene Punkte mit Ergebnisverweis unter „Zuletzt abgeschlossen“ führen; Git bewahrt die Historie. Keine automatischen Commits oder Archivierungen.
- Arbeitsstände wie „Bereit“, „Offen“ oder „Abgeschlossen“ beschreiben nur Arbeit. Sie ändern weder CANON/OPEN/PROPOSAL noch EXPLORATION/SELECTED/APPROVED/LOCKED.
- Nur tatsächlich laufende Arbeit als laufend bezeichnen. Eine Pause ist kein technischer Blocker; „blockiert“ braucht eine benannte fehlende Voraussetzung.
- Neue Widersprüche nach der Projektkonvention in [canon/conflicts.md](canon/conflicts.md) verweisen. Bewusst offene Rätsel in den Story-Akten belassen.
- Ein Eintrag ist keine Ausführungsfreigabe für alle Folgeschritte und kein Erinnerungsauftrag. Den Umfang der aktuellen Autorenanweisung beachten.
