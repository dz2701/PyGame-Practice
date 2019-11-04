import sys
import pygame as pg
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Initialize enviroment
    pg.init()
    set = Settings()
    run = 1
    #display setting
    scr = pg.display.set_mode((set.screen_w,set.screen_h))
    scr.fill([51,153,255])
    pg.display.set_caption("Testing")
    color = (51,153,255)
    #Run Game
    ship1 = Ship(scr)
    while run:
        scr.fill([51,153,255])
        ship1.blitme()
        for event in pg.event.get():
            if event.type == pg.QUIT: run=0
        pg.display.flip()

run_game()
