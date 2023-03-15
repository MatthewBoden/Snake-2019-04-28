#########################################
# Programmer: Matthew Bodenstein
# Date: 04/26/2019
# File Name: snake.py
# Description: This program is a Minecraft
#              based snake game with 3 different stages
#########################################
import pygame
import random
pygame.init()

################### GAME MUSIC ###########
pygame.mixer_music.load("snakee.ogg")    #
pygame.mixer_music.play(-1)              #
##########################################

##################################### ALL IMAGES #########################################
HEIGHT = 600
WIDTH  = 800
screen=pygame.display.set_mode((WIDTH,HEIGHT))      # SETS THE SCREEN AND DISPLAY
pic1= pygame.image.load("startmenu.jpg")            # Image properties
pic1 = pic1.convert_alpha()                 # converts the image pixel format for faster blitting
pic2= pygame.image.load("game.jpg")         # LOADS IMAGE
pic2 = pic2.convert_alpha()
pic4= pygame.image.load("gamemed.jpg")
pic4 = pic4.convert_alpha()
pic5= pygame.image.load("gamehard.jpg")
pic5 = pic5.convert_alpha()
pic3 = pygame.image.load("end.jpg")
pic3 = pic3.convert_alpha()
rules = pygame.image.load("rules.jpg")
rules = rules.convert_alpha()
backround = pic2                        # SETS BACKGROUND TO CHANGE FOR LATER
apple = pygame.image.load("Apple.png")
apple = pygame.transform.scale(apple, (30, 30))       # RESIZES THE IMAGE
apple = apple.convert_alpha()
bapple = pygame.image.load("BApple.png")
bapple = pygame.transform.scale(bapple, (30, 30))
bapple = bapple.convert_alpha()
tnt = pygame.image.load("TNT.jpg")
tnt = pygame.transform.scale(tnt, (23, 23))
tnt = tnt.convert_alpha()
head = pygame.image.load("bodyhead1.jpg")
head = pygame.transform.scale(head, (25, 25))
head = head.convert_alpha()
body = pygame.image.load("bodyhead.jpg")
body = pygame.transform.scale(body, (25, 25))
body = body.convert_alpha()
spi = pygame.image.load("spi.png")
spi = pygame.transform.scale(spi, (23, 23))
spi = spi.convert_alpha()
creep = pygame.image.load("creep.png")
creep = pygame.transform.scale(creep, (23, 23))
creep = creep.convert_alpha()
slime = pygame.image.load("slime.png")
slime = pygame.transform.scale(slime, (23, 23))
slime = slime.convert_alpha()
wither = pygame.image.load("wither.png")
wither = pygame.transform.scale(wither, (23, 23))
wither = wither.convert_alpha()
zomb = pygame.image.load("zomb.jpg")
zomb = pygame.transform.scale(zomb, (23, 23))
zomb = zomb.convert_alpha()
zpig = pygame.image.load("zpig.jpg")
zpig = pygame.transform.scale(zpig, (23, 23))
zpig = zpig.convert_alpha()
ender = pygame.image.load("ender.png")
ender = pygame.transform.scale(ender, (23, 23))
ender = ender.convert_alpha()
sped = 5
pic1X = 0 # SETS WHERE THE BACKGROUND WILL BE ON THE X-AXIS
pic1Y = 0 # SETS WHERE THE BACKGROUND WILL BE ON THE Y-AXIS
################################################################
score = 0        # sets initial score
seconds=0

###### COLOURS #######
WHITE = (255,255,255)#
BLACK = (  0,  0,  0)#
Green = (0, 255, 0)  #
Red = (255, 0, 0)    #
Blue = (0,0,255)     #
colour = BLACK       # SET BECAUSE THE COLOUR FOR TEXT WILL CHANGE
######################

end_music = False  # SET SO THE END MUSIC WILL PLAY ONCE
easy = False       # SETS EASY MODE
medium = False     # SETS MEDIUM MODE
hard = False       # SETS HARD MODE
visible = False    # VISIBLE SPAWNS THE EASY MODE MOBS/ENEMY'S
visible2 = False   # VISIBLE SPAWNS THE MEDIUM MODE MOBS/ENEMY'S
visible3 = False   # VISIBLE SPAWNS THE HARD MODE MOBS/ENEMY'S
outline=0
screen.blit(rules, (pic1X, pic1Y))  # puts rules on screen
pygame.time.delay(12500)  # delays screen for 12.5 seconds so user can read rules
pygame.display.update()
###### ALL OF THE ITEMS SPAWNS #######
ax = random.randrange(40,760,20)
ay = random.randrange(100, 560,20)
bx = random.randrange(40,760,20)
by = random.randrange(100, 560,20)
tx = 0
ty = 0
m1x = 0
m1y = 0
m2x = 0
m2y = 0
m3x = 0
m3y = 0
m4x = 0
m4y = 0
m5x = 0
m5y = 0
m6x = 0
m6y = 0
m7x = 0
m7y = 0
m8x = 0
m8y = 0
m9x = 0
m9y = 0
m10x = 0
m10y = 0
m11x = 0
m11y = 0
m12x = 0
m12y = 0
m13x = 0
m13y = 0
m14x = 0
m14y = 0
m15x = 0
m15y = 0
m16x = 0
m16y = 0
m17x = 0
m17y = 0
m18x = 0
m18y = 0
###################

#---------------------------------------#
# snake's properties                    #
#---------------------------------------#
BODY_SIZE = 12   # SETS BODY SIZE
HSPEED = 20      # SETS X SPEED
VSPEED = 20      # SETS Y SPEED
speedX = 0
speedY = -VSPEED
segx = [int(WIDTH/2.)]*3
segy = [HEIGHT-100, HEIGHT+VSPEED-100, HEIGHT+2*VSPEED-100]
start = True       # RUNS GAME TO START
inPlay = False     # RUNS THE GAME TO BE IN PLAY
time_length = 20   # SETS THE STARTING TIME TO 20 SECONDS
start_time = 0
time_started=False # SETS WHEN THE TIME STARTS TO COUNT DOWN
#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#

########### DRAWS THE APPLES DURING EVERY DIFFICULTY ##########
def draw_app():                                               #
    screen.blit(apple, (ax - 15, ay - 20), (0, 0, 160, 160))  #
    screen.blit(bapple, (bx - 15, by - 20), (0, 0, 160, 160)) #
###############################################################

################## DRAWS THE MOBS FOR EASY MODE ################
def draw_easy(visible):                                        #
    screen.blit(zomb, (m5x - 15, m5y - 15), (0, 0, 160, 160))  # ZOMBIE MOB
    screen.blit(spi, (m1x - 15, m1y - 15), (0, 0, 160, 160))   # SPIDER MOB
    screen.blit(creep, (m2x - 15, m2y - 15), (0, 0, 160, 160)) # CREEPER MOB
    screen.blit(slime, (m3x - 15, m3y - 15), (0, 0, 160, 160)) # SLIME MOB
    screen.blit(tnt, (tx - 15, ty - 15), (0, 0, 160, 160))     # TNT OBJ
    visible = True     # SETS BACKGROUND BOOLEAN               #
    return visible                                             #
################################################################

################## DRAWS THE MOBS FOR MEDIUM MODE ###############
def draw_medium(visible2):                                      #
    screen.blit(wither, (m4x - 15, m4y - 15), (0, 0, 160, 160)) # WITHER MOB
    screen.blit(zpig, (m6x - 15, m6y - 15), (0, 0, 160, 160))   # ZOMBIE PIG MOB
    screen.blit(wither, (m7x - 15, m7y - 15), (0, 0, 160, 160)) #
    screen.blit(zpig, (m8x - 15, m8y - 15), (0, 0, 160, 160))   #
    screen.blit(wither, (m9x - 15, m9y - 15), (0, 0, 160, 160)) #
    screen.blit(zpig, (m10x - 15, m10y - 15), (0, 0, 160, 160)) #
    visible2 = True   # SETS BACKGROUND BOOLEAN                 #
    return visible2                                             #
#################################################################

################# DRAWS THE MOBS FOR HARD MODE ###################
def draw_hard(visible3):                                         #
    screen.blit(ender, (m11x - 15, m11y - 15), (0, 0, 160, 160)) # ENDERMAN MOB
    screen.blit(ender, (m12x - 15, m12y - 15), (0, 0, 160, 160)) #
    screen.blit(ender, (m13x - 15, m13y - 15), (0, 0, 160, 160)) #
    screen.blit(ender, (m14x - 15, m14y - 15), (0, 0, 160, 160)) #
    screen.blit(ender, (m15x - 15, m15y - 15), (0, 0, 160, 160)) #
    screen.blit(ender, (m16x - 15, m16y - 15), (0, 0, 160, 160)) #
    screen.blit(ender, (m17x - 15, m17y - 15), (0, 0, 160, 160)) #
    screen.blit(ender, (m18x - 15, m18y - 15), (0, 0, 160, 160)) #
    visible3 = True   # SETS BACKGROUND BOOLEAN                  #
    return visible3                                              #
##################################################################

################# SETS THE END OF THE GAME SCREEN AND SHOWS THE SCORE ####################
def endgame(end_music):                                                                  #
    screen.blit(pic3, (pic1X, pic1Y))                                                    #
    font = pygame.font.SysFont("Ariel Black", 70)  # create a variable font              #
    text = font.render("SCORE:", 1, Green)  # put the font and the message together      #
    screen.blit(text, (260, 350))  # draw it on the screen at the text_X and text_Y      #
    text2 = font.render(str(score), 1, Green)  # put the font and the message together   #
    screen.blit(text2, (470, 350))  # draw it on the screen at the text_X and text_Y     #
    return end_music                                                                     #
##########################################################################################

##################### COUNTS DOWN THE TIMER #####################
def countdown(game_over, colour):                               #
    if visible == True: # DEPENDING ON THE MODE SETS THE COLOUR #
        colour = BLACK                                          #
    elif visible2 == True:                                      #
        colour = WHITE                                          #
    elif visible3 == True:                                      #
        colour = WHITE                                          #
    seconds=pygame.time.get_ticks()/1000                        # SETS SECONDS
    elapsed_time= seconds-start_time                            # converts into seconds
    elapsed_time=time_length-elapsed_time                       # -1 to time
    font=pygame.font.SysFont("Ariel Black",50)                  # SETS FONT
    timer_text=font.render(str(round(elapsed_time)),1,colour)   # SETS WHAT WILL BE PRINTED ON SCREEN
    screen.blit(timer_text,(100,20))                            # BLITS TEXT ON SCREEN
    pygame.display.update()                                     # UPDATES GAME
    if elapsed_time<=0:                                         # it is 0 it will end
        game_over = True                                        # ENDS THE GAME
    return game_over                                            #
#################################################################

################# this redraws the screen and blits all of the images ###############################
def redraw_screen(game_over, end_music,visible, visible2, visible3, colour ,backround):             #
    if visible == True:                                                                             #
        backround = pic2        # CHANGES BACKGROUND BASED ON GAMEMODE                              #
        colour = BLACK          # CHANGES FONT COLOUR                                               #
    elif visible2 == True:                                                                          #
        backround = pic4                                                                            #
        colour = WHITE                                                                              #
    elif visible3 == True:                                                                          #
        backround = pic5                                                                            #
        colour = WHITE                                                                              #
    screen.blit(backround, (pic1X, pic1Y))                                                          #
    font = pygame.font.SysFont("Ariel Black", 50)       # create a variable font                    #
    text = font.render(str(score), 1, colour)    # put the font and the message together            #
    screen.blit(text, (735, 20))        # draw it on the screen at the text_X and text_Y            #
    time1 = font.render(str(), 1, colour)   # SETS WHAT THE TIME ON THE SCREEN WILL BE              #
    screen.blit(time1, (200, 20))  # PRINTS TIME ON SCREEN                                          #
    game_over = countdown(game_over, colour) # CALLS THE COUNTDOWN FUNCTION TO COUNT DOWN THE TIME  #
    draw_app()         # DRAWS THE APPLES                                                           #
    if easy == True:                                                                                #
        visible = draw_easy(visible)                              # SPAWNS MOBS                     #
    if medium == True:                             # sets medium mode by adding some mobs/enemys    #
        visible2 = draw_medium(visible)                                                             #
    if hard == True:                                # sets hard mode by adding more mobs/enemys     #
        visible3 = draw_hard(visible3)                                                              #
    for i in range(len(segx)):     # THIS FOR LOOP MAKES THE BODY                                   #
        if game_over == False:                                                                      #
            if i == 0:                                                                              #
                screen.blit(head, (segx[i]-15, segy[i]-15), (0, 0, 160, 160))   # CREATES THE HEAD  #
                pygame.time.delay(sped)                                                             #
            else:                                                                                   #
                screen.blit(body, (segx[i] - 15, segy[i] - 15), (0, 0, 160, 160))# CREATES THE BODY #
                pygame.time.delay(sped)   # DELAYS BASED ON SCORE AND SPEED                         #
    if segx[0] == ax and segy[0] == ay:                                                             #
        segx.append(segx[-1])        # APPENDS 1 BLOCK ONTO THE SNAKE WHEN COLLISON WITH THE APPLE  #
        segy.append(segy[-1])                                                                       #
        if len(segx) == 1:    # IF THE SNAKE IS JUST THE HEAD, THE GAME ENDS                        #
            game_over = True                                                                        #
    if game_over == True:                                                                           #
        endgame(end_music)      # CALLS ENDGAME FUNCTION IF GAMEOVER IS TRUE AND ENDS GAME          #
        if end_music == False:                                                                      #
            pygame.mixer_music.load("deathsound.ogg")            # LOADS DEATH SOUND                #
            pygame.mixer_music.play(0)                           # PLAYS DEATH SOUND                #
            end_music = True                                                                        #
    pygame.display.update()             # display updates                                           #
    return game_over, end_music,visible, visible2, visible3                                         #
#####################################################################################################

#### STARTS THE GAME, SETS THE BUTTONS, CHANGES THE X AND Y OF EACH OBJECT DEPENDING ON DIFFICULTY ##########################################################
def gameStart(start, inPlay, easy, medium, hard, m1x, m1y, m2x, m2y, m3x, m3y, m4x, m4y, m5x, m5y, m6x, m6y, m7x, m7y, m8x, m8y, m9x, m9y, m10x, m10y, m11x #
              , m11y, m12x, m12y, m13x, m13y, m14x, m14y, m15x, m15y, m16x, m16y, m17x, m17y, m18x, m18y, tx, ty):                                          # this loads up the start screen and all of the buttons and text for it
    screen.blit(pic1, (pic1X, pic1Y))              # DISPLAYS START SCREEN
    font = pygame.font.SysFont("Ariel Black", 70)  # create a variable font
    text = font.render("SNAKE", 1, Green)          # put the font and the message together
    warning = font.render("-100 POINTS MEANS DEATH!", 1, Red)
    screen.blit(warning, (50, 500))
    screen.blit(text, (315, 100))                  # draw it on the screen at the text_X and text_Y

    # BUTTON VARIABLES
    stayBtnX = 350
    stayBtnY = HEIGHT // 2
    stay2BtnX = 350
    stay2BtnY = (HEIGHT // 2) + 50
    stay3BtnX = 350
    stay3BtnY = (HEIGHT // 2) + 100
    pygame.draw.rect(screen, Green, (stayBtnX - 10, stayBtnY - 10, 150, 50))
    pygame.draw.rect(screen, Blue, (stay2BtnX - 10, stay2BtnY - 10, 150, 50))
    pygame.draw.rect(screen, Red, (stay3BtnX - 10, stay3BtnY - 10, 150, 50))
    stayFont = pygame.font.SysFont("Arial Black", 50)
    screen.blit(stayFont.render("  EASY", 1, BLACK), (stayBtnX, stayBtnY))
    stay2Font = pygame.font.SysFont("Arial Black", 50)
    screen.blit(stay2Font.render("MEDIUM", 1, BLACK), (stay2BtnX, stay2BtnY))
    stay3Font = pygame.font.SysFont("Arial Black", 50)
    screen.blit(stay3Font.render("  HARD", 1, BLACK), (stay3BtnX, stay3BtnY))

    ########################### EASY BUTTON #############################
    if (pygame.Rect((stayBtnX, stayBtnY), (stayFont.size("EASY"))).colliderect((pygame.mouse.get_pos()), (1, 1)) and
            pygame.mouse.get_pressed()[0]):
        start = False
        easy = True                           # SETS HARD MODE
        inPlay = True
        tx = random.randrange(40, 760, 20)    #
        ty = random.randrange(100, 560, 20)   #
        m1x = random.randrange(40, 760, 20)   #
        m1y = random.randrange(100, 560, 20)  #
        m2x = random.randrange(40, 760, 20)   #
        m2y = random.randrange(100, 560, 20)  #
        m3x = random.randrange(40, 760, 20)   #
        m3y = random.randrange(100, 560, 20)  #
        m5x = random.randrange(40, 760, 20)   #
        m5y = random.randrange(100, 560, 20)  #

    ########################### MEDIUM BUTTON #############################
    if (pygame.Rect((stay2BtnX, stay2BtnY), (stayFont.size("MEDIUM"))).colliderect((pygame.mouse.get_pos()), (1, 1)) and
            pygame.mouse.get_pressed()[0]):
        start = False
        inPlay = True
        medium = True                          # SETS MEDIUM MODE
        m4x = random.randrange(40, 760, 20)    #
        m4y = random.randrange(100, 560, 20)   #
        m7x = random.randrange(40, 760, 20)    #
        m7y = random.randrange(100, 560, 20)   #
        m6x = random.randrange(40, 760, 20)    #
        m6y = random.randrange(100, 560, 20)   # CHANGES THE X AND Y OF EACH MOB/ENEMY
        m8x = random.randrange(40, 760, 20)    #
        m8y = random.randrange(100, 560, 20)   #
        m9x = random.randrange(40, 760, 20)    #
        m9y = random.randrange(100, 560, 20)   #
        m10x = random.randrange(40, 760, 20)   #
        m10y = random.randrange(100, 560, 20)  #

    ########################### HARD BUTTON #############################
    if (pygame.Rect((stay3BtnX, stay3BtnY), (stayFont.size("HARD"))).colliderect((pygame.mouse.get_pos()), (1, 1)) and
            pygame.mouse.get_pressed()[0]):
        start = False
        inPlay = True
        hard = True         # SETS MODE TO HARD WHEN YOU CLICK THE BUTTON
        m11x = random.randrange(40, 760, 20)   #
        m11y = random.randrange(100, 560, 20)  #
        m12x = random.randrange(40, 760, 20)   #
        m12y = random.randrange(100, 560, 20)  #
        m13x = random.randrange(40, 760, 20)   #
        m13y = random.randrange(100, 560, 20)  #
        m14x = random.randrange(40, 760, 20)   # CHANGES THE X AND Y OF EACH MOB/ENEMY
        m14y = random.randrange(100, 560, 20)  #
        m15x = random.randrange(40, 760, 20)   #
        m15y = random.randrange(100, 560, 20)  #
        m16x = random.randrange(40, 760, 20)   #
        m16y = random.randrange(100, 560, 20)  #
        m17x = random.randrange(40, 760, 20)   #
        m17y = random.randrange(100, 560, 20)  #
        m18x = random.randrange(40, 760, 20)   #
        m18y = random.randrange(100, 560, 20)  #
    return (start, inPlay, easy, medium, hard, m1x, m1y, m2x, m2y, m3x, m3y, m4x, m4y, m5x, m5y, m6x, m6y, m7x, m7y, m8x, m8y, m9x, m9y,
            m10x, m10y,m11x, m11y, m12x, m12y, m13x, m13y, m14x, m14y, m15x, m15y, m16x, m16y, m17x, m17y, m18x, m18y, tx, ty)
############################################################################################################################################

#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
game_over = False
while start:
# check for events
    #pygame.event.get()
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:       # If user clicked close
            inPlay = False
    start, inPlay, easy, medium, hard, m1x, m1y, m2x, m2y, m3x, m3y, m4x, m4y, m5x, m5y, m6x, m6y, m7x, m7y, m8x, m8y, m9x, m9y, m10x, m10y,m11x, m11y, m12x, m12y, m13x, m13y, m14x, m14y, m15x, m15y, m16x, m16y, m17x, m17y, m18x, m18y, tx, ty = gameStart(start, inPlay, easy, medium, hard, m1x, m1y, m2x, m2y, m3x, m3y, m4x, m4y, m5x, m5y, m6x, m6y, m7x, m7y, m8x, m8y, m9x, m9y, m10x, m10y,m11x, m11y, m12x, m12y, m13x, m13y, m14x, m14y, m15x, m15y, m16x, m16y, m17x, m17y, m18x, m18y, tx, ty)
    pygame.display.update()

while inPlay:
# check for events
    #pygame.event.get()
    if not time_started:
        start_time = pygame.time.get_ticks() / 1000
        time_started = True

    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:       # If user clicked close
            inPlay = False                # Flag that we are done so we exit this loop
        keys = pygame.key.get_pressed()
    # act upon key events
        if keys[pygame.K_LEFT] and not speedX ==HSPEED and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            speedX = -HSPEED
            speedY = 0
        if keys[pygame.K_RIGHT]and not speedX == -HSPEED and not keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            speedX = HSPEED
            speedY = 0
        if keys[pygame.K_UP]and not speedY ==VSPEED and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            speedX = 0
            speedY = -VSPEED
        if keys[pygame.K_DOWN]and not speedY == -VSPEED and not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            speedX = 0
            speedY = VSPEED

    # move all segments
    for i in range(len(segx)-1,0,-1):   # start from the tail, and go backwards:
        segx[i]=segx[i-1]               # every segment takes the coordinates
        segy[i]=segy[i-1]               # of the previous one

    if segx[0] == ax and segy[0] == ay: # APPLE COLLISION
        score += 10
        ax = random.randrange(40, 760, 20)
        ay = random.randrange(100, 560, 20)
        a = pygame.mixer.Sound("eatting.wav")
        start_time = pygame.time.get_ticks()/1000
        a.play(0)

    if segx[0] == bx and segy[0] == by: # BONUS APPLE COLLISION
        score += 5
        bx = random.randrange(40, 760, 20)
        by = random.randrange(100, 560, 20)
        b = pygame.mixer.Sound("bonus.wav")
        start_time = pygame.time.get_ticks()/1000  # RESETS THE TIME TO 20 SEC
        b.play(0)

    if segx[0] == tx and segy[0] == ty:
        score -= 10
        tx = random.randrange(40, 760, 20)
        ty = random.randrange(100, 560, 20)
        t = pygame.mixer.Sound("TNTSOUND.wav")
        t.play(0)

    if score <= -100: # IF SCORE IS LESS THAN 100, YOU LOSE
        game_over = True

###### MOVES THE HEAD OF THE SNAKE#####
    segx[0] = segx[0] + speedX
    segy[0] = segy[0] + speedY


############### CHECKS COLLISION AROUND THE SCREEN SO PLAYER CANNOT GO OUT OF BOUNDS ##############
    if segx[0] <= 0 or segy[0] <= 73 or segy[0] >= 600 or segx[0] >= 800:                         #
        game_over = True                                                                          #
###################################################################################################


############################# PRINTS REDRAW SCREEN FUNCTION #############################
    game_over, end_music,visible, visible2, visible3 = redraw_screen(game_over, end_music,visible, visible2, visible3,colour, backround)


############# CHECKS COLLISION IN BODY ################
    for i in range(3, len(segx)):                     #
        if segx[0] == segx[i] and segy[0] == segy[i]: #
            game_over = True                          #
#######################################################


# WHEN THE HEAD COLLIDES WITH THE OBJECT IT SWITCHES X AND Y AND CHANGES SCORE #
##########################################################################
    if segx[0] == tx and segy[0] == ty: # CHECKS COLLISION               #
        segx.remove(segx[-1])           # REMOVES 1 BLOCK                #
        segy.remove(segy[-1])           # REMOVES 1 BLOCK                #
    if (segx[0] == m1x and segy[0] == m1y):                              #
        t = pygame.mixer.Sound("spis.wav")    # LOADS SOUND              #
        m1x = random.randrange(40, 760, 20)   # CHANGES X CORD OF OBJ    #
        m1y = random.randrange(100, 560, 20)  # CHANGES Y CORD OF OBJ    #
        score -= 10                           # CHANGES SCORE            #
        t.play(0)                             # PLAYS SOUND              #
    if (segx[0] == m2x and segy[0] == m2y):                              #
        t = pygame.mixer.Sound("TNTSOUND.wav")                           #
        m2x = random.randrange(40, 760, 20)                              #
        m2y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m3x and segy[0] == m3y):                              #
        t = pygame.mixer.Sound("slimes.wav")                             #
        m3x = random.randrange(40, 760, 20)                              #
        m3y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m4x and segy[0] == m4y):                              #
        t = pygame.mixer.Sound("withers.wav")                            #
        m4x = random.randrange(40, 760, 20)                              #
        m4y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m5x and segy[0] == m5y):                              #
        t = pygame.mixer.Sound("zombs.wav")                              #
        m5x = random.randrange(40, 760, 20)                              #
        m5y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m6x and segy[0] == m6y):                              #
        t = pygame.mixer.Sound("zombps.wav")                             #
        m6x = random.randrange(40, 760, 20)                              #
        m6y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m7x and segy[0] == m7y):                              #
        t = pygame.mixer.Sound("withers.wav")                            #
        m7x = random.randrange(40, 760, 20)                              #
        m7y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m9x and segy[0] == m9y):                              #
        t = pygame.mixer.Sound("withers.wav")                            #
        m9x = random.randrange(40, 760, 20)                              #
        m9y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m8x and segy[0] == m8y):                              #
        t = pygame.mixer.Sound("zombps.wav")                             #
        m8x = random.randrange(40, 760, 20)                              #
        m8y = random.randrange(100, 560, 20)                             #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m10x and segy[0] == m10y):                            #
        t = pygame.mixer.Sound("zombps.wav")                             #
        m10x = random.randrange(40, 760, 20)                             #
        m10y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m11x and segy[0] == m11y):                            #
        t = pygame.mixer.Sound("enders1.wav")                            #
        m11x = random.randrange(40, 760, 20)                             #
        m11y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m12x and segy[0] == m12y):                            #
        t = pygame.mixer.Sound("enders2.wav")                            #
        m12x = random.randrange(40, 760, 20)                             #
        m12y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m13x and segy[0] == m13y):                            #
        t = pygame.mixer.Sound("enders3.wav")                            #
        m13x = random.randrange(40, 760, 20)                             #
        m13y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m14x and segy[0] == m14y):                            #
        t = pygame.mixer.Sound("enders1.wav")                            #
        m14x = random.randrange(40, 760, 20)                             #
        m14y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m15x and segy[0] == m15y):                            #
        t = pygame.mixer.Sound("enders2.wav")                            #
        m15x = random.randrange(40, 760, 20)                             #
        m15y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m16x and segy[0] == m16y):                            #
        t = pygame.mixer.Sound("enders3.wav")                            #
        m16x = random.randrange(40, 760, 20)                             #
        m16y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m17x and segy[0] == m17y):                            #
        t = pygame.mixer.Sound("enders1.wav")                            #
        m17x = random.randrange(40, 760, 20)                             #
        m17y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
    if (segx[0] == m18x and segy[0] == m18y):                            #
        t = pygame.mixer.Sound("enders2.wav")                            #
        m18x = random.randrange(40, 760, 20)                             #
        m18y = random.randrange(100, 560, 20)                            #
        score -= 10                                                      #
        t.play(0)                                                        #
##########################################################################

######## CHANGES SPEED BASED ON SCORE ########
    if score >= 100 and score <= 250:        #
        sped = 4                             #
    if score >= 251 and score <= 350:        #
        sped = 3                             #
    if score >= 351 and score <= 500:        #
        sped = 2                             #
    if score >= 501 and score <= 700:        #
        sped = 1                             #
    if score >= 701:                         #
        sped = 0                             #
##############################################
pygame.time.delay(30)
pygame.quit()                           # always quit pygame when done!
