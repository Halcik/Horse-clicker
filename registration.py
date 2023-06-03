# -*- coding: utf-8 -*-
import pyautogui as pg
import time

def h_registration(r): # do naprawy też
    registration = pg.locateOnScreen('Image/Registration.jpg', confidence=0.9)

    if registration:
        left, top, right, down = registration[0], registration[1], registration[0]+registration[2], registration[1]+registration[3]
        pg.moveTo(registration.x, registration.y, r, pg.easeOutQuad)
        pg.click()
        time.sleep(3.0)
        h_registration2(r)
    

def h_registration2(r): # i to też do naprawy
    reserved = pg.locateCenterOnScreen('Image/Reserved.jpg', confidence=0.8)

    if reserved:
        pg.moveTo(reserved.x, reserved.y, r, pg.easeOutQuad)
        pg.click()
        box = pg.locateCenterOnScreen('Image/Box.jpg', confidence=0.8, grayscale=False)
        pg.moveTo(box.x, box.y, r, pg.easeOutQuad)
        pg.click()
        time.sleep(3)
        pd = pg.locateCenterOnScreen('Image/PD.JPG', confidence=0.9)

        if pd == None:
            print("Wystąpił błąd rejestrowania")
            pg.press('f5')
            time.sleep(2.0)
            h_registration2( r)
    else:
        r_days = pg.locateCenterOnScreen('Image/Days.JPG', confidence=0.9)

        if r_days:
            pg.moveTo(r_days.x, r_days.y, r, pg.easeOutQuad)
            pg.click()
            time.sleep(3)
            r_price = pg.locateCenterOnScreen('Image/Price.JPG', confidence=0.9, grayscale=False)
            pg.moveTo(r_price.x, r_price.y, r, pg.easeOutQuad)
            pg.click()

def cancel_reg(r):
    time.sleep(1.5)
    cancel= pg.locateCenterOnScreen('Image/cancel.JPG', confidence=0.85)
    if cancel:
        pg.moveTo(cancel.x, cancel.y, r, pg.easeOutQuad)
        pg.click()
        pg.press('enter')