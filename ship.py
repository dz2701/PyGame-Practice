import pygame as pg
class Ship():
     def __init__(self,settings,screen):
         self.screen = screen
         self.shipset = settings
         self.image = pg.image.load('images/ship.bmp')
         self.rect = self.image.get_rect()
         self.screen_rect = screen.get_rect()
         self.rect.centerx = self.screen_rect.centerx
         self.rect.bottom = self.screen_rect.bottom
         self.moving_right, self.moving_left = False, False
         self.center = float(self.rect.centerx)
         self.shoot = False

     def blitme(self):
        self.screen.blit(self.image, self.rect)

     def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.shipset.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.shipset.ship_speed
        self.rect.centerx = int(self.center)



     def modmove(self,n):
        self.shipset.ship_speed = n
