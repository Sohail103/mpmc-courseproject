import pygame
import math

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 256
CENTER_X = SCREEN_WIDTH // 2 
CENTER_Y = SCREEN_HEIGHT // 2

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Oscilloscope screen")
clock = pygame.time.Clock()

# main loop

running = True

angle=0
radius=100

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x = int(CENTER_X + radius*math.cos(math.radians(angle)))
    y = int(CENTER_Y + radius*math.sin(math.radians(angle)))

    screen.fill((0,0,0))        # background

    screen.set_at((x,y), (255,255,255))
    
    pygame.display.flip()       # updates screen
    clock.tick(60)             # 60 fps

pygame.quit()