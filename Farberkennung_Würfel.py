import cv2
import numpy as np

#prepare images
cube1 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_ungeloest_neu_1.jpg")
cube2 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_ungeloest_neu_2_1.jpg")
scale_percent = 100 # percent of original size
width = int(cube1.shape[1] * scale_percent / 100)
height = int(cube1.shape[0] * scale_percent / 100)
dim = (width, height)
resized1 = cv2.resize(cube1, dim)
resized2 = cv2.resize(cube2, dim)
resized_list = [resized1, resized2]


#define stuff

#general
coordinates = [[[[376,354],[329,245],[289,153],[264,240],[243,310],[268,391],[293,489],[329,432],[292,329]],[[474,301],[591,287],[678,270],[607,191],[548,125],[474,118],[371,111],[422,194],[526,195]],[[481,409],[419,479],[375,534],[471,511],[560,491],[614,435],[681,365],[588,389],[520,458]]],[[[395,265],[426,357],[449,429],[479,357],[502,299],[488,227],[467,141],[436,197],[460,283]],[[311,211],[364,149],[407,97],[315,106],[239,114],[189,166],[127,228],[212,224],[268,158]],[[310,307],[213,313],[127,312],[181,383],[227,439],[300,451],[377,465],[350,394],[258,391]]]]
avgcol = [[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]]
colors = ["yellow", "orange", "blue", "white", "red", "green"]
tilecol_correct = [[["yellow", "blue  ", "red   ", "blue  ", "white ", "orange", "green ", "yellow", "white "], ["blue  ", "white ", "orange", "green ", "red   ", "yellow", "white ", "yellow", "green "], ["red   ", "green ", "orange", "red   ", "white ", "orange", "yellow", "red   ", "red   "]], [["green ", "orange", "yellow", "white ", "blue  ", "green ", "orange", "orange", "yellow"], ["red   ", "blue  ", "orange", "red   ", "blue  ", "red   ", "green ", "yellow", "orange"], ["white ", "white ", "green ", "green ", "yellow", "blue  ", "blue  ", "white ", "blue  "]]]

#method 1
tilecol_1 = [[["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]], [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]]
tilenum_1 = [0, 0, 0, 0, 0, 0]
f = 0.2 #relativer Faktor
a = 255 #absoluter Faktor
boundaries = [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]

#method 2
tilecol_2 = [[["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]], [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]]
tilenum_2 = [0, 0, 0, 0, 0, 0]
distances = [[[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]], [[[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]]]


#find average color of tiles
for i in range(2):
    for j in range(3):
        for k in range(9):
            for l in range(3):
                col = 0
                cv2.rectangle(resized_list[i], (coordinates[i][j][k][1]-12, coordinates[i][j][k][0]-12), (coordinates[i][j][k][1]+12, coordinates[i][j][k][0]+12), (0,0,0), -1)
                for m in range(25):
                    for n in range(25):
                        col += resized_list[i][coordinates[i][j][k][0]-12+m][coordinates[i][j][k][1]-12+n][l]
                avgcol[i][j][k][l] = col/625



for i in range(2):
    for j in range(3):
        for k in range(9):
            BGR = np.uint8([[[avgcol[i][j][k][0], avgcol[i][j][k][1], avgcol[i][j][k][2]]]])
            hsv = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
            print(hsv)
        print("----------")
#method 1: shrinking boundaries

#define boundaries of middle
for i in range (2): # coordinates1/2
    for j in range (3): #m1/2/3
        for k in range (3): # colors
            m_c = avgcol[i][j][8][k]
            boundaries[j+3*i][k][0] = m_c - a
            boundaries[j+3*i][k][1] = m_c + a

#match tiles to a middle
for i in range(2): #coordinates1/2
    for j in range(3): #side
        for k in range(9): #tile
            extra = 0
            col = 0
            while True:
                num = 0
                for l in range(6): #test for six colors
                    var = 0
                    for m in range(3): #BGR
                        if avgcol[i][j][k][m] >= (boundaries[l][m][0] + extra) and  avgcol[i][j][k][m] <= (boundaries[l][m][1] - extra):
                            var += 1
                    if var == 3:
                        col = l
                        num += 1
                if num > 1:
                    extra += 1
                else:
                    break
            tilecol_1[i][j][k] = colors[col]
            tilenum_1[col] += 1

#correct number of each color
for i in range(6): #six colors
    extra2 = 255
    stayorchange = [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]]
    socvar = 0
    while tilenum_1[i] > 9:
        for j in range(2):
            for k in range(3):
                for l in range(9):
                    if tilecol_1[j][k][l] == colors[i]:
                        extra2 -= 1
                        for m in range(6): #test for six colors
                            var = 0
                            for n in range(3): #BGR
                                if avgcol[j][k][l][n] >= (boundaries[m][n][0] + extra2) and  avgcol[j][k][l][n] <= (boundaries[m][n][1] - extra2):
                                    var += 1
                            if var == 3 and colors[m] == colors[i] and socvar < 9 and stayorchange[j][k][l] == 0:
                                socvar += 1
                                stayorchange[j][k][l] = 1
                            if var == 3 and colors[m] != colors[i] and tilenum_1[i] > 9 and tilenum_1[m] < 9 and stayorchange[j][k][l] == 0:
                                tilecol_1[j][k][l] = colors[m]
                                tilenum_1[i] -= 1
                                tilenum_1[m] += 1




#method 2: calculate distance to middle values

#evaluate color of each tile
for i in range(2):
    for j in range(3):
        for k in range(9):
            col = 200000
            for l in range(6):
                l_2 = 0
                l_3 = 0
                if l - 3 < 0:
                    l_3 = l
                else:
                    l_2 = 1
                    l_3 = l-3
                dist = 0
                for m in range(3):
                    dist += (avgcol[i][j][k][m]-avgcol[l_2][l_3][8][m]) ** 2
                distances[i][j][k][l] = dist
                if dist < col:
                    col = dist
                    tilecol_2[i][j][k] = colors[l]
            for l in range(6):
                if tilecol_2[i][j][k] == colors[l]:
                    tilenum_2[l] += 1

#correct number of each color
for i in range(6):
    while tilenum_2[i] > 9:
        a1 = 0
        a2 = 0
        a3 = 0
        counter = 0
        big_dist = 0
        breaker = 0
        for j in range(2):
            for k in range(3):
                for l in range(9):
                    if tilecol_2[j][k][l] == colors[i] and distances[j][k][l][i] > big_dist:
                        big_dist = distances[j][k][l][i]
                        a1 = j
                        a2 = k
                        a3 = l
        while breaker == 0:
            for j in range(6):
                if tilenum_2[j] < 9 and distances[a1][a2][a3][j] < counter:
                    tilecol_2[a1][a2][a3] = colors[j]
                    tilenum_2[i] -= 1
                    tilenum_2[j] += 1
                    breaker = 1
                else: counter += 1




#print results
print(tilecol_1)
print(tilecol_2)

cv2.imshow('image',resized_list[0])
cv2.imshow('imaggre',resized_list[1])
cv2.waitKey(0)