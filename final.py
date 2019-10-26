import cv2
import numpy as np
import math as mt
import sys

# prepare images
cube1 = cv2.imread("Wuerfel_normal_Test_1_1_1.jpg")
cube2 = cv2.imread("Wuerfel_normal_Test_1_1_2.jpg")
pics = [cube1, cube2]

# define stuff

# general
coordinates = [
    [[372, 340], [329, 245], [279, 154], [261, 244], [243, 310], [268, 391], [293, 489], [329, 432], [292, 329]],
    [[468, 279], [585, 271], [674, 261], [609, 185], [548, 117], [463, 111], [359, 105], [406, 182], [516, 182]],
    [[473, 392], [418, 467], [373, 529], [469, 506], [552, 488], [609, 431], [681, 359], [583, 377], [522, 447]],
    [[402, 278], [430, 366], [451, 435], [480, 366], [504, 301], [489, 232], [469, 147], [439, 209], [464, 291]],
    [[324, 225], [372, 158], [405, 106], [320, 115], [246, 122], [197, 169], [133, 227], [222, 226], [276, 163]],
    [[310, 307], [213, 313], [127, 312], [181, 383], [227, 439], [300, 451], [377, 465], [350, 394], [258, 391]]]
avgcol = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
colors = ["w", "g", "r", "y", "b", "o"]
tilecol = [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
           ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
           ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
           ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]

# lose white
white_question = 0
whitemid = 256
whitemidvar = 0
whiteout = [256, 256, 256, 256, 256, 256, 256, 256]
whiteoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]

# lose black
black_question = 0
blackmid = 256
blackmidvar = 0
blackout = [256, 256, 256, 256, 256, 256, 256, 256]
blackoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
blackoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]

# evaluate
tilenum = [0, 0, 0, 0, 0, 0]
distances = [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]]

# probability
p = 1
knee = 0.25  # ratio at which probability is 99%
const = np.log(100) / knee

# find average color of tiles
for i in range(2):
    for j in range(3):
        for k in range(9):
            for l in range(3):
                col = 0
                for m in range(20):
                    for n in range(20):
                        col += pics[i][coordinates[3 * i + j][k][0] - 10 + m][coordinates[3 * i + j][k][1] - 10 + n][l]
                avgcol[3 * i + j][k][l] = int(col / 400)

# convert to HSV
for i in range(6):
    for j in range(9):
        BGR = np.uint8([[[avgcol[i][j][0], avgcol[i][j][1], avgcol[i][j][2]]]])
        hsv = cv2.cvtColor(BGR, cv2.COLOR_BGR2HSV)
        avgcol[i][j][0] = hsv[0][0][0] * 255 / 179
        avgcol[i][j][1] = hsv[0][0][1]
        avgcol[i][j][2] = hsv[0][0][2]
        if avgcol[i][j][1] < 50:
            white_question += 1
        if avgcol[i][j][2] < 50:
            black_question += 1

# lose black
if black_question == 9:
    for i in range(6):
        if avgcol[i][8][2] < blackmid:
            blackmid = avgcol[i][8][2]
            blackmidvar = i
        for j in range(8):
            biggestsat = 0
            biggestsatpos = 100
            for k in range(8):
                if avgcol[i][j][2] < blackout[k] and blackout[k] > biggestsat:
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

# lose white
if white_question == 9:
    for i in range(6):
        if avgcol[i][8][1] < whitemid:
            whitemid = avgcol[i][8][1]
            whitemidvar = i
        for j in range(8):
            biggestsat = 0
            biggestsatpos = 100
            for k in range(8):
                if avgcol[i][j][1] < whiteout[k] and whiteout[k] > biggestsat:
                    biggestsat = whiteout[k]
                    biggestsatpos = k
            if biggestsatpos < 100:
                whiteout[biggestsatpos] = avgcol[i][j][1]
                whiteoutvar1[biggestsatpos] = i
                whiteoutvar2[biggestsatpos] = j
    tilecol[whitemidvar][8] = "w"
    tilenum[whitemidvar] = 9
    colors[whitemidvar] = "w"
    for i in range(8):
        tilecol[whiteoutvar1[i]][whiteoutvar2[i]] = "w"
elif white_question != 0:
    sys.exit("ERROR")

# evaluate color of each tile
for i in range(2):
    for j in range(9):
        if tilecol[i][j] != "w" and tilecol[i][j] != "ba":
            col = 200000
            for k in range(6):
                if tilecol[k][8] != "w" and tilecol[k][8] != "ba":
                    dist = 0
                    if abs(avgcol[i][j][0] - avgcol[k][8][0]) > 113:
                        dist += 256 - abs(avgcol[i][j][0] - avgcol[k][8][0])
                    else:
                        dist += abs(avgcol[i][j][0] - avgcol[k][8][0])
                    distances[i][j][k] = dist
                    if dist < col:
                        col = dist
                        tilecol[i][j] = colors[k]
            for k in range(6):
                if tilecol[i][j] == colors[k]:
                    tilenum[k] += 1

# correct number of each color
for i in range(6):
    while tilenum[i] > 9:
        a1 = 0
        a2 = 0
        col = 0
        counter = 0
        small_dist = 99999999
        breaker = 0
        for j in range(6):
            for k in range(8):
                if tilecol[j][k] == colors[i]:
                    for l in range(6):
                        if tilenum[l] < 9 and distances[j][k][l] < small_dist:
                            small_dist = distances[j][k][l]
                            a1 = j
                            a2 = k
                            col = l
        tilecol[a1][a2] = colors[col]
        tilenum[i] -= 1
        tilenum[col] += 1

# probability
for i in range(6):
    if colors[i] != "ba" and colors[i] != "w":
        for j in range(i):
            if colors[j] != "ba" and colors[j] != "w":
                small_disti = 9999999
                small_distj = 9999999
                ai1 = 0
                ai2 = 0
                aj1 = 0
                aj2 = 0
                dist_out = 500
                dist_mid = 500
                for k in range(6):
                    for l in range(9):
                        if tilecol[k][l] == colors[i] and distances[k][l][j] < small_disti:
                            small_disti = distances[k][l][j]
                            ai1 = k
                            ai2 = l
                        elif tilecol[k][l] == colors[j] and distances[k][l][i] < small_distj:
                            small_distj = distances[k][l][i]
                            aj1 = k
                            aj2 = l
                dist_out = abs(avgcol[ai1][ai2][0] - avgcol[aj1][aj2][0])
                if dist_out > 113:
                    dist_out = 256 - dist_out
                dist_mid = abs(avgcol[i][8][0] - avgcol[j][8][0])
                if dist_mid > 113:
                    dist_mid = 256 - dist_mid
                ratio = dist_out / dist_mid
                prob = 1 / (1 + mt.e ** (-(const * ratio)))
                p *= prob

print(tilecol)
cv2.imshow('image', pics[0])
cv2.imshow('imaggre', pics[1])
cv2.waitKey(0)
