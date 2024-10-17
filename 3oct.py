import cv2, datetime, time

cap = cv2.VideoCapture("video1.mp4")
video_fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS: {video_fps}")
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
print(f"Ancho: {width} y Alto: {height}")

now = datetime.datetime.now()
print(now)
tiempo = now.strftime("%H:%M:%S")
print(tiempo)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
color = (255, 255, 255)

# Forzar fps a fps de video
# Colocar reloj en tiempo real en el video
# Contar la canatidad total frames de su video y mostrarlo en pantalla

frame_duration = 1.0 / video_fps
count = 0
while cap.isOpened():
    cycle_time = video_fps
    start_time = time.time()
    count += 1
    ret, frame = cap.read()
    fps = 1000 / video_fps
    cv2.resize(frame, (int(width/2), int(height/2)))
    now = datetime.datetime.now()
    tiempo = now.strftime("%H:%M:%S")
    cv2.putText(frame, tiempo, (10, 50), font, font_scale, color, 2)
    cv2.putText(frame, f"Frames count: {count}", (10, 100), font, font_scale, color, 2)
    cv2.putText(frame, f"FPS: {1000/cycle_time}", (10, 150), font, font_scale, color, 2)
    cv2.putText(frame, "189304", (10, 200), font, font_scale, color, 2)

    cv2.imshow("Video", frame)
    sleep_time = int(fps)
    end_time = time.time()
    cycle_time = end_time - start_time
    sleep_time = max(0, frame_duration - cycle_time)
    time.sleep(sleep_time)

    # time.sleep(sleep_time/1000)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()