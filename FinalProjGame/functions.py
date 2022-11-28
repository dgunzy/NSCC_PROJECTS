import pygame as py
import os as os
import datetime
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

FEAR_FONT = py.font.SysFont('comicsans', 40)
INSTRUCTION_FONT = py.font.SysFont('comicsans', 30)
END_FONT = py.font.SysFont('comicsans', 100)
SCORE_FONT = py.font.SysFont('comicsans', 60)
WHITE = (255, 255, 255)
PURPLE = (62, 12, 94)
scroll = 0
PURPLE = (62, 12, 94)




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
            objectposition.x = random.randint(1300, 2400)
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
    
def openingscreen():
    clock = py.time.Clock()
    startscreen = py.Rect(0,0,WIDTH, HEIGHT)
    start_text = END_FONT.render("Charlie's Adventure", 1, WHITE)
    instructions1 = INSTRUCTION_FONT.render("Welcome to Charlie's Adventure.", 1, WHITE)
    instructions2 = INSTRUCTION_FONT.render("Press space to jump, left and right arrow to move.", 1, WHITE)
    instructions3 = INSTRUCTION_FONT.render("Avoid getting Scared, collect tennis balls to relax.", 1, WHITE)
    begin_text = INSTRUCTION_FONT.render("Press Space to start!!!", 1, WHITE)
    run = True 
    while run:
        clock.tick(30)
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
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

