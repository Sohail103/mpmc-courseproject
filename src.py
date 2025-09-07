import pygame
import math

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
CENTER_X = SCREEN_WIDTH // 2 
CENTER_Y = SCREEN_HEIGHT // 2

pygame.display.init()
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

    #x = int(CENTER_X + radius*math.cos(math.radians(angle)))
    #y = int(CENTER_Y + radius*math.sin(math.radians(angle)))
    #angle += 1

    x = int(256*math.sin(math.radians(clock.get_time()))) + CENTER_X
    y = CENTER_Y

    #screen.fill((0,0,0))        # background

    screen.set_at((x,y), (255,255,255))
    
    pygame.display.flip()       # updates screen
    clock.tick(60)             # 60 fps

pygame.quit()