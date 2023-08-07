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

class Player(pygame.sprite.Sprite):
     def __init__(self, color, posx, posy):
         width = 40
         height = 40
         super().__init__()#sprite is super class
         self.image = pygame.Surface([width, height],pygame.SRCALPHA)
         self.image.fill(color)
         self.image.set_colorkey(color)
         pygame.draw.rect(self.image, color, [0, 0, width, height])
         self.rect = self.image.get_rect()
         self.rect.x = posx
         self.rect.y = posy
         self.velx = 0 #x and y coordinates to use in vector of velocity
         self.vely = 0
         self.velocity = [self.velx,self.vely]
         self.posx = posx
         self.posy = posy
     def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
     def reset(self):
        self.rect.x = self.posx
        self.rect.y = self.posy
        self.velocity = [0,0]        
     def moveUp(self, pixels):
          self.rect.y -= pixels
          if self.rect.y < 0:#bring slider back to screen
               self.rect.y = 0
     def moveDown(self, pixels):
          self.rect.y += pixels
          if self.rect.y > 400:
               self.rect.y = 400
     def moveLeft(self, pixels):
          self.rect.x -= pixels
          if self.rect.x < 0:
               self.rect.x = 0
     def moveRight(self, pixels):
          self.rect.x += pixels
          if self.rect.x > 400:
               self.rect.x = 400
     def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-3,3)
        

