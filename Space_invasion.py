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
playerimg=pygame.transform.scale(playerimg,(55,55))#resize image to 55*55 px
x_position=260
y_position=430

def player(x,y):  #display image of space ship 
    screen.blit(playerimg,(x,y))

running=True
while running:   #anything that u want to be shown consisitently on screen 
    screen.fill((60 ,60,60))

    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_position=-10
            elif event.key==pygame.K_RIGHT:
                x_position=+10
    
    player(x_position,y_position)
    pygame.display.update()

