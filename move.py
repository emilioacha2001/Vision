from modules import Robot
import time, cv2

robot = Robot()
robot.tilt(-10)
robot.turn(30)

while True:
    frame = robot.cameraCapture()
    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

robot.camera.stop()
cv2.destroyAllWindows()