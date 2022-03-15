# -*- coding: utf-8 -*-
import pyautogui
from types import NoneType
import time

def death( r):
    death = pyautogui.locateCenterOnScreen('Image\death.jpg', confidence=0.9)
    if(death != None):
        pyautogui.moveTo(death.x, death.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
        h_arrow = pyautogui.locateCenterOnScreen('Image\Arrowb.jpg', confidence=0.9)
        pyautogui.moveTo(h_arrow.x, h_arrow.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return 