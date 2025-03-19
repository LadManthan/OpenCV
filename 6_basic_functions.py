import cv2 as cv

def load_image(image_path):
    img = cv.imread(image_path)
    img = cv.resize(img, (512, 512))
    return img

def convert_to_grayscale(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def apply_gaussian_blur(img, kernel_size=(7,7)):
    return cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)

def detect_edges(img, threshold1=125, threshold2=175):
    #finding edges present in image
    return cv.Canny(img, threshold1, threshold2)

def dilate_image(img, kernel_size=(7,7), iterations=3):
    #thickens edges, connects broken lines
    return cv.dilate(img, kernel_size, iterations=iterations)

def erode_image(img, kernel_size=(3,3), iterations=4):
    #removes noise, thins edges
    return cv.erode(img, kernel_size, iterations=iterations)

def resize_image(img, size=(300, 300)):
    return cv.resize(img, size)

def crop_image(img, height=128):
    return img[0:height, :]

def main():
    image_path = 'car.jpeg'  #path of your image
    img = load_image(image_path)
    
    gray = convert_to_grayscale(img)
    blur = apply_gaussian_blur(img)
    canny = detect_edges(img)
    dilated = dilate_image(canny)
    eroded = erode_image(dilated)
    resized = resize_image(img)
    cropped = crop_image(img)
    
    cv.imshow('Original Image', img)
    cv.imshow('Gray Image', gray)
    cv.imshow('Blur Image', blur)
    cv.imshow('Canny Edge', canny)
    cv.imshow('Dilated Image', dilated)
    cv.imshow('Eroded Image', eroded)
    cv.imshow('Resized Image', resized)
    cv.imshow('Cropped Image', cropped)
    
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
