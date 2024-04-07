import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("6222.png"))

if img is None:
    sys.exit("image not found. exiting...")

cv.imshow("display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("6222.png")
