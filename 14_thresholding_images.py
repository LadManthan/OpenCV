import cv2

img = cv2.imread('car.jpeg')
cv2.imshow('Image',img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#simple thresholding
threshold,thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold image',thresh)

#inverse thresholding
threshold,inv_thresh = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Inverse Threshold image',inv_thresh)

cv2.waitKey(0)