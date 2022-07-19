# -*- coding: utf-8 -*-
import pyautogui as pg
import time

def h_next( r):
    n_horse = pg.locateCenterOnScreen('Image/Arrow.jpg', confidence=0.9)
    
    if n_horse:
        pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
        pg.click()
    
    else:
        n_horse = pg.locateCenterOnScreen('Image/Arrow2.JPG', confidence=0.9)
        if n_horse:
            pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
            pg.click()
        else:
            n_horse = pg.locateCenterOnScreen('Image/Arrow4.JPG', confidence=0.9)
            if n_horse:
                pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                pg.click()
            else:
                n_horse = pg.locateCenterOnScreen('Image/Arrow3.JPG', confidence=0.9)
                if n_horse:
                    pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                    pg.click()
                else:
                    n_horse = pg.locateCenterOnScreen('Image/Arrow5.JPG', confidence=0.9)
                    if n_horse:
                        pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                        pg.click()
                    else:
                        print("Wystąpił błąd z przechodzeniem do następnego konia")
                        pg.press('f5')
                        time.sleep(1.5)
                        pg.click()
