# -*- coding: utf-8 -*-
import pyautogui as pg
import random

def death( r):
    death = pg.locateOnScreen('Image/death.JPG', confidence=0.9)

    if death:
        left, top, right, down = death[0], death[1], death[0]+death[2], death[1]+death[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
        pg.hotkey('Alt', 'left')
        pg.click()


