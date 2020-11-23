import cv2 
  
# capture frames from a video 
cap = cv2.VideoCapture('/Users/shikhharsiingh/Desktop/Study/Productathon/Footage.mp4') 
  
# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('/Users/shikhharsiingh/Desktop/Study/Productathon/cars.xml') 
  
# loop runs if capturing has been initialized.
ret = 1 
while ret: 
    # reads frames from a video 
    ret, frames = cap.read() 
      
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
      
    # Detects cars of different sizes in the input image 
    cars = car_cascade.detectMultiScale(gray, 1.1, 5) 
      
    # To draw a rectangle in each cars 
    for (x,y,w,h) in cars: 
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) 
        
    # Display frames in a window  
    cv2.imshow('video2', frames) 
      
    # Wait for Esc key to stop 
    if cv2.waitKey(1) == 27: 
        break
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows() 