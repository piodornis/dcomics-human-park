> Importiertes Entstehungsprotokoll vom 2026-09-14. Zeitgebundene Aussagen wie „noch nicht im Repo“ beschreiben den damaligen Stand. Aktuelle Auswahl und Handoffs stehen in den Designakten. Lokale Links wurden bei der Übernahme angepasst; Prompts bleiben inhaltlich erhalten.

# Zugang Fundanlage — v2

Status: EXPLORATION. Werkzeug: eingebautes image_gen, gezielter Bildedit.
Autorenkorrektur: rechtes Geländer korrekt am Eingang ausrichten.
Ergebnis: rechte Geländerführung nach außen zur rechten Eingangskante versetzt; Durchgang frei. Die unmittelbar angrenzende Stegkante wurde vom Bildmodell mit angepasst. Grundkomposition und übrige Motive weitgehend erhalten. V1 bleibt erhalten; Projekt-Repo unverändert.

## Exakter Prompt

Use case: precise-object-edit.
Input image is the edit target, Human Park underground facility access v1.
User request: align the RIGHT-HAND RAILING correctly with the entrance.
Change ONLY the right-hand walkway railing and its local mounting points. The existing rear end incorrectly drifts inward across the doorway. Rebuild it as a straight coherent handrail along the RIGHT OUTSIDE EDGE of the grated approach, meeting the RIGHT OUTER DOOR JAMB at the threshold, never the center of the entrance.
Geometry: preserve the nearest right post at approximately (1004,990) in the 1536x1024 image. Follow the existing right boundary of the grated walkway toward the right-hand side of the outer doorway at approximately x=1040, threshold y=650. The final rear post should have its foot attached to the walkway's right structural side member immediately outside that right door jamb, around (1030,665), with its top around (1030,545). Align the upper handrail and lower horizontal rail in perspective between the foreground and this final rear post, straight and parallel in world space to the walkway edge. Intermediate posts vertical, proportional height diminishing with depth, bolted to the right edge structure. A clean wall bracket or neat end at the right jamb completes the handrail. Match the left railing's real-world height, tube diameter, weathering and two horizontal rail levels.
Remove the old misaligned inward-running rail and its posts completely, restoring the underlying grate and vestibule where they were. Keep the entire doorway passage unobstructed. Do not place any railing in front of the inner door, across the threshold, or along the center of the ramp.
LOCK all other elements: left railing, grating position and width, old wall and doors, pipes, lights, surrounding ice, camera, crop, perspective, palette and detailed comic ink style. Local occlusion changes caused by relocated rail are expected, but do not redesign the scene. No new objects, characters or text. Status EXPLORATION.

