# Countour -- line joining all the points along the boundary of an image

# Used in : shape analysis, size of the object, and object detection.

# findContour() function  
# drawContours()


# Algorithms:
# CHAIN_APPROX_SIMPLE
# CHAIN_APPROX_NONE   

# Read the Image and convert it to Grayscale Format
# Apply Binary Thresholding
# Find the Contours
# Draw Contours on the Original Image

import cv2
import numpy as np


# read the image
image = cv2.imread('img/Puppy.jpg')

slide = np.zeros(image.shape, dtype='uint8')

img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img_gray, (5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur image', blur)

canny = cv2.Canny(blur, 125, 175)
cv2.imshow('Canny Edges', canny)

# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')



cv2.drawContours(image, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=1, )
cv2.imshow('DrawContour', image)

cv2.imwrite('contours_none_image1.jpg', image)

cv2.waitKey(0)
