# Poker Ranges

Editor für Poker-Ranges in der 13×13-Matrix: eigene Farben, 50/50-Mixe, Range-Text zum Kopieren und Einfügen.

Live: https://jpolack.github.io/Poker-ranges/

Die Ranges werden nur im Browser des jeweiligen Geräts gespeichert. Auf dem iPhone die Seite über „Teilen → Zum Home-Bildschirm“ anlegen, sonst kann Safari den Speicher nach 7 Tagen ohne Besuch löschen.

## Updates

Die Seite prüft beim Öffnen, beim Zurückkehren in die App und alle 5 Minuten `version.json` am Cache vorbei und lädt sich bei einer neuen Version selbst neu. Vor jedem Commit `python3 scripts/bump-version.py` ausführen, sonst erkennt die App das Update nicht.
