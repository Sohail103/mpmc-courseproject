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

fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade_surface.set_alpha(1)
fade_surface.fill((0,0,0))

# main loop

running = True

angle1 = 0
angle2 = 0
amplitude = 200
frequency = 10

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fade_surface, (0,0))

    x1 = CENTER_X + amplitude * math.sin(math.radians(frequency * angle1))
    y1 = CENTER_Y

    #screen.fill((0,0,0))        # background

    #screen.set_at((x,y), (255,255,255))
    pygame.draw.circle(screen, (255,255,255), (x1,y1), 2)
    angle1 += 0.1

    x2 = int(CENTER_X + amplitude*math.cos(math.radians(angle2)))
    y2 = int(CENTER_Y + amplitude*math.sin(math.radians(angle2)))
    angle2 += 1
    pygame.draw.circle(screen, (255,255,255), (x2,y2), 2)
    
    pygame.display.flip()       # updates screen
    clock.tick(1000)              # 60 fps

pygame.quit()