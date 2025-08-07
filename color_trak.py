import cv2
import numpy as np

def nothing(x):
    print(x)

img_original = cv2.imread("my.jpg")  # Read the image from file

cv2.namedWindow('Trackbar', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Trackbar', 512, 300)

cv2.createTrackbar('cp', 'Trackbar', 10, 400, nothing)
switch = 'color/gray'
cv2.createTrackbar(switch, 'Trackbar', 0, 1, nothing)

while True:
    s = cv2.getTrackbarPos(switch, 'Trackbar')
    pos = cv2.getTrackbarPos('cp', 'Trackbar')

    img = img_original.copy()

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (10, 30), font, 1, (255, 255, 255), 2)

    if s == 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # convert back to BGR so putText doesn't break

    cv2.imshow('Trackbar', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

