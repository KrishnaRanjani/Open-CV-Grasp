import cv2 as cv
import numpy as np

img = cv.imread('img/book.jpg')

# zeros (height, width, no of colour channels)
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

#  Paint the image a certain colour
a = blank[200:300, 300:400] = 0,255, 0
cv.imshow('Green', a)

# Draw a Rectangle outline
#  Syntax: cv.rectangle(image, start_point, end_point, color, thickness)

b = cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle outline', b)

c = cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle filled', c)

# Draw a Rectangle 
d= cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', d)

#  Draw A circle
# Syntax: cv.circle(image, center_coordinates, radius, color, thickness)
e= cv.circle(blank, (250,250) , 40, (0,0,255), thickness=3)
cv.imshow('Circle', blank)
cv.imshow('Circle', e)

f = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=1)
cv.imshow('Circle', f)

# Draw a line
g = cv.line(img, (150,250), (300,400), (0,255,0), thickness=3)
cv.imshow('Line', g)

# Write text
# Syntax: putText: (img, text, org, fontFace, fontScale, color, thickness=..., lineType=..., bottomLeftOrigin=...)
e= cv.putText(blank, 'WE are learning OpenCV', (20,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', e)


cv.waitKey(0)
