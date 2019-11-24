# find average color of tiles
for rgb in range(3): # R-, G-, und B-Werte einzeln auslesen
    col = 0
    for m in range(20):
        for n in range(20):
            col += picture[x - 10 + m][y - 10 + n][rgb] # Werte einzelner Pixel addieren
    avgcol[side][tile][rgb] = int(col / 400) # Durchschnitt in Liste speichern

# evaluate color of each tile
col = 200000
for middle in range(6): # sechs Mitten durchgehen
    dist = 0
    for rgb in range(3):
        dist += (avgcol[side][tile][rgb] -
                 avgcol[middle][8][rgb]) ** 2 # Quadrate addieren
    distances[side][tile][middle] = mt.sqrt(dist)
    if dist < col: # testen, ob Mitte am naechsten ist
        col = dist
        tilecol[side][tile] = colors[middle]



if avgcol[side][tile][1] < 50:
    white_question += 1 # Variable, die weisse Felder zaehlt
if avgcol[side][tile][2] < 50:
    black_question += 1 # Variable, die schwarze Felder zaehlt



if black_question == 9:
    for middle in range(6):
        if avgcol[middle][8][2] < lowvaluemid: # Vergleich, ob Value am tiefsten ist
            lowvaluemid = avgcol[middle][8][2]
            blackmidposition = middle
elif black_question != 0: # Programmabbruchbedingung
    sys.exit("ERROR!")






# method 1: furthest from own middle
for color in range(6):
    while tilenum[color] > 9:
        big_dist = 0
        small_dist = 99999999
        sidetpos = 0
        tilepos = 0
        for side in range(6):
            for tile in range(9):
                if tilecol[side][tile] == colors[color]:
                    if big_dist < distances[side][tile][color]: # Vergleich von aktuell groesster Distanz und Distanz von Seite
                        big_dist = distances[side][tile][color]
                        sidetpos = side
                        tilepos = tile
        for diffcol in range(6):
            if tilenum[diffcol] < 9:
                if small_dist > distances[sidetpos][tilepos][diffcol]: # Zuordnen zu naechster Mitte
                    small_dist = distances[sidetpos][tilepos][diffcol]
                    colpos = diffcol
        tilecol[sidetpos][tilepos] = colors[colpos] # Farbe wird geaendert
        tilenum[colpos] += 1 # Anzahl Felder wird angepasst
        tilenum[color] -= 1



# method 2: closest to another color
for color in range(6):
    while tilenum[color] > 9:
        sidepos = 0
        tilepos = 0
        colpos = 0
        counter = 0
        small_dist = 99999999
        breaker = 0
        for side in range(6):
            for tile in range(8):
                if tilecol[side][tile] == colors[color]:
                    for diffcol in range(6):
                        if tilenum[diffcol] < 9 and distances[side][tile][
                            diffcol] < small_dist: # Abstand wird verglichen
                            small_dist = distances[side][tile][diffcol]
                            sidepos = side # Feld wird gespeichert
                            tilepos = tile
                            colpos = diffcol # Farbe wird gespeichert
        tilecol[sidepos][tilepos] = colors[colpos] # Farbe wird geaendert
        tilenum[color] -= 1 # Anzahl Felder wird angepasst
        tilenum[colpos] += 1