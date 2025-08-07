###############matplot.py###############
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("hadi.jpg")    

#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
print(img.shape)
plt.imshow(img) 
plt.show() # Show the plot
