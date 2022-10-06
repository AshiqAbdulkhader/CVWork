#laplase transform
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('lena.jpg',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.show()

