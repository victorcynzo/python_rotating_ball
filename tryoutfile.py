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
        
        # automate ball spawn so don't have to retype the next few lines for each line
        # need to create class for that
        # or make a ball.py file with a functino for the ball drawing and spawning

        x = int(math.cos(ANGLE) * 200) + (SCREEN_HEIGHT/2)
        y = int(math.sin(ANGLE) * 200) + (SCREEN_WIDTH/2)

        color = 200 - (((math.cos(ANGLE)) + 1) * 100)
        pygame.draw.circle(screen, (color, color, color), (x, y), BALL_RADIUS)

        x_2 = int(math.cos(ANGLE + math.pi) * 200) + (SCREEN_HEIGHT/2)
        y_2 = int(math.sin(ANGLE + math.pi) * 200) + (SCREEN_WIDTH/2)

        color_2 = 200 - (((math.cos(ANGLE + math.pi)) + 1) * 100)
        pygame.draw.circle(screen, (color_2, color_2, color_2), (x_2, y_2), BALL_RADIUS)

        color = 200 - (((math.cos(ANGLE)) + 1) * 100)
        pygame.draw.circle(screen, (color, color, color), (x, y), BALL_RADIUS)

        x_3 = int(math.cos(ANGLE + ((1/2) * math.pi)) * 200) + (SCREEN_HEIGHT/2)
        y_3 = int(math.sin(ANGLE + ((1/2) * math.pi)) * 200) + (SCREEN_HEIGHT/2)

        color_3 = 200 - (((math.cos(ANGLE + math.pi)) + 1) * 100)
        pygame.draw.circle(screen, (color_3, color_3, color_3), (x_3, y_3), BALL_RADIUS)

        x_4 = int(math.cos(ANGLE + ((3/2) * math.pi)) * 200) + (SCREEN_HEIGHT/2)
        y_4 = int(math.sin(ANGLE + ((3/2) * math.pi)) * 200) + (SCREEN_HEIGHT/2)

        color_4 = 200 - (((math.cos(ANGLE + math.pi)) + 1) * 100)
        pygame.draw.circle(screen, (color_4, color_4, color_4), (x_4, y_4), BALL_RADIUS)

        pygame.display.update()
        ANGLE += ROTATE_SPEED
  
    pygame.quit()

if __name__ == '__main__':
    main()