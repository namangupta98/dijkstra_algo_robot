# Dijkstra's Algorithm for Point and Rigid Robot
Coursework project for ENPM661: Planning for Autonomous Robots.
## Overview
The aim is to navigate a point robot and a rigid robot from start point to goal point using Dijkstra's algorithm in a known environment.

## Dependencies

- Opencv
- Python3.5 (use queue)
- Python2.7 (use Queue)
- Numpy

## Instructions

To run the code for point robot, open the terminal in Codes folder and type
```
python3 Dijkstra_point.py
``` 

To run the code for rigid robot, open the terminal in Codes folder and type
```
python3 Dijkstra_rigid.py
```

## Time for execution

Keeping start point as (5, 5) and goal point as (195, 295)

- Algorithm time for point robot: 1.2 seconds and visualization time for point robot: 85 seconds

  <p align="center">
    <img src="https://github.com/namangupta98/dijkstra_algo_robot/blob/master/Output/Dijkstra-Point-fast.gif"><br \>
    <b>Figure 1 - Point Robot</b>
  </p>

- Algorithm time for rigid robot: 1.2 seconds and visualization time for rigid robot: 74 seconds

  <p align="center">
    <img src="https://github.com/namangupta98/dijkstra_algo_robot/blob/master/Output/Dijkstra-Rigid-fast.gif"><br \>
    <b>Figure 2 - Rigid Robot with Radius=2 and Clearance=1</b>
  </p>
