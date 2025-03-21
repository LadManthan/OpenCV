import cv2
import numpy as np

def load_image(path):
    img = cv2.imread(path)
    return img

def translation(img,x,y):
    translateMatrix = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img,translateMatrix,dimension)

def rotation(img,angle,rotationpoint=None):
    (height,width) = img.shape[:2]
    if rotationpoint == None:
        rotationpoint = (width//2,height//2) #taking center as rotation point

    rotationMatrix = cv2.getRotationMatrix2D(rotationpoint,angle,scale=1.0)
    dimension = (width,height)
    
    return cv2.warpAffine(img,rotationMatrix,dimension)

def flip(img,value):
    #value = 0 : flips vertically
    #value = 1 : flips horizontally
    #value = -1 : flips both horizontally & vertically
    return cv2.flip(img,value)

def main():
    path = 'car.jpeg'
    img = load_image(path)
    
    translated = translation(img,50,100)
    rotated = rotation(img,60)
    flipped = flip(img,0)
    
    cv2.imshow('Original Image',img)
    cv2.imshow('Translated Image',translated)
    cv2.imshow('Rotated', rotated)
    cv2.imshow('Flipped',flipped)
    
    cv2.waitKey(0)
    
if __name__ == '__main__':
    main()