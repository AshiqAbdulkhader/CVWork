import cv2
import numpy as np

img1 = cv2.imread('seed.jpeg', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)

imgKp1 = cv2.drawKeypoints(img1, kp1, None)

cv2.imshow('Kp1',imgKp1)
cv2.imshow('img1',img1)
cv2.waitKey(0)