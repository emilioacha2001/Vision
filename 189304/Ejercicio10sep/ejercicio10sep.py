import cv2

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

img = cv2.imread('pokeball_opencv.png')
cv2.imshow('original', img)

# Escala de 0.1 rotacion 30 grados
ej1 = rotate(img, 30, None, 0.1)
cv2.imshow("Escala de 0.1 rotacion 30 grados", ej1)
cv2.imwrite("Escala de 0.1 rotacion 30 grados.png", ej1)
# Escala de 0.5 rotacion 45 grados
ej2 = rotate(img, 45, None, 0.5)
cv2.imshow("Escala de 0.5 rotacion 45 grados", ej2)
cv2.imwrite("Escala de 0.5 rotacion 45 grados.png", ej2)
# Escala de 2.0 rotacion 60 grados
ej3 = rotate(img, 60, None, 2.0)
cv2.imshow("Escala de 2.0 rotacion 60 grados", ej3)
cv2.imwrite("Escala de 2.0 rotacion 60 grados.png", ej3)
# Rotacion 90 grados
ej4 = rotate(img, 90)
cv2.imshow("Rotacion 90 grados", ej4)
cv2.imwrite("Rotacion 90 grados.png", ej4)
# Rotacion 100 grados
ej5 = rotate(img, 100)
cv2.imshow("Rotacion 100 grados", ej5)
cv2.imwrite("Rotacion 100 grados.png", ej5)
# Rotacion 270 grados
ej6 = rotate(img, 270)
cv2.imshow("Rotacion 270 grados", ej6)
cv2.imwrite("Rotacion 270 grados.png", ej6)
# Rotacion 90 grados centro 0,h
ej7 = rotate(img, 90, (0, img.shape[0]))
cv2.imshow("Rotacion 90 grados centro 0,h", ej7)
cv2.imwrite("Rotacion 90 grados centro 0,h.png", ej7)
# Rotacion 90 grados centro w,0
ej8 = rotate(img, 90, (img.shape[1], 0))
cv2.imshow("Rotacion 90 grados centro w,0", ej8)
cv2.imwrite("Rotacion 90 grados centro w,0.png", ej8)

cv2.waitKey(0)
cv2.destroyAllWindows()