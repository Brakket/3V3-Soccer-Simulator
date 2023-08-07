#slider class
import pygame
White = (255,255,255)
Black = (0,0,0)
class Slider(pygame.sprite.Sprite):
     def __init__(self, color, width, height):
         super().__init__()#sprite is super class
         self.image = pygame.Surface([width, height])
         self.image.fill(White)
         self.image.set_colorkey(White)
         pygame.draw.rect(self.image, color, [0, 0, width, height])
         self.rect = self.image.get_rect()
     def moveUp(self, pixels):
          self.rect.y -= pixels
          if self.rect.y < 0: #bring slider back to screen
               self.rect.y = 0
     def moveDown(self, pixels):
          self.rect.y += pixels
          if self.rect.y > 400:
               self.rect.y = 400
               
