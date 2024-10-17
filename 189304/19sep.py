import cv2
import time
import numpy as np

blue = (255, 0, 0)
red = (0, 0, 255)
thickness = 5
canvas = np.zeros((800, 800, 3), dtype=np.uint8)
canvas += 255

start_time = time.time()

i = 1
fps = (1/24)*1000
fps = (1/28)*1000
while True:
    i += 1
    texto = f"Contador: {i}"
    canvas = np.zeros((800, 800, 3), dtype=np.uint8)
    canvas += 255
    cv2.line(canvas, (0,0), (800,800), blue, thickness)
    cv2.circle(canvas, (400, 400), 200, blue, thickness)
    cv2.putText(canvas, "189304", (200, 100), cv2.FONT_ITALIC, 2, red, thickness)
    cv2.putText(canvas, texto, (250, 50), cv2.FONT_ITALIC, 2, blue, 1)
    cv2.imshow("Canvas", canvas)
    if cv2.waitKey(int(fps)) & 0xFF == ord('q'): 
        break

    end_time = time.time()
    cycle_time = end_time - start_time
    start_time = end_time 

    if cycle_time <= 0:
        cycle_time = 0.0000001

    print(f"FPS: {round(1 / cycle_time, 2)}")

cv2.imwrite("19sep.png", canvas)
cv2.destroyAllWindows() 