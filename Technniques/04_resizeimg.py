
import cv2 as cv

# Reading Img
img = cv.imread('img/Dog.jpg')

Directresize = cv.resize(img, (780, 540),interpolation = cv.INTER_NEAREST)


def rescale_Frame(frame, percent=50):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation =cv.INTER_AREA)


frame_resized = rescale_Frame(img)

cv.imshow('Dog', img)
cv.imshow('Direct_resize', Directresize)
cv.imshow('image_resize', frame_resized)

cv.waitKey(0)



#The five such interpolation methods provided with OpenCV are INTER_NEAREST, INTER_LINEAR, INTER_AREA, INTER_CUBIC, and INTER_LANCZOS4.


 
 
    