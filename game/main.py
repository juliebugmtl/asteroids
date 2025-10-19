import pygame
import sys
from asteroidfield import *
from player import Player
from constants import *
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting Asteroids!")
	print("Screen width: 1280")
	print("Screen height: 720")
	clock = pygame.time.Clock()
	dt = 0

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	Shot.containers = (updatable, drawable, shots)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroidfield = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill("black")
		updatable.update(dt)
		for sprite in drawable:
			sprite.draw(screen)
		for asteroid in asteroids:
			if player.collides_with(asteroid):
				print("Game over!")
				sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if shot.collides_with(asteroid):
					asteroid.split()
					shot.kill()
					break

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()