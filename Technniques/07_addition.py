import cv2 
import numpy as np 
     

image1 = cv2.imread('img/image1.jpg') 
image2 = cv2.imread('img/image2.jpg')
  
# cv2.add()
# cv2.addWeighted is applied over the

# image inputs with applied parameters
# Syntax : cv2.addWeighted(img1, wt1, img2, wt2, gammaValue)
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
  
# Output image with the weighted sum 
cv2.imshow('Weighted Image', weightedSum)
  
# De-allocate any associated memory usage  
if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows()