


from bs4 import BeautifulSoup as BS

import clipboard as CB

import re

import time

import sys

from Abstract import *

WMURL = "https://www.walmart.com"

productsPath = r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Products\ProductsLink.txt"

problem = []

def defineMenuName(link):
    rawLocation = link.replace(WMURL,"")

    if rawLocation.startswith("/browse"):
        location = rawLocation.replace("/browse/","")

    elif rawLocation.startswith("/cp"):
        location = rawLocation.replace("/cp/","")

    else:
        # print(rawLocation)
        location = rawLocation

    locNameList = location.split("/")
    tempList = []

    for i in locNameList:
        i = i.replace("-"," ")
        tempList.append(i)
    name = ""
    if not re.findall("[0-9]",tempList[(len(tempList)*-1)+1]):
        name = " ".join(tempList[0:2])
    else:
        name = tempList[0]

    if not re.findall("[a-z]",name):
        problem.append(name)

    return name.lstrip().rstrip().capitalize()
            


with open(productsPath,"r", encoding="utf-8") as f1:

    content = f1.readlines()


for i in content:
    i = i.rstrip()
    i.replace("\n","")
    print(defineMenuName(i))

for i in problem:
    print(i)