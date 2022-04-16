import pygame
pygame.init()
sc=pygame.display.set_mode((800,600))
x=50
y=50
speed=20
FPS=60
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x>25:
           x-=speed
             

    elif keys[pygame.K_RIGHT]:
        
        if x<775:
            x+=speed
    elif keys[pygame.K_UP]:
        
        if y>25:
            y-=speed
    elif keys[pygame.K_DOWN]:
        
        if y<575:
            y+=speed
    sc.fill((255,255,255))
    pygame.draw.circle(sc,(255,0,0),(x,y),25)
    pygame.display.update()
    clock.tick(FPS)