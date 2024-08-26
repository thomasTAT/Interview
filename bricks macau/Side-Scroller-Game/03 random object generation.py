import pygame
from pygame.locals import *
import os
import sys
import math
import random

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

class saw(object):
    rotate = [pygame.image.load(os.path.join('images', 'SAW0.PNG')),pygame.image.load(os.path.join('images', 'SAW1.PNG')),pygame.image.load(os.path.join('images', 'SAW2.PNG')),pygame.image.load(os.path.join('images', 'SAW3.PNG'))]
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)  # Defines the accurate hitbox for our character 
        
        if self.rotateCount >= 8:  
            self.rotateCount = 0


        win.blit(pygame.transform.scale(self.rotate[self.rotateCount//2], (64,64)),(self.x,self.y)) # scales our image down to 64x64 before drawing
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        self.rotateCount += 1


class spike(saw):  # We are inheriting from saw

    def __init__(self,x,y,width,height):
        super().__init__(x,y,width,height)

    img = pygame.image.load(os.path.join('images', 'spike.png'))

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y, 28,315)  # defines the hitbox
        win.blit(self.img, (self.x,self.y))
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    

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
            
            
            if self.jumpCount > 108:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
                
            self.y -= self.jumpList[self.jumpCount] * 1.2
            win.blit(self.jump[self.jumpCount//16], (self.x,self.y))
            self.jumpCount += 1


        
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
            
        else:
            if self.runCount > 42:
                self.runCount = 0

            win.blit(self.run[self.runCount//6], (self.x,self.y))
            self.runCount += 1
        


def redrawWindow():
    win.blit(bg, (bgX, 0))  # draws our first bg image
    win.blit(bg, (bgX2, 0))  # draws the seconf bg image'
    runner.draw(win)

    # spikee.draw(win)
    # saww.draw(win)

    for obstacle in obstacles:
        obstacle.draw(win)

    pygame.display.update()  # updates the screen

run = True
speed = 60  # NEW

# 每隔 0.5 秒触发 一个叫做 USEREVENT+1 的事件
pygame.time.set_timer(USEREVENT+1, 500) 
pygame.time.set_timer(USEREVENT+2, random.randrange(4000, 5000)) # Will trigger every 2 - 3.5 seconds


runner = player(200, 313, 64, 64)

spikee = spike(300,0,48,320)
saww = saw(300,300,64,64)
obstacles =[]

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
    
        if event.type == USEREVENT+2:
            r = random.randrange(0,2)
            if r == 0:
                obstacles.append(saw(810, 310, 64, 64))
            elif r == 1:
                obstacles.append(spike(810, 0, 48, 310))


    keys = pygame.key.get_pressed() 

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]: # If user hits space or up arrow key
        if not(runner.jumping):  # If we are not already jumping
            runner.jumping = True

    if keys[pygame.K_DOWN]:  # If user hits down arrow key
        if not(runner.sliding):  # If we are not already sliding
            runner.sliding = True
            

    for obstacle in obstacles: 
        obstacle.x -= 1.4
        if obstacle.x < obstacle.width * -1: # If our obstacle is off the screen we will remove it
            obstacles.pop(obstacles.index(obstacle))

    clock.tick(speed) 
    redrawWindow()