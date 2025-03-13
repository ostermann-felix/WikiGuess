# WikiGuess
================

Ein Quiz-Spiel, das auf Wikipedia-Daten basiert

## Über das Spiel
---------------

Wikiguess ist ein Quiz-Spiel, das den Spieler herausfordert, seine Kenntnisse über europäische Länder und ihre Hauptstädte zu testen. Das Spiel verwendet Wikipedia-Daten, um Fragen zu generieren und die Antworten zu überprüfen.

### Funktionen
------------

* Interaktives Hauptmenü
* Fragen über europäische Länder und ihre Hauptstädte
* Punktzahl-System
* Anleitung und Spielregeln

### Technologie
--------------

* Python als Programmiersprache
* Wikipedia-API für die Datenabfrage
* VS Code als Entwicklungsumgebung

### Lizenz
-------

Dieses Projekt ist unter der [MIT-Lizenz](https://opensource.org/licenses/MIT) lizenziert.

### Beschreibung
-------------

Das Spiel besteht aus mehreren Modulen, die jeweils eine bestimmte Funktion übernehmen:

* `main.py`: Die Hauptdatei des Spiels, die den Spielablauf steuert.
* `intro.py`: Enthält die Funktion `introduction_of_game`, die den Spieler begrüßt und seinen Namen abfragt.
* `main_menu.py`: Enthält die Funktion `main_menu`, die das Hauptmenü des Spiels anzeigt und die Spielerinteraktionen verarbeitet.
* `wikimedia_fetch.py`: Enthält die Funktion `european_countries_and_capitals`, die Wikipedia-Daten über europäische Länder und ihre Hauptstädte abruft.
* `question.py`: Enthält die Funktion `question`, die dem Spieler Fragen stellt und seine Antworten auswertet.
* `manual.py`: Enthält die Funktion `manual`, die dem Spieler die Spielanleitung anzeigt.
* `scoreboard.py`: Enthält die Funktion `show_scoreboard`, die die aktuelle Punktzahl des Spielers anzeigt.

### Systemanforderungen
--------------------

* Python 3.x
* Wikipedia-API-Zugang
