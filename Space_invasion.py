import pygame
import random
pygame.init()

#Screen
screen=pygame.display.set_mode((600,500))
#title
pygame.display.set_caption("Space Invader")
#icon
icon=pygame.image.load('spaceship.webp')
pygame.display.set_icon(icon)
#background
background=pygame.image.load('background.jpg')
background=pygame.transform.scale(background,(600,500))
 
#Alien
alien_img=pygame.image.load('alien.png')
alien_img=pygame.transform.scale(alien_img,(40,40))
a_xposition=random.randint(0,560)
a_yposition=random.randint(0,260)
a_xchange=0.09
a_ychange=20


#Player
playerimg=pygame.image.load('spaceship.webp ')
playerimg=pygame.transform.scale(playerimg,(55,55))
x_position=260
y_position=430
xchange=0
ychange=0

def player(x,y):  #display image of space ship 
    screen.blit(playerimg,(x,y))
   
def alien(x,y):  #display image of alien
    screen.blit(alien_img,(x,y))

running=True
while running:   
    screen.blit(background,(0,0))

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                xchange=-0.1
            if event.key==pygame.K_RIGHT:
                xchange=+0.1                
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                ychange=-0.1
            if event.key==pygame.K_DOWN:
                ychange=+0.1

        if event.type==pygame.KEYUP:
            xchange=0
            ychange=0

    
    x_position+=xchange
    
    if x_position<=0 :
        x_position=0
    elif x_position>=545:
        x_position=545

    y_position+=ychange

    if y_position<=0 :
        y_position=0
    elif y_position>=445:
        y_position=445


    a_xposition+=a_xchange
    if a_xposition<=0 :
        a_xchange=0.09
        a_yposition+=a_ychange
    elif a_xposition>=560:
        a_xchange=-0.09
        a_yposition+=a_ychange

    player(x_position,y_position) 
    alien(a_xposition,a_yposition)
    pygame.display.update() 

