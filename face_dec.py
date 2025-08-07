# import numpy as np
# import cv2
# face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# image=cv2.imread("face.jpg")
# gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# face=face_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5)

# for(x,y,w,h)in face:
#     cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
#     cv2.putText(image,"Face",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2) 

# cv2.imshow("output  Image", image)
# cv2.waitKey(0)


##########for video##############
import numpy as np
import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while cap.isOpened():
    _,img=cap.read()
    gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5)

    for(x,y,w,h)in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(img,"Face",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2) 
        cv2.imshow("output  Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release
