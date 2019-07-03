import numpy as np
import cv2
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

print(cap.get(3)) #width
print(cap.get(4)) #height
print(cap.get(5)) # fps

frameList = []

numberOfSavedFrames = 30*7

i=0
vidNb = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()


    frameList.append(frame)

    if(len(frameList) > numberOfSavedFrames):
#        cv2.imshow('frame',frameList[len(frameList)-1])
        frameList.pop(0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    input_state = GPIO.input(18)
    if(input_state == False):
        out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640, 480))
        for frame in frameList:
            out.write(frame)
        vidNb += 1
        
        
    i += 1

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()
