import cv2 as cv


#READING IMAGES
img = cv.imread('OpenCV\porsche.jpg')  #path where image is stored
cv.imshow('Porsche',img)  #take 2 arg : name of window and actual matrix/pixel to display

cv.waitKey(0) #delay


#READING VIDEOS
capture = cv.VideoCapture('OpenCV\porsche.mp4')  #path where video is stored

#capture = cv.VideoCapture(0) #accessing through webcam
# 0 : webcam , 1,2,3... : Additional cameras connected to your computer.

while True:
    isTrue, frame = capture.read() # takes 2 arg : frame-reads video frame by frame and isTrue-a boolean that says whether the video was successfully read or not
    
    cv.imshow('Porsche Video',frame) #display video frame by frame
    
    #termination condition
    if cv.waitKey(5) & 0xFF==ord('m'):  #will break when 'm' is pressed
        break

capture.release()
cv.destroyAllWindows()  #destroy all the windows