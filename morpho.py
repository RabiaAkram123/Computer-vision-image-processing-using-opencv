import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("bubble.png",cv2.IMREAD_GRAYSCALE)
_,MASK=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)

kernal=np.ones((5,5),np.uint8)
dilation=cv2.dilate(MASK,kernal)
erosion=cv2.erode(MASK,kernal)
opening=cv2.morphologyEx(MASK,cv2.MORPH_OPEN,kernal)
closing=cv2.morphologyEx(MASK,cv2.MORPH_CLOSE,kernal)

titles=['Original Image', 'Mask','dilation','erosion', 'opening','closing']
imges=[img,MASK,dilation,erosion,opening,closing]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(imges[i],'gray')
    plt.title(titles[i])
    plt.show()