import cv2
import numpy as np

img = cv2.imread('car.jpeg')
cv2.imshow("Original image :",img)

#convert to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray image : ",gray)

#canny edge detection
canny = cv2.Canny(gray,125,175)
cv2.imshow("Canny edge : ",canny)

#_______________________________________
#contour detection using findContour function
contours,hierarchies = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print("No. of contours found : ",len(contours))

#_______________________________________
#drwaing contours
blank = np.zeros(img.shape,dtype='uint8')
cv2.imshow("Blank : ",blank)

cv2.drawContours(blank, contours, -1, (0,0,255),1)
cv2.imshow("Contours drawn : ",blank)

cv2.waitKey(0)

'''
#we can also find contours by bluring the image and by using threshold function

#_______________________________________
#contour detection after blurring image
blur = cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Blur :",blur)
blur_canny = cv2.Canny(blur,125,175)
contours,hierarchies = cv2.findContours(blur_canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print("No. of contour after blurring : ",len(contours))

#_______________________________________
#contour detection using threshold
#density of pixel : <125 :- black, >255 :- white
ret, thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)

contours,hierarchies = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print("No. of contours using threshold :",len(contours))
cv2.imshow("Threshold image : ",thresh)
cv2.waitKey(0)
'''