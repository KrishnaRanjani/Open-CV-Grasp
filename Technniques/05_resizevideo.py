
import cv2 as cv
# Reading Videos

capture = cv.VideoCapture('Dog.mp4')

#The five such interpolation methods provided with OpenCV are INTER_NEAREST, INTER_LINEAR, INTER_AREA, INTER_CUBIC, and INTER_LANCZOS4.

def rescale_Frame(frame, percent = 70):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation =cv.INTER_AREA)

while True:
    isTrue, frame = capture.read()
    frame_resized = rescale_Frame(frame)
    if isTrue:    
        cv.imshow('Video', frame)
        cv.imshow('Video_resize', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
 
 
 
    