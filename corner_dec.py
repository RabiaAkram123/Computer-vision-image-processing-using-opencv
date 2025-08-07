# ###############corner detect################3
# import numpy as np
# import cv2
 
# img=cv2.imread("chesboard.png")
# cv2.imshow("input Image", img)

# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray1=np.float32(gray)

# dst=cv2.cornerHarris(gray1,2,3,0.04)
# dst1=cv2.dilate(dst,None)
# img[dst1>0.01*dst1.max()]=[0,0,255]

# cv2.imshow("output Image", img)
# if cv2.waitKey(0) & 0xFF == 27:
#     cv2.destroyAllWindows()
    
################shi tomasi corner detection##############
import numpy as np
import cv2

img = cv2.imread("chesboard.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray, 25, 0.01, 10)

corners1 = corners.astype(int)  

for i in corners1:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow("output Image", img)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
