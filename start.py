import pyautogui as pg
import time
import random
from feed import h_feed
from registration import h_registration, cancel_reg
from groom_functions import h_groom, h_sleep
from next_horse import h_next
from death import death
from multiplication import h_multiplication, h_birth
import os
from datetime import timedelta, datetime

def start_sitter(n, v, func_sleep, multiplication, reg, shutdown):
    #Przerwa po kazdym wywolaniu pyautogui - tu 0,3 sekundy
    pg.PAUSE = 0.3

    if n>10:
        pd_rest = random.randrange(1, n)
    else:
        pd_rest = -1
        
    beg = datetime.today()
    for i in range(n):
        if i==pd_rest:
            time.sleep(30)
        #randomizacja czasu trwania przesunięcia myszki
        random.seed(a=None, version=2)
        r = random.uniform(0.1, 0.5)
        for j in range(2):
            time.sleep(1.5)
            done_h = pg.locateCenterOnScreen('Image/done.JPG', confidence=0.9)
            if done_h and j==1:
                break
            else:
                #cancel_reg( r)
                h_birth( r, j)
                #zwykłe oporządzenie
                if reg == "y" or reg =="Y":
                    h_registration( r)
                h_feed( r, v)
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