# -*- coding: utf-8 -*-
import pyautogui
from types import NoneType

def h_feed( r, v):
    feeding = pyautogui.locateCenterOnScreen('Image\Feed.jpg', confidence=0.9)
    care = pyautogui.locateCenterOnScreen('Image\Care.jpg', confidence=0.9)
    if (feeding != None):
        pyautogui.moveTo(feeding.x, feeding.y, r, pyautogui.easeOutQuad)
        #print(feeding.x, feeding.y)
        pyautogui.click()
    elif (care != None):
        pyautogui.moveTo(care.x, care.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        return
    
    if (v != 1 and care == None):
        Feed14 = pyautogui.locateCenterOnScreen('Image\Feed14.jpg', confidence=0.9)
        #print("14: ", Feed14)

        Feed12 = pyautogui.locateCenterOnScreen('Image\Feed12.jpg', confidence=0.9)
        #print("12: ", Feed12)

        Feed10 = pyautogui.locateCenterOnScreen('Image\Feed10.jpg', confidence=0.9)
        #print("10: ", Feed10)

        Feed8 = pyautogui.locateCenterOnScreen('Image\Feed8.jpg', confidence=0.9)
        #print("8: ", Feed8)

        Feed20 = pyautogui.locateCenterOnScreen('Image\Feed20.jpg', confidence=0.9)
        #print("20: ", Feed20)

        Feed6 = pyautogui.locateCenterOnScreen('Image\Feed6.jpg', confidence=0.9)
        #print("6: ", Feed6)

        Feed16 = pyautogui.locateCenterOnScreen('Image\Feed16.jpg', confidence=0.93)
        #print("16: ", Feed16)

        Feed0 = pyautogui.locateCenterOnScreen('Image\Feed0.jpg', confidence=0.93)
        #print("0: ", Feed0)

        Feed4 = pyautogui.locateCenterOnScreen('Image\Feed4.jpg', confidence=0.9)
        #print("4: ", Feed4)

        if(Feed0 != None):
            quantity = pyautogui.locateCenterOnScreen('Image\quantity0.jpg', confidence=0.9)
            pyautogui.moveTo(quantity.x, quantity.y, r, pyautogui.easeOutQuad)
        elif(Feed20 != None):
            pyautogui.move(196, 172, r, pyautogui.easeOutQuad)
        elif(Feed12 != None):
            pyautogui.move(107, 88 , r, pyautogui.easeOutQuad)
        elif(Feed10 != None):
            pyautogui.move(85, 88, r, pyautogui.easeOutQuad)
        elif(Feed8 != None):
            pyautogui.move(64, 88, r, pyautogui.easeOutQuad)
        elif(Feed4 != None):
            pyautogui.move(21, 88, r, pyautogui.easeOutQuad)
        elif(Feed14 != None):
            pyautogui.move(130, 88, r, pyautogui.easeOutQuad)
        elif(Feed6 != None):
            pyautogui.move(42, 88, r, pyautogui.easeOutQuad)
        elif(Feed16 != None):
            pyautogui.move(152, 88, r, pyautogui.easeOutQuad)
        
        pyautogui.click()

    feed_it = pyautogui.locateCenterOnScreen('Image\Feeding.jpg', confidence=0.8)
    if(feed_it != None):
        pyautogui.moveTo(feed_it.x, feed_it.y, r, pyautogui.easeOutQuad)
        pyautogui.click()
    else:
        pass