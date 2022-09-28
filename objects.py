import pygame
import numpy as np
from color import Color
from camera import Camera

class Object():
	def __init__(self, points, joins, camera, color = Color.black):
		self.points = np.array(points).T  # Has to be a list of lists. Each list containing x, y, and z coordinates in that order with a 1 at the end.
		self.joins = joins  # Has to be an array of arrays that contain to integers representing two points to be joined.
		self.calculate_2d_version(camera)
		self.color = color

	def calculate_2d_version(self, camera):
		points = self.points
		points = np.dot(camera.camera_offset_matrix, points)
		points = np.dot(camera.camera_model_matrix, points)
		points = points.T
		for point in points:
			if point[2] == 0:
				point[2] = 0.001
			point[0] /= point[2]
			point[1] /= point[2]
		self.points_in_2d = points

	def draw(self, screen):
		x_offset = screen.width / 2
		y_offset = screen.height / 2

		for point in self.points_in_2d:
			point[1] = -point[1]
			pygame.draw.circle(screen.screen, self.color, (point[0] + x_offset, point[1] + y_offset), 2)

		for join in joins:
			starting_pos = (self.points_in_2d[join[0]][0] + x_offset, self.points_in_2d[join[0]][1] + y_offset)
			ending_pos = (self.points_in_2d[join[1]][0] + x_offset, self.points_in_2d[join[1]][1] + y_offset)
			pygame.draw.line(screen.screen, self.color, starting_pos, ending_pos)





points = [
[10, 10, 10, 1],
[10, 10, -10, 1],
[10, -10, 10, 1],
[10, -10, -10, 1],
[-10, 10, 10, 1],
[-10, 10, -10, 1],
[-10, -10, 10, 1],
[-10, -10, -10, 1],
]

joins = [
(0,4), (1,5), (2,6), (3,7),  # Lines on the x axis
(0,2), (1,3), (4,6), (5,7),  # Lines on the y axis
(0,1), (2,3), (4,5), (6,7),  # Lines on the z axis
]