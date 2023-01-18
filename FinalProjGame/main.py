#!/usr/bin/python3
import pygame as py
import os as os
import functions as f
import random


py.font.init()
clock = py.time.Clock()
###These are the variables that set the image and screen sizes, game speed, and title###
WIDTH = 1200
HEIGHT = 600
FPS = 60
VEL = 6
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Charlie's Adventure")
BG = py.image.load(os.path.join('assets',"background.png")).convert()
PLAYER = py.image.load(os.path.join('assets', 'charlie.png'))
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




### This is the main function that runs the program, The variables inside the main function will be modified###
### And therefore need to be assigned in the function###
def main():
    playerposition = py.Rect(200, 380, 100, 90)
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
    f.openingscreen(WIDTH, HEIGHT, END_FONT, WHITE, INSTRUCTION_FONT, SCREEN, PURPLE, run)
    """THe main function runs and calls the necessary game functions in the correct order """
    while run:
        clock.tick(FPS)
        gameclock += 1
        immunetimer -= 1
        boosttimer -= 1
        itemvel = int(gameclock / 300) + 6 #This increases the speed as the game time progresses
        for event in py.event.get(): #This loop handles game events, such as quitting the game or the charlie hit or boost 
            if event.type == py.QUIT:
                run = False
                return
            elif event.type == CHARLIE_HIT:
                charlie_fear += 1
                immunetimer = 60
            elif event.type == CHARLIE_BOOST and charlie_fear > 0:
                charlie_fear -= 1
                boosttimer = 60
                ballposition.x = random.randint(3500, 5000)
        keys_pressed = py.key.get_pressed()
        f.player_movement(keys_pressed, playerposition, VEL)
        if not(jump):   #This handles the jump when the player hits the spacebar 
            if keys_pressed[py.K_SPACE]:
                jump = True

        if jump == True:
            if jumpcount >= -13:
                    playerposition.y -=(jumpcount *abs(jumpcount)) * 0.5
                    jumpcount -= 1
                    
            else:
                    jumpcount = 13
                    jump = False
                    playerposition.y = 380
        f.object_movement(200, gameclock, coneposition, itemvel, 1200, 2200)
        f.object_movement(350, gameclock, blenderposition, itemvel, 1400, 3000)
        f.object_movement(450, gameclock, ballposition, itemvel, 3000,5000)
        f.object_movement(1111, gameclock, pigposition, itemvel, 2000, 5000)
   
        f.collision(playerposition, coneposition, blenderposition, pigposition, ballposition, immunetimer, boosttimer, CHARLIE_HIT, CHARLIE_BOOST)
        
        scroll = f.draw_background(playerposition, SCREEN, WIDTH, BG, scroll) #this reassigns the scroll variable the correct return from the background scrolling function        
        f.draw_gamewindow(playerposition, coneposition, blenderposition, ballposition, pigposition, charlie_fear, SCREEN, CONE, BLENDER,BALL,PIG,FEAR_FONT, PLAYER,PURPLE)
        py.display.update()
        if charlie_fear == 5:  #This ends the game when the fear is 5
            
            f.gameover(gameclock, END_FONT, WHITE, SCORE_FONT, SCREEN, WIDTH, HEIGHT)
            main()
            
    if run == False:  #when the exit is pressed, the run is false and py.quit() is called
            py.quit()

if __name__ == "__main__":
    main()