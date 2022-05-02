

import os
from sys import exit
import pyautogui as pag
from bs4 import BeautifulSoup as BS

import clipboard
import time


firefoxExplorerPath = "C:/Progra~1/Mozill~1/firefox.exe"

filePath = "C:/Users/Lenovo/Desktop/NewFile1.txt"



def createNewFile(info: str, path = filePath):
    with open(path,"x") as f1:
        f1.write(info)
    return print(f"Created file: {path.split('/')[-1]}")

def writeToFile(info: str, path = filePath):
    if not os.path.exists(path):
        return createNewFile(info,path)
    else:
        with open(path,"w+") as f1:
            f1.write(info)
    return print(f"Written on: {path.split('/')[-1]}")


writeToFile(info = "Hello World")