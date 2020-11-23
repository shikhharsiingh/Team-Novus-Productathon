import cv2
import numpy as np

frame = cv2.VideoCapture("/Users/shikhharsiingh/Desktop/Study/Productathon/Footage.mp4")

success = 1

images = []

kernel = np.ones((4, 4), np.uint8)
while(success):
    success, img = frame.read()
    images.append(img)

for i in range(len(images) - 1):
    grayA = cv2.cvtColor(images[i], cv2.COLOR_RGB2GRAY)
    grayB = cv2.cvtColor(images[i + 1], cv2.COLOR_RGB2GRAY)

    diff = cv2.absdiff(grayA, grayB)

    _,thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, kernel, iterations=1)

    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    height, width = dilated.shape
    min_x, min_y = width, height
    max_x = max_y = 0
    
    amg = images[i].copy()
    
#    for cnts, hier in zip(contours, hierarchy):
#        (x,y,w,h) = cv2.boundingRect(cnts)
#        min_x, max_x = min(x, min_x), max(x+w, max_x)
#        min_y, max_y = min(y, min_y), max(y+h, max_y)
#        cv2.rectangle(amg, (x,y), (x+w,y+h), (255, 0, 0), 2)
#    
#    if max_x - min_x > 0 and max_y - min_y > 0:
#        cv2.rectangle(amg, (min_x, min_y), (max_x, max_y), (255, 0, 0), 2)

#    amg = images[i].copy()
    i = 0;
    for cnts in contours:
        i += 50
        cv2.drawContours(amg, cnts, -1, ((3 * i)%255, (2 * i)%255, (i + 50)%255), 3)
        (x,y,w,h) = cv2.boundingRect()

    cv2.imshow("res", amg)
    
    if cv2.waitKey(15) == 27:
        break;