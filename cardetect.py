import cv2
import numpy as np

frame = cv2.VideoCapture("Footage.mp4")

count = 0
success = 1

while(success):
    success, img = frame.read()

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    res, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    

    for cnts in contours:
        area = cv2.contourArea(cnts)
        if(area > 700):
            cv2.drawContours(thresh, cnts, -1, (0, 255, 0), 3)
    
    cv2.imshow("res", thresh)
    cv2.waitKey(1)