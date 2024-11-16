from picamera2 import Picamera2
import cv2, time

picam2 = Picamera2()
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

start_time = time.time()
fps_count = 0
while True:
    frame = picam2.capture_array()

    end_time = time.time()
    cycle_time = end_time - start_time
    start_time = end_time 

    fps_count += 1
    if cycle_time <= 0:
        cycle_time = 0.0000001

    fps  = f"{round(1 / cycle_time, 2)}"
    cv2.putText(frame, fps, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Camara", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

picam2.stop()
cv2.destroyAllWindows()