import cv2                                                                   #import OpenCV
import numpy as np                                                            #import numpy
cap=cv2.VideoCapture(0)                                                       #capture video
while(True):                
    ret,frame=cap.read()                                                       #read frame
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)                             #convert to gray scale
    blur=cv2.GaussianBlur(gray,(5,5),0)                                      #blur the frame
    ret,th = cv2.threshold(blur,20,255,cv2.THRESH_BINARY_INV)                #apply threshold inverse
    contours, hierarchy = cv2.findContours(th,1,cv2.CHAIN_APPROX_NONE)        #find contours
    if len(contours) > 0:                                                     
        for cnt in contours:                                                   #iterate through all the contours
            rect=cv2.minAreaRect(cnt)                                          #find minimum enclosing rectangle
            box=cv2.boxPoints(rect)                                             #find coordinates of the rectamgle
            box=np.int0(box)
            cv2.drawContours(frame,[box],0,(0,0,255),2)                         #draw rectangle around the contour
    cv2.imshow('final',frame)                                                   #display video feed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
