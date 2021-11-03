import cv2 as cv

img = cv.imread('img/Dog.jpg')
cv.imshow('Dog', img)

img1 = cv.imread('img/Dog.jpg', 0)
cv.imshow('Dog', img1)


cv.waitKey(0)