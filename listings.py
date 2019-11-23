# find average color of tiles
for rgb in range(3):
    col = 0
    for m in range(20):
        for n in range(20):
            col += picture[x - 10 + m][y - 10 + n][rgb]
    avgcol[side][tile][rgb] = int(col / 400)

# evaluate color of each tile
col = 200000
for middle in range(6):
    dist = 0
    for rgb in range(3):
        dist += (avgcol[side][tile][rgb]-avgcol[middle][8][rgb]) ** 2
    distances[side][tile][middle] = mt.sqrt(dist)
    if dist < col:
        col = dist
        tilecol[side][tile] = colors[middle]



if avgcol[side][tile][1] < 70:
    white_question += 1
if avgcol[side][tile][2] < 0:
    black_question += 1



if black_question == 9:
    for side in range(6):
        if avgcol[side][8][2] < lowvaluemid:
            lowvaluemid = avgcol[side][8][2]
            blackmidposition = side
    tilecol[blackmidposition][8] = "black"
    colors[blackmidposition] = "black"
    tilenum[blackmidposition] = 9
elif black_question != 0:
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
                    if big_dist < distances[side][tile][color]:
                        big_dist = distances[side][tile][color]
                        sidetpos = side
                        tilepos = tile
        for othercolor in range(6):
            if tilenum[othercolor] < 9:
                if small_dist > distances[sidetpos][tilepos][othercolor]:
                    small_dist = distances[sidetpos][tilepos][othercolor]
                    colpos = othercolor
        tilecol[sidetpos][tilepos] = colors[colpos]
        tilenum[colpos] += 1
        tilenum[color] -= 1