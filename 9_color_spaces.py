import cv2

img = cv2.imread('car.jpeg') #BGR format
rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)


cv2.imshow('BGR',img)
cv2.imshow('RGB',rgb)
cv2.imshow('Gray',gray)
cv2.imshow('HSV',hsv)
cv2.imshow('LAB',lab)

cv2.waitKey(0)