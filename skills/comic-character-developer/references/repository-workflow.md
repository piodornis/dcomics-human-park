# Repository Workflow

## Ziel

Charakterakten so bearbeiten, dass sie in einem lokal vorgehaltenen und nach GitHub synchronisierten Repository nachvollziehbar versioniert werden können.

## Prioritäten

1. Bestehende Repository-Konventionen erkennen und beibehalten.
2. Aktuelle Charakterakte eindeutig von historischen Fassungen trennen.
3. Keine destruktiven oder externen Aktionen ohne ausdrücklichen Nutzerauftrag durchführen.

## Empfohlene Struktur bei neuem Repository

```text
characters/
  <character-id>/
    profile.md
    references/
archive/
  characters/
    <character-id>/
      2026-09-12_profile.md
```

Diese Struktur nur verwenden, wenn noch keine etablierte Struktur existiert.

## Aktualisierung

Bei einer Überarbeitung:

1. aktuelle Datei lesen;
2. neue vollständige Fassung erzeugen;
3. Unterschiede und Folgewirkungen zusammenfassen;
4. Archivierung der alten Fassung nur nach Zustimmung durchführen;
5. aktuelle Datei ersetzen oder schreiben;
6. optional `git diff` bzw. den resultierenden Änderungsumfang prüfen, wenn Git lokal verfügbar ist;
7. Commit nur auf ausdrücklichen Auftrag erstellen;
8. Push zu GitHub nur auf ausdrücklichen Auftrag durchführen.

## Archivierung

- Vor dem Verschieben oder Kopieren einer alten Fassung Zustimmung einholen, sofern sie nicht bereits erteilt wurde.
- Archivierte Fassungen unverändert lassen.
- Eindeutige Datums- oder Versionskennung verwenden.
- Keine alte Version allein deshalb löschen, weil eine neue existiert.

## Git-Hinweise

Wenn der Nutzer einen Commit verlangt, eine knappe, nachvollziehbare Commit-Beschreibung verwenden, z. B.:

```text
update(character): revise <name> profile and continuity
```

Bei mehreren Figuren oder größeren Story-Auswirkungen lieber getrennte Commits vorschlagen.
