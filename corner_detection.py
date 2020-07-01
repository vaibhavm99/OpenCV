import cv2
import numpy as np
img = cv2.imread('corner.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = np.float32(img_gray) # Just to satisfy the algorithm
corners = cv2.goodFeaturesToTrack(img_gray, 100, 0.01, 10) # (on what image, how many are we willing to find, quality, min dist between corners)
corners = np.int0(corners)
# Filling the corners
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, (0,255,0), -1)
cv2.imshow('Corners', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
