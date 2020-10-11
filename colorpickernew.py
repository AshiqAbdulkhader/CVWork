import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

image_hsv = None
pixel = (0,0,0)

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixelbgr = frame[y,x]
        print("At (x,y):","("+str(x)+","+str(y)+")")
        print("B:",pixelbgr[0],"G:",pixelbgr[1],"R:",pixelbgr[2])
        print("__________________________________________________")

val = input("Choose between using your webcam or a locally stored image(webcam/image):")
cap = cv2.VideoCapture(0)

if(val.lower() == "cam" or val.lower() == "webcam"):
    while(1):
        _,frame = cap.read()
        cv2.imshow("Feed",frame)
        cv2.setMouseCallback("Feed", pick_color)
        k = cv2.waitKey(5) & 0xFF
        if(k == 27):
            break

if(val.lower() == "img" or val.lower() == "image"):
    file_path = filedialog.askopenfilename()
    frame = cv2.imread(file_path)
    cv2.imshow("BGR",frame)
    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    cv2.imshow("HSV",frame_hsv)
    frame_bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("BW",frame_bw)
    cv2.setMouseCallback("HSV", pick_color)
    cv2.setMouseCallback("BGR", pick_color)
    cv2.setMouseCallback("BW", pick_color)

cv2.waitKey(0)
cv2.destroyAllWindows()