#https://bitworks.software/en/scalable-realtime-opencv-processing-with-zeromq.html
#https://github.com/wasit7/2020/tree/master/zmq
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    #out = frame
    out = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',out)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()