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

class player(object):
    run = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(8,16)]
    jump = [pygame.image.load(os.path.join('images', str(x) + '.png')) for x in range(1,8)]
    slide = [pygame.image.load(os.path.join('images', 'S1.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')),pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S2.png')), pygame.image.load(os.path.join('images', 'S3.png')), pygame.image.load(os.path.join('images', 'S4.png')), pygame.image.load(os.path.join('images', 'S5.png'))]
    jumpList = [1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,-1,-1,-1,-1,-1,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4,-4]
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.slideCount = 0
        self.jumpCount = 0
        self.runCount = 0
        self.slideUp = False

    def draw(self, win):
        if self.jumping:

            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//18], (self.x,self.y))
            self.jumpCount += 1

            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0

        # sliding 和 slide up
        elif self.sliding or self.slideUp:

            if self.slideCount < 20:
                self.y += 1

            # 滑行結束，上升。
            elif self.slideCount == 80:
                self.y -= 19
                self.sliding = False
                self.slideUp = True

            # 動畫，滑行完全結束。
            if self.slideCount >= 110:
                self.slideCount = 0
                self.slideUp = False
                self.runCount = 0

            # 請參考滑行 list
            win.blit(self.slide[self.slideCount//10], (self.x,self.y))
            self.slideCount += 1

        # 普通跑步    
        else:
            if self.runCount > 42:
                self.runCount = 0

            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1

def redrawWindow():
    win.blit(bg, (bgX, 0))  # draws our first bg image
    win.blit(bg, (bgX2, 0))  # draws the seconf bg image
    runner.draw(win)
    pygame.display.update()  # updates the screen

# Call this from the game loop!

run = True
speed = 30  # NEW

# 這段代碼的作用是每隔 0.5 秒觸發一次指定的事件
pygame.time.set_timer(USEREVENT+1, 500) # Sets the timer for 0.5 seconds

runner = player(200, 313, 64, 64)

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
    

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]: # If user hits space or up arrow key
        if not(runner.jumping):  # If we are not already jumping
            runner.jumping = True

    if keys[pygame.K_DOWN]:  # If user hits down arrow key
        if not(runner.sliding):  # If we are not already sliding
            runner.sliding = True

    clock.tick(speed) 
    redrawWindow()

