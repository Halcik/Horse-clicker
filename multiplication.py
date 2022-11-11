 # -*- coding: utf-8 -*-
import pyautogui as pg
import time
 
def h_multiplication( r):
    reproduce_check = pg.locateCenterOnScreen('Image/mating_mares.JPG', confidence=0.8)
    if reproduce_check:
       pg.moveTo(reproduce_check.x, reproduce_check.y, r, pg.easeOutQuad)
       pg.click()
       time.sleep(3)
       price_repro = pg.locateCenterOnScreen('Image/price_repro.JPG', confidence=0.8)
       if price_repro:
              pg.moveTo(price_repro.x, price_repro.y, r, pg.easeOutQuad)
              pg.click()
              time.sleep(1)

              select_horse = pg.locateCenterOnScreen('Image/select_horse.JPG', confidence=0.8)
              pg.moveTo(select_horse.x, select_horse.y, r, pg.easeOutQuad)
              pg.click()
              time.sleep(2)

              mating = pg.locateCenterOnScreen('Image/mating.JPG', confidence=0.8)
              pg.moveTo(mating.x, mating.y, r, pg.easeOutQuad)
              pg.click()