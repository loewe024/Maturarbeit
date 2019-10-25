import cv2
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import math as mt

#prepare images
cube1 = cv2.imread("Wuerfel_normal_Test_1_1_1.jpg")
cube2 = cv2.imread("Wuerfel_normal_Test_1_1_2.jpg")
scale_percent = 100 # percent of original size
width = int(cube1.shape[1] * scale_percent / 100)
height = int(cube1.shape[0] * scale_percent / 100)
dim = (width, height)
resized1 = cv2.resize(cube1, dim)
resized2 = cv2.resize(cube2, dim)
resized_list = [resized1, resized2]


#define stuff

#general
coordinates = [[[[372,340],[329,245],[279,154],[261,244],[243,310],[268,391],[293,489],[329,432],[292,329]],[[468,279],[585,271],[674,261],[609,185],[548,117],[463,111],[359,105],[406,182],[516,182]],[[473,392],[418,467],[373,529],[469,506],[552,488],[609,431],[681,359],[583,377],[522,447]]],[[[402,278],[430,366],[451,435],[480,366],[504,301],[489,232],[469,147],[439,209],[464,291]],[[324,225],[372,158],[405,106],[320,115],[246,122],[197,169],[133,227],[222,226],[276,163]],[[310,307],[213,313],[127,312],[181,383],[227,439],[300,451],[377,465],[350,394],[258,391]]]]
avgcol = [[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]]
colors = ["w", "g", "r", "y", "b", "o"]
tilecol_correct_1_1 = [[["r", "r", "o", "w", "w", "y", "o", "r", "w"], ["y", "y", "g", "y", "y", "w", "g", "w", "g"], ["b", "g", "g", "y", "r", "o", "w", "g", "r"]], [["r", "b", "b", "r", "r", "g", "b", "w", "y"], ["y", "g", "w", "o", "w", "b", "b", "b", "b"], ["g", "r", "o", "b", "y", "o", "o", "o", "o"]]]
tilecol_correct_1_2 = [[["r", "b", "b", "r", "r", "g", "b", "w", "y"], ["g", "r", "o", "b", "y", "o", "o", "o", "o"], ["y", "g", "w", "o", "w", "b", "b", "b", "b"]], [["r", "r", "o", "w", "w", "y", "o", "r", "w"], ["b", "g", "g", "y", "r", "o", "w", "g", "r"], ["y", "y", "g", "y", "y", "w", "g", "w", "g"]]]
tilecol_correct_2_1 = [[["y", "r", "o", "o", "b", "r", "o", "r", "b"], ["r", "w", "g", "o", "y", "o", "g", "b", "w"], ["g", "g", "w", "b", "w", "g", "o", "g", "r"]], [["w", "r", "r", "w", "w", "y", "g", "o", "g"], ["b", "g", "r", "w", "b", "w", "y", "b", "y"], ["r", "y", "o", "y", "y", "b", "b", "y", "o"]]]
tilecol_correct_2_2 = [[["w", "r", "r", "w", "w", "y", "g", "o", "g"], ["r", "y", "o", "y", "y", "b", "b", "y", "o"], ["b", "g", "r", "w", "b", "w", "y", "b", "y"]], [["y", "r", "o", "o", "b", "r", "o", "r", "b"], ["g", "g", "w", "b", "w", "g", "o", "g", "r"], ["r", "w", "g", "o", "y", "o", "g", "b", "w"]]]
tilecol = [[["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]], [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]]

#lose white
white_question = 0
whitemid = 256
midvar1 = 0
midvar2 = 0
whiteout = [256, 256, 256, 256, 256, 256, 256, 256]
whiteoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar3 = [0, 0, 0, 0, 0, 0, 0, 0]

#evaluate
tilenum = [0, 0, 0, 0, 0, 0]
distances = [[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]], [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]]]
varnum = 1 #how many variables to find color (H, S, V, R, G, B)



#find average color of tiles
for i in range(2):
    for j in range(3):
        for k in range(9):
            for l in range(3):
                col = 0
                #cv2.rectangle(resized_list[i], (coordinates[i][j][k][1]-10, coordinates[i][j][k][0]-10), (coordinates[i][j][k][1]+9, coordinates[i][j][k][0]+9), (0,0,0), -1)
                for m in range(20):
                    for n in range(20):
                        col += resized_list[i][coordinates[i][j][k][0]-10+m][coordinates[i][j][k][1]-10+n][l]
                avgcol[i][j][k][l] = col/400

#convert to HSV
for i in range(2):
    for j in range(3):
        for k in range(9):
            BGR = np.uint8([[[avgcol[i][j][k][0], avgcol[i][j][k][1], avgcol[i][j][k][2]]]])
            hsv = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
            #print(BGR)
            #print(hsv)
            avgcol[i][j][k][0] = hsv[0][0][0] * 255 / 179
            avgcol[i][j][k][1] = hsv[0][0][1]
            avgcol[i][j][k][2] = hsv[0][0][2]
            if avgcol[i][j][k][1] < 50:
                white_question = 1
        print("----------")

#lose white
if white_question == 1:
    for i in range(2):
        for j in range(3):
            if avgcol[i][j][8][1] < whitemid:
                whitemid = avgcol[i][j][8][1]
                midvar1 = i
                midvar2 = j
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
    tilecol[midvar1][midvar2][8] = "w"
    tilenum[3 * midvar1 + midvar2] = 9
    for i in range(8):
        tilecol[whiteoutvar1[i]][whiteoutvar2[i]][whiteoutvar3[i]] = "w"

#evaluate color of each tile
for i in range(2):
    for j in range(3):
        for k in range(9):
            if tilecol[i][j][k] != "w":
                col = 200000
                for l in range(6):
                    l_2 = 0
                    l_3 = 0
                    if l - 3 < 0:
                        l_3 = l
                    else:
                        l_2 = 1
                        l_3 = l-3
                    if tilecol[l_2][l_3][8] != "w":
                        dist = 0
                        for m in range(varnum):
                            if abs(avgcol[i][j][k][m]-avgcol[l_2][l_3][8][m]) > 113:
                                dist += 256 -abs(avgcol[i][j][k][m]-avgcol[l_2][l_3][8][m])
                            else:
                                dist += abs(avgcol[i][j][k][m]-avgcol[l_2][l_3][8][m])
                            #dist += mt.sqrt((avgcol[i][j][k][m]-avgcol[l_2][l_3][8][m]) ** 2)
                        distances[i][j][k][l] = dist
                        if dist < col:
                            col = dist
                            tilecol[i][j][k] = colors[l]
                for l in range(6):
                    if tilecol[i][j][k] == colors[l]:
                        tilenum[l] += 1
print(tilecol)
#correct number of each color



#method 2 for correct number
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
    if i > 2:
        i1 = 1
        i2 = i-3
    else:
        i1 = 0
        i2 = i
    for j in range(i):
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
        print(prob)
        p *= prob

print(p)


#calculate number of errors
error = 0
for i in range(2):
    for j in range(3):
        for k in range(9):
            if tilecol[i][j][k] != tilecol_correct_1_1[i][j][k]:
                error += 1


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


for i in range(2):
    for j in range(3):
        for k in range(9):
            if tilecol_correct_1_1[i][j][k] == "r":
                print(avgcol[i][j][k], "r")
                ax.scatter(avgcol[i][j][k][0], avgcol[i][j][k][1], avgcol[i][j][k][2], color = 'red', marker = 'o')
            elif tilecol_correct_1_1[i][j][k] == "o":
                ax.scatter(avgcol[i][j][k][0], avgcol[i][j][k][1], avgcol[i][j][k][2], color = 'orange', marker = 'o')
                print(avgcol[i][j][k], "o")



for k in range(7):
    for j in range(7):
        ax.plot([0, 256], [50*j, 50*j], [50*k, 50*k], color = "grey", linestyle = ":")
        ax.plot([50*j, 50*j], [0, 256], [50*k, 50*k], color = "grey", linestyle = ":")
        ax.plot([50*k, 50*k], [50*j, 50*j], [0, 256], color = "grey", linestyle = ":")


ax.grid(True)
#plt.show()
print(tilecol)
print(tilecol_correct_1_1)
print(error)
print(distances)

cv2.imshow('image',resized_list[0])
cv2.imshow('imaggre',resized_list[1])
cv2.waitKey(0)

