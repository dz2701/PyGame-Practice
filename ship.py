import pygame as pg
class Ship():
     def __init__(self,screen):
         self.screen = screen
         self.image = pg.image.load('images/ship.bmp')
         self.rect = self.image.get_rect()
         self.screen_rect = screen.get_rect()

         self.rect.centerx = self.screen_rect.centerx
         self.rect.bottom = self.screen_rect.bottom
         self.moving_right = False
         self.moveunit = 10

     def blitme(self):
        self.screen.blit(self.image, self.rect)

     def update(self):
        if self.moving_right:
            self.rect.centerx += self.moveunit

     def modmove(self,n):
        self.moveunit = n
