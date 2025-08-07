import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("eye.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

kernal=np.ones((5,5),np.float32)/25

dst=cv2.filter2D(img,-1,kernal)  
blur=cv2.blur(img,(5,5))
gblur=cv2.GaussianBlur(img,(5,5),0)
mblur=cv2.medianBlur(img,5)


titles = ['Image','2D convolution','blurred image','Gaussian blurred image','Median blurred image']
images = [img,dst,blur,gblur,mblur]

for i in range(5):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i],'gray')   # No 'gray' here, since it's a color image
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    plt.show()
