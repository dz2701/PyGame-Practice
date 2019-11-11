import sys
import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf
from bullet import Bullet
from enemy import Enemy

from pygame.sprite import Group

def run_game():
    #Initialize enviroment
    pg.init()
    set = Settings()
    #display setting
    scr = pg.display.set_mode((set.screen_w,set.screen_h))
    scr.fill(set.color)
    pg.display.set_caption("Test game")
    #Set ship1
    ship1 = Ship(set,scr)
    #set bullets
    bullets = Group()
    enemy = Group()
    gf.create_fleet(set,scr,ship1,enemy)


    #run game
    while True:
        gf.check_events(set,scr,ship1,bullets)
        ship1.update()
        enemy.update()
        gf.update_bullets(bullets,set)
        gf.update_screen(set,scr,ship1, enemy, bullets)

#execute run game
run_game()
