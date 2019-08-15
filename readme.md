#Maturaarbeit

##to do
* Farberkennung einzelne pixel
* Seiten den Mittelsteinen zuordnen
* HSV statt RGB oder beides
* Kantenerkennung statt feste Pixel
* mehrere Pixel pro Seite
* mehrere Bilder aufnehmen und Durchschnitt nehmen
* wenn Farberkennung fertig Algorithmus anzeigen
* statt Grenzen mit Faktor zu bestimmen absolute Grenzen einfügen
* bei Grenzen Gross anfangen und dann kleiner werden bis eindeutig
* wenn uneindeutig Wahrscheinlichkeiten angeben, wo es eher ist
* wenn von einer Farbe zu viel vorhanden, die, die am wenigsten zutreffen zu neuer Farbe ändern
* Einschränkungen: nur vier von einer Farbe auf Ecken/Kanten
* jede Farbe nur einmal pro Ecke/Kante
* gegenüberliegende Farben nicht erlaubt auf gleichem Stein

##Versionen

###first test

* erstes Kennenlernen von opencv
* erkennt auf einem Bild alle Pixel mit gleichen Farben, wie ein ausgewählter Pixel
* Grenzen für die erlaubten Farbwerte durch Ausprobieren festgelegt

###Version 1.0

####08.08.2019

* Koordinaten Reihenfolge: auf einer Seite vom vordersten Stein im Uhrzeigersinn mit Mittelstein am Schluss
* Reihenfolge Seiten: oben, links, rechts von Bild 1, dann gleich Bild 2
* erstes einfaches Programm, welches Felder den Mittelsteinen zuordnet
* funktioniert sehr schlecht
* blau und orange relativ gut, bei weiss und gelb sind immer weiss/gelb/orange dabei
* bei grün kommt weiss/gelb/grün heraus und bei rot kommt rot/orange/weiss/gelb heraus
* Grenzen bei +- 50%

###Version 1.1

####09.08.2019

* code übersichtlicher gemacht
* Reihenfolge Boundaries: Seiten gleich wie bei Koordinaten
* dann Reihenfolge blue/green/red und zuerst lower, dann upper
* blau benötigt eine hohe Abweichung, um erkannt zu werden
* weiss und gelb benötigen eine kleine Abweichung, damit nicht zu viele Farben zutreffen
* absolute Grenzen statt relative: bei Grenzen von +- 50 werden blau, grün und orange perfekt erkannt
* bei rot werden zwei felder nicht erkannt
* gelb und weiss sind nicht voneinander unterscheidbar
* bei einer Grenze von +- 20 sind gelb und weiss verlässlich voneinander unterscheidbar
* bei rot und blau werden jedoch einige Felder nicht erkannt

###Version 1.2: sich verändernde Grenzen

####09.08.2019

* Programm beginnt mit sehr grossen Grenzen
* wenn Farbe uneindeutig werden Grenzen so lange verkleinert, bis nur noch eine einzige Farbe übrig bleibt
* Fazit: 52 von 54 Flächen wurden erkannt, zwei rote Flächen wurden als gelb erkannt

###Version 1.3: alle Farben kommen neun mal vor

####10.08.2019

* wenn eine Farbe zu oft vorkommt, werden die Grenzen so lange wieder vergrössert, bis bei den ersten Flächen andere Farben auftreten und diese werden dann verändert
* ein gelbes Feld als rot und ein rotes Feld als gelb

###Version 1.4

####10.08.2019

* bei zu vielen Feldern einer Farbe werden nicht die verändert, die am nächsten an einer anderen Farbe sind, sondern die, die am weitesten weg von der aktuellen Farbe sind
* das erste mal, wo der gelöste Würfel mit guten Lichtverhältnissen komplett richtig erkannt wurde

###Version 1.5

####11.08.2019

* nicht mehr einzelne Pixel sondern Durchschnitte von Quadrat mit Seitenlänge 30 Pixel
* diese Durchschnitte neu in einem Array für Übersichtlichkeit
* bei ungelöstem Bild noch probleme bei gelb/weiss/orange (gesamt 6 Fehler)
* rot, blau, grün komplett richtig erkannt

###Version 1.6

####14.08.2019

* HSV statt RGB verwendet (ohne Hue)
* weiss wurde erkannt, der rest nicht (bsp. Gelb wurde als gelb, orange, blau und grün erkannt)

###Version 1.7

####15.08.2019
* wieder RGB
* code ein bisschen übersichtlicher gestaltet
* neue Methode ausprobiert: statt Grenzen direkt den Abstand zu den Mittelpunkten messen
* noch keine Einschränkungen wie von jeder Farbe neun
* insgesamt 9 Fehler
* 8 davon gelb oder weiss falsch erkannt, einmal orange falsch