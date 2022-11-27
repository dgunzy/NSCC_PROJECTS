import pygame as py
import os as os
playerposition = py.Rect(200, 450, 100, 90)
coneposition = py.Rect(1400, 450, 150, 75)
blenderposition = py.Rect(1400, 420, 150, 75)
ballposition = py.Rect(1400,200, 60,60)
pigposition = py.Rect(3000, 450, 200, 128)
charlie_fear = 0

jump = True
jumpcount = 13
scrollstartx = 0
scroll = 0
move = 1200
gameclock = 0
itemvel = 4
immunetimer = 60
boosttimer = 0
run = True
WIDTH = 1200
HEIGHT = 600
FPS = 60
VEL = 5
SCREEN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Charlie's Adventure")
BG = py.image.load(os.path.join('assets',"background.png")).convert()

def control_object(itemvel, timestart, objectposition, object):
    if gameclock >= timestart:
        objectposition.x -= itemvel
        screen.blit(object, (objectposition.x, objectposition.y))
        if objectposition.x <= -2000:
            objectposition.x = 1400
def gameover():
    game_over_text = END_FONT.render("GAME OVER", 1, WHITE)
    score_text = SCORE_FONT.render("You scored " + str(gameclock//60), 1, WHITE)
    screen.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2 - game_over_text.get_height()/2))
    screen.blit(score_text, (WIDTH/2 - score_text.get_width()/2, 400))
    py.display.update()
    with open("scores.txt", "a") as f:
                f.write("The score by player is " + str(gameclock//60))
    py.time.delay(5000)

def draw_gamewindow():
    SCREEN.blit(BG, (0,0))
    py.display.update()