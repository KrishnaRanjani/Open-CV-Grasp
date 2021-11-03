import numpy as np
import cv2 as cv

image = cv.imread('img\Glider.jpg')
cv.imshow('Sugar Glider', image)

# cv2.cv.rotate( src, rotateCode[, dst] )

# Rotation
def rotate(img, angle, rotation_Point=None):
    (height,width) = img.shape[:2]

    if rotation_Point is None:
        rotation_Point = (width//2,height//2)
    
    # syntax : getRotationMatrix2D: (center, angle, scale)
    rotationMatrix = cv.getRotationMatrix2D(rotation_Point, angle, 1.0)
    dimensions = (width,height)

    # Syntax :  warpAffine: (src, M, dsize, dst=..., flags=..., borderMode=..., borderValue=...)
    return cv.warpAffine(img, rotationMatrix, dimensions)

rotatedimg = rotate(image, 40)
cv.imshow('Rotated 40', rotatedimg )

rotated = rotate(image, -40)
cv.imshow('Rotated -40', rotated)

rotated_rotated = rotate(rotated, 40)
cv.imshow('Rotated Rotated', rotated_rotated)

cv.waitKey(0)
