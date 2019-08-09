import cv2
import numpy as np

cube1 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_geloest_1.jpg")
cube2 = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_geloest_2.jpg")
scale_percent = 40 # percent of original size
width = int(cube1.shape[1] * scale_percent / 100)
height = int(cube1.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized1 = cv2.resize(cube1, dim)
resized2 = cv2.resize(cube2, dim)
resized_list = [resized1, resized2]

coordinates = [[[[376,432],[270,272],[190,156],[124,320],[72,456],[116,586],[184,746],[280,610],[194,444]],[[546,348],[704,362],[844,378],[724,248],[628,140],[490,108],[334,78],[432,196],[592,218]],[[524,520],[420,690],[322,820],[482,798],[618,780],[718,664],[832,526],[692,526],[586,674]]],[[[376,432],[270,272],[190,156],[124,320],[72,456],[116,586],[184,746],[280,610],[194,444]],[[546,348],[704,362],[844,378],[724,248],[628,140],[490,108],[334,78],[432,196],[592,218]],[[524,520],[420,690],[322,820],[482,798],[618,780],[718,664],[832,526],[692,526],[586,674]]]]

colors = ["blue", "yellow", "orange", "red", "white", "green"]


f = 0.2 #relativer Faktor
a = 255 #absoluter Faktor

boundaries = [[[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0]]]

for i in range (2): # coordinates1/2
    for j in range (3): #m1/2/3
        for k in range (3): # colors
            m_c = resized_list[i] [coordinates[i][j][8][0]][coordinates[i][j][8][1]][k]
            boundaries[j+3*i][k][0] = m_c - a
            boundaries[j+3*i][k][1] = m_c + a
            #if  boundaries[j+3*i][k][0] < 0:
                #boundaries[j+3*i][k][0] = 0
            #if boundaries[j+3*i][k][1] > 255:
                #boundaries[j+3*i][k][1] = 255

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
                        if resized_list[i] [coordinates[i][j][k][0]][coordinates[i][j][k][1]][m] >= (boundaries[l][m][0] + extra) and  resized_list[i] [coordinates[i][j][k][0]][coordinates[i][j][k][1]][m] <= (boundaries[l][m][1] - extra):
                            var += 1
                    if var == 3:
                        #print(colors[l])
                        col = l
                        num += 1
                if num > 1:
                    extra += 1
                else:
                    break
            print(colors[col])
            print("-----")
        print("----------")
