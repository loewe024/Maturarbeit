import cv2
import numpy as np
import math as mt
import sys

# prepare images
cube1 = cv2.imread("Wuerfel_Bilder_final/Bild_10_1.jpg")
cube2 = cv2.imread("Wuerfel_Bilder_final/Bild_10_2.jpg")

pics = [cube1, cube2]

# define stuff

# general
coordinates = [
    [[441, 340], [400, 244], [361, 177], [342, 265], [326, 334], [345, 402], [373, 493], [404, 429], [370, 336]],
    [[540, 279], [655, 280], [750, 284], [677, 202], [621, 145], [536, 138], [435, 128], [482, 188], [588, 199]],
    [[548, 388], [492, 473], [451, 538], [548, 522], [636, 504], [684, 448], [753, 366], [658, 383], [595, 463]],
    [[329, 223], [370, 311], [398, 377], [428, 307], [451, 239], [428, 181], [401, 94], [367, 149], [405, 239]],
    [[245, 166], [294, 106], [332, 53], [253, 62], [188, 77], [134, 125], [73, 178], [146, 176], [205, 116]],
    [[248, 264], [150, 270], [69, 268], [130, 342], [177, 399], [249, 408], [332, 416], [291, 350], [206, 348]]]
avgcol = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
          [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
colors = ["b", "o", "w", "g", "r", "y"]
tilecol = [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
           ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
           ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"],
           ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]

correct_1 = [["w", "g", "r", "r", "w", "y", "r", "g", "b"], ["b", "o", "o", "g", "g", "b", "y", "y", "o"],
             ["o", "r", "y", "o", "w", "w", "y", "b", "w"],
             ["o", "g", "o", "w", "b", "b", "g", "o", "g"], ["g", "w", "r", "y", "b", "r", "r", "b", "r"],
             ["y", "y", "b", "w", "g", "r", "w", "o", "y"]]
correct_2 = [["o", "b", "g", "g", "o", "y", "r", "g", "b"], ["w", "g", "o", "g", "r", "o", "y", "w", "r"],
             ["b", "w", "w", "b", "y", "y", "y", "r", "y"],
             ["b", "w", "b", "y", "b", "b", "r", "o", "g"], ["r", "b", "g", "r", "g", "o", "g", "y", "o"],
             ["w", "r", "w", "o", "o", "y", "y", "r", "w"]]
correct_3 = [["r", "g", "g", "g", "y", "b", "r", "o", "w"], ["w", "o", "o", "b", "o", "y", "o", "w", "b"],
             ["g", "y", "b", "w", "y", "y", "y", "b", "o"],
             ["y", "o", "b", "w", "b", "b", "g", "r", "y"], ["r", "g", "o", "r", "w", "r", "r", "w", "g"],
             ["b", "o", "g", "y", "w", "r", "w", "g", "r"]]
correct_4 = [["b", "b", "b", "o", "y", "w", "w", "g", "r"], ["o", "y", "o", "r", "g", "y", "y", "y", "y"],
             ["w", "w", "r", "o", "r", "w", "y", "r", "b"],
             ["w", "w", "w", "g", "b", "b", "g", "b", "o"], ["g", "r", "y", "y", "b", "r", "g", "g", "w"],
             ["o", "o", "o", "b", "r", "g", "r", "o", "g"]]
correct_5 = [["r", "w", "g", "w", "o", "g", "r", "y", "w"], ["y", "b", "o", "g", "o", "r", "y", "g", "b"],
             ["b", "o", "b", "w", "g", "y", "y", "y", "o"],
             ["g", "r", "w", "r", "b", "g", "r", "b", "y"], ["r", "r", "w", "b", "w", "o", "w", "b", "g"],
             ["y", "o", "b", "o", "o", "y", "g", "w", "r"]]
correct_6 = [["w", "y", "w", "b", "w", "b", "w", "r", "w"], ["b", "b", "o", "g", "r", "o", "r", "o", "b"],
             ["o", "y", "r", "o", "r", "w", "y", "y", "o"],
             ["g", "y", "b", "r", "b", "r", "g", "w", "y"], ["y", "b", "y", "w", "b", "r", "o", "g", "g"],
             ["o", "w", "g", "o", "g", "g", "y", "g", "r"]]
correct_7 = [["o", "y", "r", "y", "o", "g", "w", "g", "r"], ["y", "o", "o", "g", "y", "r", "b", "b", "g"],
             ["g", "y", "r", "o", "o", "b", "y", "g", "r"],
             ["w", "r", "g", "r", "b", "w", "g", "o", "o"], ["r", "w", "w", "b", "b", "w", "w", "r", "b"],
             ["g", "y", "b", "o", "y", "b", "r", "w", "w"]]
correct_8 = [["w", "b", "y", "r", "r", "o", "r", "y", "b"], ["o", "b", "o", "o", "y", "y", "o", "o", "y"],
             ["g", "o", "y", "g", "w", "w", "y", "w", "o"],
             ["w", "g", "g", "w", "b", "r", "b", "r", "g"], ["b", "g", "o", "y", "b", "g", "w", "b", "w"],
             ["r", "r", "g", "y", "g", "b", "r", "w", "r"]]
correct_9 = [["y", "o", "g", "r", "y", "r", "w", "b", "r"], ["g", "g", "o", "b", "b", "w", "w", "w", "y"],
             ["o", "o", "o", "r", "w", "o", "w", "w", "b"],
             ["b", "r", "w", "w", "b", "y", "r", "b", "o"], ["r", "y", "g", "b", "g", "g", "b", "g", "w"],
             ["w", "o", "r", "w", "r", "g", "o", "y", "g"]]
correct_10 = [["o", "o", "g", "y", "g", "y", "r", "b", "o"], ["w", "b", "o", "b", "y", "b", "w", "w", "g"],
              ["b", "r", "b", "y", "y", "r", "y", "y", "w"],
              ["g", "w", "g", "w", "b", "g", "b", "r", "r"], ["y", "w", "r", "o", "w", "g", "w", "g", "b"],
              ["o", "o", "o", "r", "r", "o", "r", "g", "w"]]
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
                #cv2.rectangle(pics[i], (coordinates[3 * i + j][k][1]-10, coordinates[3 * i + j][k][0]-10), (coordinates[3 * i + j][k][1]+9, coordinates[3 * i + j][k][0]+9), (0,0,0), -1)
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
        if avgcol[i][j][2] < 10:
            black_question += 1
cv2.waitKey(0)
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
for i in range(6):
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
