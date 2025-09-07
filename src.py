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
fade_surface.set_alpha(15)
fade_surface.fill((0,0,0))

# main loop

running = True

angle = 0
amplitude = 200
frequency = 10

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #x = int(CENTER_X + radius*math.cos(math.radians(angle)))
    #y = int(CENTER_Y + radius*math.sin(math.radians(angle)))
    #angle += 1

    screen.blit(fade_surface, (0,0))

    x = CENTER_X + amplitude * math.sin(math.radians(frequency * angle))
    y = CENTER_Y

    #screen.fill((0,0,0))        # background

    #screen.set_at((x,y), (255,255,255))
    pygame.draw.circle(screen, (255,255,255), (x,y), 2)
    angle += 0.1
    
    pygame.display.flip()       # updates screen
    clock.tick(60)              # 60 fps

pygame.quit()