# This is how green screens work
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    '''
    hsv = hue saturation value
    hue - which color
    saturation - how much
    value - what intensity of that color
    Just another way to define colors
    '''
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    '''
    Using T-shirt having gray and yellow colors
    '''
    lower_gray = np.array([20,20,20])
    upper_gray = np.array([190,190,190])
    mask = cv2.inRange(frame, lower_gray, upper_gray) # Anything that is within this range, initially everything(in the range = 1, not in range = 0)
    result = cv2.bitwise_and(frame, frame, mask = mask) # In the frame where there is something in frame and mask is true
    # Averaging to remove noise
    kernel = np.ones((5,5),np.float32)/25 # 15 * 15 = 225
    smoothed = cv2.filter2D(result, -1, kernel)
    blur = cv2.GaussianBlur(result, (5,5), 0) # Gaussian Blur
    median = cv2.medianBlur(result, 5) # Median Blur
    cv2.imshow('Median Blur', median)
    cv2.imshow('Smoothed', smoothed)
    cv2.imshow('Gaussian Blur', blur)
    '''
    Morphological Transformations
    '''
    '''
    Erosion - a slider moves, if all pixels are same except one in slider odd one out is changed
    Dialation - it does opposite of erosion, it pushes out the pixels
    '''
    kernel1 = np.ones((5,5),np.uint8)
    erosion = cv2.erode(mask, kernel1, iterations = 1) # Erode using the mask
    dialation = cv2.dilate(mask, kernel1, iterations = 1) # Dialate using mask
    '''
    Personal testing
    '''
    mine1 = cv2.bitwise_or(erosion, erosion, mask = dialation)
    mine = cv2.bitwise_and(frame, frame, mask = mine1)
    '''
    Opening - removing false positives(stuff from background)
    Closing - removing false negatives
    '''
    opening = cv2.morphologyEx(mine, cv2.MORPH_OPEN, kernel1)
    closing = cv2.morphologyEx(mine, cv2.MORPH_CLOSE, kernel1)



    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
    cv2.imshow('Final', mine)
    cv2.imshow('Mine', mine1)
    cv2.imshow('Erosion', erosion)
    cv2.imshow('Dialation', dialation)
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)    
    if cv2.waitKey(1) & 0xFF == ord('q'): # quit if pressed q
        break
cv2.destroyAllWindows()
cap.release()
