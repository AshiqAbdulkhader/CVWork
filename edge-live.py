import cv2 
import numpy as np 

cap = cv2.VideoCapture(0) 

while(1): 
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([30,150,50]) 
    upper_red = np.array([255,255,180])
    mask = cv2.inRange(hsv, lower_red, upper_red)  
    res = cv2.bitwise_and(frame,frame, mask= mask) 
    edges = cv2.Canny(frame,100,200) 
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)
    cv2.imshow("edges",edges)
    cv2.imshow("Contours", frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break

cap.release() 
cv2.destroyAllWindows()
