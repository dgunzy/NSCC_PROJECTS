#!/usr/bin/python3
import pygame as py
import os as os
import functions as f
import random

py.font.init()
clock = py.time.Clock()

WIDTH = 1200
HEIGHT = 600
FPS = 60
VEL = 6
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
INSTRUCTION_FONT = py.font.SysFont('comicsans', 30)
FEAR_FONT = py.font.SysFont('comicsans', 40)
END_FONT = py.font.SysFont('comicsans', 100)
SCORE_FONT = py.font.SysFont('comicsans', 60)
WHITE = (255, 255, 255)
PURPLE = (62, 12, 94)
PURPLE = (62, 12, 94)





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
    f.openingscreen(WIDTH, HEIGHT, END_FONT, WHITE, INSTRUCTION_FONT, SCREEN, PURPLE)
    
    while run:
        clock.tick(FPS)
        gameclock += 1
        immunetimer -= 1
        boosttimer -= 1
        itemvel = int(gameclock / 300) + 6
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == CHARLIE_HIT:
                charlie_fear += 1
                immunetimer = 60
            if event.type == CHARLIE_BOOST and charlie_fear > 0:
                charlie_fear -= 1
                boosttimer = 60
                ballposition.x = random.randint(3500, 5000)
        keys_pressed = py.key.get_pressed()
        f.player_movement(keys_pressed, playerposition, VEL)
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
        f.object_movement(200, gameclock, coneposition, itemvel)
        f.object_movement(350, gameclock, blenderposition, itemvel)
        f.object_movement(450, gameclock, ballposition, itemvel)
        f.object_movement(1111, gameclock, pigposition, itemvel)
   
        f.collision(playerposition, coneposition, blenderposition, pigposition, ballposition, immunetimer, boosttimer, CHARLIE_HIT, CHARLIE_BOOST)
        if charlie_fear == 5:
            f.gameover(gameclock, END_FONT, WHITE, SCORE_FONT, SCREEN, WIDTH, HEIGHT)
            main()
        scroll = f.draw_background(playerposition, SCREEN, WIDTH, BG, scroll)        
        f.draw_gamewindow(playerposition, coneposition, blenderposition, ballposition, pigposition, charlie_fear, SCREEN, CONE, BLENDER,BALL,PIG,FEAR_FONT, PLAYER,PURPLE)
        py.display.update()
    if run == False:
            py.quit()

main()