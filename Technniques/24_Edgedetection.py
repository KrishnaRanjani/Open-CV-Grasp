import cv2 
import numpy as np

image = cv2.imread("img/Kola.jpg")
cv2.imshow("orginal",image)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


canny_image = cv2.Canny(gray,150, 200)
cv2.imshow("canny_image",canny_image)

# Erosion and Dilation
kernel = np.ones((5,5), np.uint8)

#Dilation
dilate_image = cv2.dilate(canny_image, kernel, iterations=1)
cv2.imshow("dilate_image",dilate_image)

#Erosion
kernel = np.ones((1,1), np.uint8)
erode_image = cv2.erode(dilate_image,kernel, iterations=1)
cv2.imshow("erode_image",erode_image)

display = np.hstack((canny_image,dilate_image,erode_image))
cv2.imshow("Display",display)

cv2.waitKey(0)