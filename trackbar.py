import cv2
import numpy as np

def nothing(x):
    print(x)

cv2.namedWindow('Trackbar', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Trackbar', 512, 300)

cv2.createTrackbar('R', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('G', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('B', 'Trackbar', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON '
cv2.createTrackbar(switch, 'Trackbar', 0, 1, nothing)  #  create the switch trackbar

while True:
    r = cv2.getTrackbarPos('R', 'Trackbar')
    g = cv2.getTrackbarPos('G', 'Trackbar')
    b = cv2.getTrackbarPos('B', 'Trackbar')
    s = cv2.getTrackbarPos(switch, 'Trackbar')

    img = np.zeros((300, 512, 3), np.uint8)  

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

    cv2.imshow('Trackbar', img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
