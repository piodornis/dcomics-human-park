> Importiertes Entstehungsprotokoll vom 2026-09-14. Zeitgebundene Aussagen wie „noch nicht im Repo“ beschreiben den damaligen Stand. Aktuelle Auswahl und Handoffs stehen in den Designakten. Lokale Links wurden bei der Übernahme angepasst; Prompts bleiben inhaltlich erhalten.

# Human Park — Earth Stiltest

Designstatus: EXPLORATION. Narrative Ausgestaltung: PROPOSAL innerhalb bestehender Earth-Constraints. Keine Auswahl oder Freigabe vorweggenommen.

Erzeugt mit dem eingebauten image_gen-Werkzeug. Das Projekt-Repo dcomics-human-park wurde nicht verändert.

## Ergebnisse

- earth-a-reduziert.png: finale reduzierte Variante, drittes im Chat gezeigtes Bild.
- earth-b-detailreich.png: detailreiche Variante, zweites im Chat gezeigtes Bild.
- Das erste Chat-Bild war die gemeinsame Ausgangsfassung und ist kein dritter Auswahlkandidat.

Beide verwenden dieselbe grundlegende Ansicht. A vereinfacht Fassaden, Eis und Wolken stark; B betont Nieten, Fugen, Gebrauchsspuren und Materialzeichnung. Die Generierung hat bei A zusätzlich den Satellitenhimmel ausgedünnt; der Vergleich ist daher nicht vollständig auf Oberflächendetails beschränkt. Empfehlung des Style Directors: B weiterentwickeln, bei Bedarf mit ruhigeren Teilflächen für kleine Panels. Kein SELECTED-Status gesetzt.

## Quellen und Grenzen

Source of Truth: dcomics-human-park (Projekt-Repo)
Gelesene Grundlagen: project.md, design-project.md, relevante Kanonakten und Originaltexte der Hefte, B-21/B-73-Profile und Beziehung, Charakterbilder und Earth 01–03.
Direkte Bildreferenz der Ausgangsgenerierung: design/environments/earth/references/earth-01.png, ausschließlich für Umgebung, Palette und Stil. Roboter und Geräte ausgeschlossen.
Stilworkflow: comic-framework-design/skills/comic-style-director. Story-Constraints: comic-framework-story. Modulgrenzen: comic-framework-docs.

KANON: verlassene, technisch weiter aktive Erde; alte Energie-/Recheninfrastruktur; Satelliten-/Archivhülle; fortgesetzte Wartung.
PROPOSAL: dieses konkrete Gebäude, Materiallayout und Wartungseingang. Keine Festlegung als B-21s Fundanlage.
Handoff: konkrete Ortsgeometrie und weitere Funktionsausarbeitung an Comic Environment Designer; neue narrative Fakten bleiben Story-Entscheidungen.

## Exakte Prompts

### Ausgangsgenerierung

Use case: illustration-story.
Asset type: Human Park comic style exploration A, reduced detail, not approved canon or final location design.
Generate a new wide landscape illustration based on Image 1 ONLY for Earth environment palette, ink language and atmosphere. Ignore its foreground robot and all robot equipment completely. Do not reproduce any characters.
Scene: Exterior of an immense ancient but still operating data center on frozen Earth. A coherent monolithic industrial building with old patched metal/concrete facade, tall server-cooling structures and a clearly readable recessed maintenance entrance. Snow and ice on ledges. Foreground frozen service approach leads toward the entrance, distant industrial silhouettes recede in depth. Dense orbital satellite/archive shell overhead as small distant technical silhouettes, never toy-like hovering robots. Earth is officially deserted but its maintenance infrastructure continues operating.
Style: confident black comic contours with heavier exterior contours and lighter interior lines; hard-edged graphic shadow shapes, clear separated colors, stylized ink drawing, no photorealism or painterly wash. Deep blue and violet dusk, cyan ice, sparse restrained amber lights signal working systems. Visible patch plates and limited wear communicate long maintenance rather than total destruction.
Composition: single landscape scene, wide ground-level three-quarter establishing view, architectural focal point at maintenance entrance, clear foreground/midground/background hierarchy, enough open foreground for readability. This image will be edited into a matched detailed version.
Variant A treatment: deliberately reduced detail density, broad calm readable shapes, few selected panel seams, a handful of deliberate repairs, grouped ice shapes, sparse internal hatching. Preserve monumentality and functional legibility without intricate surface noise. Keep a dense orbital shell readable as grouped distant points and silhouettes.
Avoid: any people, robots, cleaning equipment, vehicles, plants, action, explosions, neon goo, fantasy technology capabilities, all-over ruin rubble, text, labels, borders, watermarks. No new story events.

### Variante B — Edit der Ausgangsgenerierung

Use case: style-transfer.
Asset type: Human Park Earth style exploration B, high surface detail density.
Image 1 is the edit target, the complete immutable composition and architectural design baseline.
Create exactly the same image with ONLY a higher density of drawn surface details and material texture.
Strict invariants: identical image dimensions and crop, camera viewpoint, perspective, all building silhouettes, facade divisions, cooling structures, entrance dimensions and position, background skyline, foreground ice formations and service path, sky and satellite positions, palette, dusk brightness, amber light locations, shadow masses. No new structural objects, pipes, buildings, machines, characters or events.
Change only the fine ink rendering: enrich existing facade panels and existing patch plates with small visible screw heads, repair weld seams, layered weathering scratches, chipped paint, restrained rust at joins, fine graphic hatching in recessed surfaces. Enrich existing ice edges with fine crystalline fractures. Elaborate existing vent slats and recesses with layered smaller ink details. Background remains less detailed than foreground to preserve depth. Increase detail density clearly compared with Image 1 while keeping the exact same underlying design and large tonal shapes.
Medium: hand-inked comic drawing with strong clean exterior contours, finer interior lines, hard-edged graphic shadows, cold blue/cyan/violet palette and restrained warm amber working lights. No photorealism, gradients replacing ink, painterly rendering, added text, labels, border or watermark. No people, robots, cleaning equipment, vehicles, vegetation or explosions.
This is a rendering-density comparison only, EXPLORATION, not a final environment design.

### Finale Variante A — Edit der Ausgangsgenerierung

Use case: style-transfer. Image 1 is the edit target. Produce a clearly simplified, low-detail comic rendering of EXACTLY this same frozen data-center exterior. This is final comparison candidate A, EXPLORATION.
Keep absolutely the same crop, camera, perspective, building silhouettes, architectural proportions, door position, sky composition, satellite positions, snow banks, path, cold blue/cyan/violet palette, amber light placements and major hard-edged shadow masses.
Change ONLY surface-detail density. Dramatically reduce the number of small drawn marks by about 75 percent. Turn facades into broad quiet graphic color planes with only the main panel divisions and a few essential rectangular repair patches. Remove most individual rivets, speckling, scratch marks, hatching and tiny ice cracks. Simplify vent grilles into grouped bold horizontal slats. Simplify foreground ice into broad readable polygonal shapes with a few selected fracture lines. Simplify cloud internal textures into several large flat cel-shaded shapes. Keep the satellites in their same positions but reduce their internal tiny line details.
The result must visibly read as a restrained hand-inked comic panel at small size, with bold confident exterior contours, economical lighter interior lines, flat separated colors and graphic shadows. Retain selected patch plates to show ongoing maintenance. Do not redesign geometry or change lighting, do not add anything, no characters, robots, equipment, text or labels. No painterly or photoreal rendering.

