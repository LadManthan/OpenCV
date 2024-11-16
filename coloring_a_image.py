import cv2 as cv
import numpy as np

#coloring image

#_________________________creating a blank image____________________________
blank = np.zeros((500,500,3), dtype='uint8')  
#500,500,3 : refers to height width and no. of color channels
#uint8 is data type for image

cv.imshow('Blank image',blank)


#________________________painting the image with color______________________

blank[100:300,200:400] = 0,255,0  #coloring particular pixels
cv.imshow('Coloring particular pixels',blank)

blank[:] = 0,255,0  #refrencing all the pixels to green color
cv.imshow('Coloring all the pixels',blank)

cv.waitKey(0)