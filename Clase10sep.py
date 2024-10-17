import cv2
import numpy as np

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

image = cv2.imread('pokeball_opencv.png')
cv2.imshow('original', image)
img_flip = cv2.flip(image, 1)
cv2.imshow("Flip Vertical", img_flip)

transposed_img = cv2.transpose(image)
cv2.imshow("Transpose", transposed_img)

transposed_img = cv2.transpose(transposed_img)
cv2.imshow("Transpose 1", transposed_img)

# height, width = image.shape[:2]
# image_resized = cv2.resize(image, (int(width/2), int(height/2)))
# cv2.imshow("Resized", image_resized)

rotated = rotate(image, 180)
cv2.imshow("Rotated", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()