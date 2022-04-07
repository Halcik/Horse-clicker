# -*- coding: utf-8 -*-
import pyautogui as pg

def death( r):
    death = pg.locateCenterOnScreen('Image\death.jpg', confidence=0.9)

    if(death != None):
        pg.moveTo(death.x, death.y, r, pg.easeOutQuad)
        pg.click()
        h_arrow = pg.locateCenterOnScreen('Image\Arrowb.jpg', confidence=0.9)
        pg.moveTo(h_arrow.x, h_arrow.y, r, pg.easeOutQuad)
        pg.click()