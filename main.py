# -*- coding: utf-8 -*-
import pyautogui
#Przerwa po kazdym wywolaniu pyautogui - tu 1,5 sekundy
pyautogui.PAUSE = 1.5

# Zarejestrowanie w osrodku
registration = pyautogui.locateCenterOnScreen('Image\Registration.jpg', confidence=0.9)
print(registration)
pyautogui.moveTo(registration.x, registration.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()

reserved = pyautogui.locateCenterOnScreen('Image\Reserved.jpg', confidence=0.9)
pyautogui.moveTo(reserved.x, reserved.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()

box = pyautogui.locateCenterOnScreen('Image\Box.jpg', confidence=0.9, grayscale=False)
pyautogui.moveTo(box.x, box.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()
# Nakarmienie
feeding = pyautogui.locateCenterOnScreen('Image\Feed.jpg', confidence=0.9)
pyautogui.moveTo(feeding.x, feeding.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()
# Oporzadzenie
# Polozenie spac
# Przejscie do nastepnego konia