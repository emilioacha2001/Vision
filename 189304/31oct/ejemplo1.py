import cv2, os
import numpy as np

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

img = cv2.imread("image.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier("models/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("models/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("models/haarcascade_smile.xml")
faces = face_cascade.detectMultiScale(gray, 1.1, 2)
eyes = eye_cascade.detectMultiScale(gray, 1.4, 6)
smiles = smile_cascade.detectMultiScale(gray, 1.8, 20)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_color, 1.4, 5)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        # cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)

# for (x, y, w, h) in eyes:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

for (x, y, w, h) in smiles:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

cv2.putText(img, "189304", (40, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (250, 30, 150), 2)


cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()