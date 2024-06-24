import pygame
import math
from settings import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

pos_list = [] # all variables stored in a list for positions

for i in range(23):
    posit  = (i / 23) * (2 * math.pi) #distancing is not good between balls
    pos_list.append(posit)

print(pos_list)

def main():
    running = True
    ANGLE = START_SPEED
        
    for i in range(len(pos_list)):
        func_pos = pos_list[i]
        x = (math.cos(ANGLE + func_pos) * 200) + (SCREEN_HEIGHT/2)
        y = (math.sin(ANGLE + func_pos) * 200) + (SCREEN_WIDTH/2)
        color = 200 - ( ( math.cos(ANGLE + func_pos) + 1) * 100)

    while running:
        clock.tick(FPS)
        screen.fill(BACKGROUND_COLOUR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.draw.circle(screen, (color, color, color), (x, y), BALL_RADIUS)

        pygame.display.update()
        ANGLE += ROTATE_SPEED
  
    pygame.quit()

if __name__ == '__main__':
    main()