import pyautogui as pg
import time
import pytesseract
from PIL import Image

test = pg.locateOnScreen("test_uru.JPG", confidence=0.9)
#na tym jest funkcje lokalizacji w pyautogui

if test==None:
    test = pg.locateOnScreen("uru2.JPG", confidence=0.9)


left = test[0]
top = test[1]
width = test[2]
height = test[3]


pg.screenshot("test.jpg", region=(left, top, width, height))


pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'


img = Image.open('test.JPG')
ocr = pytesseract.image_to_string(img, lang='pol', config='--psm 6 --oem 3') # -c tessedit_char_whitelist=0123456789/')) #psm i oem to sposoby szukania, whitelist, to dozwolone znaki

#paczka języka do pobrania dodatkowo

ocr = ocr.splitlines()

for i in ocr:
    if 'niedowagę' in i:
        print("Trzeba dać 20")
        break
    elif 'nadwagę' in i:
        print("Nie karmimy")
        break
    else:
        if ')' in i:
            feed = i[-4:]
            feed = feed.strip()
            #feed = '016'
            l_feed = len(feed)
            if l_feed==3:
                feed = feed[-1]
            elif l_feed==4:
                feed = feed[-2:]
            print("Trzeba dać:", feed)
            break