import cv2

# Load the cascade

face_cascade = cv2.CascadeClassifier('haarcascade\haarcascade_frontalface_default.xml')

# To capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, img = cap.read()
    
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1 ,minNeighbors = 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(10) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()