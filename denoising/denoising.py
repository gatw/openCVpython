import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('10543gs.png')

dst = cv.fastNlMeansDenoisingColored(img,None,10,10,7,21)

plt.subplot(121)
plt.title('original')
plt.imshow(img)

plt.subplot(122)
plt.title('denoised')
plt.imshow(dst)

plt.show()
