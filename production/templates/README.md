# Satz- und Prüfvorlagen

Vorlagen pro Ausgabe kopieren; die Header-Dateien enthalten bewusst keine erfundenen Dialoge oder Produktionsdaten.

## lettering.csv

Eine Zeile je Textobjekt. `text_id` dauerhaft eindeutig; `story_page_id`, `panel_id` und `physical_slot_id` aus den vorhandenen Story-/Produktionsakten. `reading_order` ist eine positive, innerhalb der Seite eindeutige Zahl. `kind`: narration, dialogue, thought, system, sfx oder editorial. `speaker_id`: bestehende Figuren-ID oder leer bei Erzähler/Redaktion; unbekannte Sprecher nicht erfinden. `text` enthält den exakten Wortlaut einschließlich Satzzeichen. `source_ref` ist ein Repo-Pfad mit Abschnitt/Panelanker, `source_revision` ein Commit oder eindeutig datierter Quellstand. `text_status`: DRAFT, REVIEW oder APPROVED; APPROVED nur mit Nachweis in `approval_ref`.

`x_mm,y_mm,width_mm,height_mm`: optional für erste Skizzen, vor positionsgesteuertem Import vollständig und numerisch; Ursprung links oben am Endformat jeder Seite. Negative Werte nur für bewusst in den Beschnitt reichende Objekte. `paragraph_style` und `object_style` müssen in der Vorlage existieren. `tail_target` beschreibt das Ziel des Sprechblasenausläufers, `notes` gestalterische Hinweise. Kontur und exakte Ausläufergeometrie werden im Satz geführt.

UTF-8, Komma, Standard-CSV-Quoting: Text mit Komma, Anführungszeichen oder Zeilenumbruch in doppelte Anführungszeichen einschließen; enthaltene Anführungszeichen verdoppeln. `OPEN` in Pflichtfeldern ist ein offener Befund, kein importierbarer Wert.

## assets.csv

Eine Zeile je platziertem Asset. `asset_id` stabil, `file_path` relativ zum Repo, `sha256` für exakt diese Dateifassung. `placement_id` identifiziert den Einsatz, da ein Asset mehrfach vorkommen kann. Quell-/Designakte und Freigabenachweis angeben. `effective_ppi` erst nach Platzierung bestimmen; ein hoher Metadaten-DPI-Wert ersetzt keine ausreichende Pixelzahl. `status` beschreibt den belegten Designstatus, kein automatisches APPROVED durch Ablage.

## changes.csv

Jede Textkorrektur mit alter/neuer Fassung, Grund und Quelle protokollieren. `status`: OPEN, ACCEPTED, REJECTED oder APPLIED. APPLIED erst, wenn Story-Abgleich, Satzliste und InDesign dokumentiert synchronisiert sind. Originalskripte nicht überschreiben; gegebenenfalls genehmigte Adaption separat führen.

[print-spec.md](print-spec.md) führt technische Vorgaben; [review.md](review.md) protokolliert eine konkrete Ausgaberevision. Leere Vorlagen gelten nicht als abgeschlossene Prüfung.
