import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_red = np.array([255, 0, 0])
    upper_red = np.array([255, 0,21])
    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255]) 

    # Object Tracking
    # HSV - Hue, Saturation and Value 
    # Threshold the HSV image to get only blue colors
    # syntax: resultarray = inRange(sourcearray, upperboundarray, lowerboundarray)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask1 = cv2.inRange(hsv,lower_red, upper_red )
    mask2 = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask + mask1 +mask2)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()