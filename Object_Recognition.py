#PROJECT IS ABOUT CONTROLLING MOUSE VIA OPEN CV
import cv2 as cv#capture video from camera
import numpy as np  


cap=cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
fgbg = cv.createBackgroundSubtractorMOG2()
while True:
    ret,frame=cap.read()#capture frame by frame of video
    if not ret:
        print("Can't read video")
        break
    #operation on frame by frame reading of video
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    fgmask = fgbg.apply(frame)
    contours, _ = cv.findContours(fgmask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv.contourArea(cnt) > 2300:  # ignore small movements/noise
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)#(x, y)-->top left corner of rectangle and (0, 255, 0) means green (B=0, G=255, R=0).
            
    # Step 5: Display result of detected objects
    cv.imshow('Detected Objects', frame)



    if(cv.waitKey(1)==ord('q')): 
        break
cap.release()#necessary to destroy video
cv.destroyAllWindows()
#Code
#In all the above functions, you will see some common arguments as given below:

#img : The image where you want to draw the shapes
#color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
#thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
#lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curves.