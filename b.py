import pygame
pygame.init()
sc=pygame.display.set_mode((800,600))
albom=['1.mp3','2.mp3','3.mp3']

clock=pygame.time.Clock()
FPS=60
vol=1.0
flPause=False
r=int(0)
i=int(0)
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                flPause=not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                     pygame.mixer.music.unpause()
            elif event.key==pygame.K_UP:
                vol+=0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key==pygame.K_DOWN:
                vol-=0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key==pygame.K_RIGHT:
                i=int(1)
            elif event.key==pygame.K_LEFT:
                i=int(2)
        if i==1:
            r+=1
        elif i==2:
            r-=1
        pygame.mixer.music.load(albom[r])
        pygame.mixer.music.play(-1)



    clock.tick(FPS)