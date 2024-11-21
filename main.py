from modules import TrackImage, Robot
import cv2, time, os, math
import numpy as np

robot = Robot()
robot.tilt(-10)
direction = 1
angle = 0
start = time.time()
stopped_time = 0
stopped = False

while True:
    frame = robot.cameraCapture()

    track = TrackImage(frame)
    fy, fx, _ = track.frame.shape
    furthest_line = track.getSmallestCountour(track.lines)
    if furthest_line is not None and len(furthest_line) > 0:
        cx, cy = track.getContourCentroid(furthest_line)
        center_x = fx // 2
        alpha = math.atan( (cx - center_x) / (fy - cy) )
        alpha = math.degrees(alpha)
        duration = stopped_time - start

        if alpha * direction < -5: continue
        if len(track.people) > 0:
            robot.stop()
            continue
        if len(track.stops) == 1 and not stopped:
            robot.stop()
            start = time.time()
            stopped_time = time.time()
            stopped = True
        elif stopped and duration <= 5: 
            stopped_time = time.time()
            continue
        elif stopped and duration <= 8:
            stopped_time = time.time()
            robot.pan(alpha/2)
            robot.turn(alpha/2)
            robot.forward(1)
        else:
            stopped = False
            robot.pan(alpha/2)
            robot.turn(alpha/2)
            robot.forward(1)

    elif track.isInsideBorder():
        robot.turn(90*direction)
        robot.pan(10*direction)
        # robot.forward(1)
    else: 
        robot.stop()

    track.drawPeople()
    track.drawStops()
    track.drawLines()
    cv2.imshow("Test 1", track.frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

robot.stop()
cv2.waitKey(0)
cv2.destroyAllWindows()
