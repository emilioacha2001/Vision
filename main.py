from modules import TrackImage, Robot
import cv2, time, os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

background = cv2.imread("test_images/street.jpg.webp")
mujer = cv2.imread("test_images/mujer.png")
hombre = cv2.imread("test_images/hombre.png")
alto = cv2.imread("test_images/alto.png")

background = cv2.resize(background, (1600, 1200))
frame = background.copy()
frame[200:mujer.shape[0]+200, 200:mujer.shape[1]+200] = mujer
frame[400:alto.shape[0]+400, 1300:alto.shape[1]+1300] = alto
# frame[200:hombre.shape[0]+200, 800:hombre.shape[1]+800] = hombre

# Test 1
track = TrackImage(frame)
track.drawPeople()
track.drawRedLights()
track.drawLines()
cv2.imshow("Test 1", track.frame)

cv2.waitKey(0)
cv2.destroyAllWindows()