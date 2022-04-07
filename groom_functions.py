# -*- coding: utf-8 -*-
import pyautogui as pg

#Oporządzenie
def h_groom( r):
    groom = pg.locateCenterOnScreen('Image\Groom.jpg', confidence=0.9)

    if(groom != None):
        pg.moveTo(groom.x, groom.y, r, pg.easeOutQuad)
        pg.click()


# Polozenie spac
def h_sleep( r):
    sleep_horse = pg.locateCenterOnScreen('Image\Sleep.jpg', confidence=0.8)

    if(sleep_horse != None):
        pg.moveTo(sleep_horse.x, sleep_horse.y, r, pg.easeOutQuad)
        pg.click()