import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('flame.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "image not found"

edges = cv.Canny(img,100,200)

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.title('original')

plt.subplot(122)
plt.imshow(edges, cmap = 'gray')
plt.title('edges')

plt.show()


