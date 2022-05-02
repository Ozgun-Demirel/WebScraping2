


from bs4 import BeautifulSoup as BS

import bs4

import clipboard as CB

import time

import pyautogui as pag

import os 

from Abstract import *


#SourcesPath = r"C:\Users\Lenovo\Desktop\ex.txt"
#content = getContent(SourcesPath)
#soup = BS(content,"html.parser")



list1 = ["1","2","3","4"]

list2 = ["5","2","3","6"]

list1.extend(x for x in list2 if x not in list1)

print(list1)
