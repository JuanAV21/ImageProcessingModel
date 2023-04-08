#
#
# File Created: April 6, 2023
# Description: This file is to open all of the images and retrieve them to other scripts
#
#

import numpy as np
import cv2 as cv
import os


class Images:

    src_path = "/Users/jfarizpevega20@students.desu.edu/Desktop/ImageProcessingModel/Images"
    images = []

    def __init__(self):
        self.Load()

    def length(self):
        return len(self.images)

    def getImage(self, index=0):
        # Returns the desired image. Default is the first image in the list
        return self.images[index]

    def Load(self):
        pic_List = os.listdir(self.src_path)
        for filename in pic_List:
            loadedImage = cv.imread(self.src_path + "/" + filename)
            loadedImage = cv.cvtColor(loadedImage, cv.COLOR_BGR2GRAY)
            loadedImage = np.float32(loadedImage)
            self.images.append(loadedImage)

