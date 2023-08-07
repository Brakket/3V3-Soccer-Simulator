from math import sqrt
import pygame
from random import randint

#colors
Black = (0,0,0)
White = (255,255,255)
Red = (122.5,0,0)
Blue = (0,0,122.5)
Green = (0,122.5,0)
Yellow = (122.5,122.5,0)
bbBlue = (0,10,225)
Grey = (200,200,200)
DGrey = (150,150,150)

class Ball(pygame.sprite.Sprite):
    def __init__(self,color,width, height):
        super().__init__()

        self.image = pygame.Surface([width, height],pygame.SRCALPHA)
        self.image.fill(Green)
        self.image.set_colorkey(Green)

        pygame.draw.circle(self.image, Black,(int(width/2),int(height/2)),8,0)
        
        self.velx = 6 #x and y coordinates to use in vector of velocity
        self.vely = 6 
        self.velocity = [self.velx,self.vely]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
    def pause(self):
        self.velocity= [0,0]
    def continuationLeft(self):
        self.velocity = [-self.velx,self.vely]
    def continuationRight(self):
        self.velocity = [self.velx, self.vely]
    def shootRight(self):
        self.velocity = [randint(0,8),randint(-8,8)]
    def shootLeft(self):
        self.velocity = [randint(-8,0),randint(-8,8)]
    def finishRight(self):
        goal = [680,250]
        speedx = (goal[0] - self.rect.x)/sqrt(goal[0]**2 + goal[1]**2)
        speedy = (goal[1] - self.rect.y)/sqrt(goal[0]**2 + goal[1]**2)
        self.velocity = [speedx*randint(0,8),speedy*randint(-8,8)]
    def finishLeft(self):
        goal = [10,250]
        speedx = (goal[0] - self.rect.x)/sqrt(goal[0]**2 + goal[1]**2)
        speedy = (goal[1] - self.rect.y)/sqrt(goal[0]**2 + goal[1]**2)
        self.velocity = [speedx*randint(-8,0),speedy*randint(-8,8)]