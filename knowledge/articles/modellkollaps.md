# Modellkollaps: Wenn Trainingsdaten an Vielfalt verlieren

ID: model-collapse · Sprache: Deutsch · Stand: 2026-09-16.
Status: **DRAFT**, quellengeprüfter redaktioneller Entwurf; noch keine Veröffentlichungsfreigabe. Verantwortliche Fachredaktion: OPEN. Vor Veröffentlichung aktuelle Literatur und Quellenfassungen prüfen. [Bewertung und Quellenregister](../reviews/modellkollaps-2026-09-16.md).

## Kurz erklärt

Modellkollaps bezeichnet eine mögliche Verschlechterung über Modellgenerationen, wenn erzeugte Daten wieder als Trainingsgrundlage dienen und die ursprüngliche Verteilung dabei zunehmend schlechter abgebildet wird. Seltene Muster können verloren gehen; spätere Modelle können stärker von der ursprünglichen Verteilung abweichen. Das ist keine feste Abfolge, die jedes Sprachmodell zwangsläufig durchläuft. [Shumailov et al., Vorveröffentlichung](https://arxiv.org/html/2305.17493v3)

## Ein vereinfachtes Beispiel

Stell dir eine Sammlung von Geschichten aus vielen Regionen vor. Ein Modell erzeugt daraus neue Geschichten, in denen manche seltene Ausdrucksweisen kaum vorkommen. Wird nur diese neue Sammlung für die nächste Generation verwendet, fehlen ihr möglicherweise wichtige Beispiele. Die Texte können weiterhin flüssig klingen, während etwas von der ursprünglichen Vielfalt verloren geht. Das ist ein didaktisches Beispiel, kein konkretes Versuchsergebnis und keine feste Zehn-Generationen-Regel.

## Synthetische Daten sind nicht grundsätzlich schädlich

Entscheidend ist, wie sie erzeugt, ausgewählt und mit anderen Daten kombiniert werden. Gerstgrasser und Mitautor*innen fanden in ihren Untersuchungen, dass das Beibehalten ursprünglicher Daten zusammen mit neu hinzukommenden synthetischen Daten Kollaps vermeiden konnte. Daraus folgt keine Garantie für beliebige Trainingsrezepte. [Studie, Version 2](https://arxiv.org/abs/2404.01413v2)

Ein weiterer Ansatz nutzt Detektoren zur Gewichtung und erneuten Auswahl von Trainingsbeispielen. Dazu liegen Ergebnisse für bestimmte Modelle und Aufgaben vor; daraus lässt sich keine perfekte Erkennung aller KI-Texte ableiten. [Drayson und Lampos](https://arxiv.org/abs/2502.15654)

## Im Comic

Human Park greift widersprüchliche Quellen und verlorenes Wissen erzählerisch auf. Die Großen Vergessen sind Fiktion. Sie erklären nicht, wie reale LLMs funktionieren. Auch gezieltes Machine Unlearning und Informationen, die nicht mehr im aktuellen Kontext vorliegen, sollten separat erklärt werden; das Wort „Vergessen“ allein macht sie nicht zum selben Vorgang.

## Merksatz

Nicht allein die Herkunft „von einer KI“ entscheidet über die Qualität von Trainingsdaten. Wichtig ist, welche Informationen erhalten bleiben, was geprüft wird und wie der Trainingsprozess gestaltet ist.

Verwandte Einträge: LLM, Trainingsdaten, synthetische Daten, Machine Unlearning — noch auszuarbeiten. Bezug: Heft 1, Recherche zu den Großen Vergessen; keine Spoiler späterer Hefte.
