import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    blurred = cv2.blur(frame, (3, 3))
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,100,200)
    detected_circles = cv2.HoughCircles(edges,
    				cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
    			param2 = 30, minRadius = 1, maxRadius = 40)
    cv2.imshow("blurred",gray)
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            cv2.circle(frame, (a, b), r, (0, 255, 0), 2) 
            cv2.circle(frame, (a, b), 1, (0, 0, 255), 3) 
            cv2.imshow("Detected Circle", frame)
cap.release() 
cv2.destroyAllWindows()