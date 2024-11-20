import cv2, time, os, sys
from modules import Robot

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

robot = Robot()
pan = 0

while True:
    sample = robot.cameraCapture()
    object_name = "stop"
    timestamp = time.time()

    cv2.imshow(f"Sample", sample)
    key = cv2.waitKey(1)
    if key == ord('q'):
        cv2.destroyAllWindows()
        break
    elif key == ord('p'): 
        print("Positive sample")
        cv2.imwrite(f"{object_name}/positive/{timestamp}.jpg", sample)
    elif key == ord('n'): 
        print("Negative sample")
        cv2.imwrite(f"{object_name}/negative/{timestamp}.jpg", sample)
    elif key == ord('r'):
        pan += 1
        robot.pan(pan)
    elif key == ord('l'):
        pan -= 1
        robot.pan(pan)

robot.camera.stop()
cv2.destroyAllWindows()