# importing pygame
import pygame
import random

# importing math
import math

# importing mixer


r = "ready"
b = 2
space = 0
x = 50
y = 515
start = 10
width = 40
height = 5
# Asteroid
Asteroid1 = []
Asteroid_x = []
Asteroid_y = []
Asteroid_x_change = []
Asteroid_y_change = []
for i in range(30):

    Asteroid_x.append(random.randint(0, 800))
    Asteroid_y.append(random.randint(50, 150))
    Asteroid_x_change.append(3.8)
    Asteroid_y_change.append(6)
pygame.init()
# Changing the icon of the screen

pygame.display.set_icon(icon)
# Creating the screen
screen = pygame.display.set_mode((800, 600))
# background pic
background = pygame.image.load("space.jpg")
pygame.display.set_caption("Space shooter")
# Colour
BLUE = (100, 100, 255)
RED = (255, 0, 0)
LIME = (180, 255, 100)
"""Asteroid"""
# Player
player = pygame.image.load("player.png")
player_x = 370
player_y = 480
# Bullet
Bullet = pygame.image.load("Bullet.png")
Bullet_x = 370
Bullet_y = 480
Bullet_x_change = 9
Bullet_y_change = 60
Bullet_state = r
# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 25)
text_x = 200
text_y = 10


# Creating score function
def score(X, Y):
    scores = font.render("Score : {}".format(score_value), True, BLUE)
    screen.blit(scores, (X, Y))


# Creating fire function
def fire(x, y):
    global Bullet_state
    Bullet_state = fire
    screen.blit(Bullet, (x + 18, y + 10))


# Creating fire function
def play(X, Y):
    screen.blit(player, (X, Y))


# Creating  Asteroid function
def asteroid_function(X, Y, i):
    screen.blit(Asteroid1[i], (X, Y))


# Creating background function
def background_function():
    screen.blit(background, (0, 0))


# While loop
run = True
while run:
    # calling the background function
    background_function()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    # player movement
    if keys[pygame.K_LEFT]:
        player_x -= 3
    if keys[pygame.K_RIGHT]:
        player_x += 3
        # Bullet shooting
        laser_sound = mixer.Sound("C:\\laser.wav")
        laser_sound.play()
        Bullet_x = player_x
        fire(Bullet_x, Bullet_y)
        fire(Bullet_x, Bullet_y)
        Bullet_y -= Bullet_y_change
    if Bullet_y <= 0:
        Bullet_y = 480
        Bullet_state = r
        # collision
    if score_value == 300:
        print("you win")
        run = False

    def collision(Bullet_x, Bullet_y, Asteroid_x, Asteroid_y):
        distance = math.sqrt(
            math.pow(Asteroid_x - Bullet_x, 2) + math.pow(Asteroid_y - Bullet_y, 2)
        )
        if distance < 27:
            return True
        else:
            return False
        # collision

    # boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    # boundaries enemy
    for i in range(30):
        Asteroid_x[i] += Asteroid_x_change[i]
        if Asteroid_x[i] <= 0:
            Asteroid_x_change[i] = 3.8
            Asteroid_y[i] += Asteroid_y_change[i]
        elif Asteroid_x[i] >= 736:
            Asteroid_x_change[i] = -3.8
            Asteroid_y[i] += Asteroid_y_change[i]
        collisions = collision(Asteroid_x[i], Asteroid_y[i], Bullet_x, Bullet_y)
        if collisions:
            Bullet_y = 480
            Bullet_state = "ready"
            score_value = score_value + 1
            laser_sound = mixer.Sound("C:\\explosion.wav")
            laser_sound.play()
            Asteroid_x.append(random.randint(0, 800))
            Asteroid_y.append(random.randint(50, 150))
        # calling the asteroid function
        asteroid_function(Asteroid_x[i], Asteroid_y[i], i)
    if event.type == pygame.KEYDOWN:
        # quitting the game
        if event.key == ord("q"):
            pygame.quit()
        # changing the spaceship
        if event.key == ord("s"):
            b = b + 1
            if b == 1:
                player = pygame.image.load("player.png")
            if b == 2:
                player = pygame.image.load("l.png")
            if b == 3:
                player = pygame.image.load("player2.png")
            if b == 4:
                b = 1
    # calling the player function
    play(player_x, player_y)
    # calling the score function
    score(text_x, text_y)
    # Refresh Screen
    pygame.display.flip()
