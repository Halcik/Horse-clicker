import pyautogui as pg
import random, os, time

def death( r, path_project):
    death = pg.locateOnScreen(os.path.join(path_project, 'Image', 'death.JPG'), confidence=0.9)

    if death:
        left, top, right, down = death[0], death[1], death[0]+death[2], death[1]+death[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
        pg.hotkey('Alt', 'left')
        pg.click()

def h_birth( r, j, path_project):
    if j==0:
        birth_check = pg.locateOnScreen(os.path.join(path_project, 'Image', 'birth_check.JPG'), confidence=0.8)
        if birth_check:
            left, top, right, down = birth_check[0], birth_check[1], birth_check[0]+birth_check[2], birth_check[1]+birth_check[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(3)
            name = pg.locateOnScreen(os.path.join(path_project, 'Image', 'name.JPG'), confidence=0.8)
            left, top, right, down = name[0], name[1], name[0]+name[2], name[1]+name[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            pg.press('P')
            pg.press('D')
            birth_accept = pg.locateOnScreen(os.path.join(path_project, 'Image', 'b_accept.JPG'), confidence=0.8)
            left, top, right, down = birth_accept[0], birth_accept[1], birth_accept[0]+birth_accept[2], birth_accept[1]+birth_accept[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(3.5)
            pg.hotkey('Alt', 'left')
            pg.hotkey('Alt', 'left')
            time.sleep(2)
        elif j==1: #do zrobienia another time
            pass