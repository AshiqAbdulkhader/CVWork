import cv2
import numpy as np

cap = cv2.VideoCapture(0)
h = s = v = []
frame = None

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = hsv[y,x]
        print("At (x,y):","("+str(x)+","+str(y)+")")
        print("H:",pixel[0],"S:",pixel[1],"V:",pixel[2])
        print("__________________________________________________")
        h.append(pixel[0])
        s.append(pixel[1])
        v.append(pixel[2])

def show_color(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEMOVE:
        pixel = hsv[y,x]
        print("At (x,y):","("+str(x)+","+str(y)+")")
        print("H:",pixel[0],"S:",pixel[1],"V:",pixel[2])
        print("__________________________________________________")

while(1):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('feed',frame)
    cv2.setMouseCallback("feed", pick_color)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    if k == 101:# press e to generate mask based on selected points
        cv2.destroyWindow('feed')
        lower = np.array([min(h),min(s),min(v)])
        upper = np.array([max(h),max(s),max(v)])
        while(1):
            _,frame = cap.read()
            cv2.imshow('feed',frame)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv,lower,upper)
            res = cv2.bitwise_and(frame,frame, mask = mask)
            cv2.imshow('detection', res)
            cv2.setMouseCallback("feed", show_color)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                exit()
                break

cv2.destroyAllWindows()