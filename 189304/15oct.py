import cv2, os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

image = cv2.imread("coins.jpeg")
cv2.imshow("Original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("imagen gris", gray)

# ret, binary = cv2.threshold(gray, 244, 255, cv2.THRESH_BINARY)
# cv2.imshow("binario", binary)

ret, binary = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("binario", binary)

# countours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
countours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(f"Numero de monedas: {len(countours)}")
# cv2.drawContours(image, countours, -1, (0, 0, 255), 1)
# cv2.imshow("Contornos", image)

coins = 0
copy_image = image.copy()
for c in countours:
    area = cv2.contourArea(c)
    if area > 500:
        print(f"Area: {area}")
        cv2.drawContours(copy_image, [c], -1, (0, 0, 255), 3)
        coins += 1

cv2.imshow("Contornos", image)
print(f"Numero de monedas: {coins}")

binary = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
first_column = np.concatenate((image, binary), axis=0)
second_column = np.concatenate((gray, copy_image), axis=0)
final_image = np.concatenate((first_column, second_column), axis=1)
cv2.putText(final_image, "189304", (200, 350), cv2.FONT_ITALIC, 4, (0, 0, 255), 10)

cv2.imshow("Final", final_image)
cv2.imwrite("coins.png", final_image)

cv2.waitKey(0)
cv2.destroyAllWindows()