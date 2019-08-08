import cv2
import numpy as np

cube = cv2.imread(r"C:\Users\le\SynologyDrive\Gymnasium\Maturarbeit\Wuerfel_geloest_1.jpg")
scale_percent = 40 # percent of original size
width = int(cube.shape[1] * scale_percent / 100)
height = int(cube.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(cube, dim)

print(resized[162][450][0])
print('Resized Dimensions : ',resized.shape)

# define boundaries of BGR-Spectrum
f = 0.5
b = resized[162][450][0]
blower = b - b*f
bupper = b +b*f
if blower < 0:
    blower = 0
if bupper > 255:
    bupper = 255
g = resized[162][450][1]
glower = g - g*f
gupper = g +g*f
if glower < 0:
    glower = 0
if gupper > 255:
    gupper = 255
r = resized[162][450][2]
rlower = r - r*f
rupper = r +r*f
if rlower < 0:
    rlower = 0
if rupper > 255:
    rupper = 255

blue_lower = np.array([blower,glower,rlower],np.uint8)
blue_upper = np.array([bupper,gupper,rupper],np.uint8)

# make new image
mask = cv2.inRange(resized, blue_lower, blue_upper)
output = cv2.bitwise_and(resized, resized, mask = mask)

cv2.imshow("only_blue", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("hello world")