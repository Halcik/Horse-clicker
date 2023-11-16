import pyautogui as pg
from sample.helpful_things import locate_image

def death( r, path_project):
    death = locate_image("death.JPG", path_project, r)
    if death:
        pg.hotkey('Alt', 'left')
        pg.click()

def h_birth( r, j, path_project):
    if j==0:
        birth_check = locate_image("birth_check.JPG", path_project, r)
        if birth_check:
            pg.sleep(3)
            name = locate_image("name.JPG", path_project, r)
            if name:
                pg.press('P')
                pg.press('D')
                birth_accept = locate_image("b_accept.JPG", path_project, r)
                if birth_accept:
                    pg.sleep(3.5)
                    pg.hotkey('Alt', 'left')
                    pg.hotkey('Alt', 'left')
                    pg.sleep(2)
        elif j==1: #do zrobienia another time
            pass