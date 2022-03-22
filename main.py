from ast import Pass #this imports Pass from ast
import pygame #this imports pygame
from pygame import mixer #this imports mixer from pygame
import random #this imports random
import math #this imports math
import keyboard #this imports keyboard
from scipy import rand #this imports rand from scipy
pygame.init() #this initializes pygame
dimensions = (1280, 720) #this sets the dimensions of the game window
screen = pygame.display.set_mode(dimensions) #this sets the dimensions of the game window
player_dimensions = (70, 70) #this sets the dimensions of the player
bgcolor = (255, 0, 255) #this sets the background color

pygame.display.set_caption("Flappy Bird") #this sets the title of the game

icon = pygame.transform.scale(pygame.image.load("icon.png"), (32, 32)) #this sets the icon of the game
pygame.display.set_icon(icon) #this sets the icon of the game

bg = pygame.transform.scale(pygame.image.load("bg.png"), dimensions) #this sets the background of the game

playerd = pygame.transform.scale(pygame.image.load("player_down.png"), player_dimensions)  #this sets the player image
playeru = pygame.transform.scale(pygame.image.load("player_up.png"), player_dimensions) #this sets the player image
player = playerd #this sets the player image to playerd
playerdd = pygame.transform.rotate(playerd, -90) #this rotates the player image
playeruu = pygame.transform.rotate(playeru, -90) #this rotates the player image
playerx = 200 #this sets the x position of the player
playery = 200 #this sets the y position of the player
playerc = 10 #this sets the speed of the player

lp = pygame.image.load("Lower_part.png") #this loads the lower part of the pipe
lp1 = pygame.image.load("Lower_part.png") #this loads the lower part of the pipe
lpx = 0 #this sets the x position of the lower part of the pipe
lpc = -7 #this sets the speed of the lower part of the pipe
lp1x = lpx + 1280 #this sets the x position of the lower part of the pipe

obs = pygame.image.load("obs.png") #this loads the upper part of the pipe
# obs_size = (600, 1000)
obs_size = (600, 1000) #this sets the size of the upper part of the pipe
obsu = pygame.transform.scale(obs, obs_size) #this sets the upper part of the pipe
obsd = pygame.transform.rotate(obsu, 180) #this rotates the upper part of the pipe
obsx = [300, 650, 1000, 1350]   #this sets the x position of the upper part of the pipe
obsuy = [random.choice([-650, -750, -850, -950]) for i in range(len(obsx))] #this sets the y position of the upper part of the pipe
# obsuy = -700
obsly = [(i + 1200) for i in obsuy] #this sets the y position of the lower part of the pipe
obsc = lpc #this sets the speed of the upper part of the pipe
# exit screen
game_over = pygame.image.load("end.png") #this loads the end screen
game_over = pygame.transform.scale(game_over, (400, 100)) #this sets the size of the end screen

gox, goy = 450, 165    #this sets game over x and y

score_card = pygame.image.load("score_card_2.png") #this loads score card png file
score_card = pygame.transform.scale(score_card, (400, 300)) #this sets the size of the score card
scx, scy = 440, 170 #this sets the x and y position of the score card
run = True #this sets the run variable to true
falling = True #this sets the falling variable to true
flap = 1 #this sets the flap variable to 1
n = 0 #this sets the n variable to 0
mixer.music.load("song.mp3") #this loads the song
# a--------------------------------------a
# mixer.music.play(-1)
font = pygame.font.Font("Minecraft.ttf", 200) #this loads the font
font1 = pygame.font.Font("Minecraft.ttf", 210) #this loads the font
scorex, scorey = 600, 30  #this sets the x and y position of the score
score = 0 #this sets the score to 0
killed = False #this sets the killed variable to false
score_added = False #this sets the score_added variable to false
collision = False   #this sets the collision variable to false
restart_status = False #this sets the restart_status variable to false
restarter = 0 #this sets the restarter variable to 0
# space_pressed = False
font2 = pygame.font.Font("Minecraft.ttf", 25) #this loads the font
font3 = pygame.font.Font("Minecraft.ttf", 32) #this loads the font
hitt = False #this sets the hitt variable to false
quit_game=False #this sets the quit_game variable to false
re_varibale = 0 #this sets the re_varibale variable to 0
highest_score = 0  #this sets the highest_score variable to 0
game_started = False #this sets the game_started variable to false
intro_done = False #this sets the intro_done variable to false
intro_image = pygame.image.load("intro_screen.png") #this loads the intro screen
#1200, 720
# intro_image = pygame.transform.scale(intro_image, (1000, 600))
random_variable = 0 #this sets the random_variable variable to 0
insta_logo = pygame.image.load("insta_logo.png") #this loads the insta logo
insta_logo = pygame.transform.scale(insta_logo, (15, 15)) #this sets the size of the insta logo
intro_font = pygame.font.Font("intro_font.ttf", 10) #this loads the intro font
while run: #this runs the game
    if game_started: #this runs the game if the game has started
        intro_done = True #this sets the intro_done variable to true
        if score > highest_score: #this runs the game if the score is greater than the highest score
            highest_score = score #this sets the highest score to the score
        score_change = 0 #this sets the score_change variable to 0
        scored = False #this sets the scored variable to false
        for event in pygame.event.get(): #this gets the events
            if event.type == pygame.QUIT: #this runs the game if the event is quit
                run = False #this sets the run variable to false
            if event.type == pygame.KEYDOWN: #this runs the game if the event is keydown
                # print("Keydown")
                if event.key == pygame.K_SPACE: #this runs the game if the key is space
                    if not killed: #this runs the game if the player is not killed
                        playerc = -20 #this sets the speed of the player
                        falling = False #this sets the falling variable to false
                        mixer.Sound("wing.mp3").play() #this plays the wing sound
                        if killed: #this runs the game if the player is killed
                            pass #this does nothing
            if event.type == pygame.KEYUP: #this runs the game if the event is keyup
                if not killed: #this runs the game if the player is not killed
                    playerc = 10 #this sets the speed of the player
                    falling = True #this sets the falling variable to true

                # print('Keyup')

        screen.fill(bgcolor) #this fills the screen with the background color
        screen.blit(bg, (0, 0)) #this blits the background
        sc=font.render(str(score),True,(255,255,255)) #this renders the score
        sc1=font1.render(str(score),True,(0, 0, 0)) #this renders the score


        # sc 
        if not killed: #this runs the game if the player is not killed
            # screen.blit(sc1, (scorex-2.5, scorey-3))
            screen.blit(sc1, (scorex, scorey)) #this blits the score
            screen.blit(sc, (scorex, scorey)) #this blits the score
            # screen.blit(pass)
        # obstacle
        # Leaving and entering screen 
        # -342
        # 900 fully eneterd
        # if n % 150 == 0:
        #     obsx = 600
        # -----hta diyo yeh pagal ^-------
        for i in range(len(obsx)): #this runs the game for the length of the obsx
            screen.blit(obsu, (obsx[i], obsuy[i])) #this blits the upper part of the pipe
            screen.blit(obsd, (obsx[i], obsly[i])) #this blits the lower part of the pipe
            obsx[i] += obsc #this adds the speed of the pipe to the x position of the pipe
            if obsx[i] < -350: #this runs the game if the x position of the pipe is less than -350
                collision, score_added = False, False #this sets the collision and score_added variables to false
                obsuy[i] = random.choice([-650, -750, -850, -950]) #this sets the y position of the upper pipe 
                obsly[i] = obsuy[i] + 1200 #this sets the y position of the lower pipe
                obsx[i] = 1060 #this sets the x position of the pipe
            if not collision : #this runs the game if the player is not killed
                if obsx[i] in range(5, -118, -1): #this runs the game if the x position of the pipe is in range
                    if playery not in range(obsuy[i] + 973, obsly[i]-50): #this runs the game if the y position of the player is not in range
                        collision = True #this sets the collision variable to true
                        # print(f"obsx: {obsx[i]} | obsuy: {obsuy[i]} | obsly: {obsly[i]}")
                elif obsx[i] < -118 and not score_added: #this runs the game if the x position of the pipe is less than -118 and the score is not added
                    score += 1 #this adds 1 to the score
                    if score % 5 == 0 and score > 0: #this runs the game if the score is divisible by 5 and the score is greater than 0
                        obsc -= 1 #this adds 1 to the speed of the pipe
                        lpc -= 1 #this adds 1 to the speed of the player
                    if 11 > score > 9 : #this runs the game if the score is greater than 9
                        scorex -= 50 #this adds 50 to the x position of the score
                    score_added = True #this sets the score_added variable to true
        
        if lpx <= -1280: #this runs the game if the x position of the player is less than -1280
            lpx = 0 #this sets the x position of the player to 0
            lp1x = 1280 #this sets the x position of the player to 1280
        screen.blit(lp, (lpx, 660)) #this blits the player
        screen.blit(lp1, (lp1x, 660)) #this blits the player
        lpx += lpc #this adds the speed of the player to the x position of the player
        lp1x += lpc #this adds the speed of the player to the x position of the player

        screen.blit(player, (playerx, playery)) #this blits the player
        playery += playerc #this adds the speed of the player to the y position of the player
        if playery > 610: #this runs the game if the y position of the player is greater than 610
            playery = 610 #this sets the y position of the player to 610
            collision = True #this sets the collision variable to true
        if playery < -20: #this runs the game if the y position of the player is less than -20
            playery = -20 #this sets the y position of the player to -20
        
        # -342
        # 900 fully eneterd
        
        # print(obsx)
        n += 1 #this adds 1 to the n variable
        # flapping
        if flap in range(1, 5): #this runs the game if the flap is in range
            if not killed: #this runs the game if the player is not killed
                player = playeru #this sets the player to the upper player
            else: #this runs the game if the player is killed
                player = playeruu #this sets the player to the upper player
        else: #this runs the game if the flap is not in range
            if not killed: #this runs the game if the player is not killed
                player = playerd #this sets the player to the lower player
            else:  #this runs the game if the player is killed
                player = playerdd #this sets the player to the lower player
        flap += 1 #this adds 1 to the flap variable
        if flap > 10: #this runs the game if the flap is greater than 10
            flap = 1 #this sets the flap to 1
        # endscreen
        if collision:   #this runs the game if the player is killed
            # game_over = pygame.image.load("end.png")
            if not hitt: #this runs the game if the player is not killed
                mixer.Sound("sfx_hit.wav").play() #this plays the hit sound
                mixer.Sound("sfx_die.wav").play() #this plays the die sound
            obsc, lpc, playerc = 0, 0, 35 #this sets the speed of the pipe, the speed of the player, and the speed of the player
            killed = True #this sets the killed variable to true
            if playery < -20: #this runs the game if the y position of the player is less than -20
                pass #this does nothing
            
            screen.blit(game_over, (gox, goy)) #this shows game over screen
            # replay=font2.render("Press 'Q' to Quit & 'R' to Restart",True,(0, 0, 0))
            # to_quit = font2.render("Click Here To Quit ^", True, (0, 0, 0))

            if flap in range(1, 6): #this runs the game if the flap is in range
                replay=font2.render("Press 'Q' to Quit & 'R' to Restart",True,(0, 0, 0)) #this shows the replay text
                screen.blit(replay, (450, 490)) #this blits the replay text
                replay=font2.render("Press 'Q' to Quit & 'R' to Restart",True,(255, 255, 255)) #this shows the replay text
                screen.blit(replay, (449, 489)) #this blits the replay text
                # screen.blit(to_quit, (1020, 10))


            score_display = font3.render(str(score), True, (255,117,78)) #this shows the score
            highest_score_display = font3.render(str(highest_score), True, (255,117,78)) #this shows the highest score
            screen.blit(score_card, (scx, scy)) #this blits the score card
            screen.blit(score_display, (735, 330)) #this blits the score
            screen.blit(highest_score_display, (737, 395)) #this blits the highest score
            
            hitt = True   #this sets the hitt variable to true
            try: #this runs the game if the player is killed
                if keyboard.is_pressed('r'): #this runs the game if the r key is pressed
                    print('Restarted!') #this prints the restarted message
                    # quit_game=True
                    restart_status=True #this sets the restart_status variable to true

            except: #this runs the game if the player is killed
                # quit_game = False   
                restart_status=False  #this sets the restart_status variable to false
            # if killed and not restart_status:
            #     restarter+=1 
            # if restarter==100:
            #     restart_status=True
            if restart_status: #this runs the game if the restart_status variable is true
                restarter += 1 #this adds 1 to the restarter variable
                # loading = font3.render(str("Loading..." + "."*int(restarter/5)), True, (255,117,78))
                loading = font2.render(str("Loading...")[0 : int(restarter/5) + 1], True, (0, 0, 0)) #this shows the loading text
                # loading = font2.render(str("#"*int(restarter/5 + 1)), True, (0, 0, 0))
                # screen.blit(loading, (550, 540))
                screen.blit(loading, (570, 540)) #this blits the loading text
                if restarter == 50: #this runs the game if the restarter variable is greater than 50
                    killed = False #this sets the killed variable to false
                    collision = False #this sets the collision variable to false
                    hitt = False #this sets the hitt variable to false
                    restarter=0 #this sets the restarter variable to 0
                    restart_status=False #this sets the restart_status variable to false
                    playery = 200 #this sets the y position of the player to 200
                    obsx = [300, 650, 1000, 1350] #this sets the x position of the pipe to 300, 650, 1000, and 1350
                    score = 0 #this sets the score to 0
                    playerc = 10 #this sets the speed of the player to 10
                    lpc = -10 #this sets the speed of the pipe to -10
                    obsc = lpc #this sets the speed of the pipe to the speed of the pipe
                
            try: #this runs the game if the player is killed
                if keyboard.is_pressed('q'): #this runs the game if the q key is pressed
                    print('Game Over!') #this prints the game over message
                    quit_game=True #this sets the quit_game variable to true
            except: #this runs the game if the player is killed
                quit_game = False #this sets the quit_game variable to false
            if quit_game: #this runs the game if the quit_game variable is true
                break #this breaks the game

    else: #this runs the game if the game is not running
        screen.blit(bg, (0, 0)) #this blits the background
        for i in range(len(obsx)): #this runs the game for the length of the obsx variable
            screen.blit(obsu, (obsx[i]-300, obsuy[i] )) #this blits the upper pipe
            screen.blit(obsd, (obsx[i]-300, obsly[i] )) #this blits the lower pipe
        screen.blit(lp, (0, 660)) #this blits the lower pipe
        screen.blit(intro_image, (340, 150)) #this blits the intro image
        intro_text=font2.render("Press SPACE to play!",True,(0, 0, 0)) #this shows the intro text
        if random_variable in range(17): #this runs the game if the random variable is in range
            screen.blit(intro_text, (500, 450)) #this blits the intro text
        if random_variable >34: #this runs the game if the random variable is greater than 34
            random_variable = 0 #this sets the random variable to 0
        random_variable += 1 #this adds 1 to the random variable
        for event in pygame.event.get(): #this runs the game for the events
            if event.type == pygame.QUIT: #this runs the game if the event is quit
                run = False #this sets the run variable to false
            if event.type == pygame.KEYDOWN: #this runs the game if the event is a key down
                # print("Keydown")
                if event.key == pygame.K_SPACE: #this runs the game if the key is space
                    game_started = True
    credits_=intro_font.render("©TheParthK",True,(0, 0, 0)) #this shows the credits
    screen.blit(credits_, (5, 700)) #this blits the credits
    credits_=intro_font.render("@SupItsParth",True,(0, 0, 0)) #this shows the credits
    screen.blit(credits_, (1218, 700))  #this blits the credits
    screen.blit(insta_logo, (1200, 699)) #this blits the insta logo
    pygame.display.update() #this updates the display