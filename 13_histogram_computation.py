import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('car.jpeg')
cv2.imshow("Image",img)

#________________________________________
#computing histogram for grayscale image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

hist = cv2.calcHist([gray],[0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()

#________________________________________
#computing histogram for color image
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')

colors = ['r','g','b']
for i,col in enumerate(colors):
    hist = cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

#________________________________________
#applying mask and then computing that particular areas histogram
blank = np.zeros(img.shape[:2],dtype='uint8')

circle = cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),200,255,-1)

masked = cv2.bitwise_and(img,img,mask=circle)
cv2.imshow("Masked image",masked)

plt.figure()
plt.title('Color Histogram for masked image')
plt.xlabel('Bins')
plt.ylabel('No. of pixels')

colors = ['r','g','b']
for i,col in enumerate(colors):
    hist = cv2.calcHist([img],[i],circle,[256],[0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv2.waitKey(0)