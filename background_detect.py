# import cv2
# import numpy as np
# cap=cv2.VideoCapture("welcome.mp4")
# fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)
# while True:
#     ret,frame=cap.read()
#     if frame is None:
#         break  
#     fgmask=fgbg.apply(frame) 
    
#     cv2.imshow("input Image",frame)
#     cv2.imshow("fg frame",fgmask)
    
#     keyboard=cv2.waitKey(30)
#     if keyboard==27:
#         break
# cap.release()
# cv2.destroyAllWindows()
#################second method for background detection##############
import cv2
import numpy as np
cap=cv2.VideoCapture("welcome.mp4")
fgbg=cv2.createBackgroundSubtractorKNN()
while True:
    ret,frame=cap.read()
    if frame is None:
        break  
    fgmask=fgbg.apply(frame) 
    
    cv2.imshow("input Image",frame)
    cv2.imshow("fg frame",fgmask)
    
    keyboard=cv2.waitKey(30)
    if keyboard==27:
        break
cap.release()
cv2.destroyAllWindows()