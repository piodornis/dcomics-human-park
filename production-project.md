# Human Park — Production Project

- Vertrag: `comic-production-standard-v0.1-draft`
- Kompatibilität: `comic-project-standard-v1`, `comic-design-standard-v1`
- Stand: 2026-09-16; Planungsstatus: DRAFT
- Sprache: Deutsch
- Autorisierung: Start der Produktionsplanung für Ausgabe 1. Zwei ganze Innenanzeigen sind ausdrücklich gewünscht; 24 Seiten werden als Pilotumfang angesetzt. Keine weitergehende Freigabe von Format, konkreter Belegung, Seitenadaption oder finalen Bildern daraus ableiten.

## Einstieg und Zuständigkeiten

[Projekt](project.md), [Design](design-project.md), [Arbeitsübersicht](work-status.md).
[Ausgabe 1 — Produktionsplan](production/issues/issue-001/production-plan.md).
[Storyboardentwurf Revision 2](issues/issue-001/storyboard.md): 16 Storyseiten, 73 Panels; texttreuer Inszenierungsvorschlag, Annahme OPEN. [Seitenübersicht](issues/issue-001/seitenuebersicht.md).

Production führt Format, physische Seiten, Panelbudgets und Anzeigenreservierungen. Story führt Text, narrative Seiten-/Panelabsicht und Dramaturgie. Design führt visuelle Identität und Referenzfreigaben. Das veröffentlichte Prosaskript bleibt unverändert.

## Vorläufige Arbeitswerte (PROPOSAL)

- Profil `us-modern-metric`, Version 0.1: Endformat 170 × 260 mm.
- Beschnitt: 3 mm je Außenkante; Dateiumfang 176 × 266 mm.
- Sicherheitsabstand: 10 mm innerhalb des Endformats je Seite; Safe Area 150 × 240 mm.
- Quelle: `comic-framework-production/format-profiles/README.md`, bereitgestellte metrische Anforderungen; keine Mischung mit der abweichenden Zollvariante.
- Leserichtung: links nach rechts.
- Bindungsvorschlag: Rückendrahtheftung; Seitenvielfaches 4.
- Panelziel: 5 pro Storyseite, bevorzugter Bereich 3–6; begründete Ausnahmen zulässig.
- Druckereibestätigung: OPEN; Farbe, Profil, Auflösung und Liefer-PDF bleiben OPEN.

Dies sind veränderbare Planungsannahmen. Umfang und Anzeigenbelegung werden je Ausgabe entschieden; Ausgabe 1 setzt keinen festen Umfang für die Serie.

## Pfade und Versionierung

`production/issues/<issue-id>/production-plan.md` enthält die jeweilige effektive Konfiguration und physische Seitenzuordnung. `source-register.md` daneben dokumentiert den gelesenen Quellstand und Absatzanker. Geänderte Quellen lösen einen Abgleich aus; keine automatische Neuberechnung mit stiller Inhaltsänderung.

Framework-Stand beim Start: `comic-framework-production` Commit `63e54b7aabf1b2ebc00e0c13fb601182269a3214`. Ergänzt im aktuellen Arbeitsstand um das 24-Seiten-Beispiel und Prosa-Intake. Der Entwurf ist kein installierter Production-Skill und kein Druckexport.

## Satz- und Druckworkflow — Vorbereitung 2026-09-17

InDesign ist die vorgesehene Endstation für editierbares Lettering und Druckexport. [Produktionsübersicht](production/README.md), [Arbeitsablauf](production/workflow.md), [InDesign-Konventionen](production/indesign/README.md) und [Pilot Ausgabe 1](production/issues/issue-001/pilot/README.md) ergänzen die vorhandene Planung. Das bisherige Comic-Paket wird später unter [production/references/previous-comic/](production/references/previous-comic/README.md) bereitgestellt. Satz-, Asset-, Änderungs- und Prüfvorlagen sind angelegt; native Vorlage, Importskript und PDF-Erstellung folgen nach Beispielsichtung.

Die neuen Unterordner sind eine projektspezifische Ergänzung des v0.1-draft-Frameworks. Story führt den Wortlaut, InDesign die endgültige Platzierung; Satzkorrekturen werden dokumentiert rückgeführt. Bestehende Formatwerte, physische Belegung und Story-/Designfreigaben behalten ihren Status.
