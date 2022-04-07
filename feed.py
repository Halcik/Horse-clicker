# -*- coding: utf-8 -*-
import pyautogui as pg

def h_feed( r, v):
    feeding = pg.locateCenterOnScreen('Image\Feed.jpg', confidence=0.9)
    care = pg.locateCenterOnScreen('Image\Care.jpg', confidence=0.9)

    if (feeding != None):
        pg.moveTo(feeding.x, feeding.y, r, pg.easeOutQuad)
        #print(feeding.x, feeding.y)
        pg.click()

    elif (care != None):
        pg.moveTo(care.x, care.y, r, pg.easeOutQuad)
        pg.click()
    
    if (v != 1 and care == None):
        Feed14 = pg.locateCenterOnScreen('Image\Feed14.jpg', confidence=0.9)
        #print("14: ", Feed14)

        Feed12 = pg.locateCenterOnScreen('Image\Feed12.jpg', confidence=0.9)
        #print("12: ", Feed12)

        Feed10 = pg.locateCenterOnScreen('Image\Feed10.jpg', confidence=0.9)
        #print("10: ", Feed10)

        Feed8 = pg.locateCenterOnScreen('Image\Feed8.jpg', confidence=0.9)
        #print("8: ", Feed8)

        Feed20 = pg.locateCenterOnScreen('Image\Feed20.jpg', confidence=0.9)
        #print("20: ", Feed20)

        Feed6 = pg.locateCenterOnScreen('Image\Feed6.jpg', confidence=0.9)
        #print("6: ", Feed6)

        Feed16 = pg.locateCenterOnScreen('Image\Feed16.jpg', confidence=0.93)
        #print("16: ", Feed16)

        Feed0 = pg.locateCenterOnScreen('Image\Feed0.jpg', confidence=0.93)
        #print("0: ", Feed0)

        Feed4 = pg.locateCenterOnScreen('Image\Feed4.jpg', confidence=0.9)
        #print("4: ", Feed4)

        if(Feed0 != None):
            quantity = pg.locateCenterOnScreen('Image\quantity0.jpg', confidence=0.9)
            pg.moveTo(quantity.x, quantity.y, r, pg.easeOutQuad)

        elif(Feed20 != None):
            pg.move(196, 172, r, pg.easeOutQuad)

        elif(Feed12 != None):
            pg.move(107, 88 , r, pg.easeOutQuad)

        elif(Feed10 != None):
            pg.move(85, 88, r, pg.easeOutQuad)

        elif(Feed8 != None):
            pg.move(64, 88, r, pg.easeOutQuad)

        elif(Feed4 != None):
            pg.move(21, 88, r, pg.easeOutQuad)

        elif(Feed14 != None):
            pg.move(130, 88, r, pg.easeOutQuad)

        elif(Feed6 != None):
            pg.move(42, 88, r, pg.easeOutQuad)

        elif(Feed16 != None):
            pg.move(152, 88, r, pg.easeOutQuad)

        
        pg.click()

    feed_it = pg.locateCenterOnScreen('Image\Feeding.jpg', confidence=0.8)

    if(feed_it != None):
        pg.moveTo(feed_it.x, feed_it.y, r, pg.easeOutQuad)
        pg.click()