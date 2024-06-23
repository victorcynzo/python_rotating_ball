import pygame
import math

#constants
BACKGROUND_COLOUR = 'white'
BALL_COLOUR = [0,0,0] #black, go to white = [125,125,125]
BALL_RADIUS = 10
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
FPS = 60
START_SPEED = 0
ROTATE_SPEED = 0.01

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

        for i in range(10): #create 12 circles
            x = int(math.cos(ANGLE) * 200) + (SCREEN_HEIGHT/2)
            y = int(math.sin(ANGLE) * 200) + (SCREEN_WIDTH/2)
            pygame.draw.circle(screen, (BALL_COLOUR), (x, y), BALL_RADIUS)
            x += 10
            y += 10
            
        pygame.display.update()
        ANGLE += ROTATE_SPEED
  
    pygame.quit()

if __name__ == '__main__':
    main()