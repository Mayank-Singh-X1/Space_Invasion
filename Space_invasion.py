import pygame
pygame.init()


#Screen
screen=pygame.display.set_mode((600,500))

#title
pygame.display.set_caption("Space Invader")

#icon
icon=pygame.image.load('spaceship.webp')
pygame.display.set_icon(icon)

#player
playerimg=pygame.image.load('spaceship.webp ')
playerimg=pygame.transform.scale(playerimg,(64,64))#resize image to 64*64 px
x_position=260
y_position=430

def player():  #display image of space ship 
    screen.blit(playerimg,(x_position,y_position))

running=True
while running:   #anything that u want to be shown consisitently on screen 
    screen.fill((88 ,88,88))

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            running=False

    
    player()
    pygame.display.update()

