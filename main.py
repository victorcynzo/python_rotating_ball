import pygame #screen
import math #for pi, cos, sin
from settings import *

#pygame settup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main():
    running = True
    update_freq = FPS

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            screen.fill(BACKGROUND_COLOUR)
            pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()