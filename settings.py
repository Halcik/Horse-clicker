#file with settings - soon
import os

from pyshortcuts import make_shortcut

whereIam= os.getcwd()
whereIstart = os.path.join(whereIam, 'main.py') #terminal version
whereIcon = os.path.join(whereIam, "Image", "horse-clicker.ico") #temporary

make_shortcut(whereIstart, name="Horse clicker", icon=whereIcon)