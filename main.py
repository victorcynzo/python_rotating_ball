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
        screen.fill(BACKGROUND_COLOUR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        x = int(math.cos(angle) * 100) + 100
        y = int(math.sin(angle) * 100) + 100

        angle += 0.05
        
        pygame.draw.circle(screen, BALL_COLOUR, (x, y), BALL_RADIUS)
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()