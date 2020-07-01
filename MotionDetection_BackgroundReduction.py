import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    _, frame = cap.read()
    fg_mask = fgbg.apply(frame)

    mine = cv2.bitwise_and(frame, frame, mask = fg_mask)

    # Contours are lines around the moving area, sort of boundary
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # Draing the contours
    #cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 900:
            continue
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame,'Motion', (x, y), font,1,(200,255,255),2,cv2.LINE_AA) # Writing text (image, text, start point, font, size, color, line width, something)


    cv2.imshow('Motion', mine)
    cv2.imshow('Frame', frame)
    cv2.imshow('Foreground', fg_mask)

    if cv2.waitKey(1) & 0xFF == ord('q'): # quit if pressed q
        break
cap.release()
cv2.destroyAllWindows()
