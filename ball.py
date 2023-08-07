import pygame
from random import randint

from screen import Green
Black = (0,0,0)
White = (255,255,255)

class Ball(pygame.sprite.Sprite):
    def __init__(self,color,width, height):
        super().__init__()

        self.image = pygame.Surface([width, height],pygame.SRCALPHA)
        self.image.fill(Green)
        self.image.set_colorkey(Green)

        pygame.draw.circle(self.image, Black,(int(width/2),int(height/2)),8,0)
        self.velocity = [6,0]
        self.rect = self.image.get_rect()
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)
    def hSpeed(self):
        self.velocity[0] = 12
    def slSpeed(self):
        self.velocity[0] = 3
    def regular(self):
        self.velocity = [6,0]        
