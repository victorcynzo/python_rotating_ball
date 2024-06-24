import pygame
import math
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def main():
    running = True
    ANGLE = START_SPEED
    while running:
        clock.tick(FPS)
        screen.fill(BACKGROUND_COLOUR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for i in range(23):
            pos = (i / 23) * (2 * math.pi)
            x = (math.cos(ANGLE + pos) * 200) + (SCREEN_HEIGHT/2)
            y = (math.sin(ANGLE + pos) * 200) + (SCREEN_WIDTH/2)
            color = 200 - ( (math.cos(ANGLE + pos ) + 1) * 100 )
            pygame.draw.circle(screen, (color, color, color), (x, y), BALL_RADIUS)
            print(i)

        pygame.display.update()
        ANGLE += ROTATE_SPEED
  
    pygame.quit()

if __name__ == '__main__':
    main()