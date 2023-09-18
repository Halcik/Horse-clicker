# -*- coding: utf-8 -*-
import pyautogui as pg
import time
import random
from feed import h_feed
from registration import h_registration, cancel_reg
from groom_functions import h_groom, h_sleep
from next_horse import h_next
from death import death
from multiplication import h_multiplication, h_birth
import sys

import os
from datetime import datetime

def start_sitter(n, v, func_sleep, multiplication, reg, shutdown, path_project=None):
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
            done_h = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'done.JPG'), confidence=0.9)
            if done_h and j==1:
                break
            else:
                #cancel_reg( r)
                h_birth( r, j)
                #zwykłe oporządzenie
                if reg == "y" or reg =="Y":
                    h_registration( r)
                h_feed( r, v)
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


if __name__ == "__main__":
    pg.PAUSE = 0.3
    file_a = open("account_setting.txt", "r")
    print("Zapisane ustawienia sitterki:")
    for line in file_a.readlines():
        try:
            id_sett = line.index(":")
            print(line[:id_sett])
        except:
            print("Brak ustawień")
    choose_setting = input("Wpisz nazwę ustawienia lub [n], by przejść do ręcznego ustawienia programu:\n")
    file_a.close()
    if choose_setting=="n":
        n = int(input("Wpisz liczbę koni do oporządzenia:\n"))
        v = int(input("Czy posiadasz vipa?\n 1-Tak\n 2-Nie\n"))
        func_sleep = input("Czy mam kłaść spać? [y/n]\n")
        multiplication = input("Czy chcesz pokryć klacze? [y/n]\n")
        reg = input("Czy rejestrować konie w ojku? [y/n]\n")
        shutdown = input("Czy wyłączyć komputer? [y/n]\n")
        want_save = input("Czy chcesz zapisać ustawienia? [y/n]\n")
        if want_save == "y":
            name_a = input("Podaj nazwę ustawienia:\n")
            file_a = open("account_setting.txt", "a+")
            file_a.write(f'{name_a}:{n} {v} {func_sleep} {multiplication} {reg} {shutdown}\n')
            file_a.read()
            file_a.close()
    else:
        file_a = open("account_setting.txt", "r")
        for line in file_a.readlines():
            if choose_setting in line:
                id_sett = line.index(":")
                setting_account = line[id_sett+1:]
                setting_account = setting_account.split()
        n = int(setting_account[0])
        v = int(setting_account[1])
        func_sleep = setting_account[2]
        multiplication = setting_account[3]
        reg = setting_account[4]
        shutdown = setting_account[5]
    path_project = sys.argv[0][:-7]
    start_sitter(n, v, func_sleep, multiplication, reg, shutdown, path_project)