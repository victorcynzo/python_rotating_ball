"""#drawing two opposite circles rotating
x = int(math.cos(ANGLE) * 200) + (SCREEN_HEIGHT/2)
        y = int(math.sin(ANGLE) * 200) + (SCREEN_WIDTH/2)
        pygame.draw.circle(screen, BALL_COLOUR, (x, y), BALL_RADIUS)

        x_2 = int(math.cos(ANGLE + math.pi) * 200) + (SCREEN_HEIGHT/2)
        y_2 = int(math.sin(ANGLE + math.pi) * 200) + (SCREEN_WIDTH/2)
        pygame.draw.circle(screen, BALL_COLOUR, (x_2, y_2), BALL_RADIUS)

for x in range(12):
    x = x +1
    print(f"x = {x}")

import pygame, sys, math

run = True
white = (255, 255, 255)
black = (0, 0, 0)
angle = 0
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
screen.fill(white)

while run:
    msElapsed = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(white)
    x = int(math.cos(angle) * 100) + (width/2)
    y = int(math.sin(angle) * 100) + (height/2)
    pygame.draw.circle(screen, black, (x, y), 10)

    pygame.display.flip()
    angle += 0.05

pygame.quit()'''