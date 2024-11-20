import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, image = cap.read()

    cv2.imshow(image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()