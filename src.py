import pygame
import math

SCREEN_WIDTH = 512
SCREEN_HEIGHT = 512
CENTER_X = SCREEN_WIDTH // 2 
CENTER_Y = SCREEN_HEIGHT // 2

pygame.display.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("oscilloscope screen")
clock = pygame.time.Clock()

fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fade_surface.set_alpha(1)
fade_surface.fill((0,0,0))
# main loop

l1stat = l2stat = l3stat = l4stat = 0

(l1x1, l1y1) = (-100 + CENTER_X, 100 + CENTER_Y)
(l1x2, l1y2) = (100 + CENTER_X, 100 + CENTER_Y)
(l2x1, l2y1) = (100 + CENTER_X, 100 + CENTER_Y)
(l2x2, l2y2) = (100 + CENTER_X, -100 + CENTER_Y)
(l3x1, l3y1) = (100 + CENTER_X, -100 + CENTER_Y)
(l3x2, l3y2) = (-100 + CENTER_X, -100 + CENTER_Y)
(l4x1, l4y1) = (-100 + CENTER_X, -100 + CENTER_Y)
(l4x2, l4y2) = (-100 + CENTER_X, 100 + CENTER_Y)

step = 0.01
xstep = ystep = 0
x = y = 0                   # main point that will be displayed

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fade_surface, (0,0))

    if (l1stat==0):
        xstep = (l1x2-l1x1)*step
        ystep = (l1y2-l1y1)*step
        
        if((x>l1x2) & (y>l1y2)):
            l1stat += 1
    
    else if (l2stat==0):
        xstep = (l2x2-l2x1)*step
        ystep = (l2y2-l2y1)*step
        
        if((x >= l2x2) & (y >= l2y2)):
            l2stat += 1
    
    elif (l3stat==0):
        xstep = (l3x2-l3x1)*step
        ystep = (l3y2-l3y1)*step
        
        if((x >= l3x2) & (y >= l3y2)):
            l3stat += 1

    elif (l4stat==0):
        xstep = (l4x2-l4x1)*step
        ystep = (l4y2-l4y1)*step
        
        if((x >= l4x2) & (y >= l4y2)):
            l4stat += 1

    pygame.draw.circle(screen, (255,255,255), (x,y), 2)

    if ~(l1stat & l2stat & l3stat & l4stat):
        x += xstep
        y += ystep
    
    if (l1stat == l2stat == l3stat == l4stat & l1stat !=0 ):
        l1stat = l2stat = l3stat = l4stat = 0
    
    pygame.display.flip()       # updates screen
    clock.tick(60)              # 60 fps

pygame.quit()