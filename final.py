import cv2
import numpy as np
import math as mt
import sys



#prepare images
cube1 = cv2.imread("Wuerfel_normal_Test_1_1_1.jpg")
cube2 = cv2.imread("Wuerfel_normal_Test_1_1_2.jpg")
pics_list = [cube1, cube2]



#define stuff

#general
coordinates = [[[[372,340],[329,245],[279,154],[261,244],[243,310],[268,391],[293,489],[329,432],[292,329]],[[468,279],[585,271],[674,261],[609,185],[548,117],[463,111],[359,105],[406,182],[516,182]],[[473,392],[418,467],[373,529],[469,506],[552,488],[609,431],[681,359],[583,377],[522,447]]],[[[402,278],[430,366],[451,435],[480,366],[504,301],[489,232],[469,147],[439,209],[464,291]],[[324,225],[372,158],[405,106],[320,115],[246,122],[197,169],[133,227],[222,226],[276,163]],[[310,307],[213,313],[127,312],[181,383],[227,439],[300,451],[377,465],[350,394],[258,391]]]]
avgcol = [[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]]
colors = ["w", "g", "r", "y", "b", "o"]
tilecol = [[["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]], [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]]

#lose white
white_question = 0
whitemid = 256
whitemidvar1 = 0
whitemidvar2 = 0
whiteout = [256, 256, 256, 256, 256, 256, 256, 256]
whiteoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar3 = [0, 0, 0, 0, 0, 0, 0, 0]

#lose black
black_question = 0
blackmid = 256
blackmidvar1 = 0
blackmidvar2 = 0
blackout = [256, 256, 256, 256, 256, 256, 256, 256]
blackoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
blackoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]
blackoutvar3 = [0, 0, 0, 0, 0, 0, 0, 0]

#evaluate
tilenum = [0, 0, 0, 0, 0, 0]
distances = [[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]], [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]]]



#find average color of tiles
for i in range(2):
    for j in range(3):
        for k in range(9):
            for l in range(3):
                col = 0
                for m in range(20):
                    for n in range(20):
                        col += pics_list[i][coordinates[i][j][k][0]-10+m][coordinates[i][j][k][1]-10+n][l]
                avgcol[i][j][k][l] = col/400


#convert to HSV
for i in range(2):
    for j in range(3):
        for k in range(9):
            BGR = np.uint8([[[avgcol[i][j][k][0], avgcol[i][j][k][1], avgcol[i][j][k][2]]]])
            hsv = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
            avgcol[i][j][k][0] = hsv[0][0][0] * 255 / 179
            avgcol[i][j][k][1] = hsv[0][0][1]
            avgcol[i][j][k][2] = hsv[0][0][2]
            if avgcol[i][j][k][1] < 50:
                white_question += 1
            if avgcol[i][j][k][2] < 50:
                black_question += 1



#lose black
if black_question == 9:
    for i in range(2):
        for j in range(3):
            if avgcol[i][j][8][2] < blackmid:
                blackmid = avgcol[i][j][8][2]
                blackmidvar1 = i
                blackmidvar2 = j
            for k in range(8):
                biggestsat = 0
                biggestsatpos = 100
                for l in range(8):
                    if avgcol[i][j][k][2] < blackout[l] and blackout[l] > biggestsat:
                        biggestsat = blackout[l]
                        biggestsatpos = l
                if biggestsatpos < 100:
                    blackout[biggestsatpos] = avgcol[i][j][k][2]
                    blackoutvar1[biggestsatpos] = i
                    blackoutvar2[biggestsatpos] = j
                    blackoutvar3[biggestsatpos] = k
    tilecol[blackmidvar1][blackmidvar2][8] = "ba"
    avgcol[blackmidvar1][blackmidvar2][8][1] = 255
    colors[3 * blackmidvar1 + blackmidvar2] = "ba"
    tilenum[3 * blackmidvar1 + blackmidvar2] = 9
    for i in range(8):
        tilecol[blackoutvar1[i]][blackoutvar2[i]][blackoutvar3[i]] = "ba"
        if avgcol[blackoutvar1[i]][blackoutvar2[i]][blackoutvar3[i]][1] < 50:
            avgcol[blackoutvar1[i]][blackoutvar2[i]][blackoutvar3[i]][1] = 255
            white_question -= 1
elif black_question != 0:
    sys.exit("ERROR!")


#lose white
if white_question == 9:
    for i in range(2):
        for j in range(3):
            if avgcol[i][j][8][1] < whitemid:
                whitemid = avgcol[i][j][8][1]
                whitemidvar1 = i
                whitemidvar2 = j
            for k in range(8):
                biggestsat = 0
                biggestsatpos = 100
                for l in range(8):
                    if avgcol[i][j][k][1] < whiteout[l] and whiteout[l] > biggestsat:
                        biggestsat = whiteout[l]
                        biggestsatpos = l
                if biggestsatpos < 100:
                    whiteout[biggestsatpos] = avgcol[i][j][k][1]
                    whiteoutvar1[biggestsatpos] = i
                    whiteoutvar2[biggestsatpos] = j
                    whiteoutvar3[biggestsatpos] = k
    tilecol[whitemidvar1][whitemidvar2][8] = "w"
    tilenum[3 * whitemidvar1 + whitemidvar2] = 9
    colors[3 * whitemidvar1 + whitemidvar2] = "w"
    for i in range(8):
        tilecol[whiteoutvar1[i]][whiteoutvar2[i]][whiteoutvar3[i]] = "w"
elif white_question != 0:
    sys.exit("ERROR")



#evaluate color of each tile
for i in range(2):
    for j in range(3):
        for k in range(9):
            if tilecol[i][j][k] != "w" and tilecol[i][j][k] != "ba":
                col = 200000
                for l in range(6):
                    l_2 = 0
                    l_3 = 0
                    if l - 3 < 0:
                        l_3 = l
                    else:
                        l_2 = 1
                        l_3 = l-3
                    if tilecol[l_2][l_3][8] != "w" and tilecol[l_2][l_3][8] != "ba":
                        dist = 0
                        if abs(avgcol[i][j][k][0]-avgcol[l_2][l_3][8][0]) > 113:
                            dist += 256 -abs(avgcol[i][j][k][0]-avgcol[l_2][l_3][8][0])
                        else:
                            dist += abs(avgcol[i][j][k][0]-avgcol[l_2][l_3][8][0])
                        distances[i][j][k][l] = dist
                        if dist < col:
                            col = dist
                            tilecol[i][j][k] = colors[l]
                for l in range(6):
                    if tilecol[i][j][k] == colors[l]:
                        tilenum[l] += 1



#correct number of each color
for i in range(6):
    while tilenum[i] > 9:
        a1 = 0
        a2 = 0
        a3 = 0
        col = 0
        counter = 0
        small_dist = 99999999
        breaker = 0
        for j in range(2):
            for k in range(3):
                for l in range(8):
                    if tilecol[j][k][l] == colors[i]:
                        for m in range(6):
                            if tilenum[m] < 9 and distances[j][k][l][m] < small_dist:
                                small_dist = distances[j][k][l][m]
                                a1 = j
                                a2 = k
                                a3 = l
                                col = m
        tilecol[a1][a2][a3] = colors[col]
        tilenum[i] -= 1
        tilenum[col] += 1


#probability
p = 1
knee = 0.25 # ratio at which probability is 99%
const = np.log(100) / knee
for i in range(6):
    if colors[i] != "ba" and colors[i] != "w":
        if i > 2:
            i1 = 1
            i2 = i-3
        else:
            i1 = 0
            i2 = i
        for j in range(i):
            if colors[j] != "ba" and colors[j] != "w":
                if j > 2:
                    j1 = 1
                    j2 = j-3
                else:
                    j1 = 0
                    j2 = j
                small_disti = 9999999
                small_distj = 9999999
                ai1 = 0
                ai2 = 0
                ai3 = 0
                aj1 = 0
                aj2 = 0
                aj3 = 0
                dist_out = 500
                dist_mid = 500
                for k in range(2):
                    for l in range(3):
                        for m in range(9):
                            if tilecol[k][l][m] == colors[i] and distances[k][l][m][j] < small_disti:
                                small_disti = distances[k][l][m][j]
                                ai1 = k
                                ai2 = l
                                ai3 = m
                            elif tilecol[k][l][m] == colors[j] and distances[k][l][m][i] < small_distj:
                                small_distj = distances[k][l][m][i]
                                aj1 = k
                                aj2 = l
                                aj3 = m
                dist_out = abs(avgcol[ai1][ai2][ai3][0] - avgcol[aj1][aj2][aj3][0])
                if dist_out > 113:
                    dist_out = 256 - dist_out
                dist_mid = abs(avgcol[i1][i2][8][0] - avgcol[j1][j2][8][0])
                if dist_mid > 113:
                    dist_mid = 256 - dist_mid
                ratio = dist_out / dist_mid
                prob = 1 / (1+mt.e**(-(const*ratio)))
                p *= prob





print(tilecol)
cv2.imshow('image',pics_list[0])
cv2.imshow('imaggre',pics_list[1])
cv2.waitKey(0)