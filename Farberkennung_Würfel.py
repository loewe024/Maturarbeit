import cv2
import numpy as np

cube1 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_ungeloest_hell_1.jpg")
cube2 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_ungeloest_hell_2.jpg")
scale_percent = 40 # percent of original size
width = int(cube1.shape[1] * scale_percent / 100)
height = int(cube1.shape[0] * scale_percent / 100)
dim = (width, height)

resized1 = cv2.resize(cube1, dim)
resized2 = cv2.resize(cube2, dim)
resized_list = [resized1, resized2]

#cv.cvtColor(green,cv.COLOR_BGR2HSV)

coordinates = [[[[376,432],[270,272],[190,156],[124,320],[72,456],[116,586],[184,746],[280,610],[194,444]],[[546,348],[704,362],[844,378],[724,248],[628,140],[490,108],[334,78],[432,196],[592,218]],[[524,520],[420,690],[322,820],[482,798],[618,780],[718,664],[832,526],[692,526],[586,674]]],[[[376,432],[270,272],[190,156],[124,320],[72,456],[116,586],[184,746],[280,610],[194,444]],[[546,348],[704,362],[844,378],[724,248],[628,140],[490,108],[334,78],[432,196],[592,218]],[[524,520],[420,690],[322,820],[482,798],[618,780],[718,664],[832,526],[692,526],[586,674]]]]

avgcol = [[[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]], [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]]

colors = ["white", "green", "red", "yellow", "orange", "blue"]

tilecol = [[["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]], [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]]
tilecol_correct = [[["yellow", "blue", "red", "blue", "white", "orange", "green", "yellow", "white"], ["blue", "white", "orange", "green", "red", "yellow", "white", "yellow", "green"], ["red", "green", "orange", "red", "white", "orange", "yellow", "red", "red"]], [["green", "orange", "yellow", "white", "blue", "green", "orange", "orange", "yellow"], ["red", "blue", "orange", "red", "blue", "red", "green", "yellow", "orange"], ["white", "white", "green", "green", "yellow", "blue", "blue", "white", "blue"]]]
tilenum = [0, 0, 0, 0, 0, 0]

f = 0.2 #relativer Faktor
a = 255 #absoluter Faktor

boundaries = [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]

for i in range(2):
    for j in range(3):
        for k in range(9):
            for l in range(3):
                col = 0
                for m in range(30):
                    for n in range(30):
                        col += resized_list[i] [coordinates[i][j][k][0]-15+m][coordinates[i][j][k][1]-15+n][l]
                avgcol[i][j][k][l] = col/900
                BGR_trans = np.uint8([[[avgcol[i][j][k][0], avgcol[i][j][k][1], avgcol[i][j][k][2]]]])
            HSV_trans = cv2.cvtColor(BGR_trans, cv2.COLOR_BGR2HSV)
            avgcol[i][j][k][0] = HSV_trans[0][0][1]
            avgcol[i][j][k][1] = HSV_trans[0][0][2]

for i in range (2): # coordinates1/2
    for j in range (3): #m1/2/3
        for k in range (2): # colors
            m_c = avgcol[i][j][8][k]
            boundaries[j+3*i][k][0] = m_c - a
            boundaries[j+3*i][k][1] = m_c + a

for i in range(2): #coordinates1/2
    for j in range(3): #side
        for k in range(9): #tile
            extra = 0
            col = 0
            while True:
                num = 0
                for l in range(6): #test for six colors
                    var = 0
                    for m in range(2): #BGR
                        if avgcol[i][j][k][m] >= (boundaries[l][m][0] + extra) and  avgcol[i][j][k][m] <= (boundaries[l][m][1] - extra):
                            var += 1
                    if var == 2:
                        col = l
                        num += 1
                if num > 1:
                    extra += 1
                else:
                    break
            tilecol[i][j][k] = colors[col]
            tilenum[col] += 1

for i in range(6):
    extra2 = 255
    stayorchange = [[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]]
    socvar = 0

    while tilenum[i] > 9:
        for j in range(2):
            for k in range(3):
                for l in range(9):
                    if tilecol[j][k][l] == colors[i]:
                        extra2 -= 1
                        for m in range(6): #test for six colors
                            var = 0
                            for n in range(2): #BGR
                                if avgcol[j][k][l][n] >= (boundaries[m][n][0] + extra2) and  avgcol[j][k][l][n] <= (boundaries[m][n][1] - extra2):
                                    var += 1
                            if var == 2 and colors[m] == colors[i] and socvar < 9 and stayorchange[j][k][l] == 0:
                                socvar += 1
                                stayorchange[j][k][l] = 1
                            if var == 2 and colors[m] != colors[i] and tilenum[i] > 9 and tilenum[m] < 9 and stayorchange[j][k][l] == 0:
                                tilecol[j][k][l] = colors[m]
                                tilenum[i] -= 1
                                tilenum[m] += 1

print(tilecol_correct)
print(tilecol)