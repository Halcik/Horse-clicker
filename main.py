# -*- coding: utf-8 -*-
from pickle import FALSE
from types import NoneType
import pyautogui
#Przerwa po kazdym wywolaniu pyautogui - tu 3 sekundy
pyautogui.PAUSE = 2.5

# Zarejestrowanie w osrodku
def h_registration():
    registration = pyautogui.locateCenterOnScreen('Image\Registration.jpg', confidence=0.9)
    if(registration != None):
        pyautogui.moveTo(registration.x, registration.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return
    
    reserved = pyautogui.locateCenterOnScreen('Image\Reserved.jpg', confidence=0.8)
    if(reserved != None):
        pyautogui.moveTo(reserved.x, reserved.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()

        box = pyautogui.locateCenterOnScreen('Image\Box.jpg', confidence=0.8, grayscale=False)
        pyautogui.moveTo(box.x, box.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        r_days = pyautogui.locateCenterOnScreen('Image\Days.jpg', confidence=0.9)
        pyautogui.moveTo(r_days.x, r_days.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()

        r_price = pyautogui.locateCenterOnScreen('Image\Price.jpg', confidence=0.9, grayscale=False)
        pyautogui.moveTo(r_price.x, r_price.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()

# Nakarmienie
def h_feed():
    feeding = pyautogui.locateCenterOnScreen('Image\Feed.jpg', confidence=0.9)
    pyautogui.moveTo(feeding.x, feeding.y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()
    
    quantity = pyautogui.locateCenterOnScreen('Image\quantity.jpg', confidence=0.95)
    pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()
    
    feed_it = pyautogui.locateCenterOnScreen('Image\Feeding.jpg', confidence=0.8)
    pyautogui.moveTo(feed_it.x, feed_it.y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()

# Oporzadzenie
def h_groom():
    groom = pyautogui.locateCenterOnScreen('Image\Groom.jpg', confidence=0.8)
    pyautogui.moveTo(groom.x, groom.y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()

# Polozenie spac
def h_sleep():
    sleep_horse = pyautogui.locateCenterOnScreen('Image\Sleep.jpg', confidence=0.8)
    pyautogui.moveTo(sleep_horse.x, sleep_horse.y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()

# Przejscie do nastepnego konia
def h_next():
    n_horse = pyautogui.locateCenterOnScreen('Image\Arrow.jpg', confidence=0.95)
    pyautogui.moveTo(n_horse.x, n_horse.y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()

print("Wpisz liczbę koni do oporządzenia:")
n = int(input())
print("Czy posiadasz vipa?\n 1-Tak\n 2-Nie")
v = int(input())
for x in range(n):
    h_registration()
    h_feed()
    h_groom()
    h_sleep()
    h_next()