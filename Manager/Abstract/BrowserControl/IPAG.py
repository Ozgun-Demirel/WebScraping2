
import clipboard as CB
from bs4 import BeautifulSoup as BS
from sys import exit
import os
import pyautogui as pag
import time

from Abstract.EasierFunctions.IFUNC import *


"""
    GeneralControls class uses firefox as browser. 
    In the future, more browser UI controls may be created.

    This document controls browser event such as:

    openning a new page (openURL), closing a tab (closeTab), scrolling (scrollUpDown) and more.

    
"""






WalmartURL = "https://www.walmart.com/"

firefoxExplorerPath = "C:/Progra~1/Mozill~1/firefox.exe"

filePath = "C:/Users/Lenovo/Desktop/NewFile.txt"


class GeneralControls():

    def __init__(self, explorer = firefoxExplorerPath):
        self.One = 0.1
        self.Two = 0.2
        self.Five = 0.5
        self.Ten = 1
        self.GPageCount = 1
        self.DOCTYPE =  "<!DOCTYPE html>"
        os.system(explorer)
        time.sleep(self.Five)
        pag.run("g 1835,5 c")
        time.sleep(self.Five)
        pag.run("g 960,540 c")
        time.sleep(self.Five)
        pag.run("h'super, up'")
        time.sleep(self.Five)

    def closeTab(self):
        """
        closes the tab that is 
        placed from left to right ordered count
        """ 
        print(self.GPageCount)
        if self.GPageCount >= 7:
            print("Can't close that tab!")
            print("Too Many Tabs!")
            return exit()
        else:
            if self.GPageCount == 1:
                loc = '255'
            else:
                loc = 260+(280*(self.GPageCount-1))
            pag.run(f"g{loc},25 c")
        self.GPageCount += -1
        time.sleep(self.Five)

    
    def openURL(self,URL = WalmartURL):
        
        time.sleep(self.Five)
        pag.run("g 500,80 c")
        time.sleep(self.Five)

        if URL.__contains__("\n"):
            URL.replace("\n","")
        pag.run(f"w'{URL}'")
        """ CHECK FUNCTION ABOVE
        try:
            pag.run(f"w'{URL}'")
        except Exception as err:
            print(err)
            print(URL)
            print(type(URL))
            print(URL.split())
            exit()
        """
        
        time.sleep(self.Five)
        pag.run("h'enter'")
        time.sleep(self.Five)
        return print(f"Page Opened: {URL}")


    def scrollUpDown(self,vertical:int):
        """
        positive vertical value gets scroll up
        """
        for i in range(vertical):
            time.sleep(self.Two)
            pag.scroll(clicks = 1000)
            time.sleep(self.Two)
        
        
    def exportPageSource(self,path = filePath):
        
        time.sleep(self.Five)
        pag.run("g950,230 r g+125,+240 c") # 6'th button. 6*40 = 240
        self.GPageCount += 1
        time.sleep(self.Five)
        pag.run("g1000,380 c h'ctrl,a' h'ctrl,c'")
        time.sleep(self.Five)        
        writeToFile(str(BS(CB.paste().encode("utf-8"),'html.parser')),path)
        self.closeTab()
        if not CB.paste().startswith("<!DOCTYPE html>"):
            self.exportPageSource(path)

    
    def returnPageSourceStr(self):
        time.sleep(self.Five)
        pag.run("g950,230 r g+125,+240 c")
        self.GPageCount += 1
        time.sleep(self.Five)
        pag.run("g1000,380 c h'ctrl,a'")
        time.sleep(self.Five)   
        pag.run("h'ctrl,c'")
        time.sleep(self.Two)  
        self.closeTab()
        if not CB.paste().startswith("<!DOCTYPE html>"):
            self.returnPageSourceStr()
        else:
            return str(BS(CB.paste().encode("utf-8"),'html.parser'))


    def returnPageSourceStrFromInspector(self):
        time.sleep(self.Ten)
        pag.run("g950,230 r g+130,+320 c") # 8'th button. 8*40 = 320
        time.sleep(self.Five)
        pag.run("g50,720")
        self.scrollUpDown(3)
        time.sleep(self.Five)
        pag.run("r g170,110 c")
        time.sleep(self.Two)
        pag.run("g700,780 c")
        time.sleep(self.Five)
        pag.run("h'ctrl,a'")
        time.sleep(self.Two)  
        pag.run("h'ctrl,c'")
        time.sleep(self.Five)
        source = str(BS(CB.paste().encode("utf-8"),'html.parser'))
        if not source.startswith("<html"):
            return self.returnPageSourceStrFromInspector()

        else:
            return source


    def finalize(self):
        pag.run("g 1835,5 c")
        time.sleep(self.Two)
        print("Program Closed!")
        return exit()

    def close(self):
        pag.run("h'alt,f4'")
        time.sleep(5)







