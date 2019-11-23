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
    for i in range(6):
        if avgcol[i][8][2] < blackmid:
            blackmid = avgcol[i][8][2]
            blackmidvar = i
        for j in range(8):
            biggestsat = 0
            biggestsatpos = 100
            for k in range(8):
                if avgcol[i][j][2] < blackout[k] and blackout[
                    k] > biggestsat:
                    biggestsat = blackout[k]
                    biggestsatpos = k
            if biggestsatpos < 100:
                blackout[biggestsatpos] = avgcol[i][j][2]
                blackoutvar1[biggestsatpos] = i
                blackoutvar2[biggestsatpos] = j
    tilecol[blackmidvar][8] = "ba"
    avgcol[blackmidvar][8][1] = 255
    colors[blackmidvar] = "ba"
    tilenum[blackmidvar] = 9
    for i in range(8):
        tilecol[blackoutvar1[i]][blackoutvar2[i]] = "ba"
        if avgcol[blackoutvar1[i]][blackoutvar2[i]][1] < 50:
            avgcol[blackoutvar1[i]][blackoutvar2[i]][1] = 255
            white_question -= 1
elif black_question != 0:
    sys.exit("ERROR!")