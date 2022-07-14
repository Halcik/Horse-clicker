# -*- coding: utf-8 -*-
import pyautogui as pg
import time

def h_next( r):
    n_horse = pg.locateCenterOnScreen('Image\Arrow.jpg', confidence=0.9)
    n_horse2 = pg.locateCenterOnScreen('Image\Arrow2.jpg', confidence=0.9)
    n_horse3 = pg.locateCenterOnScreen('Image\Arrow3.jpg', confidence=0.9)

    if n_horse:
        pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
        pg.click()

    elif n_horse2:
        pg.moveTo(n_horse2.x, n_horse2.y, r, pg.easeOutQuad)
        pg.click()

    elif n_horse3:
        pg.moveTo(n_horse3.x, n_horse3.y, r, pg.easeOutQuad)
        pg.click()

    else:
        print("Wystąpił błąd z przechodzeniem do następnego konia")
        pg.press('f5')
        time.sleep(1.5)
        pg.click()
