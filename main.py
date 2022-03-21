from ast import Pass
import pygame
from pygame import mixer
import random
import math
import keyboard
from scipy import rand
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
playerdd = pygame.transform.rotate(playerd, -90)
playeruu = pygame.transform.rotate(playeru, -90)
playerx = 200
playery = 200
playerc = 10

lp = pygame.image.load("Lower_part.png")
lp1 = pygame.image.load("Lower_part.png")
lpx = 0
lpc = -7
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
# exit screen
game_over = pygame.image.load("end.png")
game_over = pygame.transform.scale(game_over, (400, 100))

gox, goy = 450, 165

score_card = pygame.image.load("score_card_2.png")
score_card = pygame.transform.scale(score_card, (400, 300))
scx, scy = 440, 170
run = True
falling = True
flap = 1
n = 0
mixer.music.load("song.mp3")
# a--------------------------------------a
# mixer.music.play(-1)
font = pygame.font.Font("Minecraft.ttf", 200)
font1 = pygame.font.Font("Minecraft.ttf", 210)
scorex, scorey = 600, 30 
score = 0
killed = False
score_added = False
collision = False   
restart_status = False
restarter = 0
# space_pressed = False
font2 = pygame.font.Font("Minecraft.ttf", 25)
font3 = pygame.font.Font("Minecraft.ttf", 32)
hitt = False
quit_game=False
re_varibale = 0
highest_score = 0 
game_started = False
intro_done = False
intro_image = pygame.image.load("intro_screen.png")
#1200, 720
# intro_image = pygame.transform.scale(intro_image, (1000, 600))
random_variable = 0
insta_logo = pygame.image.load("insta_logo.png")
insta_logo = pygame.transform.scale(insta_logo, (15, 15))
intro_font = pygame.font.Font("intro_font.ttf", 10)
while run:
    if game_started:
        intro_done = True
        if score > highest_score:
            highest_score = score
        score_change = 0
        scored = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # print("Keydown")
                if event.key == pygame.K_SPACE:
                    if not killed:
                        playerc = -20
                        falling = False
                        mixer.Sound("wing.mp3").play()
                        if killed:
                            pass
            if event.type == pygame.KEYUP:
                if not killed:
                    playerc = 10
                    falling = True

                # print('Keyup')

        screen.fill(bgcolor)
        screen.blit(bg, (0, 0))
        sc=font.render(str(score),True,(255,255,255))
        sc1=font1.render(str(score),True,(0, 0, 0))


        # sc 
        if not killed:
            # screen.blit(sc1, (scorex-2.5, scorey-3))
            screen.blit(sc1, (scorex, scorey))
            screen.blit(sc, (scorex, scorey))
            # screen.blit(pass)
        # obstacle
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
                collision, score_added = False, False
                obsuy[i] = random.choice([-650, -750, -850, -950])  
                obsly[i] = obsuy[i] + 1200
                obsx[i] = 1060
            if not collision :
                if obsx[i] in range(5, -118, -1):
                    if playery not in range(obsuy[i] + 973, obsly[i]-50):
                        collision = True
                        # print(f"obsx: {obsx[i]} | obsuy: {obsuy[i]} | obsly: {obsly[i]}")
                elif obsx[i] < -118 and not score_added:
                    score += 1
                    if score % 5 == 0 and score > 0:
                        obsc -= 1
                        lpc -= 1
                    if 11 > score > 9 :
                        scorex -= 50
                    score_added = True
        
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
            collision = True
        if playery < -20:
            playery = -20
        
        # -342
        # 900 fully eneterd
        
        # print(obsx)
        n += 1
        # flapping
        if flap in range(1, 5):
            if not killed:
                player = playeru
            else:
                player = playeruu
        else:
            if not killed:
                player = playerd
            else: 
                player = playerdd
        flap += 1
        if flap > 10:
            flap = 1
        # endscreen
        if collision:
            # game_over = pygame.image.load("end.png")
            if not hitt:
                mixer.Sound("sfx_hit.wav").play()
                mixer.Sound("sfx_die.wav").play()
            obsc, lpc, playerc = 0, 0, 35
            killed = True
            if playery < -20:
                pass
            
            screen.blit(game_over, (gox, goy))
            # replay=font2.render("Press 'Q' to Quit & 'R' to Restart",True,(0, 0, 0))
            # to_quit = font2.render("Click Here To Quit ^", True, (0, 0, 0))

            if flap in range(1, 6):
                replay=font2.render("Press 'Q' to Quit & 'R' to Restart",True,(0, 0, 0))
                screen.blit(replay, (450, 490))
                replay=font2.render("Press 'Q' to Quit & 'R' to Restart",True,(255, 255, 255))
                screen.blit(replay, (449, 489))
                # screen.blit(to_quit, (1020, 10))


            score_display = font3.render(str(score), True, (255,117,78))
            highest_score_display = font3.render(str(highest_score), True, (255,117,78))
            screen.blit(score_card, (scx, scy))
            screen.blit(score_display, (735, 330))
            screen.blit(highest_score_display, (737, 395))
            
            hitt = True  
            try:
                if keyboard.is_pressed('r'):
                    print('Restarted!')
                    # quit_game=True
                    restart_status=True

            except:
                # quit_game = False   
                restart_status=False 
            # if killed and not restart_status:
            #     restarter+=1 
            # if restarter==100:
            #     restart_status=True
            if restart_status:
                restarter += 1
                # loading = font3.render(str("Loading..." + "."*int(restarter/5)), True, (255,117,78))
                loading = font2.render(str("Loading...")[0 : int(restarter/5) + 1], True, (0, 0, 0))
                # loading = font2.render(str("#"*int(restarter/5 + 1)), True, (0, 0, 0))
                # screen.blit(loading, (550, 540))
                screen.blit(loading, (570, 540))
                if restarter == 50:
                    killed = False
                    collision = False
                    hitt = False
                    restarter=0
                    restart_status=False
                    playery = 200
                    obsx = [300, 650, 1000, 1350]
                    score = 0
                    playerc = 10
                    lpc = -10
                    obsc = lpc
                
            try:
                if keyboard.is_pressed('q'):
                    print('Game Over!')
                    quit_game=True
            except:
                quit_game = False
            if quit_game:
                break

    else:
        screen.blit(bg, (0, 0))
        for i in range(len(obsx)):
            screen.blit(obsu, (obsx[i]-300, obsuy[i] ))
            screen.blit(obsd, (obsx[i]-300, obsly[i] ))
        screen.blit(lp, (0, 660))
        screen.blit(intro_image, (340, 150))
        intro_text=font2.render("Press SPACE to play!",True,(0, 0, 0))
        if random_variable in range(17):
            screen.blit(intro_text, (500, 450))
        if random_variable >34:
            random_variable = 0
        random_variable += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                # print("Keydown")
                if event.key == pygame.K_SPACE:
                    game_started = True
    credits_=intro_font.render("©TheParthK",True,(0, 0, 0))
    screen.blit(credits_, (5, 700))
    credits_=intro_font.render("@SupItsParth",True,(0, 0, 0))
    screen.blit(credits_, (1218, 700))
    screen.blit(insta_logo, (1200, 699))
    pygame.display.update()