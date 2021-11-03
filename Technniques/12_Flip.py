import numpy as np
import cv2 as cv

image = cv.imread('img\Glider.jpg')
cv.imshow('Sugar Glider', image)


# Flipping
# syntax: flip: (src, flipCode, dst=...)
# Flips a 2D array around vertical, horizontal, or both axes.

# 0 ,1,-1
flip1 = cv.flip(image, -1)
cv.imshow('Flip -1', flip1)

#  both axes
flip2 = cv.flip(image, 0)
cv.imshow('Flip 0', flip2)

flip3 = cv.flip(image, 1)
cv.imshow('Flip 1', flip3)

# Cropping
cropped = image[150:450, 150:450]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
