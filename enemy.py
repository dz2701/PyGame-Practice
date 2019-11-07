#file containing information about the enemy

import pygame
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self,set,scr):
        super().__init__()
        self.scr = scr
        self.set = set

        #this loads images
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #coordination of location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.centerx = 200

    def blitme(self):
        self.scr.blit(self.image,self.rect)
