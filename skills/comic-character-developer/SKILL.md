---
name: comic-character-developer
description: Entwickle, erschaffe und überarbeite Comicfiguren auf Basis vorhandener Markdown-Charakterakten, Bilder oder Character Sheets, freier Notizen, einer Beziehungsdynamik sowie etablierter Welt- und Canon-Unterlagen. Verwenden, wenn eine bestehende Figur angepasst oder erweitert, aus einer Weltidee, einem bestehenden Setting oder einer Beziehungsidee eine neue passende Figur entwickelt, eine konsolidierte Charakterakte erzeugt, Hintergrundgeschichte, Beziehungen oder Motivationen auf Folgewirkungen geprüft, konkrete Szenenideen vorgeschlagen oder eine neue Figurenfassung für ein lokales bzw. Git-basiertes Comic-Repository vorbereitet werden soll. Bestehenden Kanon nicht stillschweigend überschreiben; CANON, INFERENCE, PROPOSAL, CONFLICT und OPEN unterscheiden und Archivierung alter Fassungen nur nach ausdrücklicher Bestätigung durchführen.
---

# Comic Character Developer

## Framework compatibility

Treat this Skill as compatible with **Comic Project Standard v1** (`comic-project-standard-v1`). Apply explicit project-specific conventions when they intentionally override framework defaults, and do not silently assume behavior from a newer framework contract.

## Ziel

Eine Figur als konsistente, versionierbare Einheit weiterentwickeln. Vorhandene Quellen zusammenführen, Änderungen gegen den bestehenden Charakterstand prüfen und eine aktualisierte Markdown-Charakterakte erzeugen, ohne ungeklärte Annahmen als Kanon auszugeben.

## Grundprinzipien

- Bestehende explizite Angaben als **CANON** behandeln.
- Logische, aber nicht ausdrücklich dokumentierte Schlussfolgerungen als **INFERENCE** kennzeichnen.
- Neue kreative Ergänzungen als **PROPOSAL** kennzeichnen.
- Widersprüche zwischen Quellen als **CONFLICT** sichtbar machen und nicht stillschweigend auflösen.
- Bewusst ungeklärte oder noch nicht festgelegte Punkte als **OPEN** kennzeichnen.
- Neuere Angaben nicht automatisch als richtiger ansehen als ältere; bei Konflikten Herkunft und Kontext berücksichtigen.
- Bilder und Character Sheets als visuelle Evidenz verwenden, aber sichtbare Merkmale nicht ohne Grund zu biografischen Fakten hochstufen.
- Bestehende Charakterakten niemals ungefragt löschen, überschreiben oder archivieren.
- Git-Commits, Pushes oder sonstige irreversible Repository-Aktionen nur auf ausdrücklichen Auftrag durchführen.

## Quellenpriorität

Wenn mehrere Quellen vorliegen, diese Reihenfolge als Ausgangspunkt verwenden und bei Konflikten transparent bleiben:

1. ausdrücklich als kanonisch bezeichnete Angaben
2. aktuelle Charakterakte
3. frühere Charakterakten
4. bestätigte Story-/Canon-Unterlagen
5. Character Sheets und Referenzbilder
6. freie Notizen des Nutzers
7. eigene Schlussfolgerungen oder kreative Vorschläge

Eine niedrigere Quelle darf eine höhere nicht stillschweigend überschreiben.

## Arbeitsablauf

### 1. Material erfassen

- Alle bereitgestellten Markdown-Dateien, Notizen und Bilder berücksichtigen.
- Bei einer neuen Figur auch relevante Welt-, Canon-, Fraktions-, Orts- und Story-Unterlagen als Constraints einbeziehen.
- Falls ein lokales Repository oder Projektordner verfügbar ist, die relevante aktuelle Charakterakte sowie direkt abhängige Dateien identifizieren.
- Nur zusätzliche Unterlagen laden, die für die konkrete Überarbeitung nötig sind.
- Falls keine bestehende Akte vorliegt, eine neue Akte nach `references/character-record-schema.md` anlegen.
- Wenn der Nutzer von einer Welt oder groben Weltidee aus startet, im **World-first-Modus** arbeiten: zuerst prägende Weltbedingungen, Rollen, Institutionen, Konflikte und Alltagszwänge extrahieren; daraus mehrere passende Charakteransätze als **PROPOSAL** entwickeln; erst nach Auswahl oder ausreichender Festlegung eine vollständige Charakterakte ausarbeiten.
- Wenn der Nutzer von einer Beziehung, Rivalität, Partnerschaft, Familienkonstellation oder anderen Dynamik aus startet, im **Relationship-first-Modus** arbeiten: zuerst Rollen, Perspektiven, Spannungen, gemeinsame Geschichte, Machtasymmetrien und emotionale Bedürfnisse der Beziehung extrahieren; daraus passende beteiligte Figuren als **PROPOSAL** entwickeln. Bereits bestehende Figuren als Constraints behandeln und nicht stillschweigend umschreiben. Beziehung und Figuren erst nach Auswahl oder ausreichender Festlegung in vollständige Akten überführen.

### 2. Ausgangsstand rekonstruieren

Vor Änderungen intern festhalten:

- bestätigte Identität und visuelle Konstanten
- Biografie und wichtige Lebensereignisse
- Persönlichkeit, Werte, Ängste und Bedürfnisse
- Ziele und Motivationen
- Beziehungen und Abhängigkeiten
- relevante Story-Funktion und offene Entwicklungen
- ungeklärte oder widersprüchliche Angaben

### 3. Änderungswunsch einarbeiten

- Explizite Nutzeränderungen als beabsichtigte neue Fassung behandeln.
- Prüfen, welche bestehenden Aussagen dadurch direkt oder indirekt betroffen sind.
- Keine zusätzliche Änderung erfinden, nur um Widersprüche bequem zu beseitigen.
- Wenn eine Anpassung Folgeentscheidungen erfordert, Optionen als **PROPOSAL** anbieten.

### 4. Abhängigkeitsprüfung durchführen

Jede Charakterüberarbeitung mindestens gegen folgende Bereiche prüfen:

**Hintergrundgeschichte**
- Passen Lebenslauf, Herkunft, Ausbildung, Beruf, prägende Ereignisse und zeitliche Reihenfolge weiterhin zusammen?
- Entstehen neue Ursachen oder Folgen durch die Änderung?

**Beziehungen**
- Verändern sich Nähe, Konflikt, Loyalität, Machtverhältnis oder gemeinsame Geschichte zu anderen Figuren?
- Müssen bestehende Beziehungsbeschreibungen angepasst werden?

**Motivationen und Psychologie**
- Passen Ziele, Bedürfnisse, Werte, Ängste, Widersprüche und Entscheidungen noch zusammen?
- Entsteht eine Motivation ohne plausible Ursache oder eine Ursache ohne sichtbare Wirkung?

**Visuelle Kontinuität**
- Stimmen wiederkehrende Merkmale mit Character Sheets und Referenzbildern überein?
- Änderungen an Alter, Verletzungen, Kleidung, Körpermerkmalen oder Accessoires auf Story-Folgen prüfen.

**Story-Folgen**
- Prüfen, welche bisherigen oder geplanten Szenen, Konflikte oder Character Arcs durch die Änderung betroffen sein könnten.
- Betroffene Punkte nennen, aber fremde Story-Dateien nicht automatisch umschreiben.

### 5. Status jeder neuen Information bestimmen

Für neue oder geänderte Inhalte genau einen der fünf gemeinsamen Zustände verwenden:

- **CANON**: vom Nutzer ausdrücklich bestätigt oder bereits verbindlich festgelegt
- **INFERENCE**: starke Schlussfolgerung aus bestehendem Material, aber noch nicht bestätigt
- **PROPOSAL**: neu entwickelte kreative Möglichkeit
- **CONFLICT**: Aussage oder Änderung, die mit bestehendem verbindlichem Material unvereinbar ist
- **OPEN**: bewusst ungeklärter oder noch nicht entschiedener Punkt

Niemals INFERENCE, PROPOSAL oder OPEN automatisch zu CANON machen. CONFLICT niemals stillschweigend auflösen.

### 6. Neue Charakterakte erzeugen

Die aktualisierte Akte nach `references/character-record-schema.md` schreiben. Die Akte soll als eigenständige aktuelle Fassung lesbar sein und nicht nur ein Änderungsprotokoll enthalten.

Zusätzlich eine kompakte Änderungsübersicht ausgeben mit:

- bestätigten Änderungen
- Folgewirkungen auf Hintergrundgeschichte
- Folgewirkungen auf Beziehungen
- Folgewirkungen auf Motivationen
- offenen Konflikten oder Entscheidungen
- neuen PROPOSALs

### 7. Szenenideen nur als Vorschläge entwickeln

Wenn die Überarbeitung interessante erzählerische Konsequenzen erzeugt, bis zu fünf konkrete Szenenideen anbieten. Für jede Idee kurz nennen:

- dramatischer Zweck
- beteiligte Figuren
- welche Charaktereigenschaft oder Beziehung sichtbar wird
- Status: immer **PROPOSAL**, solange nicht bestätigt

Keine Szenenidee automatisch in die Charakterakte als kanonisches Ereignis übernehmen.

### 8. Archivierung vorbereiten

Wenn eine bestehende Akte ersetzt wird:

- den Nutzer fragen, ob die bisherige Fassung archiviert werden soll, sofern dies nicht bereits ausdrücklich beauftragt wurde;
- vor Zustimmung nichts verschieben oder löschen;
- nach Zustimmung eine nachvollziehbare Archivstruktur verwenden, bevorzugt `archive/characters/<character-id>/` oder die bereits vorhandene Repository-Konvention;
- Dateinamen mit Datum oder Versionskennung versehen, sofern das Projekt noch keine eigene Konvention vorgibt;
- die aktuelle Akte am etablierten Ort belassen.

Siehe `references/repository-workflow.md` für Repository-Regeln.

## Repository-Verhalten

Wenn ein lokales Git-Repository verfügbar ist:

- bestehende Ordner- und Dateinamenskonventionen zuerst erkennen und beibehalten;
- keine neue Repository-Struktur erzwingen, wenn bereits eine konsistente Struktur existiert;
- Änderungen möglichst auf die betroffene Charakterakte und explizit gewünschte Begleitdateien begrenzen;
- bei schreibenden Änderungen zuerst eine Vorschau oder klare Zusammenfassung der geplanten Änderungen liefern, sofern der Nutzer nicht ausdrücklich direkte Bearbeitung verlangt;
- keine Commits oder Pushes ohne ausdrücklichen Auftrag durchführen.

Wenn später GitHub als Connector oder Tool verfügbar ist, dieselben Freigaberegeln anwenden.

## Konfliktbehandlung

Bei Widersprüchen dieses Format verwenden:

**Konflikt:** kurze Beschreibung

**Quelle A:** Aussage + Herkunft

**Quelle B:** Aussage + Herkunft

**Auswirkung:** welche Bereiche davon betroffen sind

**Empfehlung:** bevorzugte Lösung, als PROPOSAL markieren

Bis zur Entscheidung beide Varianten als ungeklärt behandeln.

## Qualitätscheck vor Abschluss

Vor Ausgabe prüfen:

- Ist die neue Akte intern widerspruchsfrei?
- Sind alle expliziten Nutzeränderungen enthalten?
- Wurden Hintergrundgeschichte, Beziehungen und Motivationen geprüft?
- Sind visuelle Angaben mit bereitgestellten Bildern vereinbar?
- Sind CANON, INFERENCE, PROPOSAL, CONFLICT und OPEN sauber getrennt?
- Wurde nichts ungefragt archiviert, gelöscht, committed oder gepusht?
- Ist die Datei als aktuelle eigenständige Charakterakte nutzbar?

## Referenzen

- Für Aufbau und Pflichtfelder einer Charakterakte: `references/character-record-schema.md`
- Für lokale Repository-, Archiv- und Git-Regeln: `references/repository-workflow.md`
