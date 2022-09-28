import pygame
import sys
import time
import math
import numpy as np

class Camera():
	def __init__(self, x, y, z, screen, focal_length = 0.01, sensor_size_value = 10000, speed = 10):
		self.x = x
		self.y = y
		self.z = z
		self.speed = speed / 10

		self.focal_length = focal_length
		self.x_sensor_size = screen.width / sensor_size_value
		self.y_sensor_size = screen.height / sensor_size_value

		self.forward = False
		self.backward = False
		self.right = False
		self.left = False
		self.up = False
		self.down = False

		self.camera_offset_matrix = self.camera_offset_matrix()
		self.camera_model_matrix = self.camera_model_matrix(screen)

	def get_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					self.forward = True
				if event.key == pygame.K_DOWN:
					self.backward = True
				if event.key == pygame.K_RIGHT:
					self.right = True
				if event.key == pygame.K_LEFT:
					self.left = True
				if event.key == pygame.K_w:
					self.up = True
				if event.key == pygame.K_s:
					self.down = True
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					self.forward = False
				if event.key == pygame.K_DOWN:
					self.backward = False
				if event.key == pygame.K_RIGHT:
					self.right = False
				if event.key == pygame.K_LEFT:
					self.left = False
				if event.key == pygame.K_w:
					self.up = False
				if event.key == pygame.K_s:
					self.down = False

	def move(self, dt):
		if self.forward == True:
			self.z += self.speed * dt
		if self.backward == True:
			self.z -= self.speed * dt
		if self.right == True:
			self.x += self.speed * dt
		if self.left == True:
			self.x -= self.speed * dt

		if self.up == True:
			self.y += self.speed * dt
		if self.down == True:
			self.y -= self.speed * dt

	def camera_offset_matrix(self):
		return np.array([
			[1, 0, 0, -self.x],
			[0, 1, 0, -self.y],
			[0, 0, 1, -self.z],
			[0, 0, 0, 1]
			])

	def camera_model_matrix(self, screen):
		x_axis = (self.focal_length * screen.width)/(2 * self.x_sensor_size)
		y_axis = (self.focal_length * screen.height)/(2 * self.y_sensor_size)
		return np.array([
			[x_axis, 0, 0, 0],
			[0, y_axis, 0, 0],
			[0, 0, 0.1, 0],  # This might be a troublesome code line
			[0, 0, 0, 1]
			])

	def update_matrices(self):
		self.camera_offset_matrix = np.array([
			[1, 0, 0, -self.x],
			[0, 1, 0, -self.y],
			[0, 0, 1, -self.z],
			[0, 0, 0, 1]
			])