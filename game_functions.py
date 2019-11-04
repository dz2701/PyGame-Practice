import sys
import pygame as py

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(set, screen, ship):
    screen.fill(set.bg_color)
    ship.blitme()
    pygame.display.flip()
