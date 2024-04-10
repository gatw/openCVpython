import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('10543gs.png',)

assert img is not None, "image not found"

blur = cv.medianBlur(img, 5)

plt.subplot(121)
plt.imshow(img)
plt.title('original')

plt.subplot(122)
plt.imshow(blur)
plt.title('blurred')

plt.show()
