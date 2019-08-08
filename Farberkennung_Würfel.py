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
coordinates1 = [[[376,432],[270,272],[190,156],[124,320],[72,456],[116,586],[184,746],[280,610],[194,444]],[[546,348],[704,362],[844,378],[724,248],[628,140],[490,108],[334,78],[432,196],[592,218]],[[524,520],[420,690],[322,820],[482,798],[618,780],[718,664],[832,526],[692,526],[586,674]]]
coordinates2 = [[[376,432],[270,272],[190,156],[124,320],[72,456],[116,586],[184,746],[280,610],[194,444]],[[546,348],[704,362],[844,378],[724,248],[628,140],[490,108],[334,78],[432,196],[592,218]],[[524,520],[420,690],[322,820],[482,798],[618,780],[718,664],[832,526],[692,526],[586,674]]]

print(resized1[162][450][0])
print('Resized Dimensions : ',resized1.shape)

# define boundaries of BGR-Spectrum
f = 0.5

m1_b = resized1[coordinates1[0][8][0]][coordinates1[0][8][1]][0]
m1_bl = m1_b - m1_b*f
m1_bu = m1_b +m1_b*f
if m1_bl < 0:
    m1_bl = 0
if m1_bu > 255:
    m1_bu = 255
m1_g = resized1[coordinates1[0][8][0]][coordinates1[0][8][1]][1]
m1_gl = m1_g - m1_g*f
m1_gu = m1_g +m1_g*f
if m1_gl < 0:
    m1_gl = 0
if m1_gu > 255:
    m1_gu = 255
m1_r = resized1[coordinates1[0][8][0]][coordinates1[0][8][1]][2]
m1_rl = m1_r - m1_r*f
m1_ru = m1_r +m1_r*f
if m1_rl < 0:
    m1_rl = 0
if m1_ru > 255:
    m1_ru = 255
m1_lower = np.array([m1_bl,m1_gl,m1_rl],np.uint8)
m1_upper = np.array([m1_bu,m1_gu,m1_ru],np.uint8)

m2_b = resized1[coordinates1[1][8][0]][coordinates1[1][8][1]][0]
m2_bl = m2_b - m2_b*f
m2_bu = m2_b +m2_b*f
if m2_bl < 0:
    m2_bl = 0
if m2_bu > 255:
    m2_bu = 255
m2_g = resized1[coordinates1[1][8][0]][coordinates1[1][8][1]][1]
m2_gl = m2_g - m2_g*f
m2_gu = m2_g +m2_g*f
if m2_gl < 0:
    m2_gl = 0
if m2_gu > 255:
    m2_gu = 255
m2_r = resized1[coordinates1[1][8][0]][coordinates1[1][8][1]][2]
m2_rl = m2_r - m2_r*f
m2_ru = m2_r +m2_r*f
if m2_rl < 0:
    m2_rl = 0
if m2_ru > 255:
    m2_ru = 255
m2_lower = np.array([m2_bl,m2_gl,m2_rl],np.uint8)
m2_upper = np.array([m2_bu,m2_gu,m2_ru],np.uint8)

m3_b = resized1[coordinates1[2][8][0]][coordinates1[2][8][1]][0]
m3_bl = m3_b - m3_b*f
m3_bu = m3_b +m3_b*f
if m3_bl < 0:
    m3_bl = 0
if m3_bu > 255:
    m3_bu = 255
m3_g = resized1[coordinates1[2][8][0]][coordinates1[2][8][1]][1]
m3_gl = m3_g - m3_g*f
m3_gu = m3_g +m3_g*f
if m3_gl < 0:
    m3_gl = 0
if m3_gu > 255:
    m3_gu = 255
m3_r = resized1[coordinates1[2][8][0]][coordinates1[2][8][1]][2]
m3_rl = m3_r - m3_r*f
m3_ru = m3_r +m3_r*f
if m3_rl < 0:
    m3_rl = 0
if m3_ru > 255:
    m3_ru = 255
m3_lower = np.array([m3_bl,m3_gl,m3_rl],np.uint8)
m3_upper = np.array([m3_bu,m3_gu,m3_ru],np.uint8)

m4_b = resized2[coordinates2[0][8][0]][coordinates2[0][8][1]][0]
m4_bl = m4_b - m4_b*f
m4_bu = m4_b +m4_b*f
if m4_bl < 0:
    m4_bl = 0
if m4_bu > 255:
    m4_bu = 255
m4_g = resized2[coordinates2[0][8][0]][coordinates2[0][8][1]][1]
m4_gl = m4_g - m4_g*f
m4_gu = m4_g +m4_g*f
if m4_gl < 0:
    m4_gl = 0
if m4_gu > 255:
    m4_gu = 255
m4_r = resized2[coordinates2[0][8][0]][coordinates2[0][8][1]][2]
m4_rl = m4_r - m4_r*f
m4_ru = m4_r +m4_r*f
if m4_rl < 0:
    m4_rl = 0
if m4_ru > 255:
    m4_ru = 255
m4_lower = np.array([m4_bl,m4_gl,m4_rl],np.uint8)
m4_upper = np.array([m4_bu,m4_gu,m4_ru],np.uint8)

m5_b = resized2[coordinates2[1][8][0]][coordinates2[1][8][1]][0]
m5_bl = m5_b - m5_b*f
m5_bu = m5_b +m5_b*f
if m5_bl < 0:
    m5_bl = 0
if m5_bu > 255:
    m5_bu = 255
m5_g = resized2[coordinates2[1][8][0]][coordinates2[1][8][1]][1]
m5_gl = m5_g - m5_g*f
m5_gu = m5_g +m5_g*f
if m5_gl < 0:
    m5_gl = 0
if m5_gu > 255:
    m5_gu = 255
m5_r = resized2[coordinates2[1][8][0]][coordinates2[1][8][1]][2]
m5_rl = m5_r - m5_r*f
m5_ru = m5_r +m5_r*f
if m5_rl < 0:
    m5_rl = 0
if m5_ru > 255:
    m5_ru = 255
m5_lower = np.array([m5_bl,m5_gl,m5_rl],np.uint8)
m5_upper = np.array([m5_bu,m5_gu,m5_ru],np.uint8)

m6_b = resized2[coordinates2[2][8][0]][coordinates2[2][8][1]][0]
m6_bl = m6_b - m6_b*f
m6_bu = m6_b +m6_b*f
if m6_bl < 0:
    m6_bl = 0
if m6_bu > 255:
    m6_bu = 255
m6_g = resized2[coordinates2[2][8][0]][coordinates2[2][8][1]][1]
m6_gl = m6_g - m6_g*f
m6_gu = m6_g +m6_g*f
if m6_gl < 0:
    m6_gl = 0
if m6_gu > 255:
    m6_gu = 255
m6_r = resized2[coordinates2[2][8][0]][coordinates2[2][8][1]][2]
m6_rl = m6_r - m6_r*f
m6_ru = m6_r +m6_r*f
if m6_rl < 0:
    m6_rl = 0
if m6_ru > 255:
    m6_ru = 255
m6_lower = np.array([m6_bl,m6_gl,m6_rl],np.uint8)
m6_upper = np.array([m6_bu,m6_gu,m6_ru],np.uint8)

for i in range(len(coordinates1)):
    for j in range(len(coordinates1[i])):
        var = 0
        for k in range (3):
            if resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] >= m1_lower[k] and resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] <= m1_upper[k]:
                var += 1
        if var == 3:
            print(1)
        var = 0
        for k in range (3):
            if resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] >= m2_lower[k] and resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] <= m2_upper[k]:
                var += 1
        if var == 3:
            print(2)
        var = 0
        for k in range (3):
            if resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] >= m3_lower[k] and resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] <= m3_upper[k]:
                var += 1
        if var == 3:
            print(3)
        var = 0
        for k in range (3):
            if resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] >= m4_lower[k] and resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] <= m4_upper[k]:
                var += 1
        if var == 3:
            print(4)
        var = 0
        for k in range (3):
            if resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] >= m5_lower[k] and resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] <= m5_upper[k]:
                var += 1
        if var == 3:
            print(5)
        var = 0
        for k in range (3):
            if resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] >= m6_lower[k] and resized1[coordinates1[i][j][0]][coordinates1[i][j][1]][k] <= m6_upper[k]:
                var += 1
        if var == 3:
            print(6)
        print("-----")
    print("----------")
for i in range(len(coordinates2)):
    for j in range(len(coordinates2[i])):
        var = 0
        for k in range (3):
            if resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] >= m1_lower[k] and resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] <= m1_upper[k]:
                var += 1
        if var == 3:
            print(1)
        var = 0
        for k in range (3):
            if resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] >= m2_lower[k] and resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] <= m2_upper[k]:
                var += 1
        if var == 3:
            print(2)
        var = 0
        for k in range (3):
            if resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] >= m3_lower[k] and resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] <= m3_upper[k]:
                var += 1
        if var == 3:
            print(3)
        var = 0
        for k in range (3):
            if resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] >= m4_lower[k] and resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] <= m4_upper[k]:
                var += 1
        if var == 3:
            print(4)
        var = 0
        for k in range (3):
            if resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] >= m5_lower[k] and resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] <= m5_upper[k]:
                var += 1
        if var == 3:
            print(5)
        var = 0
        for k in range (3):
            if resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] >= m6_lower[k] and resized2[coordinates2[i][j][0]][coordinates2[i][j][1]][k] <= m6_upper[k]:
                var += 1
        if var == 3:
            print(6)
        print("-----")
    print("----------")