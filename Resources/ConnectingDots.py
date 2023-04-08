#
#
# File Created: April 7, 2023
# Description: This file is to Connect the lines with the dots
#
#

from Resources.ProcessFilters import ProcessFilters
from Resources.Images import Images
import numpy as np

def search_area(corner, dist):
    x = corner[0]
    y = corner[1]
    return np.array([[x-dist, y+dist], [x+dist, y-dist]])

def is_there_a_true(edges, searchArea):
    for y in range(searchArea[1][1], searchArea[0][1]):
        for x in range(searchArea[0][0], searchArea[1][0]):
            if edges[y][x]:
                return np.array([y,x])
    return False




image = Images()
taskOne = ProcessFilters(image.getImage())

area = search_area(taskOne.corners[0], 2)
#print(type(taskOne.corners[0]))
print("search area: ", area)
print("Coordinate(corner): ", taskOne.corners[0])
#print(area[0][0])
print(is_there_a_true(taskOne.edges, area))
