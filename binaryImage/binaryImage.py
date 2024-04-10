# import the necessary libraries
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# read the image as a gray scale image
img = cv.imread('10543.png', cv.IMREAD_GRAYSCALE)

#exception flag for wrong file name
assert img is not None, "file not found"

# information of the image
numberOfPixels = img.size
resolution = img.shape
print("number of pixels = " + str(numberOfPixels))
print("resolution = " + str(resolution))

# cross checking pixel intensity
px = img[100,100]
print(px)
print(type(px))

# how the pixel intensity is stored
print(img[0])

##### binarization of the image #####

# simple binarization
# if the pixel intensity > 30 ---> pixel intensity = 255 else ---> 0
ret1, imgSimpleBin = cv.threshold(img, 30, 255, cv.THRESH_BINARY) 

# blur the image to reduce noise and then otsu thresholding
imgBlur = cv.medianBlur(img, 7)
ret2,imgOtsu = cv.threshold(imgBlur, 0, 255, cv.THRESH_OTSU)

imgBlur2 = cv.medianBlur(img,101)
ret3, imgOtsu2 = cv.threshold(imgBlur2, 0, 255, cv.THRESH_OTSU)


plt.subplot(141)
plt.title('image')
plt.imshow(img, cmap = 'gray')

plt.subplot(142)
plt.title('simple binary')
plt.imshow(imgSimpleBin, 'gray', vmin = 0, vmax = 255)

plt.subplot(143)
plt.title('otsu binary')
plt.imshow(imgOtsu, 'gray', vmin = 0, vmax = 255)

plt.subplot(144)
plt.title('otsu binary')
plt.imshow(imgOtsu2, 'gray', vmin = 0, vmax = 255)
plt.show()
