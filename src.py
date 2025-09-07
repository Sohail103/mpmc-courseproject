import pygame
import math

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
CENTER_X = SCREEN_WIDTH // 2
CENTER_Y = SCREEN_HEIGHT // 2

pygame.display.init() 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Oscilloscope Square")
clock = pygame.time.Clock()

fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade_surface.set_alpha(10)
fade_surface.fill((0, 0, 0))

corners = [
    (-10 + CENTER_X, -10 + CENTER_Y), # 0 = top left
    ( 10 + CENTER_X, -10 + CENTER_Y), # 1 = top right
    ( 10 + CENTER_X,  10 + CENTER_Y), # 2 = bottom right
    (-10 + CENTER_X,  10 + CENTER_Y)  # 3 = bottom left
]

current_side = 0 # 0: top, 1: right, 2: bottom, 3: left
x, y = corners[0] # point starts at top left
speed = 2 # pixels to move per frame

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fade_surface, (0, 0))
    
    # top side drawing
    if current_side == 0:
        x += speed
        if x >= corners[1][0]:
            x, y = corners[1] # snap to corner
            current_side = 1  # next side

    # right side
    elif current_side == 1:
        y += speed
        if y >= corners[2][1]:
            x, y = corners[2]
            current_side = 2

    # bottom side
    elif current_side == 2:
        x -= speed
        if x <= corners[3][0]:
            x, y = corners[3]
            current_side = 3

    # left side
    elif current_side == 3:
        y -= speed
        if y <= corners[0][1]:
            x, y = corners[0]
            current_side = 0 # loop back

    # draw moving point
    pygame.draw.circle(screen, (100, 255, 100), (x, y), 2)

    pygame.display.flip()
    clock.tick(120)

pygame.quit()