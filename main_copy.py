import pygame
from pygame import mixer
import random
import math
pygame.init()
dimensions = (1280, 720)
screen = pygame.display.set_mode(dimensions)
player_dimensions = (70, 70)
bgcolor = (255, 0, 255)

pygame.display.set_caption("Flappy Bird")

icon = pygame.transform.scale(pygame.image.load("icon.png"), (32, 32))
pygame.display.set_icon(icon)

bg = pygame.transform.scale(pygame.image.load("bg.png"), dimensions)

playerd = pygame.transform.scale(pygame.image.load("player_down.png"), player_dimensions)
playeru = pygame.transform.scale(pygame.image.load("player_up.png"), player_dimensions)
player = playerd
playerfly = pygame.transform.rotate(player, 45)
playerfall = pygame.transform.rotate(player, -45)
playerx = 200
playery = 200
playerc = 10

lp = pygame.image.load("Lower_part.png")
lp1 = pygame.image.load("Lower_part.png")
lpx = 0
lpc = -10
lp1x = lpx + 1280

obs = pygame.image.load("obs.png")
# obs_size = (600, 1000)
obs_size = (600, 1000)
obsu = pygame.transform.scale(obs, obs_size)
obsd = pygame.transform.rotate(obsu, 180)
obsx = [300, 650, 1000, 1350]
obsuy = [random.choice([-650, -750, -850, -950]) for i in range(len(obsx))]
# obsuy = -700
obsly = [(i + 1200) for i in obsuy]
obsc = lpc


run = True
falling = True
flap = 1
n = 0
mixer.music.load("song.mp3")
# mixer.music.play(-1)
font = pygame.font.Font("pixel.ttf", 50)
scorex, scorey = 10, 10
score = 0
while run:
    score_change = 0
    scored = False
    collision = False   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            # print("Keydown")
            if event.key == pygame.K_SPACE:
                playerc = -20
                falling = False
                # mixer.Sound("wing.mp3").play()
        if event.type == pygame.KEYUP:
            playerc = 10
            falling = True
            # print('Keyup')

    screen.fill(bgcolor)
    screen.blit(bg, (0, 0))

    # obstacle
    # ------testing------
    # Leaving and entering screen 
    # -342
    # 900 fully eneterd
    # if n % 150 == 0:
    #     obsx = 600
    # -----hta diyo yeh pagal ^-------


    for i in range(len(obsx)):
        screen.blit(obsu, (obsx[i], obsuy[i]))
        screen.blit(obsd, (obsx[i], obsly[i]))
        obsx[i] += obsc
        if obsx[i] < -350:
            obsuy[i] = random.choice([-650, -750, -850, -950])  
            obsly[i] = obsuy[i] + 1200
            obsx[i] = 1060
        if obsx[i] in range(18, -118, -1):
            if playery not in range(obsuy[i] + 1000, obsly[i]):
                collision = True
            if playery in range(obsuy[i] + 1000, obsly[i]) and not collision and playerx > obsx[i]+18:
                scored = True
    if scored:
        score += 1
    print(score)
    # lower part 
    if lpx <= -1280:
        lpx = 0
        lp1x = 1280
    screen.blit(lp, (lpx, 660))
    screen.blit(lp1, (lp1x, 660))
    lpx += lpc
    lp1x += lpc

    screen.blit(player, (playerx, playery))
    playery += playerc
    if playery > 610: 
        playery = 610
    if playery < -20:
        playery = -20
    
    # -342
    # 900 fully eneterd
    
    # print(obsx)
    n += 1
    # flapping
    if flap in range(1, 5):
        player = playeru
    else:
        player = playerd
    flap += 1
    if flap > 10:
        flap = 1
    if collision:
        # print("Collided")
        pass
    sc=font.render(str(math.ceil(score/13)),True,(0,0,0))
    screen.blit(sc, (scorex, scorey))
    pygame.display.update()