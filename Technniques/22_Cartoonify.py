import cv2
import numpy as np

img = cv2.imread("img\image1.jpg")
cv2.imshow('Original Image', img)

#Converting to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow("Converting to RGB", img)

#Detecting edges of the input image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
cv2.imshow("edges",edges)

#Cartoonifying the image
color = cv2.bilateralFilter(img, 9, 250, 250)
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("cartoon",cartoon)

cv2.waitKey(0)
