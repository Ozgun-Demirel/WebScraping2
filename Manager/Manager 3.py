


from bs4 import BeautifulSoup as BS

import clipboard as CB

import time

import pyautogui as pag


from Abstract import *




RobotOrHumanDynamic = r"C:\Users\Lenovo\source\repos\Manager\Manager\RobotOrHumanDynamic.txt"
SorryTechnicalssues = r"C:\Users\Lenovo\source\repos\Manager\Manager\SorryTechnicalssues.txt"



dynamicS = BS(getContent(RobotOrHumanDynamic),"html.parser") 
# 960, 600
# 5 saniye


sorryS = BS(getContent(SorryTechnicalssues),"html.parser")


"""
RobotOrHuman = r"C:\Users\Lenovo\source\repos\Manager\Manager\RobotOrHuman.txt"
roboS = BS(getContent(RobotOrHuman),"html.parser")
inText = roboS.find("h1").text.strip()
if inText.lower() == "Robot or human?".lower():
    print("yess")
# 960, 500
# 7 saniye
"""








