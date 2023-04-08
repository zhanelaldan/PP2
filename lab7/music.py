import pygame
import os
pygame.init()

screen = pygame.display.set_mode((800,500))
running = True
songs = []
play = True 
num = 0 

font = pygame.font.SysFont("Times New Roman", 30)
for file in os.listdir('.\musics'):
    if file.endswith(".mp3"):
        songs.append(file)

clock = pygame.time.Clock()
pygame.mixer.music.load('musics/'+songs[0])
pygame.mixer.music.play()

while running:
    current = num
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play = not play
            elif event.key == pygame.K_RIGHT:
                if num < len(songs)-1:
                    num+=1
                else:
                    num = 0
            elif event.key == pygame.K_LEFT:
                if num > 0:
                    num-=1
                else:
                    num = len(songs) - 1

    screen.fill((255,255,255))

    name = songs[num].replace('.mp3','')

    text = font.render(name, False, (19, 38, 84))
    text_rect = text.get_rect(center=(800/2, 500/2))

    screen.blit(text, text_rect)
        
    if play == False:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    if(current!=num):
        pygame.mixer.music.load('musics/'+songs[num])
        pygame.mixer.music.play()
        
    pygame.display.flip()
    clock.tick(60)
