import cv2, os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

image = cv2.imread('image.png')
original = image.copy()
# cv2.imshow('Original', image)

image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
column1 = np.concatenate((original, image), axis=1)

# Rojo (Hue) de 0 a 20 y de 170 a 180
lower1 = np.array([0, 128, 128])
upper1 = np.array([10, 255, 255])

lower2 = np.array([170, 128, 128])
upper2 = np.array([179, 255, 255])

mask_red_1 = cv2.inRange(image, lower1, upper1)
mask_red_2 = cv2.inRange(image, lower2, upper2)
mask_red = mask_red_1 + mask_red_2
column1 = np.concatenate((column1, cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)), axis=1 )
# cv2.imshow('Column1', column1)

countours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
all_circles = countours
total_red_circles = len(countours)

for c in countours:
    area = cv2.contourArea(c)
    print(f"Area: {area}")
    if area == 34670.0: cv2.drawContours(original, [c], -1, (0, 0, 255), 2)
    cv2.drawContours(original, [c], -1, (0, 255, 0), 2)

area_threshold = 34670.0

# Blue (Hue) de 170 a 250
lower = np.array([85, 128, 128])
upper = np.array([125, 170, 255])
mask_blue = cv2.inRange(image, lower, upper)
column2 = np.concatenate((original, cv2.cvtColor(mask_blue, cv2.COLOR_GRAY2BGR)), axis=1)
# cv2.imshow('Mask Blue', mask_blue)
countours, _ = cv2.findContours(mask_blue, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
all_circles += countours
total_blue_circles = 0

print(len(countours))
for c in countours:
    area = cv2.contourArea(c)
    if area > 10 and area < 2501257.0:
        print(f"Area: {area}")
        total_blue_circles += 1
        cv2.drawContours(original, [c], -1, (0, 0, 255), 2)

column2 = np.concatenate((column2, original), axis=1)
print(f"Rojos totales: {total_red_circles}")
print(f"Azules totales: {total_blue_circles}")
print(f"Circulos totales: {total_red_circles + total_blue_circles}")
first_algorithm = np.concatenate((column1, column2), axis=0)
cv2.putText(first_algorithm, f"189304", (20, 100), cv2.FONT_ITALIC, 4, (0, 0, 0), 4)
cv2.putText(first_algorithm, f"Rojos: {total_red_circles}", (20, 200), cv2.FONT_ITALIC, 4, (0, 0, 0), 3)
cv2.putText(first_algorithm, f"Azules: {total_blue_circles}", (20, 300), cv2.FONT_ITALIC, 4, (0, 0, 0), 3)
cv2.putText(first_algorithm, f"Total: {total_red_circles + total_blue_circles}", (20, 400), cv2.FONT_ITALIC, 4, (0, 0, 0), 3)
cv2.imshow('First Algorithm', first_algorithm)
cv2.imwrite('first_algorithm2.png', first_algorithm)

full_mask = mask_blue + mask_red
column1 = np.concatenate((original, image), axis=1)
column1 = np.concatenate((column1, cv2.cvtColor(mask_red, cv2.COLOR_GRAY2BGR)), axis=1)
column2 = np.concatenate((cv2.cvtColor(mask_blue, cv2.COLOR_GRAY2BGR), cv2.cvtColor(full_mask, cv2.COLOR_GRAY2BGR)), axis=1)
column2 = np.concatenate((column2, original), axis=1)
second_algorithm = np.concatenate((column1, column2), axis=0)

cv2.imshow('Full Mask', full_mask)
countours, _ = cv2.findContours(full_mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(original, countours, -1, (0, 255, 0), 2)
circles_smaller_than_threshold = len([c for c in countours if cv2.contourArea(c) < area_threshold and cv2.contourArea(c) > 10 and cv2.contourArea(c) < 2551257.0])

cv2.putText(second_algorithm, f"189304", (20, 100), cv2.FONT_ITALIC, 4, (0, 0, 0), 4)
cv2.putText(second_algorithm, f"circulos mas pequeños: {circles_smaller_than_threshold}", (20, 200), cv2.FONT_ITALIC, 4, (0, 0, 0), 3)
print(f"Circulos mas pequeños: {circles_smaller_than_threshold}")

# cv2.imshow('Original1', original)   
cv2.imshow('Second Algorithm', second_algorithm)
cv2.imwrite('second_algorithm2.png', second_algorithm)

cv2.waitKey(0)
cv2.destroyAllWindows()