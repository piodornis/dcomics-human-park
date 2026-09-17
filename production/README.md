# Produktion — Satz und Druck

Stand: 2026-09-17. Vorbereitung beauftragt; technische und gestalterische Werte bleiben bis zur Prüfung offen. InDesign ist die vorgesehene Endstation für editierbaren Satz und Druckexport. Noch keine INDD/IDML-Vorlage, kein ausführbares InDesign-Skript und kein Druck-PDF erstellt.

## Einstieg

- [Ablauf und Zuständigkeiten](workflow.md)
- [InDesign-Konventionen und Automatisierung](indesign/README.md)
- [Späteres Beispiel ablegen](references/previous-comic/README.md)
- [Satzdaten: Felder und Änderungsregeln](templates/README.md)
- [Druckvorgaben erfassen](templates/print-spec.md)
- [Prüfung und Druckfreigabe](checklists/print-release.md)
- [Pilot Ausgabe 1](issues/issue-001/pilot/README.md)

Die vorhandene [Produktionsplanung](../production-project.md) und der [Heftplan](issues/issue-001/production-plan.md) bleiben maßgeblich für Formatannahmen und physische Seiten. Diese Ergänzung ist eine projektspezifische Ablagestruktur zum Framework v0.1-draft, kein neuer Framework-Standard.

## Ablage

`references/previous-comic/` bewahrt das gelieferte Beispiel. `indesign/` führt Satzkonventionen. `templates/` enthält kopierbare Arbeitsvorlagen. Unter `issues/<issue-id>/` liegen künftig `lettering/`, `artwork/`, `layout/`, `exports/` und `reviews/` für die jeweilige Ausgabe.

Text und kleine Metadaten werden über Git versioniert. Vor Aufnahme großer INDD-, PSD-, TIFF- oder PDF-Dateien Repo-Größe und vorhandene Git-LFS-Konfiguration prüfen und eine Speicherstrategie festlegen. Git LFS wurde hier nicht aktiviert. Dateien nicht vorsorglich ausschließen: Ein im Repo abgelegtes Beispiel soll auffindbar bleiben. Schriften nur ablegen, wenn die Lizenz dies erlaubt; andernfalls Namen, Version und Bezugsquelle dokumentieren.
