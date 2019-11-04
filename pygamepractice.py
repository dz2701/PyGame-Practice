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
    scr.fill(set.color)
    pg.display.set_caption("Testing")
    #Run Game
    ship1 = Ship(set,scr)
    ship1.modmove(99)
    ship1.blitme()
    while True:
        gf.check_events(ship1)
        ship1.update()
        gf.update_screen(set,scr,ship1)

        for event in pg.event.get():
            if event.type == pg.QUIT: sys.exit()
        pg.display.flip()

run_game()
