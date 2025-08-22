import pygame
import random
import math
from pygame import mixer

pygame.init()

# ----- Screen setup -----
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('spaceship.webp')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (600, 500))

# ----- Aliens -----
alien_img = []
a_xposition = []
a_yposition = []
a_xchange = []
a_ychange = []
num_of_alien = 8

for i in range(num_of_alien):
    alien_surface = pygame.image.load('alien.png')
    alien_surface = pygame.transform.scale(alien_surface, (40, 40))
    alien_img.append(alien_surface)
    a_xposition.append(random.randint(0, 560))
    a_yposition.append(random.randint(0, 260))
    a_xchange.append(0.15)
    a_ychange.append(20)

# ----- Player -----
playerimg = pygame.image.load('spaceship.webp')
playerimg = pygame.transform.scale(playerimg, (55, 55))
x_position = 260
y_position = 430
xchange = 0
ychange = 0

# ----- Bullet -----
bullet = pygame.image.load('bullet.png')
bullet = pygame.transform.scale(bullet, (25, 25))
bulletx = 0
bullety = y_position
bulletx_change = 0
bullety_change = -0.4
bulletState = 'ready'

# ----- Score -----
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 25)
x_text = 10
y_text = 10

# ----- Game Over -----
game_over_font = pygame.font.Font('freesansbold.ttf', 60)
goverx = 100
govery = 150

def game_over(x, y):
    game_over_msg = game_over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(game_over_msg, (x, y))

def show_score(x, y):
    score = score_font.render('Score : ' + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerimg, (x, y))

def alien(x, y, i):
    screen.blit(alien_img[i], (x, y))

def fire(x, y):
    global bulletState
    bulletState = 'fire'
    screen.blit(bullet, (x+20, y+20))

def iscollision(bulletx, bullety, a_xposition, a_yposition):
    distance = math.sqrt((math.pow(bulletx - a_xposition, 2) + math.pow(bullety - a_yposition, 2)))
    if distance < 25:
        return True
    else:
        return False

# ----- Main Game Loop -----
running = True
is_game_over = False  # Game Over flag

while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # No key events processed after game over
        if not is_game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xchange = -0.1
                if event.key == pygame.K_RIGHT:
                    xchange = 0.1
                if event.key == pygame.K_UP:
                    ychange = -0.1
                if event.key == pygame.K_DOWN:
                    ychange = 0.1
                if event.key == pygame.K_SPACE and bulletState == 'ready':
                    # explosion_sound = mixer.Sound('explosion-312361.mp3')
                    # explosion_sound.play()
                    bulletx = x_position - 4
                    bullety = y_position
                    bulletState = 'fire'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xchange = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    ychange = 0

    if not is_game_over:
        x_position += xchange
        y_position += ychange

        # Keep player in bounds
        if x_position < 0:
            x_position = 0
        elif x_position > 545:
            x_position = 545

        if y_position < 0:
            y_position = 0
        elif y_position > 445:
            y_position = 445

        # Aliens movement and collision
        for i in range(num_of_alien):
            a_xposition[i] += a_xchange[i]
            if a_xposition[i] <= 0:
                a_xchange[i] = 0.15
                a_yposition[i] += a_ychange[i]
            elif a_xposition[i] >= 560:
                a_xchange[i] = -0.15
                a_yposition[i] += a_ychange[i]

            # GAME OVER: If any alien reaches the bottom
            if a_yposition[i] > 400:
                is_game_over = True

            # Only check collision if game is not over
            if not is_game_over:
                collision = iscollision(bulletx, bullety, a_xposition[i], a_yposition[i])
                if collision and bulletState == 'fire':
                    explosion_sound = mixer.Sound('explosion-312361.mp3')
                    explosion_sound.play()
                    bullety = y_position
                    bulletState = 'ready'
                    score_value += 1
                    a_xposition[i] = random.randint(0, 560)
                    a_yposition[i] = random.randint(0, 260)

            alien(a_xposition[i], a_yposition[i], i)

        # Bullet movement
        if bulletState == 'fire':
            fire(bulletx, bullety)
            bullety += bullety_change
            if bullety <= 0:
                bullety = y_position
                bulletState = 'ready'

        player(x_position, y_position)
        show_score(x_text, y_text)
    else:
        game_over(goverx, govery)

    pygame.display.update()
