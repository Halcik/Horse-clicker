import pyautogui as pg
try:
    from sample.helpful_things import *
except:
    from helpful_things import *

#Karmienie
def h_feed( r, v, path_project):
    feeding = locate_image('Feed.JPG', path_project, r, 0.95)
    if feeding:
        for i in range(10):
            fed = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'fed.JPG'), confidence=0.9)
            feed_it = locate_image('Feeding.JPG', path_project, r, 0.8)
            if fed:
                break
            pg.sleep(0.3)
            feeding = locate_image('Feed.JPG', path_project, r, 0.9)
    else:
        care = locate_image('Care.JPG', path_project, r, 0.9)
    
    # if v != 1 and care == None and feeding:
    #     pass

#Oporządzenie
def h_groom( r, path_project):
    groom = locate_image('Groom.JPG', path_project, r, 0.95)
    if not groom:
        groom2 = locate_image('Groom2.JPG', path_project, r, 0.95)

# Polozenie spac
def h_sleep( r, path_project):
    sleep_horse = locate_image('Sleep.JPG', path_project, r, 0.8)

# Przejście do następnego konia
def h_next( r, path_project):
    n_horse_tab = ['Arrow.jpg', 'Arrow2.JPG', 'Arrow4.JPG', 'Arrow3.JPG', 'Arrow5.JPG', 'Arrow6.JPG']

    for img in n_horse_tab:
        n_horse = locate_image_center(img, path_project, r, 0.9)
        if n_horse:
            break
    if not n_horse:        
        print("Wystąpił błąd z przechodzeniem do następnego konia")
        pg.press('f5')
        pg.sleep(1.5)
        pg.click()

#temporary tests
# h_feed(0.3, 1, "D:\Projekty\Horse-clicker")
# h_groom(0.3, "D:\Projekty\Horse-clicker")
# h_sleep(0.3, "D:\Projekty\Horse-clicker")
# h_next(0.3, "D:\Projekty\Horse-clicker")