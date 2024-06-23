import pygame #screen
import math #for pi, cos, sin
from settings import *

#pygame settup
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
        
        x = int(math.cos(ANGLE) * 200) + (SCREEN_HEIGHT/2)
        y = int(math.sin(ANGLE) * 200) + (SCREEN_WIDTH/2)
        pygame.draw.circle(screen, BALL_COLOUR, (x, y), BALL_RADIUS)

        x_2 = int(math.cos(ANGLE+math.pi)* 200) + (SCREEN_HEIGHT/2)
        y_2 = int(math.sin(ANGLE+math.pi)* 200) + (SCREEN_WIDTH/2)
        pygame.draw.circle(screen, BALL_COLOUR, (x_2, y_2), BALL_RADIUS)

        pygame.display.update()
        ANGLE += ROTATE_SPEED
        
    pygame.quit()

if __name__ == '__main__':
    main()