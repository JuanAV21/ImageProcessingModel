#
#
# File Created: April 7, 2023
# Description: This file is to Connect the lines with the dots
#
#

from Resources.ProcessFilters import ProcessFilters
from Resources.Images import Images
import numpy as np
import math


def search_area(corner, dist):
    x = corner[0]
    y = corner[1]
    return np.array([[x-dist, y+dist], [x+dist, y-dist]])


def is_there_a_true(edges, searchArea):
    # This function returns the coordinates of the nearest line
    for y in range(searchArea[0][0], searchArea[1][0]):
        for x in range(searchArea[1][1], searchArea[0][1]):
            if edges[y][x]:
                return True
                #return np.array([y, x])
    return False


def distance(corners, target):
    length = len(corners)
    table = [0] * length
    minValue = 100
    minIndex = 0
    for i in range(length):
        d = math.sqrt(math.pow((corners[i][0]-target[0]), 2) + math.pow((corners[i][1]-target[1]), 2))
        table[i] = d
        if 0 < d < minValue:
            minValue = d
            minIndex = i
    return np.array([minValue, minIndex])


def linear_formula(cornerOne, cornerTwo):
    print("first point: ", cornerOne, "second point: ", cornerTwo, sep=" : ")
    m = (cornerTwo[1] - cornerOne[1])/(cornerTwo[0] - cornerOne[0])
    b = -(cornerOne[0] * m) + cornerOne[1]
    return np.array([m, b])

# Example that the math works out
# m = 510 - 525 / 415 - 397
# m = -15/18
# b = (397 * -.833) - 525

def y_output(var, pointA, pointB):
    linear_coord = []
    if pointB[0] > pointA[0]:
        temp = pointB
        pointB = pointA
        pointA = temp
    for x in range(pointB[0]+1, pointA[0]):
        y = var[0] * x + var[1]
        linear_coord.append(np.array([x, y]))
    return np.array(linear_coord)

def is_dots_connected(line, edges):
    for i in range(len(line)):
        




# _------___------------_------_--____--__-__--__-___-_-_-__--___----______-----_---___________-----------------------------
image = Images()
taskOne = ProcessFilters(image.getImage())

area = search_area(taskOne.corners[0], 4)
edges = taskOne.edges

print("search area: ", area)
print("Coordinate(corner): ", taskOne.corners[0])
print("This is where a line was detected: ", is_there_a_true(edges, area))

print("How many corners got detected: ", len(taskOne.corners))
nextCoord = distance(taskOne.corners, taskOne.corners[0])
print("What is the next nearest corner: ", distance(taskOne.corners, taskOne.corners[0]))

print(taskOne.corners[int(nextCoord[1])])
print(linear_formula(taskOne.corners[int(nextCoord[1])], taskOne.corners[0]))
print(y_output(linear_formula(taskOne.corners[int(nextCoord[1])], taskOne.corners[0]), taskOne.corners[int(nextCoord[1])], taskOne.corners[0]))
line = y_output(linear_formula(taskOne.corners[int(nextCoord[1])], taskOne.corners[0]), taskOne.corners[int(nextCoord[1])], taskOne.corners[0])

