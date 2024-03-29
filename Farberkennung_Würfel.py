import cv2
import numpy as np
import math as mt

#prepare images
cube1 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_normal_Test_2_1_1.jpg")
cube2 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_normal_Test_2_1_2.jpg")
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
colors = ["b", "w", "r", "g", "y", "o"]
tilecol_correct_1_1 = [[["r", "r", "o", "w", "w", "y", "o", "r", "w"], ["y", "y", "g", "y", "y", "w", "g", "w", "g"], ["b", "g", "g", "y", "r", "o", "w", "g", "r"]], [["r", "b", "b", "r", "r", "g", "b", "w", "y"], ["y", "g", "w", "o", "w", "b", "b", "b", "b"], ["g", "r", "o", "b", "y", "o", "o", "o", "o"]]]
tilecol_correct_1_2 = [[["r", "b", "b", "r", "r", "g", "b", "w", "y"], ["g", "r", "o", "b", "y", "o", "o", "o", "o"], ["y", "g", "w", "o", "w", "b", "b", "b", "b"]], [["r", "r", "o", "w", "w", "y", "o", "r", "w"], ["b", "g", "g", "y", "r", "o", "w", "g", "r"], ["y", "y", "g", "y", "y", "w", "g", "w", "g"]]]
tilecol_correct_2_1 = [[["y", "r", "o", "o", "b", "r", "o", "r", "b"], ["r", "w", "g", "o", "y", "o", "g", "b", "w"], ["g", "g", "w", "b", "w", "g", "o", "g", "r"]], [["w", "r", "r", "w", "w", "y", "g", "o", "g"], ["b", "g", "r", "w", "b", "w", "y", "b", "y"], ["r", "y", "o", "y", "y", "b", "b", "y", "o"]]]
tilecol_correct_2_2 = [[["w", "r", "r", "w", "w", "y", "g", "o", "g"], ["r", "y", "o", "y", "y", "b", "b", "y", "o"], ["b", "g", "r", "w", "b", "w", "y", "b", "y"]], [["y", "r", "o", "o", "b", "r", "o", "r", "b"], ["g", "g", "w", "b", "w", "g", "o", "g", "r"], ["r", "w", "g", "o", "y", "o", "g", "b", "w"]]]

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

#hsv or rgb
hsg = 1 # how many variables to describe the color


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



for i in range(2):
    for j in range(3):
        for k in range(9):
            BGR = np.uint8([[[avgcol[i][j][k][0], avgcol[i][j][k][1], avgcol[i][j][k][2]]]])
            hsv = cv2.cvtColor(BGR,cv2.COLOR_BGR2HSV)
            #print(BGR)
            print(hsv)
            avgcol[i][j][k][0] = hsv[0][0][0] * 255 / 179
            #avgcol[i][j][k][1] = hsv[0][0][1]
            #avgcol[i][j][k][2] = hsv[0][0][2]
        print("----------")
#method 1: shrinking boundaries

#define boundaries of middle
for i in range (2): # coordinates1/2
    for j in range (3): #m1/2/3
        for k in range (hsg): # colors
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
                    for m in range(hsg): #colors
                        if avgcol[i][j][k][m] >= (boundaries[l][m][0] + extra) and  avgcol[i][j][k][m] <= (boundaries[l][m][1] - extra):
                            var += 1
                    if var == hsg:
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
                            for n in range(hsg): #colors
                                if avgcol[j][k][l][n] >= (boundaries[m][n][0] + extra2) and  avgcol[j][k][l][n] <= (boundaries[m][n][1] - extra2):
                                    var += 1
                            if var == hsg and colors[m] == colors[i] and socvar < 9 and stayorchange[j][k][l] == 0:
                                socvar += 1
                                stayorchange[j][k][l] = 1
                            if var == hsg and colors[m] != colors[i] and tilenum_1[i] > 9 and tilenum_1[m] < 9 and stayorchange[j][k][l] == 0:
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
                for m in range(hsg):
                    dist += (avgcol[i][j][k][m]-avgcol[l_2][l_3][8][m]) ** 2
                    #dist += mt.sqrt((avgcol[i][j][k][m]-avgcol[l_2][l_3][8][m]) ** 2)
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



error_1 = 0
error_2 = 0
for i in range(2):
    for j in range(3):
        for k in range(9):
            if tilecol_1[i][j][k] != tilecol_correct_2_1[i][j][k]:
                error_1 += 1


for i in range(2):
    for j in range(3):
        for k in range(9):
            if tilecol_2[i][j][k] != tilecol_correct_2_1[i][j][k]:
                error_2 += 1
#print results
print(tilecol_correct_2_1)
print(tilecol_1)
print(tilecol_2)
print(tilecol_correct_2_1)
print(error_1)
print(error_2)

#cv2.imshow('image',resized_list[0])
#cv2.imshow('imaggre',resized_list[1])
#cv2.waitKey(0)