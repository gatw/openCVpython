import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('10543gs.png', cv.IMREAD_GRAYSCALE)
assert img is not None, "image not found"

#imgGS = cv.imwrite('10543gs.png', img)

edges = cv.Canny(img,10,100) # 100,200 for flame.png and 10,100 for flameIR.png

x = np.linspace(0, 1000,1000)
y = 662

plt.subplot(121)
plt.imshow(img, cmap = 'gray')
plt.axhline(662, color='red')
plt.title('original')

plt.subplot(122)
plt.imshow(edges, cmap = 'gray')
plt.title('edges')

plt.show()
