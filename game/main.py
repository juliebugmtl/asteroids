import os
os.environ["SDL_VIDEODRIVER"] = "dummy"
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
        print(".", end="", flush=True)
        pygame.time.delay(16)  # ~60 FPS

if __name__ == "__main__":
    main()