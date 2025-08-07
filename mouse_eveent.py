import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print( x, ',', y)
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 0), 1)
        cv2.imshow('image', img)

    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print( x, ',', y)
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)

img = np.zeros((512, 512, 3), np.uint8)

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
