# -*- coding: utf-8 -*-
import pyautogui as pg
import time
import random
from feed import h_feed
from registration import h_registration
from groom_functions import h_groom, h_sleep
from next_horse import h_next
from death import death

#Przerwa po kazdym wywolaniu pyautogui - tu 0,3 sekundy
pg.PAUSE = 0.3

print("Wpisz liczbę koni do oporządzenia:")
n = int(input())
print("Czy posiadasz vipa?\n 1-Tak\n 2-Nie")
v = int(input())
func_sleep = input("Czy mam kłaść spać? [y/n]\n")
print("Zaczynam")
#print("Zacznę oporządzać konie za 10 sekund.")
#time.sleep(10)
duration = [0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 0.2, 0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.45, 0.5]
for i in range(n):
    #randomizacja czasu trwania przesunięcia myszki
    random.seed(a=None, version=2)
    r = random.choice(duration)
    for j in range(2):
        time.sleep(1)
        #zwykłe oporządzenie
        h_registration( r)
        h_feed( r, v)
        h_groom( r)
        if func_sleep == "y" or func_sleep == "Y":
            h_sleep( r)
        death( r)
    print("Postęp:", i+1, "/", n)
    h_next( r)