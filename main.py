import pygame
from screen import Screen
from camera import Camera
from objects import Object

# Y is the vertical axis

def main():
	screen = Screen()
	camera = Camera(0, 0, -20, screen)

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
	(0,4), (1,5), (2,6), (3,7),
	(0,2), (1,3), (4,6), (5,7),
	(0,1), (2,3), (4,5), (6,7),
	]

	A = Object(points, joins, camera)

	while True:
		camera.get_input()
		camera.move(screen.dt)
		camera.update_matrices()

		A.calculate_2d_version(camera)

		screen.update_screen(A)


if __name__ == "__main__":
	main()