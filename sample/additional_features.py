import pyautogui as pg
import time, os, random

#rejestracja do ojka
def h_registration(r, path_project): # do naprawy też
    registration = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Registration.jpg'), confidence=0.9)
    #registration = pg.locateOnScreen('Image/Registration.jpg', confidence=0.9)

    if registration:
        #left, top, right, down = registration[0], registration[1], registration[0]+registration[2], registration[1]+registration[3]
        pg.moveTo(registration.x, registration.y, r, pg.easeOutQuad)
        pg.click()
        time.sleep(3.0)
        reserved = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Reserved.jpg'), confidence=0.8)

        if reserved:
            pg.moveTo(reserved.x, reserved.y, r, pg.easeOutQuad)
            pg.click()
            box = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Box.jpg'), confidence=0.8, grayscale=False)
            pg.moveTo(box.x, box.y, r, pg.easeOutQuad)
            pg.click()
            time.sleep(3)
            pd = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'PD.JPG'), confidence=0.9)

            if pd == None:
                print("Wystąpił błąd rejestrowania")
                pg.press('f5')
                time.sleep(2.0)
                h_registration( r, path_project)
        else:
            r_days = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Days.JPG'), confidence=0.9)

            if r_days:
                pg.moveTo(r_days.x, r_days.y, r, pg.easeOutQuad)
                pg.click()
                time.sleep(3)
                r_price = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Price.JPG'), confidence=0.9, grayscale=False)
                pg.moveTo(r_price.x, r_price.y, r, pg.easeOutQuad)
                pg.click()

    #Pierwsza zapisana opcja rejestracji i nocleg za 1200 tylko łapie 
        # fav_reg = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'favreg.jpg'), confidence=0.8)
        # pg.moveTo(fav_reg.x, fav_reg.y, r, pg.easeOutQuad)
        # pg.click()
        # pg.move(0,20)
        # pg.click()
        # time.sleep(1.5)
        # r_price = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'Price.JPG'), confidence=0.9, grayscale=False)
        # pg.moveTo(r_price.x, r_price.y, r, pg.easeOutQuad)
        # pg.click()
        # time.sleep(2)
        # pd = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'PD.JPG'), confidence=0.9)
        # if pd == None:
        #     print("Wystąpił błąd rejestrowania")
        #     pg.press('f5')
        #     time.sleep(2.0)
        #     h_registration2( r)

#anuluj ojek
def cancel_reg(r, path_project):
    time.sleep(1.5)
    cancel= pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'cancel.JPG'), confidence=0.85)
    if cancel:
        pg.moveTo(cancel.x, cancel.y, r, pg.easeOutQuad)
        pg.click()
        pg.press('enter')


def h_multiplication( r, path_project):
    reproduce_check = pg.locateOnScreen(os.path.join(path_project, 'Image', 'mating_mares.JPG'), confidence=0.8)
    if reproduce_check:
       left, top, right, down = reproduce_check[0], reproduce_check[1], reproduce_check[0]+reproduce_check[2], reproduce_check[1]+reproduce_check[3]
       pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
       pg.click()
       time.sleep(3)
       price_repro = pg.locateOnScreen(os.path.join(path_project, 'Image', 'price_repro.JPG'), confidence=0.8)
       while price_repro == None:
           price_repro = pg.locateOnScreen(os.path.join(path_project, 'Image', 'price_repro.JPG'), confidence=0.8)
       if price_repro:
            left, top, right, down = price_repro[0], price_repro[1], price_repro[0]+price_repro[2], price_repro[1]+price_repro[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(1)

            select_horse = pg.locateOnScreen(os.path.join(path_project, 'Image', 'select_horse.JPG'), confidence=0.8)
            while select_horse == None:
                select_horse = pg.locateOnScreen(os.path.join(path_project, 'Image', 'select_horse.JPG'), confidence=0.8)
            left, top, right, down = select_horse[0], select_horse[1], select_horse[0]+select_horse[2], select_horse[1]+select_horse[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            time.sleep(2)

            mating = pg.locateOnScreen(os.path.join(path_project, 'Image', 'mating.JPG'), confidence=0.8)
            while mating == None:
                mating = pg.locateOnScreen(os.path.join(path_project, 'Image', 'mating.JPG'), confidence=0.8)
            left, top, right, down = mating[0], mating[1], mating[0]+mating[2], mating[1]+mating[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()


def account_quiting( r, path_project, quit_game): #this is temporary location for this function-  I must change place for every functions
    time.sleep(2)
    if "w" in quit_game: #wyjście ze współki
        share_account = pg.locateOnScreen(os.path.join(path_project, 'Image', 'account_share.JPG'), confidence=0.9)
        if share_account:
            left, top, right, down = share_account[0], share_account[1], share_account[0]+share_account[2], share_account[1]+share_account[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            exit_share = pg.locateOnScreen(os.path.join(path_project, 'Image', 'exit_share.JPG'), confidence=0.9)
            if exit_share:
                left, top, right, down = exit_share[0], exit_share[1], exit_share[0]+exit_share[2], exit_share[1]+exit_share[3]
                pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
                pg.click()

    if "k" in quit_game: #wyjście z własnego konta
        time.sleep(2)
        account = pg.locateOnScreen(os.path.join(path_project, 'Image', 'account.JPG'), confidence=0.9)
        if account:
            left, top, right, down = account[0], account[1], account[0]+account[2], account[1]+account[3]
            pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
            pg.click()
            turn_share = pg.locateOnScreen(os.path.join(path_project, 'Image', 'turn_share.JPG'), confidence=0.9)
            if turn_share:
                left, top, right, down = turn_share[0], turn_share[1], turn_share[0]+turn_share[2], turn_share[1]+turn_share[3]
                pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
                pg.click()
                time.sleep(1)
                agree = pg.locateOnScreen(os.path.join(path_project, 'Image', 'agree.JPG'), confidence=0.9)
                if agree:
                    left, top, right, down = agree[0], agree[1], agree[0]+agree[2], agree[1]+agree[3]
                    pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
                    pg.click()