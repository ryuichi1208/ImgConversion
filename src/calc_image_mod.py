import numpy as np
import cv2
import matplotlib.pyplot as plt

def makecontour(path):
    kernel = np.ones((5,5), np.uint8)
    kernel[0,0] = kernel[0,4] = kernel[4,0] = kernel[4,4] = 0
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img.shape[2] == 4:
        mask = img[:,:,3] == 0
        img[mask] = [255] * 4
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dilated = cv2.dilate(gray, kernel, iterations=1)
    diff = cv2.absdiff(dilated, gray)
    contour = cv2.adaptiveThreshold(255 - diff, 255,
                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY, 7, 8)
    return contour


plt.set_cmap("gray")
contour = makecontour("bug_chou_tawamureru_kids.png")
plt.imshow(contour)
cv2.imwrite("190831a.png", contour)
