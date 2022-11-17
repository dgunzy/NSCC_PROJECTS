#!/usr/bin/python3


import pygame
import os

import gamefunctions as gf
pygame.font.init()
pygame.mixer.init()
#### variables ###
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

FPS = 60
VEL = 5
BULLET_VEL = 14
MAX_BULLETS = 5
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space.png')), (900,500))
SPACESHIPWIDTH = 55
SPACESHIPHEIGHT = 40
BORDER = pygame.Rect(445,0,10,HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("Assets", "Gun+Silencer.mp3"))

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIPWIDTH,SPACESHIPHEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIPWIDTH,SPACESHIPHEIGHT)), 270)
######end variables ####

def main():
    yellow = pygame.Rect(100,300, SPACESHIPWIDTH, SPACESHIPHEIGHT)
    red = pygame.Rect(700,300, SPACESHIPWIDTH, SPACESHIPHEIGHT)
     
    red_bullets = []
    yellow_bullets = []
    red_health = 10
    yellow_health = 10
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
                # pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RALT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <=0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            gf.draw_winner(winner_text)
            break

       
        keys_pressed = pygame.key.get_pressed()
        
        gf.yellow_handle_movement(keys_pressed, yellow)
        gf.red_handle_movement(keys_pressed, red)
            ##redtime
        
        gf.handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        gf.draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    if run == False:
        pygame.quit()
    else:
        main()

if __name__ == "__main__":
    main()




