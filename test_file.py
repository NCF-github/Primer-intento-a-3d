import numpy as np

points = np.array([
[10, 10, 10, 1],
[10, 10, -10, 1],
[10, -10, 10, 1],
[10, -10, -10, 1],
[-10, 10, 10, 1],
[-10, 10, -10, 1],
[-10, -10, 10, 1],
[-10, -10, -10, 1],
]).T

transformation1 = np.array([
[1, 0, 0, 0],
[0, 1, 0, -20],
[0, 0, 1, 0],
[0, 0, 0, 1]
])

transformation2 = np.array([
[500, 0, 0, 0],
[0, 500, 0, 0],
[0, -1, 1, 0],
[0, 0, 0, 1]
])

print(np.dot(transformation2, (np.dot(transformation1, points))))