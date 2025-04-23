#file with settings - soon - this is not testing yet
import os

#necessary library
os.system("pip install -r requirements.txt")
from pyshortcuts import make_shortcut



#shortcut on desktop
whereIam= os.getcwd()
whereIstart = os.path.join(whereIam, 'main.py') #terminal version
whereIcon = os.path.join(whereIam, "Image", "horse-clicker.ico") #temporary
make_shortcut(whereIstart, name="Horse clicker", icon=whereIcon)



