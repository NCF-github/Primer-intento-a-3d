import pygame
import time
from color import Color
from camera import Camera

class Screen():
	def __init__(self, width = 800, height = 600, background_color = Color.white, tick = 60):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.background_color = background_color
		self.clock = pygame.time.Clock()
		self.tick = tick
		self.dt = 0
		self.a = time.time()

	def update_screen(self, object):
		self.dt = (time.time() - self.a) * 100
		self.a = time.time()
		self.screen.fill(self.background_color)

		object.draw(self)

		self.clock.tick(self.tick)
		pygame.display.update()