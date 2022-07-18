# -*- coding: utf-8 -*-
import pyautogui as pg

def h_feed( r, v):
    feeding = pg.locateCenterOnScreen('Image/Feed.JPG', confidence=0.9)
    care = pg.locateCenterOnScreen('Image/Care.JPG', confidence=0.9)

    if feeding:
        pg.moveTo(feeding.x, feeding.y, r, pg.easeOutQuad)
        #print(feeding.x, feeding.y)
        pg.click()

    elif care:
        pg.moveTo(care.x, care.y, r, pg.easeOutQuad)
        pg.click()
    
    if v != 1 and care == None and feeding:
        try:
            feed0 = pg.locateCenterOnScreen('Image/Feed0.JPG', confidence=0.93)
            print("0: ", feed0)
            if feed0:
                quantity = pg.locateCenterOnScreen('Image/quantity0.JPG', confidence=0.9)
                pg.moveTo(quantity.x, quantity.y, r, pg.easeOutQuad)
            else:
                raise ErrorFeed()

        except ErrorFeed:
            try:
                feed20 = pg.locateCenterOnScreen('Image/Feed20.JPG', confidence=0.9)
                print("20: ", feed20)
                if feed20:
                    pg.move(196, 172, r, pg.easeOutQuad)
                else:
                    raise ErrorFeed()

            except ErrorFeed:
                try:
                    feed12 = pg.locateCenterOnScreen('Image/Feed12.JPG', confidence=0.9)
                    print("12: ", feed12)
                    if feed12:
                        pg.move(107, 88 , r, pg.easeOutQuad)
                    else:
                        feed12 = pg.locateCenterOnScreen('Image/Feed12_2.JPG', confidence=0.9)
                        print("12_2: ", feed12)
                        if feed12:
                            pg.move(107, 88 , r, pg.easeOutQuad)
                        else:
                            raise ErrorFeed()

                except ErrorFeed:
                    try:
                        feed10 = pg.locateCenterOnScreen('Image/Feed10.JPG', confidence=0.9)
                        print("10: ", feed10)
                        if feed10:
                            pg.move(85, 88, r, pg.easeOutQuad)
                        else:
                            feed10 = pg.locateCenterOnScreen('Image/Feed10_2.JPG', confidence=0.9)
                            print("10_2: ", feed10)
                            if feed10:
                                pg.move(85, 88, r, pg.easeOutQuad)
                            else:
                                raise ErrorFeed()

                    except ErrorFeed:
                        try:
                            feed8 = pg.locateCenterOnScreen('Image/Feed8.JPG', confidence=0.9)
                            print("8: ", feed8)
                            if feed8:
                                pg.move(64, 88, r, pg.easeOutQuad)
                            else:
                                feed8 = pg.locateCenterOnScreen('Image/Feed8_2.JPG', confidence=0.9)
                                print("8_2: ", feed10)
                                if feed8:
                                    pg.move(64, 88, r, pg.easeOutQuad)
                                else:
                                    raise ErrorFeed()

                        except ErrorFeed:
                            try:
                                feed4 = pg.locateCenterOnScreen('Image/Feed4.JPG', confidence=0.9)
                                print("4: ", feed4)
                                if feed4:
                                    pg.move(21, 88, r, pg.easeOutQuad)
                                else:
                                    raise ErrorFeed()

                            except ErrorFeed:
                                try:
                                    feed14 = pg.locateCenterOnScreen('Image/Feed14.JPG', confidence=0.9)
                                    print("14: ", feed14)
                                    if feed14:
                                        pg.move(130, 88, r, pg.easeOutQuad)
                                    else:
                                        raise ErrorFeed()

                                except ErrorFeed:
                                    try:
                                        feed6 = pg.locateCenterOnScreen('Image/Feed6.JPG', confidence=0.9)
                                        print("6: ", feed6)
                                        if feed6:
                                            pg.move(42, 88, r, pg.easeOutQuad)
                                        else:
                                            feed6 = pg.locateCenterOnScreen('Image/Feed6_2.JPG', confidence=0.9)
                                            print("6_2: ", feed6)
                                            if feed6:
                                                pg.move(42, 88, r, pg.easeOutQuad)
                                            else:
                                                raise ErrorFeed()

                                    except ErrorFeed:
                                        try:
                                            feed16 = pg.locateCenterOnScreen('Image/Feed16.JPG', confidence=0.93)
                                            print("16: ", feed16)
                                            if feed16:
                                                pg.move(152, 88, r, pg.easeOutQuad)
                                            else:
                                                raise ErrorFeed()

                                        except:
                                            pg.move(107, 88 , r, pg.easeOutQuad)
                                            print("Zastosowano alternatywę")

        finally:
            pg.click()

    feed_it = pg.locateCenterOnScreen('Image/Feeding.JPG', confidence=0.8)

    if(feed_it != None):
        pg.moveTo(feed_it.x, feed_it.y, r, pg.easeOutQuad)
        pg.click()


class ErrorFeed(Exception):
    pass
