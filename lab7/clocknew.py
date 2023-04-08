import pygame
import math
import datetime 

pygame.init()

screen = pygame.display.set_mode((1400, 1050))
pygame.display.set_caption("Clock")

clock=pygame.time.Clock()
image = pygame.image.load('./img/mickeyclock12.png')
image_Sec=pygame.image.load('./img/test.png')
image_Min=pygame.image.load('./img/minut.png')
topleft = (0, 0)
angle = 90
done = False




def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

while not done:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        t = datetime.datetime.now()
        angle = -(int(t.strftime("%S")) * 6) - 6
        angleM = -(int(t.strftime("%M")) * 6 + (int(t.strftime("%S")) * 6 / 60)) - 54
        screen.blit(image, topleft) 
        blitRotateCenter(screen,image_Sec,topleft,angle)
        blitRotateCenter(screen,image_Min,topleft,angleM)
        pygame.display.flip()