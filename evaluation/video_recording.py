import numpy as np
import cv2

cap = cv2.VideoCapture('input.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi',fourcc, 20.0, (640,480))
while(cap.isOpened()):
    ret, frame = cap.read()
    frame=cv2.resize(frame,(int(640),int(480)))

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
