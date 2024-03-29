# not yet in use
import pyautogui as pg
import os, random

def locate_image_center(image, path_project, r, conf_v, gray_sc=True):
    image_find = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', image), confidence=conf_v, grayscale=gray_sc)
    if image_find:
        pg.moveTo(image_find.x, image_find.y, r, pg.easeOutQuad)
        pg.click()
        return 1
    else:
        return 0
        

def locate_image(image, path_project, r, conf_v, gray_sc=True):
    image_find = pg.locateOnScreen(os.path.join(path_project, 'Image', image), confidence=conf_v, grayscale=gray_sc)
    if image_find:
        left, top, right, down = image_find[0], image_find[1], image_find[0]+image_find[2], image_find[1]+image_find[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
        return 1
    else:
        return 0
        