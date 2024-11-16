import cv2 as cv
import numpy as np

#_________________________creating a blank image________________________________________

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank image',blank)

#_________________________drawing rectangle_____________________________________________

#cv.rectangle takes arguments : image, start pixel, end pixel, color, thickness, lineType
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle',blank)


#another way to draw rectangle
#cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2),(0,255,0),thickness=2)
#cv.imshow('Rectangle',blank)

#_________________________drawing a circle_____________________________________________

#cv.circle takes arguments : image,centre,radius,color,thickness
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=2)
cv.imshow('Circle',blank)

#_________________________drawing a line_______________________________________________

#cv.line takes arguments : image,start point,end point,color,thickness
cv.line(blank,(375,0),(125,250),(255,255,255),thickness=2)
cv.imshow('Line',blank)

cv.waitKey(0)


#_________________________filling color to the rectangle________________________________

#cv.Filled fills the specified color to the shape
#can also use thickness=-1 for coloring
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
#cv.imshow('Rectangle',blank)


#_________________________filling color to the circle___________________________________
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)

cv.waitKey(0)
