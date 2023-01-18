import pygame as py
import os as os
import datetime
import random

py.font.init()




def draw_background(playerposition, SCREEN, WIDTH, BG,scroll):
    """This function handles the scrolling by iterating through a range and blitting the background in sequence"""
    for i in range(0,2):
        if playerposition.x > 350:
            SCREEN.blit(BG, (i * WIDTH + scroll,0))
            scroll -= 3 #This controls the speed of the background
            if abs(scroll) > WIDTH:
                scroll = 0
        if playerposition.x <= 350:
            SCREEN.blit(BG, (i * WIDTH + scroll,0))
    return scroll    #scroll must be returned and assigned again in the main function    
    
def draw_gamewindow(playerposition, coneposition, blenderposition, ballposition, pigposition, charlie_fear, SCREEN, CONE, BLENDER,BALL,PIG,FEAR_FONT, PLAYER,PURPLE):
    """This function draws all the objects and text that is displayed during the game."""
    SCREEN.blit(CONE, (coneposition.x, coneposition.y))
    SCREEN.blit(BLENDER, (blenderposition.x, blenderposition.y))
    SCREEN.blit(BALL, (ballposition.x ,ballposition.y))
    SCREEN.blit(PIG, (pigposition.x, pigposition.y))
    charlie_fear_text = FEAR_FONT.render("Charlie's Fear level: " + str(charlie_fear) + "                 She gets Scared at 5!", 1, PURPLE )
    SCREEN.blit(charlie_fear_text, (10, 10))
    SCREEN.blit(PLAYER, (playerposition.x, playerposition.y))
    

def player_movement(keys_pressed, playerposition, VEL):
    """This handles the left and right movement of the player"""
    if keys_pressed[py.K_LEFT] and playerposition.x > 0: 
        playerposition.x -= VEL
    if keys_pressed[py.K_RIGHT] and playerposition.x < 1100: 
            playerposition.x += VEL + 1


def object_movement(timestart, gameclock, objectposition, itemvel, randomint1, randomint2):
    """This is the function that will control all the objects in the game"""
    if gameclock > timestart: #The object spawns at a time 
        objectposition.x -= itemvel
        if objectposition.x < -500:
            objectposition.x = random.randint(randomint1, randomint2)    # when the object goes past -500 it respawns at a random number, to keep it interesting
            return objectposition
        return objectposition

def collision(playerposition, coneposition, blenderposition, pigposition, ballposition, immunetimer, boosttimer, CHARLIE_HIT, CHARLIE_BOOST):
    """This function handles the collision of the player and various objects, the bad one post the event Charlie_hit and good ones CHarlie_boost
    There is a timer in place so you cant get hit for 1 second if you are already hit, by checking for the immunetimer and boosttimer variable"""
    if playerposition.colliderect(coneposition) and immunetimer < 0:
        py.event.post(py.event.Event(CHARLIE_HIT))
    if playerposition.colliderect(blenderposition) and immunetimer < 0:
        py.event.post(py.event.Event(CHARLIE_HIT))
    if playerposition.colliderect(pigposition) and immunetimer < 0:
        py.event.post(py.event.Event(CHARLIE_HIT))
    if playerposition.colliderect(ballposition) and boosttimer < 0:
        py.event.post(py.event.Event(CHARLIE_BOOST))
      
def gameover(gameclock, END_FONT, WHITE, SCORE_FONT, SCREEN, WIDTH, HEIGHT):
    """This runs like a mini version of the game, displaying the player score and breaks with a spacebar to call the main function."""
    game_over_text = END_FONT.render("GAME OVER", 1, WHITE)
    score_text = SCORE_FONT.render("You scored " + str(gameclock//60), 1, WHITE)
    return_text = SCORE_FONT.render("Press Space to return try again!!", 1, WHITE)
    clock = py.time.Clock()
    time = datetime.datetime.now()
    run = True
    with open("scores.txt", "a") as f: #This writes to a text doc the score and the time
                f.write("\nThe score by player is " + str(gameclock//60) + " at " + str(time))
    while run:
        clock.tick(30)

        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()  #This prevents a traceback when the program closes
        keys_pressed = py.key.get_pressed()
        if keys_pressed[py.K_SPACE]:
            run = False
        SCREEN.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2 - game_over_text.get_height()/2))
        SCREEN.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 400))
        SCREEN.blit(return_text, (WIDTH/2 - return_text.get_width()/2, 500))
        py.display.update()
        
    
def openingscreen(WIDTH, HEIGHT, END_FONT, WHITE, INSTRUCTION_FONT, SCREEN, PURPLE, run):
    """This runs like a mini version of the game, but with a purple screen and instructions on how to play.  
    it breaks out with a space bar."""
    clock = py.time.Clock()
    startscreen = py.Rect(0,0,WIDTH, HEIGHT)
    start_text = END_FONT.render("Charlie's Adventure", 1, WHITE)
    instructions1 = INSTRUCTION_FONT.render("Welcome to Charlie's Adventure.", 1, WHITE)
    instructions2 = INSTRUCTION_FONT.render("Press space to jump, left and right arrow to move.", 1, WHITE)
    instructions3 = INSTRUCTION_FONT.render("Avoid getting Scared, collect tennis balls to relax.", 1, WHITE)
    begin_text = INSTRUCTION_FONT.render("Press Space to start!!!", 1, WHITE)
    
    
    while run:
        clock.tick(30)

        for event in py.event.get():
            if event.type == py.QUIT:
                
                py.quit()
                exit()  #This prevents a traceback when the program closes
                 
        keys_pressed = py.key.get_pressed()
        if keys_pressed[py.K_SPACE]:
            run = False
        py.draw.rect(SCREEN, PURPLE, startscreen)           
        SCREEN.blit(start_text, (WIDTH/2 - start_text.get_width()/2, 50))
        SCREEN.blit(instructions1, (WIDTH/2 - instructions1.get_width()/2, 200))
        SCREEN.blit(instructions2, (WIDTH/2 - instructions2.get_width()/2, 250))
        SCREEN.blit(instructions3, (WIDTH/2 - instructions3.get_width()/2, 300))
        SCREEN.blit(begin_text, (WIDTH/2 - begin_text.get_width()/2, 400))
        py.display.update()
    
        

