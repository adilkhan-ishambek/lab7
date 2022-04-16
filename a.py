import pygame
import datetime
sc=pygame.display.set_mode((1116,720))
img=pygame.image.load('layer.png')
left=pygame.image.load('left_hand.png')
right=pygame.image.load('right_hand.png')
clock=pygame.time.Clock()
FPS=140
while 1:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        sc.blit(img,(0,0))
        t=datetime.datetime.now()
        angle_second=t.second*6
        angle_minute=t.minute*6
        rot_second=pygame.transform.rotate(left,-angle_second)
        rot_minute=pygame.transform.rotate(right,-angle_minute)
        sc.blit(rot_second,rot_second.get_rect(center=left.get_rect(center=(558,360)).center).topleft)
        sc.blit(rot_minute,rot_minute.get_rect(center=left.get_rect(center=(558,360)).center).topleft)
        pygame.display.update()
        clock.tick(FPS)