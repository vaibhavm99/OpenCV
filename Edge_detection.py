import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _,frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F) # Gradient (frame, data type)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5) # Gradient in x direction
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5) # Gradient in x direction
    edges = cv2.Canny(frame, 80, 100) # Using canny edge detection

    cv2.imshow('Edges', edges)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('Original', frame)
    cv2.imshow('Laplacian', laplacian)
    if cv2.waitKey(1) & 0xFF == ord('q'): # quit if pressed q
        break
cv2.destroyAllWindows()
cap.release()
