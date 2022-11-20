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

def h_birth( r, j):
    if j==0:
        birth_check = pg.locateCenterOnScreen('Image/birth_check.JPG', confidence=0.8)
        if birth_check:
            pg.moveTo(birth_check.x, birth_check.y, r, pg.easeOutQuad)
            pg.click()
            time.sleep(3)
            name = pg.locateCenterOnScreen('Image/name.JPG', confidence=0.8)
            pg.moveTo(name.x, name.y, r, pg.easeOutQuad)
            pg.click()
            pg.press('P')
            pg.press('D')
            birth_accept = pg.locateCenterOnScreen('Image/b_accept.JPG', confidence=0.8)
            pg.moveTo(birth_accept.x, birth_accept.y, r, pg.easeOutQuad)
            pg.click()
            time.sleep(3.5)
            pg.hotkey('Alt', 'left')
            pg.hotkey('Alt', 'left')
            time.sleep(2)
        elif j==0:
            pass