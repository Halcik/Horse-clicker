# -*- coding: utf-8 -*-
from pickle import FALSE
from types import NoneType
import pyautogui
import time

#Przerwa po kazdym wywolaniu pyautogui - tu 3 sekundy
pyautogui.PAUSE = 1.0

# Zarejestrowanie w osrodku
def h_registration():
    registration = pyautogui.locateCenterOnScreen('Image\Registration.jpg', confidence=0.9)
    if(registration != None):
        pyautogui.moveTo(registration.x, registration.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()
        time.sleep(3.0)
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
    if (feeding != None):
        pyautogui.moveTo(feeding.x, feeding.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return
    
    if (v != 1):
        Feed14 = pyautogui.locateCenterOnScreen('Image\Feed14.jpg', confidence=0.9)
        #print("14: ", Feed14)

        Feed12 = pyautogui.locateCenterOnScreen('Image\Feed12.jpg', confidence=0.9)
       # print("12: ", Feed12)

        Feed10 = pyautogui.locateCenterOnScreen('Image\Feed10.jpg', confidence=0.93)
        #print("10: ", Feed10)

        Feed8 = pyautogui.locateCenterOnScreen('Image\Feed8.jpg', confidence=0.9)
        #print("8: ", Feed8)

        Feed20 = pyautogui.locateCenterOnScreen('Image\Feed20.jpg', confidence=0.9)
        #print("20: ", Feed20)

        Feed6 = pyautogui.locateCenterOnScreen('Image\Feed6.jpg', confidence=0.9)
       # print("6: ", Feed6)

        Feed16 = pyautogui.locateCenterOnScreen('Image\Feed16.jpg', confidence=0.93)
        #print("16: ", Feed16)

        Feed0 = pyautogui.locateCenterOnScreen('Image\Feed0.jpg', confidence=0.93)
        #print("0: ", Feed0)

        if(Feed20 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity20.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
        elif(Feed0 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity0.jpg', confidence=0.9)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
            pyautogui.click()
            return
        elif(Feed12 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity12.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
        elif(Feed10 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity10.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
        elif(Feed8 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity8.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
        elif(Feed14 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity14.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
        elif(Feed6 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity6.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
        elif(Feed16 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity16.jpg', confidence=0.95)
            pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
        else:
            pass
        
        pyautogui.click()
    else:
        pass

    feed_it = pyautogui.locateCenterOnScreen('Image\Feeding.jpg', confidence=0.8)
    pyautogui.moveTo(feed_it.x, feed_it.y, 0.5, pyautogui.easeOutQuad)
    pyautogui.click()
 
# Oporzadzenie
def h_groom():
    groom = pyautogui.locateCenterOnScreen('Image\Groom.jpg', confidence=0.9)
    if(groom != None):
        pyautogui.moveTo(groom.x, groom.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return

# Polozenie spac
def h_sleep():
    sleep_horse = pyautogui.locateCenterOnScreen('Image\Sleep.jpg', confidence=0.8)
    if(sleep_horse != None):
        pyautogui.moveTo(sleep_horse.x, sleep_horse.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return

# Przejscie do nastepnego konia
def h_next():
    n_horse = pyautogui.locateCenterOnScreen('Image\Arrow.jpg', confidence=0.9)
    if(n_horse != None):
        pyautogui.moveTo(n_horse.x, n_horse.y, 0.5, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        print("Wystąpił błąd")
        h_next()

print("Wpisz liczbę koni do oporządzenia:")
n = int(input())
print("Czy posiadasz vipa?\n 1-Tak\n 2-Nie")
v = int(input())
print("Zacznę oporządzać konie za 15 sekund.")
time.sleep(15)
for x in range(n):
    for y in range(2):
        h_registration()
        h_feed()
        h_groom()
        h_sleep()
    print(x+1, "/", n)
    h_next()
    