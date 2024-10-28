import cv2, os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

image = cv2.imread('image.png')
original = image.copy()
cv2.imshow('Original', image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Rojo (Hue) de 0 a 20 y de 170 a 180
lower1 = np.array([0, 128, 128])
upper1 = np.array([10, 255, 255])

lower2 = np.array([170, 128, 128])
upper2 = np.array([179, 255, 255])

mask_red_1 = cv2.inRange(image, lower1, upper1)
mask_red_2 = cv2.inRange(image, lower2, upper2)
mask_red = cv2.bitwise_or(mask_red_1, mask_red_2)

countours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(original, countours, -1, (0, 255, 0), 2)

cv2.imshow('Mask Red', mask_red)
cv2.imshow('Image', original)

cv2.waitKey(0)
cv2.destroyAllWindows()