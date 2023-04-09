import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.util import random_noise
from skimage import feature
from Resources.Images import Images
import cv2 as cv

# Generate noisy image of a square
#image = np.zeros((128, 128), dtype=float)
#image[32:-32, 32:-32] = 1

#image = ndi.rotate(image, 15, mode='constant')
#image = ndi.gaussian_filter(image, 4)
#image = random_noise(image, mode='speckle', mean=0.1)

pic = Images()
image = pic.getImage()
# Compute the Canny filter for two values of sigma


edges1 = feature.canny(image)
print(type(edges1))
#for i in range(len(edges1)):
#    print(edges1[i])
edges2 = feature.canny(image, sigma=5)

# display results
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(8, 3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('noisy image', fontsize=20)

ax[1].imshow(edges1, cmap='gray')
ax[1].set_title(r'Canny filter, $\sigma=1$', fontsize=20)

ax[2].plot(510, 415, color='cyan', marker='o', linestyle='None', markersize=3)
ax[2].plot(510, 413, color='red', marker='o', linestyle='None', markersize=3)

ax[2].plot(525, 397, color='red', marker='o', linestyle='None', markersize=3)
ax[2].imshow(edges2, cmap='gray')
ax[2].set_title(r'Canny filter, $\sigma=3$', fontsize=20)

for a in ax:
    a.axis('off')

fig.tight_layout()
plt.show()