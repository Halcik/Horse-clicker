# -*- coding: utf-8 -*-
import pyautogui as pg
import random
import os
import time

def death( r, path_project):
    death = pg.locateOnScreen(os.path.join(path_project, 'Image', 'death.JPG'), confidence=0.9)

    if death:
        left, top, right, down = death[0], death[1], death[0]+death[2], death[1]+death[3]
        pg.moveTo(random.uniform(left, right), random.uniform(top, down), r, pg.easeOutQuad)
        pg.click()
        pg.hotkey('Alt', 'left')
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

