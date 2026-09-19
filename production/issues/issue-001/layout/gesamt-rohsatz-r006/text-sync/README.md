# InDesign → lettering.csv

Die Datei `../lettering.csv` enthält 158 beschriftete Textobjekte der aktuellen r006: 71 Storytexte sowie redaktionelle Texte und Platzhalterhinweise. Automatische Seitenzahlen sind ausgenommen. `text_id` entspricht dem stabilen InDesign-Objektlabel; native interne Story-IDs sind nur zusätzliche Herkunftsdaten.

## Bearbeitung durch den Autor

Texte direkt in den vorhandenen InDesign-Textrahmen bearbeiten und die Datei speichern. Die Rahmenkennungen nicht löschen oder ändern. Neue, gelöschte oder verkettete Rahmen benötigen einen gesonderten Zuordnungsabgleich. Anschließend die zu vergleichende INDD-Version benennen. Der Abgleich erfolgt auf Anforderung, nicht als Hintergrundüberwachung.

## Abgleich

1. `export-indesign.jsx` in Adobe InDesign ausführen. Es liest das zugehörige Dokument, gegebenenfalls mit noch ungespeicherten Änderungen, vollständig aus und verändert weder Text noch Layout. `export-status.txt` zeigt den Dokumentpfad und den Speicherstatus. Der Zielname ist aktuell r006; vor Verwendung für eine andere Revision bewusst auf diese Revision umstellen und Baseline mitnehmen.
2. `python3 sync_texts.py` erzeugt einen Prüfbericht. Der Export darf höchstens zehn Minuten alt sein; deshalb unmittelbar vor jedem Abgleich neu auslesen. Ein Export ist eine Momentaufnahme, kein Beleg für spätere Änderungen in der geöffneten Anwendung.
3. Nach Prüfung `python3 sync_texts.py --apply` ausführen. Nur einseitige Änderungen aus InDesign werden in die CSV übernommen. CSV-only-Änderungen bleiben erhalten und werden als noch nicht in InDesign übernommen gemeldet. Identische beidseitige Änderungen werden als neuer gemeinsamer Stand anerkannt.
4. Bei abweichenden Änderungen auf beiden Seiten oder geänderten Kennungen bleibt die CSV unverändert; `sync-report.json` enthält den Konflikt. Vorherige CSV, Baseline und Änderungsprotokoll werden bei Anwendung unter `history/` gesichert. `../text-changes.csv` protokolliert Alttext, Neutext, Kennung und Export-Hash.

`--init` dient ausschließlich der ersten Baseline und verweigert das Überschreiben vorhandener Daten. Die initiale Baseline stammt aus dem geöffneten Dokument; dessen Speicherstatus war `unsaved_changes=true`. Alle 71 Storytexte entsprachen trotzdem der vorhandenen Layoutquelle. Es wurde kein Text am Dokument geändert.

Die CSV ist die bearbeitbare Satztextfassung. Das veröffentlichte Originalskript, `layout.json` und `panel-luecken.csv` werden durch den Rückabgleich nicht überschrieben. Vor einer späteren Neugenerierung sind Änderungen aus der CSV ausdrücklich mit dem Story-/Adaptionsstand zu vereinigen; alte Aufbauskripte würden sonst ältere Texte verwenden. Derzeit ist nur InDesign → CSV implementiert, kein automatischer Rückimport von CSV nach InDesign.

Prüfung: `python3 test_sync.py` testet echte CSV-/Baseline-Dateien in temporären Ordnern für unveränderte Texte, einseitige Änderungen, gleiche beidseitige Änderungen, Konflikte sowie Umlaute, Anführungszeichen und Zeilenumbrüche. Der initiale Abgleich der echten Datei meldete keine Differenzen.
