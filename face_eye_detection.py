import cv2
import numpy as np

# Importing the classifier
face_classifier = cv2.CascadeClassifier('C:\Python\Python38\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('C:\Python\Python38\Lib\site-packages\cv2\data\haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Converting to grayscale
    faces = face_classifier.detectMultiScale(gray, 1.3, 5) # Detecting faces
    for (x, y, w, h) in faces: # iterating for all faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi = gray[y:y+h, x:x+w] # As eye will never be detected outside face, so it will prevent false positives
        roi_color =  frame[y:y+h, x:x+w]
        eyes = eye_classifier.detectMultiScale(roi) # Going with default values
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
