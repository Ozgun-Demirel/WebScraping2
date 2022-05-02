

import time

import pyautogui as pag
from Abstract import *


gc = GeneralControls()
WalmartURL = "https://www.walmart.com/"
WmAllDepsURL = "https://www.walmart.com/all-departments"


gc.openURL(WalmartURL)

time.sleep(0.5)
pag.run("g1877, 169 c")
pag.run("g950,230 c")

def scrollDown(times=16):
    for i in range(times):
        gc.scrollUpDown(-4000)
        time.sleep(0.1)

scrollDown()


