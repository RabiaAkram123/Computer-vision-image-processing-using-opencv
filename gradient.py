import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("sudoko.png",cv2.IMREAD_GRAYSCALE)
lap=cv2.Laplacian(img,cv2.CV_64F,ksize=5)  # Laplacian filter
lap=np.uint8(np.absolute(lap))  # Convert to uint8
sobl_x=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # Sobel filter in x direction
sobl_y=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # Sobel filter in y direction

sobl_x=np.uint8(np.absolute(sobl_x))  # Convert to uint8
sobl_y=np.uint8(np.absolute(sobl_y))  # Convert to uint8
canny=cv2.Canny(img,100,200)  # Canny edge detection
 
titles=['img','Laplacian','Sobel X','Sobel Y','canny']
images=[img,lap,sobl_x,sobl_y,canny]

for i in range(5):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    plt.show()


