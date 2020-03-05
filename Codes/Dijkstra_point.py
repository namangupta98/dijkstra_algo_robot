import cv2
import numpy as np
import math
from queue import PriorityQueue

obstacle = 1


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
def minCost(costs, node):
    x, y = node

    if
    pass


# function to explore neighbors and lot more
def explorer(costs, c_pq, paren, node, goal):
    x, y = node

    while not c_pq.empty():
        top = c_pq.get()
        for i in (x-1, x+2):
            for j in (y-1, y+2):
                if world[i, j] == 1:
                    break
                else:
                    if costs[top[0]] + costs[i, j] <                     

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
    costs.
    new_node = costs.get()
    node =
    return explorer(costs, paren, )

# function for the sake of algo
def dijkstra(costs, c_pq, paren, node, goal):
    costs.put(((node), 0))

    if node == goal:
        return #TODO: pata nhi
    else:

        # let's explore neighbors
        explorer(costs, c_pq, paren, node, goal)


# main function
if __name__ == '__main__':

    # world map
    world = np.zeros(100)

    # Get points
    start_point = startPoint()
    goal_point = goalPoint()

    # Arrays for cost, parent
    cost_pq = PriorityQueue()
    parent = np.empty_like(world)
    cost = np.empty_like(world)

    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            parent[i, j] = None
            cost[i, j] = float('inf')

    dijkstra(cost, cost_pq, parent, start_point, goal_point)

