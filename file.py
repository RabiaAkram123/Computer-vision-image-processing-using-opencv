import numpy as np
import cv2

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 250), (255, 255, 255), -1)
img2 = cv2.imread("img.png")

img2 = cv2.resize(img2, (500, 250))
#bitand = cv2.bitwise_and(img2, img1)
#bitor = cv2.bitwise_or(img2, img1)
#bitxor = cv2.bitwise_xor(img2, img1)
bitnot1 = cv2.bitwise_not(img2)
bitnot2 = cv2.bitwise_not(img2)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
#cv2.imshow('bitand', bit)
#cv2.imshow('bitor', bitor)
#cv2.imshow('bitxor', bitxor)
cv2.imshow('bitnot1', bitnot1)
cv2.imshow('bitnot2', bitnot2)
cv2.waitKey(0)
cv2.destroyAllWindows()
