import cv2
import numpy as np

img = cv2.imread('car.jpeg')
cv2.imshow("Image",img)

blank = np.zeros(img.shape[:2],dtype='uint8')

#creating a mask
mask = cv2.circle(blank, (img.shape[1]//2,img.shape[0]//2 + 60),250,255,-1)
masked = cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("masked image",masked)
cv2.waitKey(0)

'''
#applying mask on video
capture = cv2.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    
    blank = np.zeros(frame.shape[:2],dtype='uint8')
    
    #creating mask
    mask = cv2.circle(blank, (frame.shape[1]//2,frame.shape[0]//2),200,255,-1)
    masked = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("masked video",masked)
    
    if cv2.waitKey(5) & 0xFF == ord('m'):
        break

capture.release()
cv2.destroyAllWindows()
'''