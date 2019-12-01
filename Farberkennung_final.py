import cv2
import numpy as np
import sys

# prepare images
cube1 = cv2.imread("Wuerfel_Bilder_final/Bild_10_1.jpg")
cube2 = cv2.imread("Wuerfel_Bilder_final/Bild_10_2.jpg")
pics = [cube1, cube2]

# define stuff

# general

# coordinates of the centers of each tile were read out with "gimp" and then stored in this array
coordinates = [
    [[441, 340], [400, 244], [361, 177], [342, 265], [326, 334],
     [345, 402], [373, 493], [404, 429], [370, 336]],
    [[540, 279], [655, 280], [750, 284], [677, 202], [621, 145],
     [536, 138], [435, 128], [482, 188], [588, 199]],
    [[548, 388], [492, 473], [451, 538], [548, 522], [636, 504],
     [684, 448], [753, 366], [658, 383], [595, 463]],
    [[329, 223], [370, 311], [398, 377], [428, 307], [451, 232],
     [428, 181], [401, 94], [367, 149], [405, 239]],
    [[245, 166], [294, 106], [332, 53], [253, 62], [188, 77],
     [134, 125], [73, 178], [146, 176], [205, 116]],
    [[248, 264], [150, 270], [69, 268], [130, 342], [177, 399],
     [249, 408], [332, 416], [291, 350], [206, 348]]]

# array, in which the HSV values of the tiles are stored
avgcol = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
     [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
     [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
     [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
     [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
     [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],
     [0, 0, 0], [0, 0, 0], [0, 0, 0]]]

# array with the names of the six colors the names can be freely chosen, because the program doesn't recognise the
# absolute colors they were named after the colors that are really on the cube, so it's easier to compare the results
# with the solutions and the pictures
# white is not named white right now, because the program is able to recognise white tiles as "white"
# the order in which the colors must be entered is dependant on the positions of the middle tiles in the pictures
# the order is: picture one top, left, right   picture 2 bottom, left, right
colors = ["orange", "green", "white will be assigned later in the program", "red", "blue", "yellow"]

# array in which the final result will be stored
tilecol = [["nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing"],
           ["nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing"],
           ["nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing"],
           ["nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing"],
           ["nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing"],
           ["nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing", "nothing"]]

# correct solutions to compare with
correct_1 = [["white", "green", "red", "red", "white", "yellow", "red", "green", "blue"],
             ["blue", "orange", "orange", "green", "green", "blue", "yellow", "yellow", "orange"],
             ["orange", "red", "yellow", "orange", "white", "white", "yellow", "blue", "white"],
             ["orange", "green", "orange", "white", "blue", "blue", "green", "orange", "green"],
             ["green", "white", "red", "yellow", "blue", "red", "red", "blue", "red"],
             ["yellow", "yellow", "blue", "white", "green", "red", "white", "orange", "yellow"]]
correct_2 = [["orange", "blue", "green", "green", "orange", "yellow", "red", "green", "blue"],
             ["white", "green", "orange", "green", "red", "orange", "yellow", "white", "red"],
             ["blue", "white", "white", "blue", "yellow", "yellow", "yellow", "red", "yellow"],
             ["blue", "white", "blue", "yellow", "blue", "blue", "red", "orange", "green"],
             ["red", "blue", "green", "red", "green", "orange", "green", "yellow", "orange"],
             ["white", "red", "white", "orange", "orange", "yellow", "yellow", "red", "white"]]
correct_3 = [["red", "green", "green", "green", "yellow", "blue", "red", "orange", "white"],
             ["white", "orange", "orange", "blue", "orange", "yellow", "orange", "white", "blue"],
             ["green", "yellow", "blue", "white", "yellow", "yellow", "yellow", "blue", "orange"],
             ["yellow", "orange", "blue", "white", "blue", "blue", "green", "red", "yellow"],
             ["red", "green", "orange", "red", "white", "red", "red", "white", "green"],
             ["blue", "orange", "green", "yellow", "white", "red", "white", "green", "red"]]
correct_4 = [["blue", "blue", "blue", "orange", "yellow", "white", "white", "green", "red"],
             ["orange", "yellow", "orange", "red", "green", "yellow", "yellow", "yellow", "yellow"],
             ["white", "white", "red", "orange", "red", "white", "yellow", "red", "blue"],
             ["white", "white", "white", "green", "blue", "blue", "green", "blue", "orange"],
             ["green", "red", "yellow", "yellow", "blue", "red", "green", "green", "white"],
             ["orange", "orange", "orange", "blue", "red", "green", "red", "orange", "green"]]
correct_5 = [["red", "white", "green", "white", "orange", "green", "red", "yellow", "white"],
             ["yellow", "blue", "orange", "green", "orange", "red", "yellow", "green", "blue"],
             ["blue", "orange", "blue", "white", "green", "yellow", "yellow", "yellow", "orange"],
             ["green", "red", "white", "red", "blue", "green", "red", "blue", "yellow"],
             ["red", "red", "white", "blue", "white", "orange", "white", "blue", "green"],
             ["yellow", "orange", "blue", "orange", "orange", "yellow", "green", "white", "red"]]
correct_6 = [["white", "yellow", "white", "blue", "white", "blue", "white", "red", "white"],
             ["blue", "blue", "orange", "green", "red", "orange", "red", "orange", "blue"],
             ["orange", "yellow", "red", "orange", "red", "white", "yellow", "yellow", "orange"],
             ["green", "yellow", "blue", "red", "blue", "red", "green", "white", "yellow"],
             ["yellow", "blue", "yellow", "white", "blue", "red", "orange", "green", "green"],
             ["orange", "white", "green", "orange", "green", "green", "yellow", "green", "red"]]
correct_7 = [["orange", "yellow", "red", "yellow", "orange", "green", "white", "green", "red"],
             ["yellow", "orange", "orange", "green", "yellow", "red", "blue", "blue", "green"],
             ["green", "yellow", "red", "orange", "orange", "blue", "yellow", "green", "red"],
             ["white", "red", "green", "red", "blue", "white", "green", "orange", "orange"],
             ["red", "white", "white", "blue", "blue", "white", "white", "red", "blue"],
             ["green", "yellow", "blue", "orange", "yellow", "blue", "red", "white", "white"]]
correct_8 = [["white", "blue", "yellow", "red", "red", "orange", "red", "yellow", "blue"],
             ["orange", "blue", "orange", "orange", "yellow", "yellow", "orange", "orange", "yellow"],
             ["green", "orange", "yellow", "green", "white", "white", "yellow", "white", "orange"],
             ["white", "green", "green", "white", "blue", "red", "blue", "red", "green"],
             ["blue", "green", "orange", "yellow", "blue", "green", "white", "blue", "white"],
             ["red", "red", "green", "yellow", "green", "blue", "red", "white", "red"]]
correct_9 = [["yellow", "orange", "green", "red", "yellow", "red", "white", "blue", "red"],
             ["green", "green", "orange", "blue", "blue", "white", "white", "white", "yellow"],
             ["orange", "orange", "orange", "red", "yellow", "orange", "yellow", "yellow", "blue"],
             ["blue", "red", "white", "white", "blue", "yellow", "red", "blue", "orange"],
             ["red", "yellow", "green", "blue", "green", "green", "blue", "green", "white"],
             ["white", "orange", "red", "white", "red", "green", "orange", "yellow", "green"]]
correct_10 = [["orange", "orange", "green", "yellow", "green", "yellow", "red", "blue", "orange"],
              ["white", "blue", "orange", "blue", "yellow", "blue", "white", "white", "green"],
              ["blue", "red", "blue", "yellow", "yellow", "red", "yellow", "yellow", "white"],
              ["green", "white", "green", "white", "blue", "green", "blue", "red", "red"],
              ["yellow", "white", "red", "orange", "white", "green", "white", "green", "blue"],
              ["orange", "orange", "orange", "red", "red", "orange", "red", "green", "white"]]

# initialize some variables for: lose white
white_question = 0
whitemid = 256
whitemidvar = 0
whiteout = [256, 256, 256, 256, 256, 256, 256, 256]
whiteoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]

# initialize some variables for: lose black
black_question = 0
blackmid = 256
blackmidvar = 0
blackout = [256, 256, 256, 256, 256, 256, 256, 256]
blackoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
blackoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]

# evaluate
# array which holds info on how many tiles of each color there are
tilenum = [0, 0, 0, 0, 0, 0]

# all distances from each tile to each middle
# distance form a tile to a middle is how far apart their hue values are
distances = [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]],
             [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]]]

# find average color of tiles
for i in range(2):
    for j in range(3):
        for k in range(9):
            for l in range(3):
                col = 0
                # average of 400 pixels ( more, and there's a risk, that pixels form other tiles are used,
                # less and it's less accurate)
                for m in range(20):
                    for n in range(20):
                        col += pics[i][coordinates[3 * i + j][k][0] - 10 + m][coordinates[3 * i + j][k][1] - 10 + n][l]
                avgcol[3 * i + j][k][l] = int(col / 400)

# convert to HSV
for i in range(6):
    for j in range(9):
        # convert the RGB values into HSV values
        BGR = np.uint8(
            [[[avgcol[i][j][0], avgcol[i][j][1], avgcol[i][j][2]]]])
        hsv = cv2.cvtColor(BGR, cv2.COLOR_BGR2HSV)
        avgcol[i][j][0] = hsv[0][0][0] * 255 / 179  # make it, so hue ranges also from 0-255
        avgcol[i][j][1] = hsv[0][0][1]
        avgcol[i][j][2] = hsv[0][0][2]
        # counters for how many tiles have low saturation or low value
        # the "70" has to be tuned for each picture
        if avgcol[i][j][1] < 70:
            white_question += 1
            # low value disabled, because the used cube doesn't have black, so it couldn't get tested enough
        if avgcol[i][j][2] < 0:
            black_question += 1

# lose black
# if there are exactly 9 tiles with a low value,
# they will all be called "black" and they will be ignored for the rest of the program
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
    tilecol[blackmidvar][8] = "black"
    avgcol[blackmidvar][8][1] = 255
    colors[blackmidvar] = "black"
    tilenum[blackmidvar] = 9
    for i in range(8):
        tilecol[blackoutvar1[i]][blackoutvar2[i]] = "black"
        if avgcol[blackoutvar1[i]][blackoutvar2[i]][1] < 50:
            avgcol[blackoutvar1[i]][blackoutvar2[i]][1] = 255
            white_question -= 1
elif black_question != 0:
    sys.exit("ERROR!")

# lose white
# if there are exactly 9 tiles with a low saturation,
# they will all be called "white" and they will be ignored for the rest of the program
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
    tilecol[whitemidvar][8] = "white"
    tilenum[whitemidvar] = 9
    colors[whitemidvar] = "white"
    for i in range(8):
        tilecol[whiteoutvar1[i]][whiteoutvar2[i]] = "white"
elif white_question != 0:
    sys.exit("ERROR")

# evaluate middle of each tile
# each tile will be assigned to the middle, which has the most similar hue value
for i in range(6):
    for j in range(9):
        if tilecol[i][j] != "white" and tilecol[i][j] != "black":
            col = 200000
            for k in range(6):
                if tilecol[k][8] != "white" and tilecol[k][8] != "black":
                    dist = 0
                    # because hue is represented in a circle, the distance cannot be bigger than 113
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

# correct number for each middle
# if there are too many side-tiles assigned to one middle,
# the one which is furthest away of said middle, is assigned to another middle, which doesn't have enough side-tiles
for i in range(6):
    while tilenum[i] > 9:
        big_dist = 0
        small_dist = 99999999
        a1 = 0
        a2 = 0
        b = 0
        for j in range(6):
            for k in range(9):
                if tilecol[j][k] == colors[i]:
                    if big_dist < distances[j][k][i]:
                        big_dist = distances[j][k][i]
                        a1 = j
                        a2 = k
        for j in range(6):
            if tilenum[j] < 9:
                if small_dist > distances[a1][a2][j]:
                    small_dist = distances[a1][a2][j]
                    b = j
        tilecol[a1][a2] = colors[b]
        tilenum[b] += 1
        tilenum[i] -= 1

print(tilecol)
cv2.imshow('image', pics[0])
cv2.imshow('imaggre', pics[1])
cv2.waitKey(0)
