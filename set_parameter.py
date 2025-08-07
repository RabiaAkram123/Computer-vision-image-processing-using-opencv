##########set_parameter.py##########
# import cv2
# cap = cv2.VideoCapture(0) 
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(3,1280)
# cap.set(4,720)
# print(cap.get(3))
# print(cap.get(4))
# while (cap.isOpened()):
#     ret, frame = cap.read()
#     if  ret==True:
        
#        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#        cv2.imshow("Video Feed", gray)
#        cv2.imshow("Video Feed", frame)
#        if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     else:
#      break
# cap.release()
# cv2.destroyAllWindows()
######SET DATE AND TIME############

import cv2
import datetime
cap = cv2.VideoCapture(0) 
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# cap.set(3,1280)
# cap.set(4,720)
# print(cap.get(3))
# print(cap.get(4))
while (cap.isOpened()):
    ret, frame = cap.read()
    if  ret==True:
        
     font=cv2.FONT_HERSHEY_SIMPLEX 
     text='width'+ str(cap.get(3)) + ' height' + str(cap.get(4)) 
     date=str(datetime.datetime.now())

     cv2.putText(frame, date, (10, 30), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
     cv2.imshow("frame", frame)
     if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
     break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()