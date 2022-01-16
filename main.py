# -*- coding: utf-8 -*-
import pyautogui
#Przerwa po kazdym wywolaniu pyautogui - tu 2.5 sekundy
pyautogui.PAUSE = 2.5

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

quantity = pyautogui.locateCenterOnScreen('Image\quantity.jpg', confidence=0.95)
pyautogui.moveTo(quantity.x, quantity.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()

feed_it = pyautogui.locateCenterOnScreen('Image\Feeding.jpg', confidence=0.9)
pyautogui.moveTo(feed_it.x, feed_it.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()

# Oporzadzenie
groom = pyautogui.locateCenterOnScreen('Image\Groom.jpg', confidence=0.9)
pyautogui.moveTo(groom.x, groom.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()

# Polozenie spac

sleep_horse = pyautogui.locateCenterOnScreen('Image\Sleep.jpg', confidence=0.9)
pyautogui.moveTo(sleep_horse.x, sleep_horse.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()

# Przejscie do nastepnego konia

n_horse = pyautogui.locateCenterOnScreen('Image\Arrow.jpg', confidence=0.95)
pyautogui.moveTo(n_horse.x, n_horse.y, 0.5, pyautogui.easeOutQuad)
pyautogui.click()