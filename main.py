from modules import TrackImage, Robot
import cv2, time, os
import numpy as np

robot = Robot()
while True:
    frame = robot.cameraCapture()

    track = TrackImage(frame)
    track.drawPeople()
    track.drawRedLights()
    track.drawLines()
    cv2.imshow("Test 1", track.frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.waitKey(0)
cv2.destroyAllWindows()
