# -*- coding: utf-8 -*-
import pyautogui
from types import NoneType
import time

def h_registration(r):
    registration = pyautogui.locateCenterOnScreen('Image\Registration.jpg', confidence=0.9)
    if(registration != None):
        pyautogui.moveTo(registration.x, registration.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
        time.sleep(3.0)
        h_registration2(r)
    else:
        return
    
def h_registration2(r):
    reserved = pyautogui.locateCenterOnScreen('Image\Reserved.jpg', confidence=0.8)
    if(reserved != None):
        pyautogui.moveTo(reserved.x, reserved.y, r, pyautogui.easeOutQuad)
        pyautogui.click()

        box = pyautogui.locateCenterOnScreen('Image\Box.jpg', confidence=0.8, grayscale=False)
        pyautogui.moveTo(box.x, box.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
        time.sleep(3)
        pd = pyautogui.locateCenterOnScreen('Image\PD.jpg', confidence=0.9)
        if(pd == None):
            print("Wystąpił błąd rejestrowania")
            pyautogui.press('f5')
            time.sleep(2.0)
            h_registration2( r)
        else:
            pass
    else:
        r_days = pyautogui.locateCenterOnScreen('Image\Days.jpg', confidence=0.9)
        if(r_days != None):
            pyautogui.moveTo(r_days.x, r_days.y, r, pyautogui.easeOutQuad)
            pyautogui.click()
            time.sleep(3)
            r_price = pyautogui.locateCenterOnScreen('Image\Price.jpg', confidence=0.9, grayscale=False)
            pyautogui.moveTo(r_price.x, r_price.y, r, pyautogui.easeOutQuad)
            pyautogui.click()
        else:
            pass