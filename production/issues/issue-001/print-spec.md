# Human Park 1 — erste Druckspezifikation für print24

Revision 1 · Recherche: 2026-09-17 · Status: DRAFT / keine Druckfreigabe.

Dienstleister print24 ist vom Autor gewählt. Arbeitsprodukt: Broschüre mit Klammerheftung. Die Angaben sind eine erste Spezifikation für das neue Heft, keine Rekonstruktion der damaligen Bestellung des Beispiel-Comics. Eine gespeicherte Produktkonfiguration mit produktspezifischem Datenblatt fehlt noch. Die konkrete Auftragsvorgabe hat Vorrang vor allgemeinen Webseiten und vor diesem Entwurf.

## Herkunft und Verbindlichkeit

- **BELEGT:** auf der angegebenen offiziellen print24-Seite recherchiert; noch keine Bestätigung einer konkreten Bestellung.
- **PROPOSAL:** Arbeitsentscheidung für Human Park, keine Druckereivorgabe.
- **OPEN:** vor verbindlichem Druckexport klären.

Quellen mit Abrufdatum, Geltungsbereich und Einschränkungen: [Quellenregister](../../printers/print24/sources-2026-09-17.md). Die folgenden Q-Verweise beziehen sich darauf.

## Produkt und Geometrie

| Merkmal | Erste Spezifikation | Status / Grundlage |
|---|---|---|
| Anbieter | print24, deutscher Shop | Autorenentscheidung |
| Produkt | Broschüre mit Klammerheftung, links gebunden | PROPOSAL; angebotene Produktart Q1 |
| Endformat geschlossen | 170 × 260 mm, Hochformat | Bestehender Projektvorschlag; genaues Sonderformat im gewählten Produkt noch bestätigen. Sonderformate grundsätzlich genannt: Q2 |
| Umfang | 24 bedruckte Seiten insgesamt: 20 Inhalt + 4 Umschlag | Projektvorschlag; Bestellung nicht versehentlich als 24 Inhalt + 4 Umschlag anlegen |
| Farbe | Inhalt und Umschlag beidseitig 4/4 CMYK | PROPOSAL; CMYK für Inhalte laut Q1 verfügbar; keine Sonderfarben bestellt |
| Inhaltspapier | 130 g/m² Bilderdruck matt als Startvorschlag | PROPOSAL; passende Papierart/-stärke laut Q1 angeboten; Auswahl und Kombination offen |
| Umschlagpapier | 250 g/m² Bilderdruck matt als Startvorschlag | PROPOSAL; Q2 nennt diesen Umschlag; Nutung berücksichtigen, Q1 empfiehlt sie ab 170 g/m² |
| Veredelung | Zunächst ohne Folie, Sonderlack oder Prägung | PROPOSAL, hält die erste Druckprobe einfach |
| Auflage | OPEN | Bestimmt konkrete Konfiguration und ggf. Druckverfahren |
| Beschnitt | 2 mm an den zu beschneidenden Seiten | BELEGT Q2; allseitige Export-/Bundbehandlung am konkreten Datenblatt bestätigen |
| Datenrechteck bei 2 mm an allen vier Kanten | 174 × 264 mm | Rechnerisch aus 170 × 260 mm; keine Aussage über zusätzlich geforderte PDF-Marken/MediaBox |
| Sicherheitsabstand für Lettering | 10 mm innerhalb des Endformats, Safe Area 150 × 240 mm | Bisheriger Projektvorschlag; bewusst nicht auf den allgemeinen FAQ-Mindestabstand von 1,5 mm reduzieren (Q3). Bund separat prüfen |

**Abweichung zur bisherigen Planung:** Dort stehen 3 mm Beschnitt und 176 × 266 mm Datenumfang. Für den print24-Kandidaten werden 2 mm und rechnerisch 174 × 264 mm vorgeschlagen. Die alten Werte bleiben als ursprüngliche Planannahme nachvollziehbar; noch keine bestätigte Formatüberschreibung. Vor Satzvorlage und finalem Export Heftplan, Dokument und Druckspezifikation auf denselben freigegebenen Stand bringen.

## PDF, Farbe und Bilddaten

| Merkmal | Anforderung bzw. Arbeitsregel | Status / Grundlage |
|---|---|---|
| Lieferung | Druck-PDF | PDF-Upload laut Q3; tatsächliche Dateiaufteilung noch OPEN |
| PDF/X-Variante | OPEN; PDF/X-4 als zu bestätigender Arbeitskandidat | Keine eindeutige aktuelle deutsche Klammerheftungs-Spezifikation für X-3/X-4 gefunden. Das alte PDF deklariert X-3:2002, beweist aber keine aktuelle Anforderung |
| Farbmodus | Prozessfarben CMYK für geplanten Vierfarbdruck | Q1 / Projektwahl; RGB-Ausgangsbilder erhalten, Ausgabekonvertierung kontrolliert vornehmen |
| ICC-Profil / Output Intent | OPEN für die konkrete Papier-/Druckkombination | Q4 nennt ISO Coated v2 (FOGRA39) für Bilderdruck sowie PSO Uncoated ISO12647 (FOGRA47) für Offset/Recycling, aber auf der Flyer-Seite. Nur Anhaltspunkt, keine Broschürenfreigabe |
| Fotos / farbige Rasterbilder | Mindestens 300 ppi effektiv bei endgültiger Platzierung | Übertragung der allgemeinen 300-dpi-Angabe Q3 auf Bilddaten; bloßes Ändern der DPI-Metadaten genügt nicht |
| Raster-Strichzeichnungen | Projektziel 600–1200 ppi für reine 1-Bit-Strichbilder, sofern eingesetzt | PROPOSAL, keine hier belegte print24-Mindestanforderung; Vektoren bevorzugen |
| Schrift und Sprechblasen | Editierbare Texte/Vektoren im Satz; sämtliche verwendeten Fonts im PDF einbetten | Einbettung BELEGT Q3; Vektorerhalt als Projektregel |
| Kleine schwarze Texte / Konturen | Projektregel C0 M0 Y0 K100; keine Passermarkenfarbe | PROPOSAL für sauberes Lettering; Vierfarb-Schwarz nicht ungeprüft auf kleine Schrift anwenden |
| Gesamtfarbauftrag / Flächenschwarz | OPEN, abhängig vom bestätigten Profil und Druckverfahren | Keine universelle Prozentgrenze aus anderen Druckereien übernehmen |
| Überdrucken | Weiße Texte/Blasen dürfen nicht versehentlich überdrucken; Schwarz gezielt kontrollieren | Projektprüfregel; keine pauschale Überdruckeinstellung aus dem Beispiel übernehmen |
| Transparenzen | Im Original erhalten; PDF-Ausgabe passend zum bestätigten Standard | Bei X-4-Kandidat nicht vorzeitig reduzieren; endgültige Vorgabe OPEN |
| Druckmarken / Infobereich | Vorläufig ohne Marken und ohne Infobereich exportieren | PROPOSAL; anhand Produktdatenblatt bestätigen |
| Sicherheit | Keine Verschlüsselung/Passwortsperre in der Lieferdatei | Projektregel |

Bei 170 × 260 mm entsprechen 300 ppi aufgerundet mindestens 2008 × 3071 Pixeln für ein ganzseitiges Rasterbild ohne Beschnitt; bei 174 × 264 mm einschließlich 2 mm je Kante mindestens 2056 × 3119 Pixeln. Dies ist eine Maßstabsrechnung, keine zusätzliche Druckereivorgabe. Panelbilder werden nach ihrer tatsächlichen Platzierung beurteilt.

## Seitenfolge und Umschlag

Interne Lesefolge: C1, C2, I001–I020, C3, C4. Keine selbst ausgeschossenen Druckbögen erzeugen. Als Arbeitsmaster fortlaufende Einzelseiten verwenden; dies ist bis zum konkreten Datenblatt eine Projektregel.

Ob print24 für das gewählte Produkt eine gemeinsame 24-seitige PDF, getrennte Inhalt-/Umschlagdateien oder eine andere Umschlaganordnung verlangt, bleibt **OPEN**. Eine Klebebindungs-Anweisung nicht auf Klammerheftung übertragen. Bei getrenntem Upload muss das Datenblatt insbesondere die Anordnung von C1–C4 festlegen. Kein erfundenes Rückenmaß ergänzen. Bundbeschnitt, eventueller Bundzuwachs und Lieferung seitenübergreifender Motive ebenfalls anhand der gewählten Konfiguration prüfen.

## InDesign-Arbeitsvorgabe für den ersten Versuch

1. Neue Vorlage im gewählten **Endformat** anlegen; Datenrechteck inklusive Beschnitt nicht als Seitengröße verwenden.
2. Für den vorläufigen print24-Versuch 170 × 260 mm und 2 mm Beschnitt als explizite Versuchskonfiguration dokumentieren. Das ist noch keine Freigabe des Heftformats.
3. Text-Sicherheitsbereich aus dem Projektplan erhalten, Hintergrundbilder bis zur Beschnittkante führen. Master/Originalbilder mit ausreichender Reserve aufbewahren.
4. Bilder verknüpfen, Fonts und effektive Auflösung prüfen; Text nicht ins Rasterbild einbacken.
5. Adobe PDF (Druck), Einzelseiten als Arbeitsausgabe; PDF/X-Variante und Zielprofil erst nach Datenblatt festschreiben. Noch keine verbindliche JOBOPTIONS-Datei erzeugt.
6. Beim finalen Export Schrift-Einbettung, tatsächliche Seitenboxen, Farben/Output Intent, Bilder, Transparenzen und Reihenfolge prüfen. Export-PDF unabhängig vom InDesign-Dokument kontrollieren.

## Befund zum gelieferten Beispiel

INDD, IDML, 86 Dateien im Assets-Ordner und das 12-seitige Referenz-PDF sind vorhanden. Dessen PDF-Metadaten nennen InDesign 21.3 (Macintosh), PDF/X-3:2002 und den Output Intent `Coated FOGRA39 (ISO 12647-2:2004)`. Das sind ausgelesene Angaben, keine vollständige PDF/X-Konformitätsprüfung.

Alle 12 PDF-Seiten haben eine TrimBox von **168 × 260 mm** und Media-/BleedBox von **172 × 264 mm**, mithin 2 mm Rand um die TrimBox. Das IDML enthält dagegen 12 Seiten mit **170 × 262 mm** Seitengeometrie und Dokument-Beschnittwerten von **0 mm**. Diese Dateien sind nicht ohne Abgleich als identisch konfigurierte Vorlage anzusehen. Ursache und Exportgeschichte sind offen; keines der Maße automatisch in Human Park übernehmen. Detailnachweis: [technischer Intake](../../references/previous-comic/technical-intake-2026-09-17.json).

## Vor verbindlichem Export auflösen

- Endformat 170 × 260 mm bestätigen oder abweichendes Wunschformat festlegen; Konfigurierbarkeit bei Klammerheftung prüfen.
- 20 Inhalt + 4 Umschlag, Papier, 4/4-Druck, Nutung, Auflage und ggf. Proof auswählen.
- Genau dazu gehörendes Datenblatt/Konfigurationsbeleg speichern.
- 2-mm-Beschnitt einschließlich Bund, PDF/X-Variante, ICC-Profil, Farbauftrag, Marken und Umschlag-Dateianordnung bestätigen.
- Konflikt IDML-Geometrie versus Beispiel-PDF klären, bevor eine Vorlage daraus abgeleitet wird.
- Finale Datei mit [Druckcheckliste](../../checklists/print-release.md) und revisionsgebundenem Prüfprotokoll prüfen und freigeben.

Recherche und Spezifikation lösen weder Upload noch Bestellung aus. Kein Druck-PDF erstellt oder als druckreif bestätigt.
