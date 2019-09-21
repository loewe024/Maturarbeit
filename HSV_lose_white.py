import cv2
import numpy as np


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
tilecol = [[["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]], [["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"], ["o", "o", "o", "o", "o", "o", "o", "o", "o"]]]

#ose white
white_question = 0
whitemid = 256
midvar1 = 0
midvar2 = 0
whiteout = [256, 256, 256, 256, 256, 256, 256, 256]
whiteoutvar1 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar2 = [0, 0, 0, 0, 0, 0, 0, 0]
whiteoutvar3 = [0, 0, 0, 0, 0, 0, 0, 0]



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
        #print("----------")

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
                biggestsatpos = 0
                for l in range(8):
                    if avgcol[i][j][k][1] < whiteout[l] and whiteout[l] > biggestsat:
                        biggestsat = whiteout[l]
                        biggestsatpos = l
                whiteout[biggestsatpos] = avgcol[i][j][k][1]
                whiteoutvar1[biggestsatpos] = i
                whiteoutvar2[biggestsatpos] = j
                whiteoutvar3[biggestsatpos] = k
    tilecol[midvar1][midvar2][8] = "w"
    for i in range(7):
        tilecol[whiteoutvar1[i]][whiteoutvar2[i]][whiteoutvar3[i]] = "w"

print(tilecol)

