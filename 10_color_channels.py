import cv2
import numpy as np

img = cv2.imread('car.jpeg')
cv2.imshow("Image",img)

#creating blank image
blank = np.zeros(img.shape[:2],dtype='uint8')

#splitting image into color channels
b,g,r = cv2.split(img)

#creating image of only one color
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

cv2.imshow("Blue Channel",blue)
cv2.imshow("Green Channel",green)
cv2.imshow("Red Channel",red)

'''
#displaying individual channels (grayscale representation)
#Brighter pixels mean higher intensity of that color in the original image.

cv2.imshow("Blue Channel",b)
cv2.imshow("Red Channel",r)
cv2.imshow("Green Channel",g)

merged = cv2.merge([b,g,r])
cv2.imshow("Merged",merged)
'''

cv2.waitKey(0)