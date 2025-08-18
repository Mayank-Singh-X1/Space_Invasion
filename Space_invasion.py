import pygame
pygame.init()

#Screen
screen=pygame.display.set_mode((800,600))

#title
pygame.display.set_caption("Space Invader")

#icon
icon=pygame.image.load('spaceship.webp')
pygame.display.set_icon(icon)

running=True
while running:
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT:
            running=False
