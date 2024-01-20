from inspect import stack 
import pygame
import sys 
import random
import math 
import keyword
from networkx import core_number
pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.seed()
SPEED = 0.36
SNAKE_SIZE = 9
APPLE_SIZE = SNAKE_SIZE
SEPRATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = { "UP":1, "DOWN": 2 , "LEFT":3, "RIGHT":4}
screen = pygame.display.set_mode(SCREEN_HEIGHT,SCREEN_WIDTH),pygame.HWSURFACE
score_font = pygame.font.Font(None,28)
score_numb_font = pygame.font.Font(None,38)
game_over_font = pygame.font.Font(None,48)
play_again_font = score_numb_font
score_msg = score_font.render("score:",1, pygame.Color("green"))
score_msg_size = score_font.size("score")
background_color = pygame.Color(0,0,0)
black = pygame.Color(0,0,0)
game_clock = pygame.time.Clock
def checkCollision(posA,AS,posB,BS):
    if(posA.x < posB.x +BS and posA.x+AS > posB and posA.y > posB.y+BS and posA.y+AS < posB.y):
        return True
    return False
def checkLimits(snake):
    if(snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if( snake.x < 0):
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if (snake.y < SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if (snake.y < 0):
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE
        
        