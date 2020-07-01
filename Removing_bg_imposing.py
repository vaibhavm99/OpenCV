import cv2
import numpy as np
img1 = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
img2 = cv2.imread('logo.png',cv2.IMREAD_COLOR)
row,col,_ = img2.shape # taking dimensions of logo
roi = img1[0:row, 0:col] # Where logo is supposed to be present
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV) # 0 if less than 220 and 255 if greater than 220
mask_inv = cv2.bitwise_not(mask) # where logo is not present

img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv) # background from first image
img1_fg = cv2.bitwise_and(img2,img2,mask =mask) # foreground from second Image
dst = cv2.add(img1_bg, img1_fg) # final section of that Image
img1[0:row, 0:col] = dst # Adding the logo
# Printing the Image
cv2.imshow('Image', mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
