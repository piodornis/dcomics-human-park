# Hier das bisherige Comic-Beispiel ablegen

Status: RECEIVED, 2026-09-17. INDD, IDML, Assets und Referenz-PDF sind eingegangen. Technischer Ersteingang siehe [intake.md](intake.md); vollständige Link-/Fontprüfung ausstehend.

## Was wohin gehört

| Ordner/Datei | Inhalt |
|---|---|
| `package/` | Das bisherige InDesign-Paket mit INDD, optional IDML und ursprünglicher Unterstruktur, insbesondere Links; interne Dateinamen unverändert lassen |
| `reference-pdf/` | Das damalige Druck-PDF, bei Bedarf zusätzlich ein Ansichts-PDF |
| `printer-specs/` | Damalige Druckvorgaben und vorhandene Exportvorgaben wie JOBOPTIONS; mit Dienstleister und Datum |
| `intake.md` | Kurze Angaben zum Beispiel und zu fehlenden Bestandteilen |

Ein vorhandenes vollständiges Paket ist ideal. Falls nur INDD/IDML und PDF vorliegen, diese trotzdem ablegen und fehlende Bilder/Schriften in `intake.md` vermerken. Schriften nur mit passender Lizenz weitergeben; Adobe-Fonts-Nutzung und genaue Fontnamen andernfalls dokumentieren. Alte Druckparameter dienen als Referenz und gelten nicht automatisch für das neue Heft.

## Nach der Ablage

1. Bestand mit Dateinamen und Revision/Prüfsummen erfassen; Original erhalten.
2. Arbeitskopie unter dem Layoutordner der Ausgabe anlegen.
3. InDesign-Version, Verknüpfungen, Schriften, Seitengeometrie, Ebenen und Formate prüfen.
4. Erzählerkästen, Sprechblasen, Ausläufer, Umbrüche und Sonderzeichen anhand des PDFs vergleichen.
5. Nutzbare Konventionen dokumentieren; daraus Vorlage und erst anschließend Importskript entwickeln.

Adobe beschreibt das Verpacken samt optionaler IDML-/PDF-Ausgabe in der [Dokumentation](https://helpx.adobe.com/de/indesign/desktop/print/preflight/package-files-for-output.html). Die Paketfunktion ersetzt keine Prüfung des Inhalts.
