import cv2
import numpy as np

cap = cv2.VideoCapture('welcome.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=50, detectShadows=True)

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened() and ret:
    fgmask = fgbg.apply(frame2)
    blur = cv2.GaussianBlur(fgmask, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        area = cv2.contourArea(contour)

        if area < 1000:
            continue
        if h < 80:
            continue

        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("feed", frame2)
    frame1 = frame2
    ret, frame2 = cap.read()
    if not ret or cv2.waitKey(40) == 27:
        break       

cap.release()
cv2.destroyAllWindows()

