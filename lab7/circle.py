import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
running = True

Bl3 = (0,0,255)
Green = (0,255,0)
Red = (255,0,0)
White = (255,255,255) 

x,y = 25,25
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pressed = pygame.key.get_pressed()    
    if pressed[pygame.K_RIGHT]:
        if x<475:
            x+=25
    elif pressed[pygame.K_LEFT]:
        if x>25:
            x-=25
    elif pressed[pygame.K_DOWN]:
        if y<475:
            y+=25
    elif pressed[pygame.K_UP]:
        if y>25:
            y-=25
            
    screen.fill(Red)         
    pygame.draw.circle(screen, Green, [x, y], 25, 0)

    pygame.display.flip()
    clock.tick(60)