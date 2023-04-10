#
#
# File Created: April 7, 2023
# Description: This file is to Connect the lines with the dots
#
#

from Resources.ProcessFilters import ProcessFilters
from Resources.Images import Images
import matplotlib.pyplot as plt
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


def get_distance_point(corners, target):
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
    #print("first point: ", cornerOne, "second point: ", cornerTwo, sep=" : ")
    if cornerTwo[0] - cornerOne[0] > 0:
        m = (cornerTwo[1] - cornerOne[1]) / (cornerTwo[0] - cornerOne[0])
    else:
        m = 0
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
        linear_coord.append(np.array([x, round(y)]))
    return np.array(linear_coord)


def is_dots_connected(line, edges):
    for i in range(len(line)):
        area = search_area(line[i], 5)
        temp = is_there_a_true(edges, area)
        if not temp:
            return False
    return True


def get_corners_connection(corners, edges):
    length = len(corners)
    table = [[0 for i in range(length)] for j in range(length)]
    row = 0
    for corner in corners:
        for index in range(length):
            #print(index, corner, sep="  :  ")
            #print(corner, corners[index], corner[0] == corners[index][0], corner[1] == corners[index][1], row, sep=" : ")
            if not (corner[0] == corners[index][0] and corner[1] == corners[index][1]):
                #print(row, index, sep=" : ")
                var = linear_formula(corner, corners[index])
                line = y_output(var, corner, corners[index])
                table[row][index] = is_dots_connected(line, edges)
            else:
                #print(row, index, sep=" : ")
                table[row][index] = False
        row += 1
    return table


# _------___------------_------_--____--__-__--__-___-_-_-__--___----______-----_---___________-----------------------------
image = Images()
taskOne = ProcessFilters(image.getImage(3))

area = search_area(taskOne.corners[0], 4)
edges = taskOne.edges

#print("search area: ", area)
#print("Coordinate(corner): ", taskOne.corners[0])
#print("This is where a line was detected: ", is_there_a_true(edges, area))

#print("How many corners got detected: ", len(taskOne.corners))
#nextCoord = get_distance_point(taskOne.corners, taskOne.corners[0])
#print("What is the next nearest corner: ", get_distance_point(taskOne.corners, taskOne.corners[0]))

#print(taskOne.corners[int(nextCoord[1])])
#print(linear_formula(taskOne.corners[int(nextCoord[1])], taskOne.corners[0]))
#print(y_output(linear_formula(taskOne.corners[int(nextCoord[1])], taskOne.corners[0]), taskOne.corners[int(nextCoord[1])], taskOne.corners[0]))
#line = y_output(linear_formula(taskOne.corners[int(nextCoord[1])], taskOne.corners[0]), taskOne.corners[int(nextCoord[1])], taskOne.corners[0])

#print(is_dots_connected(line, edges))

#print(get_corners_connection(taskOne.corners, taskOne.edges))
#print(type(image.getImage().shape))

#print(image.getImage(3).shape[0], image.getImage(3).shape[1], sep=" : ")

plt.plot(taskOne.corners[:, 1], -(taskOne.corners[:, 0]), color='cyan', marker='o', linestyle='None', markersize=6)
table = get_corners_connection(taskOne.corners, taskOne.edges)
length = len(taskOne.corners)
corners = []
print(taskOne.corners)
notConnectedIndex = []
for i in range(length):
    corners.append([taskOne.corners[i][1], -(taskOne.corners[i][0])])
print(corners)

cnt = 0
for x in range(length):
    for y in range(length):
        if table[x][y]:
            xValues = [corners[x][0], corners[y][0]]
            yValues = [corners[x][1], corners[y][1]]
            plt.plot(xValues, yValues, 'bo', linestyle="-")
        else:
            cnt += 1
    if cnt == length:
        notConnectedIndex.append(x)
    cnt = 0

#print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#print(notConnectedIndex)
#print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#print(table)
#print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
#print(corners)
#print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

for i in notConnectedIndex:
    print(corners[i])
plt.show()

