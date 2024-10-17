import cv2
import numpy as np

a = [0, 0, 0, 0, 1]
b = a
b = a.copy()
a[0] = 1

print(a)
print(b)

blue = (255, 0, 0)
red = (0, 0, 255)
thickness = 5
canvas = np.zeros((800, 800, 3), dtype=np.uint8)
canvas += 255
canvas2 = canvas.copy()

cv2.line(canvas, (0,0), (800,800), blue, thickness)
cv2.circle(canvas, (400, 400), 200, blue, thickness)
cv2.putText(canvas, "189304", (200, 100), cv2.FONT_ITALIC, 2, red, thickness)

cv2.imshow("Canvas", canvas)
cv2.imwrite("17sep.png", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()