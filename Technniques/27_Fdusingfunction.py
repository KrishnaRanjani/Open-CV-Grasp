import numpy as np
import cv2

#Loading the image 
image = cv2.imread('img\image.jpg')

#Converting to grayscale
test_image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# OpenCV loads an image in BGR format,So we write a function for convert it
def convertToRGB(images):
    return cv2.cvtColor(images, cv2.COLOR_BGR2RGB)

haar_cascade_face = cv2.CascadeClassifier('haarcascade\haarcascade_frontalface_default.xml')

# Python: cv2.CascadeClassifier.detectMultiScale(image[, scaleFactor[, minNeighbors[, flags[, minSize[, maxSize]]]]]) → objects¶

faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.1, minNeighbors = 4)
print('Faces found in image : ', len(faces_rects))

for (x,y,w,h) in faces_rects:
     cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("image",convertToRGB(image))
cv2.imshow("image",image)

cv2.waitKey(0)


