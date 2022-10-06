# perspective transform
import cv2
import numpy as np
import matplotlib.pyplot as plt

# read image
img = cv2.imread('images/road.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# define source and destination points
height = img.shape[0]
width = img.shape[1]
# source points
src = np.float32([[width/2-60, height/2+100], [width/2+60,
                 height/2+100], [0, height], [width, height]])
# destination points
dst = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# get perspective transform matrix
M = cv2.getPerspectiveTransform(src, dst)
# warp image
warped = cv2.warpPerspective(img, M, (width, height))

# plot
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
f.tight_layout()
ax1.imshow(img)
ax1.set_title('Original Image', fontsize=30)
ax2.imshow(warped)
ax2.set_title('Warped Image', fontsize=30)
plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
plt.show()
