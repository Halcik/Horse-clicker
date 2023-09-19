# -*- coding: utf-8 -*-
import pyautogui as pg
import time
import os

def h_next( r, path_project):
    n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow.jpg'), confidence=0.9)
    
    if n_horse:
        pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
        pg.click()
    
    else:
        n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow2.JPG'), confidence=0.9)
        if n_horse:
            pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
            pg.click()
        else:
            n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow4.JPG'), confidence=0.9)
            if n_horse:
                pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                pg.click()
            else:
                n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow3.JPG'), confidence=0.9)
                if n_horse:
                    pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                    pg.click()
                else:
                    n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow5.JPG'), confidence=0.9)
                    if n_horse:
                        pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                        pg.click()
                    else:
                        n_horse = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Arrow6.JPG'), confidence=0.9)
                        if n_horse:
                            pg.moveTo(n_horse.x, n_horse.y, r, pg.easeOutQuad)
                            pg.click()
                        else:
                            print("Wystąpił błąd z przechodzeniem do następnego konia")
                            pg.press('f5')
                            time.sleep(1.5)
                            pg.click()
