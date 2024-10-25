import cv2, os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

image = cv2.imread("../coins.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Blurred", blurred)

edges = cv2.Canny(blurred, 30, 50)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
cv2.imshow("Dilated", dilated)

countours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, countours, -1, (0, 0, 255), 2)

print(f"Cantidad de monedas: {len(countours)}")
for c in countours:
    area = cv2.contourArea(c)
    print(f"Area: {area}")


cv2.imshow("Original", image)
cv2.imshow("edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()