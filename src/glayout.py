import cv2
import os
img = cv2.imread("./sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("./sample_glay.jpg", gray)

from imgcat import imgcat
imgcat(open("./sample_glay.jpg"))

