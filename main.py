# -*- coding: utf-8 -*-
import pyautogui as pg
import time
import random
from feed import h_feed
from registration import h_registration
from groom_functions import h_groom, h_sleep
from next_horse import h_next
from death import death
from multiplication import h_multiplication, h_birth

import os
from datetime import timedelta, datetime

#Przerwa po kazdym wywolaniu pyautogui - tu 0,3 sekundy
pg.PAUSE = 0.3

n = int(input("Wpisz liczbę koni do oporządzenia:\n"))
v = int(input("Czy posiadasz vipa?\n 1-Tak\n 2-Nie\n"))
func_sleep = input("Czy mam kłaść spać? [y/n]\n")
multiplication = input("Czy chcesz pokryć klacze? [y/n]\n")
shutdown = input("Czy wyłączyć komputer? [y/n]\n")

beg = datetime.today()
for i in range(n):
    #randomizacja czasu trwania przesunięcia myszki
    random.seed(a=None, version=2)
    r = random.uniform(0.1, 0.5)
    for j in range(2):
        #print(j)
        time.sleep(1.5)
        #if j==0:
            #new_horse = pg.locateCenterOnScreen('Image/new_horse.JPG', confidence=0.9)
            #while new_horse== None:
                #time.sleep(0.1)
                #new_horse = pg.locateCenterOnScreen('Image/new_horse.JPG', confidence=0.9)
        done_h = pg.locateCenterOnScreen('Image/done.JPG', confidence=0.9)
        if done_h and j==1:
            break
        else:
            h_birth( r, j)
            #zwykłe oporządzenie
            h_registration( r)
            h_feed( r, v)
            time.sleep(0.1)
            h_groom( r)
            if func_sleep == "y" or func_sleep == "Y":
                h_sleep( r)
            death( r)
            if multiplication == "y" or multiplication == "Y":
                h_multiplication( r)
    print("Postęp:", i+1, "/", n)
    h_next( r)
end = datetime.today()
done = end-beg
print(f"Czas wykonania sitterki {n} koni:", done)
if shutdown=="Y" or shutdown=='y':
    os.system('shutdown /s') #wyłącza kompa

