#Maturaarbeit

##to do
* Farberkennung einzelne pixel
* Seiten den Mittelsteinen zuordnen
* HSV statt RGB oder beides
* Kantenerkennung statt feste Pixel
* mehrere Pixel pro Seite
* mehrere Bilder aufnehmen und Durchschnitt nehmen
* wenn Farberkennung fertig Algorithmus anzeigen
*statt Grenzen mit Faktor zu bestimmen absolute Grenzen einfügen

## Versionen

### first test

* erstes Kennenlernen von opencv
* erkennt auf einem Bild alle Pixel mit gleichen Farben, wie ein ausgewählter Pixel
* Grenzen für die erlaubten Farbwerte durch Ausprobieren festgelegt

### Version 1.0

#### 08.08.2019

* Koordinaten Reihenfolge: auf einer Seite vom vordersten Stein im Uhrzeigersinn mit Mittelstein am Schluss
* Reihenfolge Seiten: oben, links, rechts von Bild 1, dann gleich Bild 2
* erstes einfaches Programm, welches Felder den Mittelsteinen zuordnet
* funktioniert sehr schlecht
* blau und orange relativ gut, bei weiss und gelb sind immer weiss/gelb/orange dabei
* bei grün kommt weiss/gelb/grün heraus und bei rot kommt rot/orange/weiss/gelb heraus
* Grenzen bei +- 50%

### Version 1.1

####09.08.2019

* code übersichtlicher gemacht
* Reihenfolge Boundaries: Seiten gleich wie bei Koordinaten
* dann Reihenfolge blue/green/red und zuerst lower, dann upper