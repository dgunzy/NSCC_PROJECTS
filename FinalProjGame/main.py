#!/usr/bin/python3
import pygame as py
import os as os
import datetime
import math
import functions as f

py.font.init()
clock = py.time.Clock()

WIDTH = 1200
HEIGHT = 600
FPS = 60
VEL = 5
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Charlie's Adventure")
BG = py.image.load(os.path.join('assets',"background.png")).convert()
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
WHITE = (0, 0, 0)
PURPLE = (62, 12, 94)
scroll = 0



def draw_background(playerposition):
    global scroll
    for i in range(0,2):

        if playerposition.x > 350:
            SCREEN.blit(BG, (i * WIDTH + scroll,0))
            
            scroll -= 3
            
            if abs(scroll) > WIDTH:
                scroll = 0
                
            
        if playerposition.x <= 350:
            SCREEN.blit(BG, (i * WIDTH + scroll,0))
           
    
def draw_gamewindow(playerposition, coneposition, blenderposition, ballposition, pigposition, charlie_fear):
    SCREEN.blit(CONE, (coneposition.x, coneposition.y))
    SCREEN.blit(BLENDER, (blenderposition.x, blenderposition.y))
    SCREEN.blit(BALL, (ballposition.x ,ballposition.y))
    SCREEN.blit(PIG, (pigposition.x, pigposition.y))
    charlie_fear_text = FEAR_FONT.render("Charlie's Fear level: " + str(charlie_fear) + "                 She gets Scared at 5!", 1, PURPLE )
    SCREEN.blit(charlie_fear_text, (10, 10))
    SCREEN.blit(PLAYER, (playerposition.x, playerposition.y))
    

def player_movement(keys_pressed, playerposition):
    if keys_pressed[py.K_LEFT] and playerposition.x > 0: 
        playerposition.x -= VEL
    if keys_pressed[py.K_RIGHT] and playerposition.x < 1100: 
            playerposition.x += VEL + 1


def object_movement(timestart, gameclock, objectposition, itemvel):
    if gameclock > timestart:
        objectposition.x -= itemvel
        if objectposition.x < -500:
            objectposition.x = 1400
            return objectposition
        return objectposition

def collision(playerposition, coneposition, blenderposition, pigposition, ballposition, immunetimer, boosttimer):
    if playerposition.colliderect(coneposition) and immunetimer < 0:
        py.event.post(py.event.Event(CHARLIE_HIT))
        
        
    if playerposition.colliderect(blenderposition) and immunetimer < 0:
        py.event.post(py.event.Event(CHARLIE_HIT))
        
    if playerposition.colliderect(pigposition) and immunetimer < 0:
        py.event.post(py.event.Event(CHARLIE_HIT))
       
    if playerposition.colliderect(ballposition) and boosttimer < 0:
        py.event.post(py.event.Event(CHARLIE_BOOST))
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
    coneposition = py.Rect(1300, 450, 150, 75)
    blenderposition = py.Rect(1500, 420, 150, 75)
    ballposition = py.Rect(1400,200, 60,60)
    pigposition = py.Rect(1600, 450, 200, 128)
    clock = py.time.Clock()
    immunetimer = 0
    boosttimer = 0
    gameclock = 0
    scroll = 0
    charlie_fear = 0
    jumpcount = 13
    itemvel = 0
    jump = False
    run= True
    
    while run:
        clock.tick(FPS)
        gameclock += 1
        immunetimer -= 1
        boosttimer -= 1
        itemvel = int(gameclock / 400) + 6
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == CHARLIE_HIT:
                charlie_fear += 1
                immunetimer = 60
            if event.type == CHARLIE_BOOST and charlie_fear > 0:
                charlie_fear -= 1
                boosttimer = 60
                ballposition.x = 2000
        keys_pressed = py.key.get_pressed()
        player_movement(keys_pressed, playerposition)
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
        object_movement(200, gameclock, coneposition, itemvel)
        object_movement(350, gameclock, blenderposition, itemvel)
        object_movement(450, gameclock, ballposition, itemvel)
        object_movement(600, gameclock, pigposition, itemvel)
   
        collision(playerposition, coneposition, blenderposition, pigposition, ballposition, immunetimer, boosttimer)
        if charlie_fear == 5:
            gameover(gameclock)
            run = False
        draw_background(playerposition)        
        draw_gamewindow(playerposition, coneposition, blenderposition, ballposition, pigposition, charlie_fear)
        py.display.update()
    if run == False:
            py.quit()

main()