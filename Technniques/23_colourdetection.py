# Color Detection

import cv2
import numpy as np
#BGR - Blue, Green and Red Channels

image = cv2.imread("img/Watermelon.jpg")
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

# Green Color
lower_hue = np.array([46,0,0])
upper_hue = np.array([91,255,255])

mask = cv2.inRange(hsv,lower_hue,upper_hue)
cv2.imshow("inrange",mask)
result = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Result",result)
cv2.imshow("Original",image)
cv2.waitKey(0)