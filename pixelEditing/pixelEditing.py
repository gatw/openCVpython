import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('10543.png', cv.IMREAD_GRAYSCALE)

px1 = img[10,10]
size = img.shape

#print (size)

#print(px1)

#plt.subplot(121)
#plt.imshow(img, cmap='gray')
#plt.title('original')

#plt.show()

def denoising(image):
    imgN = image.copy()
    height,width = imgN.shape

    for h in range(0, height):
        for w in range(0, width):
            while image[h,w] != 30:
                if image[h+50,w] == 30 and image[h,w+50] == 30:
                    image[h,w] = 30

    plt.subplot(121)
    plt.imshow(image, cmap='gray')
    plt.title('original')

    plt.subplot(122)
    plt.imshow(imgN, cmap='gray')
    plt.title('denoised')
    
    plt.show()

    return imgN

imgDN = denoising(img)

