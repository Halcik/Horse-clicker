# -*- coding: utf-8 -*-
import pyautogui as pg
import random
import os

#Oporządzenie
def h_groom( r, path_project):
    groom = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Groom.JPG'), confidence=0.9)
    groom2 = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Groom2.JPG'), confidence=0.9)

    if groom:
        left, top, right, down = groom[0], groom[1], groom[0]+groom[2], groom[1]+groom[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
    elif groom2:
        left, top, right, down = groom2[0], groom2[1], groom2[0]+groom2[2], groom2[1]+groom2[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()


# Polozenie spac
def h_sleep( r, path_project):
    sleep_horse = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Sleep.JPG'), confidence=0.8)

    if sleep_horse:
        left, top, right, down = sleep_horse[0], sleep_horse[1], sleep_horse[0]+sleep_horse[2], sleep_horse[1]+sleep_horse[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()