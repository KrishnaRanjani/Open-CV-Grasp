#thresholding type
     

import cv2
import numpy as np
 
# input image
image = cv2.imread('input1.jpg')
 
# cv2.cvtColor is applied over the
# image input with applied parameters
# to convert the image in grayscale
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# cv2.threshold(source, thresholdValue, maxVal, thresholdingTechnique) 


# Input Image array (must be in Grayscale). 
# thresholdValue: Value of Threshold below and above which pixel values will change accordingly. 
# maxVal: Maximum value that can be assigned to a pixel. 
# thresholdingTechnique: The type of thresholding to be applied. 

#cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
#cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.
#cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. The pixel values are set to be the same as the threshold. All other values remain the same.
#cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
#cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.

# all pixels value above 120 will
# be set to 255
ret, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
 
# the window showing output images
# with the corresponding thresholding
# techniques applied to the input images
cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)
   
# De-allocate any associated memory usage 
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()