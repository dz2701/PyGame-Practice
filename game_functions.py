import sys
import pygame
from bullet import Bullet

def check_events(set,scr,ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        elif event.type == pygame.KEYDOWN: check_keydown_events(event,set,scr,ship,bullets)
        elif event.type == pygame.KEYUP: check_keyup_events(event,set,scr,ship,bullets)



def update_screen(set, screen, ship,bullets):
    screen.fill(set.color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    pygame.display.flip()


def check_keydown_events(event,set,scr,ship,bullets):
    if event.key == pygame.K_RIGHT: ship.moving_right = True
    elif event.key == pygame.K_LEFT: ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        newb = Bullet(set,scr,ship)
        bullets.add(newb)


def  check_keyup_events(event,set,scr,ship,bullets):
    if event.key == pygame.K_RIGHT: ship.moving_right = False
    elif event.key == pygame.K_LEFT: ship.moving_left = False
    elif event.key == pygame.K_UP: ship.shoot = False


def update_bullets(bullets,set):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0 or len(bullets.copy()) > set.bullets_allowed:
            bullets.remove(bullet)
