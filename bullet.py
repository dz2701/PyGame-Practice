import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,set,scr,ship):
        super().__init__()
        self.scr = scr

        self.rect = pygame.Rect(0,0,set.bullet_width, set.bullet_height)
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx
        self.y = float(self.rect.y)

        self.color = set.bullet_color
        self.speed_factor = set.bullet_speed_factor

    def update(self):
            self.y -= self.speed_factor
            self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.scr,self.color,self.rect)
