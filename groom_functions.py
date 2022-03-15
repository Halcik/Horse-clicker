# -*- coding: utf-8 -*-
import pyautogui
from types import NoneType
import time

#Oporządzenie
def h_groom( r):
    groom = pyautogui.locateCenterOnScreen('Image\Groom.jpg', confidence=0.9)
    if(groom != None):
        pyautogui.moveTo(groom.x, groom.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return

# Polozenie spac
def h_sleep( r):
    sleep_horse = pyautogui.locateCenterOnScreen('Image\Sleep.jpg', confidence=0.8)
    if(sleep_horse != None):
        pyautogui.moveTo(sleep_horse.x, sleep_horse.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return