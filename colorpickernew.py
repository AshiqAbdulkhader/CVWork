import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

image_hsv = None
pixel = (0,0,0)

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # pixelhsv = frame_hsv[y,x]
        pixelbgr = frame[y,x]
        # pixelbw = frame_bw[y,x]
        print("At (x,y):","("+str(x)+","+str(y)+")")
        # print("H:",pixelhsv[0],"S:",pixelhsv[1],"V:",pixelhsv[2])
        print("B:",pixelbgr[0],"G:",pixelbgr[1],"R:",pixelbgr[2])
        # print("B:",pixelbw[0],"W:",pixelbw[1])
        # print(pixelbw)
        print("__________________________________________________")

val = input("Choose between using your webcam or a locally stored image(webcam/image):")
if(val.lower() == "cam" or val.lower() == "webcam"):
    val2 = int(input("Have multiple cameras? choose one: "))
    if(val2 == ""):
        val2 = 0
    while(1):
        cap = cv2.VideoCapture(0)
        _,frame = cap.read()
        cv2.imshow("Feed",frame)
        # frame_bw = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow("B/W(Feed)",frame_bw
        # frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        # cv2.imshow("HSV(Feed)",frame_hsv)
        cv2.setMouseCallback("Feed", pick_color)
        # cv2.setMouseCallback("B/W(Feed)", pick_color)
        # cv2.setMouseCallback("HSV(Feed)", pick_color)
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