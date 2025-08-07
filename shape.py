import cv2  

img = cv2.imread("photo.jpg") # Read the image from file

print(img.shape)  # Print the shape (dimensions) of the image (height, width, channels)
print(img.size)   # Print the total number of pixels in the image
print(img.dtype)  # Print the data type of the image pixels

resized_img = cv2.resize(img, (800, 600))  # Resize the image to 800x600 pixels

b, g, r = cv2.split(resized_img)  
# print("Blue channel:\n", b, "\n")
# print("Green channel:\n", g, "\n")
# print("Red channel:\n", r, "\n")
# img = cv2.merge([b, g, r]) 
# cv2.imshow('imag', img)  
# cv2.waitKey(0)  
# cv2.destroyAllWindows()  
print("Blue channel:\n", b.shape, "\n")
print("Blue channel:\n", type(b), "\n")
print("Blue channel:\n",( b[:,3]), "\n")
print (b[8,8])
