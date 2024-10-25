import os, cv2
# os.environ["OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS"] = "0"
import numpy as np

cap = cv2.VideoCapture(0)
# cap =  cv2.VideoCapture(0, cv2.CAP_MSMF)

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)
is_first = True

while cap.isOpened():
    count = 0
    coins_count = 0
    _, image = cap.read()
    original = image.copy()

    # image = cv2.imread("image.jpeg")
    # original = cv2.imread("image.jpeg")
    # image = frame[frame.shape[0]//2:frame.shape[0],0:frame.shape[1]]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # blurred = cv2.GaussianBlur(gray, (15, 15), 3)

    edges = cv2.Canny(gray, 160, 160)
    kernel = np.ones((6, 6), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)
    cv2.imshow("Dilated", dilated)


    _, binary = cv2.threshold(dilated, 140, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("Binary", binary)

    countours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(image, countours, -1, (0, 0, 255), 2)
    # cv2.imshow("test", image)

    # coins_area = {
    #     "ten": [111.5],
    #     "one": [92.5, 110.5],
    # }


    for c in countours:
        area = cv2.contourArea(c)
        if area < 100000 and area > 3000:
            print(f"Area: {area}")
            cv2.drawContours(image, [c], -1, (0, 0, 255), 2)
            if area > 7000: 
                count += 10
                coins_count += 1
            if area > 3000 and area < 5000: 
                coins_count += 1
                count += 1

    cv2.putText(image, f"monedas: {coins_count}", (200, 350), cv2.FONT_ITALIC, 4, (0, 0, 255), 10)
    cv2.putText(image, f"dinero: {count}", (200, 550), cv2.FONT_ITALIC, 4, (0, 0, 255), 10)
    cv2.putText(image, f"189304", (20, 50), cv2.FONT_ITALIC, 2, (0, 0, 255), 2)
    cv2.putText(image, f"189521", (20, 100), cv2.FONT_ITALIC, 2, (0, 0, 255), 2)
    cv2.putText(image, f"189304", (20, 150), cv2.FONT_ITALIC, 2, (0, 0, 255), 2)
    cv2.putText(image, f"189506", (20, 200), cv2.FONT_ITALIC, 2, (0, 0, 255), 2)

    print(f"Total coins: {count}")
    cv2.imshow("Original", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

binary = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
first_column = np.concatenate((original, binary), axis=0)
second_column = np.concatenate((gray, image), axis=0)
final_image = np.concatenate((first_column, second_column), axis=1)
cv2.imwrite("coins.png", final_image)

cap.release()
cv2.destroyAllWindows()
