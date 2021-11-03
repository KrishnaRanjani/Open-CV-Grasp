import cv2 as cv
import numpy as np


img = cv.imread('img/Dog.jpg')

kernel = np.ones((5,5), np.uint8)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank imahe', blank)

#converting the image to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image', gray)

# Gaussian Blur operation --  high-frequency components are reduced.
blur1 = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur Image', blur1)

blur2 = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur grayImage', blur2)

# Canny edge detection.

canny = cv.Canny(blur1, 125, 175)
cv.imshow('Canny Edges for img', canny)

canny1 = cv.Canny(blur2, 125, 175)
cv.imshow('Canny Edges for Gray', canny)

# Erosion: 
# It is useful for removing small white noises

# Dilation:
# In cases like noise removal, erosion is followed by dilation.

# The first parameter is the original image,
# kernel is the matrix with which image is convolved 
# third parameter is the number of iterations, which will determine how much you want to erode/dilate a given image.

imgDialation = cv.dilate(canny,kernel,iterations=1)
cv.imshow("Dialation Image",imgDialation)

imgEroded = cv.erode(imgDialation,kernel,iterations=1)
cv.imshow("Eroded Image",imgEroded)

cv.waitKey(0)
