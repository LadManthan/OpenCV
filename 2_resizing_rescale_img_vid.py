import cv2 as cv
    
#resizing for images, videos and live videos

#_________________________________________________________
capture = cv.VideoCapture('OpenCV\porsche.mp4') #capturing video
#capture = cv.VideoCapture(0) #for webcam

#_________________________________________________________
#function for resizing the display window
def rescaleFrame(frame, scale=0.75):  #default value = 0.75
    width = int(frame.shape[1] * scale)  # frame.shape[1] : width of frame
    height = int(frame.shape[0] * scale)  # frame.shape[0] : height of frame
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)  # resize the frame to declared dimensions

#_________________________________________________________
#resizing videos
while True:
    isTrue, frame = capture.read()
    if not isTrue:  # Check if the frame was captured successfully
        print("Failed to grab frame.")
        break

    frame_resized = rescaleFrame(frame,scale=.3) #resizing the display screen to be 0.3 times of actual dimensions
    
    cv.imshow('Porsche Original Video', frame)  #original video
    cv.imshow('Porsche Resized Video', frame_resized)  #resized video

    if cv.waitKey(3) & 0xFF == ord('m'):  # will break when 'm' is pressed
        break

capture.release()
cv.destroyAllWindows()

#_________________________________________________________
#resizing images
img = cv.imread('OpenCV\porsche.jpg')
img_resized = rescaleFrame(img,scale=0.5)

cv.imshow('Porsche original img',img)
cv.imshow('Porsche Resized img',img_resized)

cv.waitKey(0)

#___________________________________________________________________________________



#_________________________________________________________
#resizing for Live Videos only

capture = cv.VideoCapture(0) #capturing video using webcam

#_________________________________________________________
def changeRes(width,height):
    capture.set(3,width)   #3 refrences to width
    capture.set(4,height)  #4 refrences to height


changeRes(800,600)  #changing the resolution then displaying the frame

while True:
    isTrue, frame = capture.read()
    if not isTrue:  # Check if the frame was captured successfully
        print("Failed to grab frame.")
        break

    frame_resized = rescaleFrame(frame,scale=.3)
    cv.imshow('Porsche Video', frame)

    if cv.waitKey(5) & 0xFF == ord('m'):  # will break when 'm' is pressed
        break

capture.release()
cv.destroyAllWindows()
