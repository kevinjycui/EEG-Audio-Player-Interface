import client
import pygame
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

client.setup()

pygame.mixer.music.load('sample_audio/crab_rave.mp3')
pygame.mixer.music.play(-1)

pygame.display.set_caption("Mind Music")
screen = pygame.display.set_mode((360, 480))

font = pygame.font.SysFont("Ariel Black", 24)
title_font = pygame.font.SysFont("Ariel Black", 48)


img1 = pygame.transform.scale(pygame.image.load("cover_imgs/crab_rave.jpg"), (180, 180)).convert_alpha()
img2 = pygame.transform.scale(pygame.image.load("cover_imgs/megalovania.jpg"), (180, 180)).convert_alpha()

cover = img1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (190, 80, 190)
GREY = (120, 120, 120)

back1 = BLACK
back2 = WHITE

selection = 1
change = False

vol = 0

def display():
    screen.fill(WHITE)
    pygame.draw.rect(screen, VIOLET, (0, 0, 360, 80))
    pygame.draw.rect(screen, VIOLET, (0, 420, 360, 60))
    screen.blit(title_font.render("Mind Music", 5, WHITE), (95, 30))
    screen.blit(font.render("Crab Rave", 5, back2, back1), (70, 120))
    screen.blit(font.render("Megalovania", 5, back1, back2), (190, 120))
    screen.blit(cover, (90, 170))
    screen.blit(font.render("Keep volume low, as sudden", 5, BLACK), (70, 370))
    screen.blit(font.render("increases in volume may occur", 5, BLACK), (60, 385))
    for v in range(1, 100, 20):
        if v<=vol:
            pygame.draw.rect(screen, WHITE, (120+v, 450-v//5, 10, (80+v)//5))
        else:
            pygame.draw.rect(screen, GREY, (120+v, 450-v//5, 10, (80+v)//5))            
    screen.blit(font.render(str(vol), 5, WHITE), (230, 445))
    

exit_flag = False

while not exit_flag:
   res = client.get_value(pygame.mixer.music.get_volume())
   pygame.mixer.music.set_volume(res[0])

   vol = round(pygame.mixer.music.get_volume()*100)
   
   if res[1] == 'surprised':
       selection *= -1
       change = True
       
   print('Volume:', vol)


   if selection == -1 and change:
       pygame.mixer.music.load('sample_audio/crab_rave.mp3')
       pygame.mixer.music.play(-1)
       change = False
       back1 = BLACK
       back2 = WHITE
       cover = img1
   if selection == 1 and change:
       pygame.mixer.music.load('sample_audio/megalovania.mp3')
       pygame.mixer.music.play(-1)
       change = False
       back1 = WHITE
       back2 = BLACK
       cover = img2
       
   for e in pygame.event.get():
       if e.type == pygame.QUIT:
           exit_flag = True
       if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
           exit_flag = True
           
   display()       
   pygame.display.flip()
   pygame.time.delay(4)

pygame.quit()
