

from skimage.feature import corner_harris, corner_subpix, corner_peaks
from matplotlib import pyplot as plt
from Resources.Images import Images
import numpy as np
import cv2 as cv


pic = Images()
image = pic.getImage()

coords = corner_peaks(corner_harris(image), min_distance=5, threshold_rel=0.02)
print(coords)
coords_subpix = corner_subpix(image, coords, window_size=40)
print(coords_subpix)

fig, ax = plt.subplots()
ax.imshow(image, cmap=plt.cm.gray)
ax.plot(coords[:, 1], coords[:, 0], color='cyan', marker='o',
        linestyle='None', markersize=6)
#ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
#ax.axis((0, 310, 200, 0))
ax.axis((0, 700, 700, 0))
plt.show()

