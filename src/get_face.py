import matplotlib.pyplot as plt
import cv2

img = cv2.imread("lena_std.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cascade.detectMultiScale(gray, scaleFactor=1.5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255))

plt.imshow(img[..., ::-1])
