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
            if (i-x)**2 + (j-y)**2 < radius:
                w[i][j] = 1


World = world(100, 200)
square_obstacle(40, 90, 20, World)
circle_obstacle(50, 160, 15, World)

cv2.imshow("World", World)
cv2.waitKey(0)
# plt.plot(World)
# plt.show()
