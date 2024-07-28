# -*- coding: utf-8 -*-
import pyautogui as pg
import random, os, sys
from datetime import datetime

from sample.basic_care import h_feed, h_groom, h_sleep, h_next
from sample.additional_features import h_registration, h_multiplication, account_quiting, notification, cancel_reg
from sample.checking_functions import death, h_birth

def start_sitter(n, v, feed, func_sleep, multiplication, reg, shutdown, path_project, quit_game=None):
    if n>10:
        pd_rest = random.randrange(1, n)
    else:
        pd_rest = -1
        
    beg = datetime.today()
    for i in range(n):
        if i==pd_rest:
            pg.sleep(30)
        #randomizacja czasu trwania przesunięcia myszki
        random.seed(a=None, version=2)
        r = random.uniform(0.1, 0.45)
        for j in range(2):
            pg.sleep(1.5)
            done_h = pg.locateCenterOnScreen(os.path.join(path_project, 'Image', 'done.JPG'), confidence=0.9)
            if done_h and j==1:
                break
            else:
                #cancel_reg( r, path_project)
                h_birth( r, j, path_project)
                #zwykłe oporządzenie
                if reg == "y" or reg =="Y":
                    h_registration( r, path_project)
                if feed == "y" or feed =="Y":
                    h_feed( r, v, path_project)
                h_groom( r, path_project)
                if func_sleep == "y" or func_sleep == "Y":
                    h_sleep( r, path_project)
                death( r, path_project)
                if multiplication == "y" or multiplication == "Y":
                    h_multiplication( r, path_project)
        print("Postęp:", i+1, "/", n)
        h_next( r, path_project)
    end = datetime.today()
    done = end-beg
    print(f"Czas wykonania sitterki {n} koni:", done)
    if quit_game:
        account_quiting( r, path_project, quit_game)
    # notification('https://www.facebook.com/messages/t/xyz')

    if shutdown=="Y" or shutdown=='y':
        os.system('shutdown /s') #wyłącza kompa
        return 0
    else:
        return 1


if __name__ == "__main__":
    while True:
        path_project = sys.argv[0][:-8]
        print(path_project)
        pg.PAUSE = 0.3
        file_a = open(os.path.join(path_project,"account_setting.txt"), "r")
        print("Zapisane ustawienia sitterki:")
        for line in file_a.readlines():
            try:
                id_sett = line.index(":")
                print(line[:id_sett])
            except:
                print("Brak ustawień")
        choose_setting = input("Wpisz nazwę ustawienia lub [n], by przejść do ręcznego ustawienia programu lub [k], aby zakończyć:\n")
        file_a.close()
        if choose_setting=="n":
            n = int(input("Wpisz liczbę koni do oporządzenia:\n"))
            v = int(input("Czy posiadasz vipa?\n 1-Tak\n 2-Nie\n"))
            feed = input("Czy karmić konie? [y/n]\n")
            func_sleep = input("Czy mam kłaść spać? [y/n]\n")
            multiplication = input("Czy chcesz pokryć klacze? [y/n]\n")
            reg = input("Czy rejestrować konie w ojku? [y/n]\n")
            quit_game = input("Wyjście ze współki czy konta? [w/k/wk]\n")
            shutdown = input("Czy wyłączyć komputer? [y/n]\n")
            want_save = input("Czy chcesz zapisać ustawienia? [y/n]\n")
            if want_save == "y":
                name_a = input("Podaj nazwę ustawienia:\n")
                file_a = open(os.path.join(path_project,"account_setting.txt"), "a+")
                file_a.write(f'{name_a}:{n} {v} {feed} {func_sleep} {multiplication} {reg} {shutdown} {quit_game}\n')
                file_a.read()
                file_a.close()
        elif choose_setting=="k":
            break
        else:
            file_a = open(os.path.join(path_project,"account_setting.txt"), "r")
            for line in file_a.readlines():
                if choose_setting in line:
                    id_sett = line.index(":")
                    setting_account = line[id_sett+1:]
                    setting_account = setting_account.split()
                    break
            n = int(setting_account[0])
            v = int(setting_account[1])
            feed = setting_account[2]
            func_sleep = setting_account[3]
            multiplication = setting_account[4]
            reg = setting_account[5]
            shutdown = setting_account[6]
            quit_game = setting_account[7]
            file_a.close()
        account = start_sitter(n, v, feed, func_sleep, multiplication, reg, shutdown, path_project, quit_game)
        if not account:
            break