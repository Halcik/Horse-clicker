import pyautogui as pg
from sample.helpful_things import *

#Karmienie
def h_feed( r, v, path_project):
    feeding = locate_image('Feed.JPG', path_project, r)
    if feeding:
        for i in range(10):
            fed = locate_image('fed.JPG', path_project, r)
            feed_it = locate_image('Feeding.JPG')
            if fed and feed_it:
                break
            pg.sleep(0.3)
            feeding = locate_image('Feed.JPG', path_project, r)
    else:
        care = locate_image('Care.JPG', path_project, r)
    
    # if v != 1 and care == None and feeding:
    #     pass

#Oporządzenie
def h_groom( r, path_project):
    groom = locate_image('Groom.JPG', path_project, r)
    if not groom:
        groom2 = locate_image('Groom2.JPG', path_project, r)

# Polozenie spac
def h_sleep( r, path_project):
    sleep_horse = locate_image('Sleep.JPG', path_project, r)

# Przejście do następnego konia
def h_next( r, path_project):
    n_horse_tab = ['Arrow.jpg', 'Arrow2.JPG', 'Arrow4.JPG', 'Arrow3.JPG', 'Arrow5.JPG', 'Arrow6.JPG']

    for img in n_horse_tab:
        n_horse = locate_image_center(img, path_project, r)
        if n_horse:
            break
    if not n_horse:        
        print("Wystąpił błąd z przechodzeniem do następnego konia")
        pg.press('f5')
        pg.sleep(1.5)
        pg.click()