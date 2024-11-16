import cv2 as cv
import numpy as np

#_________________________writing text_____________________________________________

#creating blank image
writing_text = np.zeros((500,500,3),dtype='uint8')
cv.imshow('Text',writing_text)

#cv.putText takes arguments  : image, start point, font family, font scale, color, thickness
cv.putText(writing_text,'Hello, how are you?',(0,125),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=1)
cv.imshow('Text',writing_text)


#creating a rectanlge and then writing text in it
cv.rectangle(writing_text, (5,170), (225,225), (255,255,255), thickness=2)
cv.imshow('Text',writing_text)

cv.putText(writing_text,"I'm fine.",(12,200),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=1)
cv.imshow('Text',writing_text)

cv.waitKey(0)