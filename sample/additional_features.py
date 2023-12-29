import pyautogui as pg
import os
import webbrowser
try: #bo z tego pliku testuję, to potrzebuję albo to, albo to
    from sample.helpful_things import *
except:
    from helpful_things import *

#rejestracja do ojka
def h_registration(r, path_project): # do naprawy też
    registration = locate_image_center('Registration.jpg', path_project, r, 0.9)

    if registration:
        pg.sleep(3.0)
        reserved = locate_image_center('Reserved.jpg', path_project, r, 0.8)

        if reserved:
            pg.sleep(1)
            box = locate_image_center('Box.jpg', path_project, r, 0.8, False)
            pg.sleep(3)
        else:
            r_days = locate_image_center('Days.JPG', path_project, r)
            if r_days:
                pg.sleep(3)
                r_price = locate_image_center('Price.JPG', path_project, r)

        pd = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'PD.JPG'), confidence=0.9)
        if pd == None:
            print("Wystąpił błąd rejestrowania")
            pg.press('f5')
            pg.sleep(2.0)
            h_registration( r, path_project)

        

    #Pierwsza zapisana opcja rejestracji i nocleg za 1200 tylko łapie 
        # fav_reg = locate_image_center('favreg.jpg', path_project, r, 0.8)
        # pg.move(0,20)
        # pg.click()
        # pg.sleep(1.5)
        # r_price = locate_image_center('Price.JPG', path_project, r, 0.9, False)
        # pg.sleep(2)


#anuluj ojek
def cancel_reg(r, path_project):
    pg.sleep(1.5)
    cancel = locate_image_center('cancel.JPG', path_project, r, 0.85)
    if cancel:
        pg.press('enter')


def h_multiplication( r, path_project):
    reproduce_check = locate_image('mating_mares.JPG', path_project, r, 0.8)
    if reproduce_check:
        pg.sleep(3)
        repro_img_tab = ['price_repro.JPG', 'select_horse.JPG', 'mating.JPG']
        for img in repro_img_tab:
            for i in range(10):
                repro_check = locate_image(img, path_project, r, 0.8)
                if repro_check:
                    pg.sleep(1.5)
                    break



def account_quiting( r, path_project, quit_game):
    pg.sleep(2)
    if "w" in quit_game: #wyjście ze współki
        share_account = locate_image('account_share.JPG', path_project, r, 0.9)
        if share_account:
            exit_share = locate_image('exit_share.JPG', path_project, r, 0.9)

    if "k" in quit_game: #wyjście z własnego konta
        pg.sleep(2)
        account = locate_image('account.JPG', path_project, r, 0.9)

        if account:
            turn_share = locate_image('turn_share.JPG', path_project, r, 0.9)
            if turn_share:
                pg.sleep(1)
                agree = locate_image('agree.JPG', path_project, r, 0.9)

def notification(url):
    webbrowser.register('msedge', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
    browser = webbrowser.get("msedge")
    browser.open(url)
    pg.sleep(20)
    pg.write("Zrobione [sitter]")
    pg.press('enter')


#temporary tests
# h_registration(0.3, "D:\Projekty\Horse-clicker")
# cancel_reg(0.3, "D:\Projekty\Horse-clicker")
# account_quiting(0.3, "D:\Projekty\Horse-clicker", "wk")