import os, cv2
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

image = cv2.imread("image.jpeg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (15, 15), 3)

edges = cv2.Canny(blurred, 70, 50)
kernel = np.ones((5, 5), np.uint8)
dilated = cv2.dilate(edges, kernel, iterations=1)
# cv2.imshow("Dilated", dilated)


_, binary = cv2.threshold(dilated, 190, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow("Binary", binary)

countours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, countours, -1, (0, 0, 255), 2)
cv2.imshow("test", image)

coins_area = {
    "ten": [111.5],
    "one": [92.5, 110.5],
}

for c in countours:
    area = cv2.contourArea(c)
    print(f"Area: {area}") 
    # if area > 80 and area < 150:
    #     print(f"Area: {area}")
    #     cv2.drawContours(image, [c], -1, (0, 0, 255), 2)

cv2.imshow("Original", image)


cv2.waitKey(0)
cv2.destroyAllWindows()
