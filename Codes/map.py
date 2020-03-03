import numpy as np
import matplotlib.pyplot as plt
import cv2


def world(length, breadth):
    w = np.zeros((length, breadth))
    return w


def square_obstacle(x, y, length, w):
    for i in range(x, x + length):
        for j in range(y, y + length):
            w[i][j] = 1


def circle_obstacle(x, y, radius, w):
    for i in range(x - radius, x + radius):
        for j in range(y - radius, y + radius):
            if (i - x) ** 2 + (j - y) ** 2 < radius:
                w[i][j] = 1


def obstacle(lines, xmin, xmax, ymin, ymax, w):
    temp_world = np.ones(((ymax - ymin + 1), (xmax - xmin + 1)))
    # print(temp_world)
    for i in range(ymin, ymax + 1):
        for j in range(xmin, xmax + 1):
            for l in lines:
                if l[3] == 0:
                    if l[0] * j + l[1] * i + l[2] > 0:
                        w[i][j] = 1 and temp_world[i - ymin][j - xmin]
                    else:
                        temp_world[i - ymin][j - xmin] = 0
                        w[i][j] = 0

                elif l[3]:
                    if l[0] * j + l[1] * i + l[2] < 0:
                        w[i][j] = 1 and temp_world[i - ymin][j - xmin]
                    else:
                        temp_world[i - ymin][j - xmin] = 0
                        w[i][j] = 1

    # print(temp_world)


# return w

def getLineParam(x1, y1, x2, y2):
    a = float((y2 - y1)/(x2 - x1))
    b = -1
    c = y1 - a * x1

    return -a, -b, -c


# def minimax(x, y):


World = world(200, 300)
square_obstacle(40, 90, 20, World)
circle_obstacle(50, 160, 15, World)

# 1 - include the portion in negative
# 0 - include the portion in positive
points = [[200, 25, 225, 40, 1],
          [250, 25, 225, 40, 1],
          [250, 25, 225, 10, 0],
          [200, 25, 225, 10, 0]]

# Get a, b, c values for every lines
lines = []
for i in range(4):
    l = []
    a, b, c = getLineParam(points[i][0], points[i][1], points[i][2], points[i][3])
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(points[i][4])
    lines.append(l)

lines = np.asarray(lines)
print(lines.shape)

# Get obstacles for world
obstacle(lines, 200, 250, 10, 40, World)


cv2.imshow("World", World)
cv2.waitKey(0)
