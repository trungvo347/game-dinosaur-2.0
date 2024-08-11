import pygame, sys
from pygame.locals import *
import random
from tkinter import messagebox

pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play()


FPS = 60
FramePerSec = pygame.time.Clock()
 
# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
# Screen information
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 350

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), RESIZABLE)
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
bg=pygame.image.load('bg.png')
bg2=pygame.image.load('bg2.png')
DISPLAYSURF.blit(bg,(0,0))
point = 0 
font = pygame.font.Font('Sevillana-Regular.ttf',32  )
diem =font.render(str(point),True,BLACK,WHITE)
diemRect= diem.get_rect()
diemRect.center = (20,20)
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("cactus.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.center=(750,213) 
 
      def move(self):
        self.rect.move_ip(-10,0)
        if (self.rect.left < 0):
            global point
            point += 1
            self.rect.left = 0
            self.rect.center = (750, 213)
      def moveFaster(self, speed):
        self.rect.move_ip(speed,0)
        if (self.rect.left < 0):
            global point
            point += 1
            self.rect.left = 0
            self.rect.center = (750, 213)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("dinosaur.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 222)
 
    def update(self,x,y):
        self.rect.center = (x, y)
       
        
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()
E2 = Enemy()

x = 50
y = 222
yjump = 12
isJumg = False
lever = 1
speed = -10
while True: 
    if lever == 1:
        if point >= 2:
            lever = 2
        if P1.rect.colliderect(E1.rect):
            messagebox.showerror("Game Over", "Your Score: " + str(point))
            pygame.quit()
            sys.exit()  
        for event in pygame.event.get():              
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.blit(bg,(0,0))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE] and isJumg == False:
            isJumg = True
        if isJumg == True:
            y -= yjump
            yjump -= 0.5
            if yjump <-12:
                isJumg = False
                yjump = 12 
        P1.update(x,y)
        E1.move()
        
        
        P1.draw(DISPLAYSURF)
        E1.draw(DISPLAYSURF)
        diem = font.render(str(point),True,GREEN,BLUE)
        DISPLAYSURF.blit(diem,diemRect)
        pygame.display.update()
        FramePerSec.tick(FPS)
    if lever == 2:
        if P1.rect.colliderect(E1.rect):
            messagebox.showerror("Game Over", "Your Score: " + str(point))
            pygame.quit()
            sys.exit()  
        for event in pygame.event.get():              
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        DISPLAYSURF.blit(bg2,(0,0))
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_SPACE] and isJumg == False:
            isJumg = True
        if isJumg == True:
            y -= yjump
            yjump -= 0.5
            if yjump <-12:
                isJumg = False
                yjump = 12 
                
        P1.update(x,y)
        E1.moveFaster(speed)        
        speed = speed - 0.01
        
        print(speed)
        P1.draw(DISPLAYSURF)
        E1.draw(DISPLAYSURF)
        diem = font.render(str(point),True,GREEN,BLUE) 
        DISPLAYSURF.blit(diem,diemRect)
        pygame.display.update()
        FramePerSec.tick(FPS)
    