

from bs4 import BeautifulSoup as BS

import bs4

import clipboard as CB

import time

import pyautogui as pag

import os 

from Abstract import *


firstMay = "C:/Users/Lenovo/Desktop/5.1.2022/Sources"

secondMay = "C:/Users/Lenovo/Desktop/5.2.2022/Sources"



productsDivClass = "flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3"

def detectAnomaly(path):

    SubDirsList = os.listdir(path)
    for i in SubDirsList:

        currentDirPath = path+"/"+i
    
        print(f"{i} : ")

        for k in os.listdir(currentDirPath):

            filePath = currentDirPath+"/"+k

            content = getContent(filePath)

            soup = BS(content,"html.parser")
        
            products = soup.find("div",{"class":productsDivClass})
        
            if type(products) is not bs4.element.Tag:
            
                print(k)


def moveOrDeleteAnomaly(path):

    SubDirsList = os.listdir(path)
    for i in SubDirsList:

        currentDirPath = path+"/"+i
    
        print(f"{i} : ")

        for k in os.listdir(currentDirPath):

            filePath = currentDirPath+"/"+k

            content = getContent(filePath)

            soup = BS(content,"html.parser")
        
            products = soup.find("div",{"class":productsDivClass})
        
            if type(products) is not bs4.element.Tag:
            
                print(k)




