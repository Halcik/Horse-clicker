# -*- coding: utf-8 -*-
import pyautogui
from types import NoneType
import time

def h_next( r):
    n_horse = pyautogui.locateCenterOnScreen('Image\Arrow.jpg', confidence=0.9)
    n_horse2 = pyautogui.locateCenterOnScreen('Image\Arrow2.jpg', confidence=0.9)
    n_horse3 = pyautogui.locateCenterOnScreen('Image\Arrow3.jpg', confidence=0.9)
    if(n_horse != None):
        pyautogui.moveTo(n_horse.x, n_horse.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    elif (n_horse2 != None):
        pyautogui.moveTo(n_horse2.x, n_horse2.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    elif (n_horse3 != None):
        pyautogui.moveTo(n_horse3.x, n_horse3.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        print("Wystąpił błąd z przechodzeniem do następnego konia")
        pyautogui.press('f5')
        time.sleep(1.5)
        pyautogui.click()
