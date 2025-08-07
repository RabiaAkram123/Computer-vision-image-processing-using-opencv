
import cv2
# import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("gradient.png",0)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY) # Simple binary thresholding
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV) # Inverted binary thresholding

_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC) # Truncate thresholding (values above threshold are set to threshold value)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO) # To zero thresholding (values below threshold are set to zero)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV) # Inverted to zero thresholding (values above threshold are set to zero)
tetiles=[th1, th2, th3, th4, th5]
titles=['Original Image', 'Binary ', 'Inverted Binary', 'Trunch', 'To Zero ', 'Inverted To Zero ']
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(tetiles[i],'gray')
    plt.title(titles[i])
    plt.show()


# cv2.imshow("image",img)
# cv2.imshow("th1",th1)
# cv2.imshow("th2",th2)
# cv2.imshow("th3",th3)
# cv2.imshow("th4",th4)
# cv2.imshow("th5",th5)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
