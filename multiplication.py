 # -*- coding: utf-8 -*-
import pyautogui as pg
import time
import random
 
def h_multiplication( r):
    reproduce_check = pg.locateOnScreen('Image/mating_mares.JPG', confidence=0.8)
    if reproduce_check:
       left, top, right, down = reproduce_check[0], reproduce_check[1], reproduce_check[0]+reproduce_check[2], reproduce_check[1]+reproduce_check[3]
       pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
       pg.click()
       time.sleep(3)
       price_repro = pg.locateOnScreen('Image/price_repro.JPG', confidence=0.8)
       while price_repro == None:
           price_repro = pg.locateOnScreen('Image/price_repro.JPG', confidence=0.8)
       if price_repro:
            left, top, right, down = price_repro[0], price_repro[1], price_repro[0]+price_repro[2], price_repro[1]+price_repro[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(1)

            select_horse = pg.locateOnScreen('Image/select_horse.JPG', confidence=0.8)
            while select_horse == None:
                select_horse = pg.locateOnScreen('Image/select_horse.JPG', confidence=0.8)
            left, top, right, down = select_horse[0], select_horse[1], select_horse[0]+select_horse[2], select_horse[1]+select_horse[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(2)

            mating = pg.locateOnScreen('Image/mating.JPG', confidence=0.8)
            while mating == None:
                mating = pg.locateOnScreen('Image/mating.JPG', confidence=0.8)
            left, top, right, down = mating[0], mating[1], mating[0]+mating[2], mating[1]+mating[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()

def h_birth( r, j):
    if j==0:
        birth_check = pg.locateOnScreen('Image/birth_check.JPG', confidence=0.8)
        if birth_check:
            left, top, right, down = birth_check[0], birth_check[1], birth_check[0]+birth_check[2], birth_check[1]+birth_check[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(3)
            name = pg.locateOnScreen('Image/name.JPG', confidence=0.8)
            left, top, right, down = name[0], name[1], name[0]+name[2], name[1]+name[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            pg.press('P')
            pg.press('D')
            birth_accept = pg.locateOnScreen('Image/b_accept.JPG', confidence=0.8)
            left, top, right, down = birth_accept[0], birth_accept[1], birth_accept[0]+birth_accept[2], birth_accept[1]+birth_accept[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(3.5)
            pg.hotkey('Alt', 'left')
            pg.hotkey('Alt', 'left')
            time.sleep(2)
        elif j==1: #do zrobienia another time
            pass