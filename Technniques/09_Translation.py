import numpy as np
import cv2 as cv

image = cv.imread('img\Glider.jpg')
cv.imshow('Park', image)

# Translation of image
# Load the image 
# Define an affine transformation matrix
# Apply cv2.warpAffine function to perform the translation

def translate(img, x, y):
    translationMatrix = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translationMatrix, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# x,y
translatedimg = translate(image, 100, 100)
cv.imshow('Translated1', translatedimg)

# -x,y
translatedimg = translate(image, -100, 100)
cv.imshow('Translated2', translatedimg)

# x,-y
translatedimg = translate(image, 100, -100)
cv.imshow('Translated3', translatedimg)

# =x,=y
translatedimg = translate(image, -100, -100)
cv.imshow('Translated4', translatedimg)

cv.waitKey(0)
