import pygame
from pygame.locals import *
import os
import sys
import math

pygame.init()

# Window
W, H = 800, 447
win = pygame.display.set_mode((W,H))
pygame.display.set_caption('Side Scroller')

# bground
bg = pygame.image.load(os.path.join('images','bg.png')).convert()
bgX = 0 # 
bgX2 = bg.get_width()

clock = pygame.time.Clock()


def redrawWindow():
    win.blit(bg, (bgX, 0))  # draws our first bg image
    win.blit(bg, (bgX2, 0))  # draws the seconf bg image
    pygame.display.update()  # updates the screen

run = True
speed = 30  # NEW

# 每隔 0.5 秒触发 一个叫做 USEREVENT+1 的事件
pygame.time.set_timer(USEREVENT+1, 500) 


while run:

    # 控制 fps，越高 fps，畫面移動更快。
    clock.tick(speed)  # NEW
    
    bgX -= 1.4  # Move both background images back
    bgX2 -= 1.4

    if bgX < bg.get_width() * -1:  # If our bg is at the -width then reset its position
        bgX = bg.get_width()
    
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            run = False    
            pygame.quit() 
            quit()

            # 每半秒增加一次速度
        if event.type == USEREVENT+1: # Checks if timer goes off
            speed += 1 # Increases speed
    

    clock.tick(speed) 
    redrawWindow()