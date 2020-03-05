import cv2
import numpy as np
import math
from Queue import PriorityQueue

obstacle = 1

def world(length, breadth):
    w = np.ones((length, breadth))
    return w


def square_obstacle(x, y, length, w):
    for j in range(x, x + length):
        for i in range(y, y + length):
            w[i][j] = 0


def circle_obstacle(x, y, a, b, radius, w):
    for j in range(x - a*radius, x + a*radius):
        for i in range(y - b*radius, y + b*radius):
            val = float(j - x)**2/a**2 + float(i - y) ** 2/b**2
            if float(j - x)**2/a**2 + float(i - y) ** 2/b**2 <= radius**2:
                w[i][j] = 0

'''
Input lines contains:

lines[3] - defines which part of the half plane should be included in the obstacle
			0: Include negative half plane
			1: Include positive half plane
'''
def obstacle(lines, xmin, xmax, ymin, ymax, w):
    for i in range(ymin, ymax + 1):
        for j in range(xmin, xmax + 1):
            # print(str(i) + ", " + str(j) + ":")
            for l in lines:
                # print(l[0] * j + l[1] * i + l[2])
                val = l[0] * j + l[1] * i + l[2]
                if l[3] == 1:
                    if l[0] * j + l[1] * i + l[2] >= 0:
                        w[i][j] = 0
                    else:
                        w[i][j] = 1
                        break

                elif l[3] == 0:
                    if l[0] * j + l[1] * i + l[2] <= 0:
                        w[i][j] = 0
                    else:
                        w[i][j] = 1
                        break

def getLineParam(x1, y1, x2, y2):
    if x2 - x1 ==0:
        return 1, 0, -x1
    else:
        a = float(y2 - y1)/float(x2 - x1)
    b = -1
    c = y1 - a * x1

    # print(a)

    return -a, -b, -c

def getMap(World):
    World = world(200, 300)

    points = [[200, 25, 225, 40, 0],
              [250, 25, 225, 40, 0],
              [250, 25, 225, 10, 1],
              [200, 25, 225, 10, 1]]

    # Get a, b, c values for every lines
    lines = []
    for i in range(4):
        l = []
        a, b, c = getLineParam(points[i][0], points[i][1], points[i][2], points[i][3])
        # print(a, b, c)
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(points[i][4])
        lines.append(l)

    lines = np.asarray(lines)
    print(lines.shape)

    # Get obstacles for world
    obstacle(lines, 200, 250, 10, 40, World)
    circle_obstacle(150, 100, 40, 20, 1, World)
    circle_obstacle(225, 150, 1, 1, 25, World)

    points = [[25, 185, 50, 185, 0],
              [50, 185, 50, 150, 0],
              [50, 150, 20, 120, 1],
              [20, 120, 25, 185, 0]]

    # Get a, b, c values for every lines
    lines1 = []
    for i in range(4):
        l = []
        a, b, c = getLineParam(points[i][0], points[i][1], points[i][2], points[i][3])
        # print(a, b, c)
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(points[i][4])
        print(l)
        lines1.append(l)

    obstacle(lines1, 20, 50, 120, 185, World)

    points = [[50, 185, 75, 185, 0],
              [75, 185, 100, 150, 0],
              [100, 150, 75, 120, 1],
              [75, 120, 50, 150, 1],
              [50, 150, 50, 185, 1]]

    # Get a, b, c values for every lines
    lines1 = []
    for i in range(4):
        l = []
        a, b, c = getLineParam(points[i][0], points[i][1], points[i][2], points[i][3])
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(points[i][4])
        lines1.append(l)

    obstacle(lines1, 50, 100, 120, 185, World)

    points = [[36, 77, 100, 39, 0],
              [100, 39, 95, 30, 1],
              [95, 30, 31, 68, 1],
              [31, 68, 36, 76, 0]]

    # Get a, b, c values for every lines
    lines1 = []
    for i in range(4):
        l = []
        a, b, c = getLineParam(points[i][0], points[i][1], points[i][2], points[i][3])
        l.append(a)
        l.append(b)
        l.append(c)
        l.append(points[i][4])
        lines1.append(l)

    obstacle(lines1, 31, 100, 30, 77, World)

    # cv2.imshow("World", World)
    # if cv2.waitKey(0) & 0xff == 27:
    #     cv2.destroyAllWindows()


# function to get start points
def startPoint():
    sx = int(input('Enter x coordinate for start point: '))
    sy = int(input('Enter y coordinate for start point: '))
    return sx, sy


# function to get goal points
def goalPoint():
    gx = int(input('Enter x coordinate for goal point: '))
    gy = int(input('Enter y coordinate for goal point: '))
    return gx, gy


# function to determine minimum cost
# def minCost(costs, node):
#     x, y = node
#
#     if
#     pass

# function to get cost of every move
def getCostOfMove(cur, i, j):
    x, y = cur

    return math.sqrt((x-i)**2 + (y-j)**2)



# function to explore neighbors and lot more
def explorer(costs, c_pq, paren):

    while not c_pq.empty():
        top = c_pq.get()
        x, y =top[0]
        for i in (x-1, x+2):
            for j in (y-1, y+2):
                if w[i, j] != 1 and top[0] != (i,j):
                    temp_cost = costs[top[0]] + getCostOfMove(top[0], i, j)
                    if temp_cost < costs[i, j]:
                        c_pq.put(((i,j), temp_cost))
                        paren[i, j] = top[0]
                        costs[i][j] = temp_cost

    # costs.put(((x-1, y), 1))
    # parent[x-1, y] = node
    # # move down
    # if world[x + 1, y] == 1:
    #     pass
    # else:
    #     costs.put(((x + 1, y), 1))
    #     parent[x + 1, y] = node
    #
    # # move left
    # if world[x, y-1] == 1:
    #     pass
    # else:
    #     costs.put(((x, y-1), 1))
    #     parent[x, y-1] = node
    #
    # # move right
    # if world[x, y+1] == 1:
    #     pass
    # else:
    #     costs.put(((x, y+1), 1))
    #     parent[x, y+1] = node
    #
    # # move top-left
    # if world[x-1, y-1] == 1:
    #     pass
    # else:
    #     costs.put(((x-1, y-1), math.sqrt(2)))
    #     parent[x-1, y-1] = node
    #
    # # move top-right
    # if world[x-1, y+1] == 1:
    #     pass
    # else:
    #     costs.put(((x-1, y+1), math.sqrt(2)))
    #     parent[x-1, y+1] = node
    #
    # # move bottom-left
    # if world[x + 1, y-1] == 1:
    #     pass
    # else:
    #     costs.put(((x + 1, y-1), math.sqrt(2)))
    #     parent[x + 1, y-1] = node
    #
    # # move bottom-right
    # if world[x - 1, y+1] == 1:
    #     pass
    # else:
    #     costs.put(((x - 1, y+1), 1))
    #     parent[x-1, y+1] = node
    # costs.
    # new_node = costs.get()
    # node =
    # return explorer(costs, paren, )

# function for the sake of algo
# def dijkstra(costs, c_pq, paren, node, goal):
#     costs.put(((node), 0))
#
#     if node == goal:
#         return #TODO: pata nhi
#     else:
#
#         # let's explore neighbors
#         explorer(costs, c_pq, paren, node, goal)


# main function
if __name__ == '__main__':

    w = world(200, 300)
    getMap(w)

    cv2.imshow("World", w)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()

    # world map
    # world = np.zeros(100)

    # Get points
    start_point = startPoint()
    goal_point = goalPoint()

    # Arrays for cost, parent
    cost_pq = PriorityQueue()
    parent = np.empty_like(w)
    cost = np.empty_like(w)

    for i in range(w.shape[0]):
        for j in range(w.shape[1]):
            parent[i, j] = None
            cost[i, j] = float('inf')

    cost[start_point] = 0
    cost_pq.put(((start_point), 0))

    explorer(cost, cost_pq, parent)

    print(cost)

