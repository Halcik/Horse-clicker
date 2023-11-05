import pyautogui as pg
import random, time, os

#Karmienie
def h_feed( r, v, path_project):
    feeding = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Feed.JPG'), confidence=0.9)
    care = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Care.JPG'), confidence=0.9)

    if feeding:
        feeded = pg.locateOnScreen(os.path.join(path_project, 'Image', 'feeded.JPG'), confidence=0.9)
        while feeded is None:
            if feeding:
                left, top, right, down = feeding[0], feeding[1], feeding[0]+feeding[2], feeding[1]+feeding[3]
                pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
                pg.click()
            feed_it = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Feeding.JPG'), confidence=0.8)
            if(feed_it != None):
                left, top, right, down = feed_it[0], feed_it[1], feed_it[0]+feed_it[2], feed_it[1]+feed_it[3]
                pg.moveTo(random.uniform(left+2, right-2), random.uniform(top-2, down+2), r, pg.easeOutQuad)
                pg.click()
            time.sleep(0.3)
            feeding = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Feed.JPG'), confidence=0.9)
            feeded = pg.locateOnScreen(os.path.join(path_project, 'Image', 'feeded.JPG'), confidence=0.9)

    elif care:
        left, top, right, down = care[0], care[1], care[0]+care[2], care[1]+care[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
    
    if v != 1 and care == None and feeding: #tego na razie nie ruszam D: another time - I have to write it again
        pass

#Oporządzenie
def h_groom( r, path_project):
    groom = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Groom.JPG'), confidence=0.9)
    groom2 = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Groom2.JPG'), confidence=0.9)

    if groom:
        left, top, right, down = groom[0], groom[1], groom[0]+groom[2], groom[1]+groom[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
    elif groom2:
        left, top, right, down = groom2[0], groom2[1], groom2[0]+groom2[2], groom2[1]+groom2[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()

# Polozenie spac
def h_sleep( r, path_project):
    sleep_horse = pg.locateOnScreen(os.path.join(path_project, 'Image', 'Sleep.JPG'), confidence=0.8)

    if sleep_horse:
        left, top, right, down = sleep_horse[0], sleep_horse[1], sleep_horse[0]+sleep_horse[2], sleep_horse[1]+sleep_horse[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()

# Przejście do następnego konia
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



class ErrorFeed(Exception):
    pass