# -*- coding: utf-8 -*-
import pyautogui as pg

def death( r):
    death = pg.locateCenterOnScreen('Image/death.jpg', confidence=0.9)

    if death:
        pg.moveTo(death.x, death.y, r, pg.easeOutQuad)
        pg.click()
        pg.hotkey('Alt', 'left')
        pg.click()


