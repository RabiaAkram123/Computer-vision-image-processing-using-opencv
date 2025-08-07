import cv2
import numpy as np
import matplotlib.pyplot as plt
img=np.zeros((200,200),np.uint8)
cv2.rectangle(img,(0,100),(200,200),(255),-1)  # Create a white rectangle
cv2.rectangle(img,(0,50),(100,100),(127),-1)  # Create a gray rectangle
# img=cv2.imread("hadi.jpg")
# resize_img=cv2.resize(img,(800,600))  
# cv2.imshow("image",resize_img)
# b,g,r=cv2.split(resize_img)  # Split the image into blue, green, and red channels
# cv2.imshow("blue",b)
# cv2.imshow("green",g)           
# cv2.imshow("red",r)

cv2.imshow("image",img)
plt.hist(img.ravel(),256,[0,256])
# plt.hist(b.ravel(),256,[0,256])
# plt.hist(g.ravel(),256,[0,256])
# plt.hist(r.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
