#!/usr/bin/python3
import pygame as py
import os as os

import datetime

py.font.init()
py.mixer.init()
py.display.init()
clock = py.time.Clock()



WIDTH = 1200
HEIGHT = 600
FPS = 60
VEL = 5
# itemvel = 3


SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Charlie's Adventure")


BG = py.image.load(os.path.join('assets',"background.png")).convert()  

WHITE = (0, 0, 0)
PLAYER = py.image.load(os.path.join('assets', 'dog.png'))
PIG = py.image.load(os.path.join('assets','pig.png'))
CONE = py.image.load(os.path.join('assets','cone.png'))
BLENDER = py.image.load(os.path.join('assets','blender.png'))
BALL = py.image.load(os.path.join('assets','ball.png'))

CHARLIE_HIT = py.USEREVENT + 1
CHARLIE_BOOST = py.USEREVENT + 2
FEAR_FONT = py.font.SysFont('comicsans', 40)
END_FONT = py.font.SysFont('comicsans', 100)
SCORE_FONT = py.font.SysFont('comicsans', 60)
PURPLE = (62, 12, 94)


# playerposition = py.Rect(200, 450, 100, 90)
# coneposition = py.Rect(1400, 450, 150, 75)
# blenderposition = py.Rect(1400, 420, 150, 75)
# ballposition = py.Rect(1400,200, 60,60)
# pigposition = py.Rect(3000, 450, 200, 128)
# charlie_fear = 0

# jump = True
# jumpcount = 13
# scrollstartx = 0
# scroll = 0
# move = 1200
# gameclock = 0
# itemvel = 4
# immunetimer = 60
# boosttimer = 0
# run = True
# playerposition = py.Rect(200, 450, 100, 90)
# coneposition = py.Rect(1400, 450, 150, 75)
# blenderposition = py.Rect(1400, 420, 150, 75)
# ballposition = py.Rect(1400,200, 60,60)
# pigposition = py.Rect(3000, 450, 200, 128)
# charlie_fear = 0

# jump = True
# jumpcount = 13
# scrollstartx = 0
# scroll = 0
# move = 1200
# gameclock = 0
# itemvel = 4
# immunetimer = 60
# boosttimer = 0
# run = True
# itemvel = 3 
def control_object(gameclock, itemvel, timestart, objectposition, object):
    if gameclock >= timestart:
        objectposition.x -= itemvel
        SCREEN.blit(object, (objectposition.x, objectposition.y))
        if objectposition.x <= -2000:
            objectposition.x = 1400
def gameover(gameclock):
    game_over_text = END_FONT.render("GAME OVER", 1, WHITE)
    score_text = SCORE_FONT.render("You scored " + str(gameclock//60), 1, WHITE)
    SCREEN.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2 - game_over_text.get_height()/2))
    SCREEN.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 400))
    py.display.update()
    time = datetime.datetime.now()
    with open("scores.txt", "a") as f:
                f.write("\nThe score by player is " + str(gameclock//60) + str(time))
    py.time.delay(5000)
    

def main():
    playerposition = py.Rect(200, 450, 100, 90)
    coneposition = py.Rect(1400, 450, 150, 75)
    blenderposition = py.Rect(1400, 420, 150, 75)
    ballposition = py.Rect(1400,200, 60,60)
    pigposition = py.Rect(3000, 450, 200, 128)
    charlie_fear = 0

    jump = True
    jumpcount = 13
    
    scroll = 0
    
    gameclock = 0
    itemvel = 4
    immunetimer = 60
    boosttimer = 0
    run = True
    itemvel = 3 

    while run:
        clock.tick(FPS)
        gameclock += 1
        immunetimer -= 1
        boosttimer -= 1
        itemvel = int((gameclock / 700) + 5)
            
        if playerposition.colliderect(coneposition) and immunetimer < 0:
            py.event.post(py.event.Event(CHARLIE_HIT))
            immunetimer = 60
        if playerposition.colliderect(blenderposition) and immunetimer < 0:
            py.event.post(py.event.Event(CHARLIE_HIT))
            immunetimer = 60
        if playerposition.colliderect(pigposition) and immunetimer < 0:
            py.event.post(py.event.Event(CHARLIE_HIT))
            immunetimer = 60
        if playerposition.colliderect(ballposition) and boosttimer < 0:
            py.event.post(py.event.Event(CHARLIE_BOOST))
            
            boosttimer = 300
        if charlie_fear <= 0:
            charlie_fear = 0

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            
            if event.type == CHARLIE_HIT:
                charlie_fear += 1
            if event.type == CHARLIE_BOOST:
                charlie_fear -= 1
                ballposition.x = 2000

        keys_pressed = py.key.get_pressed()
        if keys_pressed[py.K_LEFT] and playerposition.x > 0: #and red.x - VEL > BORDER.x + BORDER.width: #LEFT
            playerposition.x -= VEL
        if keys_pressed[py.K_RIGHT] and playerposition.x < 1150: 
            playerposition.x += VEL + 1

        for i in range(0,2):

            if playerposition.x > 350:
                SCREEN.blit(BG, (i * WIDTH + scroll,0))
                
                scroll -= 3
                if abs(scroll) > WIDTH:
                    scroll = 0
            
            if playerposition.x <= 350:
                SCREEN.blit(BG, (i * WIDTH + scroll,0))
        
        


        if not(jump):
            
            if keys_pressed[py.K_SPACE]:
                jump = True
        if jump == True:
            if jumpcount >= -13:
                playerposition.y -=(jumpcount *abs(jumpcount)) * 0.5
                jumpcount -= 1
            else:
                jumpcount = 13
                jump = False
                playerposition.y = 450
        SCREEN.blit(PLAYER, (playerposition.x, playerposition.y))
        charlie_fear_text = FEAR_FONT.render("Charlie's Fear level: " + str(charlie_fear) + "                 She gets Scared at 5!", 1, PURPLE )
        SCREEN.blit(charlie_fear_text, (10, 10))
        
        control_object(gameclock, itemvel, 197,coneposition,CONE)
        if boosttimer <= 0:
            control_object(gameclock, itemvel, 677,ballposition,BALL)
            
        control_object(gameclock, itemvel, 487,blenderposition,BLENDER)
        control_object(gameclock, itemvel, 733,coneposition,CONE)
        control_object(gameclock, itemvel, 823,blenderposition,BLENDER)
        control_object(gameclock, itemvel, 500, pigposition, PIG)
        
        if charlie_fear >= 5:
            gameover(gameclock)
            break
        py.display.update()
        if run == False:
            py.quit()
        
        
        if charlie_fear >= 5:
            gameover()
            break
        py.display.update()
        if run == False:
            py.quit()
    
main()    




    
    
 
       