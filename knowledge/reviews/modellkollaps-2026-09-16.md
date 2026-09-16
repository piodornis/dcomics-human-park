# Modellkollaps — Bewertung des eingereichten Textes

Stand: 2026-09-16. Status: quellenbasierte redaktionelle Erstprüfung, keine vollständige Literaturübersicht oder unabhängige Fachfreigabe. [Eingangstext](../intake/modellkollaps-2026-09-16.md) · [Überarbeiteter Entwurf](../articles/modellkollaps.md).

## Gesamturteil

Der Text trifft ein reales Forschungsproblem, überzeichnet aber Unvermeidlichkeit, Ursachen und Endzustand. Für Bildungsinhalte nur nach Korrektur verwenden. Der Ausdruck „Zero Distillation“ ist in der behaupteten Bedeutung unbelegt.

| Aussage | Bewertung | Redaktioneller Umgang |
|---|---|---|
| Eines der kritischsten Probleme | Unbelegte Rangordnung | Als relevantes Risiko bestimmter Trainingsverfahren beschreiben. |
| Algorithmische Inzucht als Fachbezeichnung | In den geprüften Primärquellen nicht als etablierter Begriff belegt; metaphorisch und wertend | Neutral „Modellkollaps“ verwenden. Keine biologische Analogie als Mechanismus ausgeben. |
| Training auf KI-Ausgaben verursacht zwangsläufig Degeneration | Zu allgemein | Rekursive Datennutzung, Datenmischung, Qualität und Trainingsverfahren benennen; Q1/Q2. |
| Zwei Phasen | Mit Einschränkung belegt | Q1 unterscheidet frühe Verluste in Verteilungsrändern und spätere starke Abweichungen. Keine universelle Zeittreppe aller LLMs. |
| Immer durchschnittlichere Antworten, am Ende nur Kauderwelsch | Überzeichnet | Die zugrunde liegende Verteilung kann schlechter repräsentiert sein; sprachliche Flüssigkeit ist kein ausreichender Qualitätstest. Q1. |
| Nur Fehler und Halluzinationen werden verstärkt | Zu eng | Auch endliche Stichproben und statistische Näherungsfehler spielen eine Rolle; keine absichtliche Falschinformation erforderlich. Q1. |
| Zehn Fotokopien führen zum Kollaps | Anschauliche, aber ungenaue Metapher | Keine feste Zahl von Generationen und keine physische Kopiermechanik behaupten. |
| Menschliche Daten gehen aus | Bedingte Prognose wird als Tatsache formuliert | Q4 betrifft die Skalierung öffentlich verfügbarer menschlicher Textdaten unter Annahmen, nicht ein Verschwinden vorhandener Daten. Menschliche Herkunft garantiert keine Wahrheit oder Qualität. |
| Filterung löst das Problem | Forschungsansatz, keine universelle Garantie | Q3 untersucht detektorbasierte Gewichtung/Resampling für zwei Modelle. Nicht mit fehlerfreier KI-Erkennung oder allgemeinem Löschen aller synthetischen Daten gleichsetzen. |
| Exklusivverträge sichern reine Menschendaten gegen Kollaps | So nicht belegt | Q5/Q6 belegen konkrete Partnerschaften, aber nicht diese Exklusivität, Reinheitsgarantie oder den behaupteten alleinigen Zweck. |
| Zero Distillation als moderne Anti-Kollaps-Architektur | Unbelegt | Aus dem Lehrtext streichen, bis eine eindeutige Primärquelle vorliegt. Zero-shot und Distillation nicht ohne Beleg zu einem Verfahren zusammensetzen. |

## Quellen und Prüfumfang

**Q1 — Shumailov et al.: The Curse of Recursion: Training on Generated Data Makes Models Forget.** [arXiv v3, 14.04.2024, Volltext](https://arxiv.org/html/2305.17493v3), insbesondere Abschnitte 3/3.1. Dort Theorie sowie GMM-/VAE-/Sprachmodellversuche; Aussagen sind auf untersuchte Annahmen zu beziehen. Dies ist eine Vorveröffentlichungsfassung, nicht stillschweigend die spätere korrigierte Nature-Fassung. [Nature 2024](https://www.nature.com/articles/s41586-024-07566-y); [Autorenkorrektur 2025](https://www.nature.com/articles/s41586-025-08905-3.pdf) bibliografisch vermerkt, hier nicht inhaltlich geprüft. Vor Veröffentlichung finalen Text und Korrektur abgleichen.

**Q2 — Gerstgrasser et al.: Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data.** [arXiv v2, 29.04.2024](https://arxiv.org/abs/2404.01413v2). Abstract geprüft: Ersatz ursprünglicher Daten und Akkumulation mit ursprünglichen Daten führen in den untersuchten Einstellungen zu unterschiedlichen Ergebnissen. Keine universelle Garantie für beliebige Datenmischungen. Dieser Link stand bereits in `knowledge/README.md`.

**Q3 — Drayson und Lampos: Machine-generated text detection prevents language model collapse.** [arXiv](https://arxiv.org/abs/2502.15654), eingereicht 21.02.2025. Abstract geprüft: Untersuchung von Decodingstrategien und detektorbasierter Gewichtung/Resampling, validiert mit GPT-2 und SmolLM2 für offene Textgenerierung. Begrenzte Modell-/Aufgabenauswahl, keine allgemeine Erfolgsgarantie. Versionsstand vor öffentlicher Verwendung fixieren.

**Q4 — Villalobos et al.: Will we run out of data? Limits of LLM scaling based on human-generated data.** [arXiv](https://arxiv.org/abs/2211.04325). In dieser Recherche Abstract im Suchresultat geprüft; Versionsstand und Volltext noch zu prüfen. Bedingte Prognose zum Umfang verfügbarer öffentlicher menschlicher Texte; keine nachgewiesene weltweite Erschöpfung und kein belegter Kollaps eines konkret genannten Herstellermodells.

**Q5 — Reddit: Expanding our Partnership with Google, 22.02.2024.** [Unternehmensmitteilung](https://redditinc.com/news/reddit-and-google-expand-partnership), gelesen. Beschreibt API-Zugang einschließlich effizienterer Trainingsmöglichkeiten. Belegt die angekündigte Partnerschaft, nicht die behauptete Exklusivität oder Reinheit aller Inhalte.

**Q6 — Stack Overflow / Google Cloud, 29.02.2024.** [Unternehmensmitteilung](https://stackoverflow.co/company/press/archive/google-cloud-strategic-gen-ai-partnership/), gelesen. Beschreibt die Integration von Stack-Overflow-Wissen und OverflowAPI. Belegt keine allgemeine Anti-Kollaps-Strategie und keine Exklusivität.

Recherche zu „Zero Distillation“: exakte Begriffssuche allein sowie mit LLM/Model Collapse am 2026-09-16. Kein belastbarer Primärbeleg für die eingereichte Behauptung gefunden. Das ist kein Beweis, dass die Zeichenfolge nirgends verwendet wird; der behauptete Fachinhalt ist derzeit nicht gesichert.

## Für Human Park

Der reale Forschungsbegriff kann die Quellenproblematik in Heft 1 vertiefen. Nicht behaupten, dass heutige Modelle menschliche Erinnerungen besitzen oder dass Modellkollaps die etablierte Ursache der Großen Vergessen sei. Öffentliche Fachtexte enthalten keine unveröffentlichten Serienauflösungen.
