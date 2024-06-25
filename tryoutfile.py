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
        
        index = 0
        for i in range(25):
            pos = (i / 25) * (2 * math.pi)
            x = (math.cos(ANGLE + pos) * 200) + (SCREEN_HEIGHT/2)
            y = (math.sin(ANGLE + pos) * 200) + (SCREEN_WIDTH/2)
            color = 200 - ( (math.cos(ANGLE + pos ) + 1) * 100 )
            pygame.draw.circle(screen, (color, color, color), (x, y), BALL_RADIUS)
            index += 1

        index_2 = 0
        for i in range(21):
            pos = (i / 21) * (2 * math.pi)
            x = (math.cos(ANGLE + pos) * 170) + (SCREEN_HEIGHT/2)
            y = (math.sin(ANGLE + pos) * 170) + (SCREEN_WIDTH/2)
            color = 200 - ( (math.cos(ANGLE + pos ) + 1) * 100 )
            pygame.draw.circle(screen, (color, color, color), (x, y), 12)
            index_2 += 1

        index_3 = 0
        for i in range(16):
            pos = (i / 16) * (2 * math.pi)
            x = (math.cos(ANGLE + pos) * 135) + (SCREEN_HEIGHT/2)
            y = (math.sin(ANGLE + pos) * 135) + (SCREEN_WIDTH/2)
            color = 200 - ( (math.cos(ANGLE + pos ) + 1) * 100 )
            pygame.draw.circle(screen, (color, color, color), (x, y), 14)
            index_3 += 1
        
        index_4 = 0
        for i in range(12):
            pos = (i / 12) * (2 * math.pi)
            x = (math.cos(ANGLE + pos) * 95) + (SCREEN_HEIGHT/2)
            y = (math.sin(ANGLE + pos) * 95) + (SCREEN_WIDTH/2)
            color = 200 - ( (math.cos(ANGLE + pos ) + 1) * 100 )
            pygame.draw.circle(screen, (color, color, color), (x, y), 16)
            index_4 += 1

        index_5 = 0
        for i in range(6):
            pos = (i / 6) * (2 * math.pi)
            x = (math.cos(ANGLE + pos) * 50) + (SCREEN_HEIGHT/2)
            y = (math.sin(ANGLE + pos) * 50) + (SCREEN_WIDTH/2)
            color = 200 - ( (math.cos(ANGLE + pos ) + 1) * 100 )
            pygame.draw.circle(screen, (color, color, color), (x, y), 18)
            index_5 += 1

        pygame.draw.circle(screen, (color, color, color), (SCREEN_HEIGHT/2, SCREEN_WIDTH/2), 20)

        pygame.display.update()
        ANGLE += ROTATE_SPEED
  
    pygame.quit()

if __name__ == '__main__':
    main()