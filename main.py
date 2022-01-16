# -*- coding: utf-8 -*-
import pyautogui
#Przerwa po kazdym wywolaniu pyautogui - tu 2,5 sekundy
pyautogui.PAUSE = 2.5

# Zarejestrowanie w osrodku
registration = pyautogui.locateCenterOnScreen('Registration.jpg', confidence=0.8)
print(registration)
pyautogui.moveTo(registration.x, registration.y, 0.9)
pyautogui.click()
# Nakarmienie
# Oporzadzenie
# Polozenie spac
# Przejscie do nastepnego konia