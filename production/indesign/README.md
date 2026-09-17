# InDesign — Satzkonventionen und Automatisierung

Status: PREPARED / konkrete Ausgestaltung OPEN. Zunächst Referenzdokument auswerten; noch keine technische Kompatibilität mit einer bestimmten InDesign-Version getestet.

## Vorgesehene Dokumentstruktur

Ebenen von unten nach oben: `01_ARTWORK`, `02_BALLOONS`, `03_TEXT`, `04_PAGE_ELEMENTS`, `90_GUIDES`. Hilfsebene als nicht druckend konfigurieren. Bilder verknüpfen; Blasen und Erzählerkästen als editierbare Formen, Text als editierbare Textrahmen. Text und zugehörige Form logisch zusammenhalten. Automatisch verwaltete Objekte später mit stabiler Text-/Asset-ID kennzeichnen.

Absatzformate als Startvorschlag: `HP_Narration`, `HP_Dialogue`, `HP_Thought`, `HP_System`, `HP_Credits`. Objektformate: `HP_Balloon`, `HP_Caption`, `HP_ArtworkFrame`. Unterschiede zwischen Menschen- und KI-Stimmen sind noch nicht gestalterisch freigegeben. Fonts, Größen, Zeilenabstand, Innenabstände, Konturen, Farben und Trennregeln nach Beispielsichtung und Lesetest bestimmen. Keine pauschale automatische Textverkleinerung bei Überlauf.

Dokumentseiten im Endformat anlegen; Beschnitt separat einstellen. Vorläufig 170 × 260 mm plus 3 mm Beschnitt aus dem Heftplan, nicht 176 × 266 mm als Endformat. Werte bleiben PROPOSAL. Physische Slots und Dokumentseiten explizit zuordnen, auch bei getrennten Umschlag-/Innenteil-Dateien.

## Geplanter Importvertrag

Eingang: geprüfte Satzliste, Seiten-/Panelzuordnung, Assetliste und abgestimmte Vorlage. CSV ist UTF-8 mit Komma als Trennzeichen; einen CSV-Parser verwenden, niemals einfach nach Komma aufteilen. Positionen in mm relativ zur linken oberen Endformatkante der jeweiligen Seite, nicht der Doppelseite. Maße im Import explizit konvertieren. Koordinaten und Formen bleiben bis zur Layoutprobe optional.

Ein späteres Skript soll zunächst einen lesbaren Vorprüfbericht erzeugen: unbekannte IDs, doppelte Text-IDs, fehlende Links, fehlende Formate, nicht bestätigte Maße und Textüberläufe. Bei unbekannten Pflichtwerten keinen Produktionsimport ausführen. Danach Seiten/Bildrahmen/Textrahmen mit dokumentierten Formaten anlegen, soweit diese im freigegebenen Mapping definiert sind.

Wiederholter Import darf manuelle Blasenpositionen, Konturen und Ausläufer nicht zurücksetzen: eigene stabile Objektkennungen, getrennte Modi für Erstaufbau und Textaktualisierung, Konfliktbericht bei lokalen Textänderungen. Immer Arbeitskopie/Revision sichern. Kein automatischer Druckexport oder Druckfreigabestatus durch den Import.

## Umsetzung nach Eingang des Beispiels

1. InDesign-Version und geeignete Skriptschnittstelle feststellen.
2. Tatsächliche Formate/Ebenen aufnehmen und Vorlage aus einer Kopie ableiten.
3. Minimalen Import für die Pilotseiten implementieren.
4. Erstimport, wiederholten Import, lokale Textänderung, fehlendes Bild und Textüberlauf prüfen.
5. Ergebnis visuell in InDesign und im exportierten PDF abgleichen.

Diese Datei spezifiziert die spätere Umsetzung; ein ausführbares Skript und ein natives Satzdokument werden erst mit den erforderlichen Eingaben erstellt.
