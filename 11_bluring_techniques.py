import cv2

img = cv2.imread('car.jpeg')
cv2.imshow("Original image",img)

#average blur
average = cv2.blur(img,(3,3))
cv2.imshow("Average blur",average)

#Gaussian Blur
gaussian = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow("Gaussian blur",gaussian)

#median blur
median =- cv2.medianBlur(img,3)
cv2.imshow("Median Blur",median)

#bilateral Blur
bilateral = cv2.bilateralFilter(img,20,50,50)  #higher the values more smugged the image will be
cv2.imshow("Bilateral blur",bilateral)

cv2.waitKey(0)

'''
#____________________________________________
#applying blur on video
capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read() # takes 2 arg : frame-reads video frame by frame and isTrue-a boolean that says whether the video was successfully read or not
    #cv2.imshow("Frame",frame)
    
    #average = cv2.blur(frame,(7,7))
    #cv2.imshow("Average blur",average)
    
    bilateral = cv2.bilateralFilter(frame,10,30,30)  #higher the values more smugged the image will be
    cv2.imshow("Bilateral blur",bilateral)
    
    #termination condition
    if cv2.waitKey(5) & 0xFF==ord('m'):  #will break when 'm' is pressed
        break

capture.release()
cv2.destroyAllWindows()
'''