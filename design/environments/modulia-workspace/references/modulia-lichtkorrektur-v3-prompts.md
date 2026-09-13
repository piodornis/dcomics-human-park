# Ansichten A/B v3 — Lichtkorrektur

Design state: EXPLORATION. Werkzeug: eingebautes image_gen.
Eingaben: modulia-arbeitsplatz-sicht-a-v2.png und modulia-arbeitsplatz-sicht-b-v2.png.
Ergebnisse: modulia-arbeitsplatz-sicht-a-v3.png und modulia-arbeitsplatz-sicht-b-v3.png.

Sichtprüfung: Große dreieckige Licht-/Schattenflächen auf beiden Böden entfernt. Diffuses Tageslicht vom Fenster, in A rechts und in B links, mit weichen objektgebundenen Schatten. Keine technische Lichtsimulation; leichte generative Detailabweichungen möglich. Frühere Raum- und Möbelkorrekturen bleiben sichtbar.

## Exakter Prompt A

Use case: lighting-weather / precise lighting correction. Edit ONLY illumination and cast shadows in this exact comic office image. Keep camera, architecture, all furniture, shelving, monitors, window, floor tile seams, colors and object positions completely unchanged. The user rejects the huge arbitrary triangular light/shadow wedge on the floor. ERASE that entire triangle and all zigzag diagonal spotlight-like bands. Reconstruct the same cream tiles with consistent soft daylight.
Lighting specification shared across the two opposite views of this same room: broad DIFFUSE daylight from the single real side window, no hard direct sunbeam. Brightness gently highest near window and gradually lower across room, no discrete polygon-shaped pool of light. Furniture has short soft cast shadows directed AWAY from window, attached to real objects. Dark modest contact shadows under cabinet bases, under console overhangs, at floor/wall junctions and under pots. Small soft plant/monitor shadows only on plausible receiving surfaces opposite the light. Ceiling strips provide weak even fill, not diagonal beams. Do not invent triangular occluders or mullions. Keep luminous outdoor view but make interior daylight broad and diffuse; retain ink comic shading style and material highlights. No new objects or text. EXPLORATION.
This is VIEW A. The window is on image RIGHT, so daylight travels right-to-left into the room, softly shading left/away-facing furniture surfaces. Preserve the widened rear archive wall.

## Exakter Prompt B

Use case: lighting-weather / precise lighting correction. Edit ONLY illumination and cast shadows in this exact comic office image. Keep camera, architecture, all furniture, shelving, monitors, window, floor tile seams, colors and object positions completely unchanged. The user rejects the huge arbitrary triangular light/shadow wedge on the floor. ERASE that entire triangle and all zigzag diagonal spotlight-like bands. Reconstruct the same cream tiles with consistent soft daylight.
Lighting specification shared across the two opposite views of this same room: broad DIFFUSE daylight from the single real side window, no hard direct sunbeam. Brightness gently highest near window and gradually lower across room, no discrete polygon-shaped pool of light. Furniture has short soft cast shadows directed AWAY from window, attached to real objects. Dark modest contact shadows under cabinet bases, under console overhangs, at floor/wall junctions and under pots. Small soft plant/monitor shadows only on plausible receiving surfaces opposite the light. Ceiling strips provide weak even fill, not diagonal beams. Do not invent triangular occluders or mullions. Keep luminous outdoor view but make interior daylight broad and diffuse; retain ink comic shading style and material highlights. No new objects or text. EXPLORATION.
This is VIEW B. The window is on image LEFT, so daylight travels left-to-right into the room, softly shading right/away-facing furniture surfaces. Keep the small cabinet at BACK LEFT and no cabinet at front left; no visible doorway or archive wall.

