import cv2
import numpy as np

cap = cv2.VideoCapture("car.mp4")
ret, frame = cap.read()
frame = cv2.resize(frame, (800, 600))  # move this line up

x, y, width, height = 340, 360, 70, 40
track_window = (x, y, width, height)
roi = frame[y:y+height, x:x+width]

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

cv2.imshow("Input Image", roi)

while (1):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame, (800, 600))
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)# mean shhift method for tracking
        x, y, w, h = track_window
        final_image = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("dst", dst)
        cv2.imshow("Tracking", final_image)
        cv2.imshow("Input Image", frame)
        k = cv2.waitKey(30) & 0xFF
        if k == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()



