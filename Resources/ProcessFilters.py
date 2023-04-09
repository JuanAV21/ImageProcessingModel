#
#
# File Created: April 7, 2023
# Description: This file is to process an image and identify what its corners and edges are.
#
#

from skimage.feature import corner_harris, corner_subpix, corner_peaks
from skimage import feature


class ProcessFilters:

    corners = []
    edges = []

    def __init__(self, image):
        self.process_corners(image)
        self.process_edges(image)

    def process_corners(self, target):
        self.corners = corner_peaks(corner_harris(target), min_distance=5, threshold_rel=0.02)

    def process_edges(self, target):
        self.edges = feature.canny(target, sigma=5)

    def corners_detected(self):
        return len(self.corners)

