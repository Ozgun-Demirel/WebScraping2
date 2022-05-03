

import os
from sys import exit
import time
import pyautogui as pag
from bs4 import BeautifulSoup as BS
import re

from Abstract.BrowserControl.IPAG import *
from Abstract.EasierFunctions.IFUNC import *


startTime = time.ctime()


WMURL = "https://www.walmart.com"
problemLinks = r"C:\Users\Lenovo\source\repos\Manager\Manager\ProblemLinks.txt"

class Main():

    def __init__(self):
        self.DynamicInputsPath = r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Scripts\DynamicInputs.py"
        self.AllDepsFile = "C:/Users/Lenovo/source/repos/Manager/Manager/Concrete/Walmart/Saves/AllSources/" # total 249 links
        self.AllDepsTXTPath = r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Products\ProductsLink.txt"
        self.WmAllDepsLink = r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Saves\WmAllDeps=.txt"
        self.NavbarLink = r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Saves\NavbarHtmlFile.txt"
        self.AllDepsLink = "https://www.walmart.com/all-departments"
        self.SourcesPath = "C:/Users/Lenovo/source/repos/Manager/Manager/Concrete/Walmart/Products/Sources"
        

        #to be deleted later:
        self.problemLinks = []


    def getFileContent(self,filePath):
        with open(filePath,"r") as dataFile:
            content = dataFile.readlines()
        return content 
    

    def TryCollectingDepsLinks(self):

        gc = GeneralControls()
        self.AllDepsLinkContent = self.getFileContent(self.AllDepsLink)
        """
        This function opens file that contains the links
        in Walmart All Departments page and stores each links'
        source to Concrete/Walmart/Saves/AllSources file
        """
        def openExtractClose(URLPath,path):
                gc.openURL(URLPath)
                time.sleep(2.2)
                pag.run("g1877, 169 c")
                gc.exportPageSource(path)
                gc.closeTab()

        for i in self.AllDepsLinkContent:
        
            if i.startswith("https://www.walmart.com/"):
                path = self.AllDepsFile+("".join((i.replace("https://www.walmart.com/","")).split("/")[1:-1]))+".txt"
                openExtractClose(i.replace("\n",""),path)

            elif i.startswith("/browse/"):
                path = self.AllDepsFile+ "".join(i.split("/")[2:-1])+".txt"
                openExtractClose(WMURL+i.replace("\n",""),path)

            elif i.startswith("/cp/"):
                path = self.AllDepsFile+"".join(i.split("/")[2:-1])+".txt"
                openExtractClose(WMURL+i.replace("\n",""),path)

            elif i.startswith("browse/"):
                path = self.AllDepsFile+"".join(i.split("/")[1:-1])+".txt"
                openExtractClose(WMURL+"/"+i.replace("\n",""),path)

            else:
                print("This link is unuseable: \n"+i)
        print("TryCollectingDepsLinks Function is done!")

    # þu anda kullanýlmýyor. ihtiyaç olmazsa silinecek. Tekrar kullanýlýrsa bu kýsým silinmeli
    def loadClassAttrs(self):
        with open(self.DynamicInputsPath,"r", encoding="utf-8") as f1:
            ClassContent = f1.readlines()
        self.subMenuClass = ClassContent[0].replace("\n","")
        self.productsMenuClass = ClassContent[1].replace("\n","")

    def TotalMission(self, overWrite = False):
        """
        This function opens file that contains the links
        in Walmart All Departments page , defines 
        page type (Products, subMenu container, Others yet to define)
        and extracts all requested data
        """
        self.gc = GeneralControls()
        

        def newDynamicInputTaker():
            """
            Walmart Tags' class changes dynamically.
            This happens often and should be handled when the code is running.
            There are 3 Tag classes that are needed as such:
            tagTypes = ["subMenuClass", "subNavbarClass", "subMenuSubObjectClass"]            
            """

            URLForSubNavbar = "https://www.walmart.com/browse/food/chips/976759_976787_1001390"

            def funcOpener(URLPath, filePath, sourceType):
                """
                Handles the beginning of 2 funcs below. 
                """
                self.gc.openURL(URLPath)
                time.sleep(2.2)
                pag.run("g1877, 169 c")

                if sourceType == "Inspector":
                    fileHtml = self.gc.returnPageSourceStrFromInspector()
                    writeToFile(fileHtml,filePath)

                elif sourceType == "PageSource":
                    self.gc.exportPageSource(filePath)

                with open(filePath,"r",encoding = "utf-8") as f1:
                    self.MenuContent = f1.read()
                    
            
            def subMenuClassExtractor():
                funcOpener(self.AllDepsLink, self.WmAllDepsLink, "PageSource")
                soup = BS(self.MenuContent,"html.parser")
                div = soup.select_one("div>div>div>div>main>div>div>div>div>section>div:nth-of-type(2)")
                return ' '.join(div.attrs["class"][0:2])

                """ not needed at the moment. If navbar Class gets changing in time, this function is gonna be important
            def subNavbarClassExtractor():
                funcOpener(URLForSubNavbar, self.NavbarLink, sourceType = "Inspector")
                soup = BS(self.MenuContent,"html.parser")
                tag = soup.select_one("html>body>div:nth-of-type(1)>div:nth-of-type(1)>div>div>div>div>main>div>div>div>div>div:nth-of-type(3)>div>nav")
                return ' '.join(tag.attrs["class"]) 
                """
                
            ProductMenuXPath = "html>body>div>div:nth-of-type(1)>div>div>div>div>main>div>div>div>div>div:nth-of-type(3)>div>div>section>div"
            def productsDivClassExtractor():
                funcOpener(URLForSubNavbar, self.NavbarLink, sourceType = "Inspector")
                soup = BS(self.MenuContent,"html.parser")
                tag = soup.select_one(ProductMenuXPath)
                return ' '.join(tag.attrs["class"][0:2])
            
            return [subMenuClassExtractor(), productsDivClassExtractor()] # subNavbarClassExtractor(),
        
        
        classContents = getContent(self.DynamicInputsPath, readType =  "readlines")
        self.subMenuClass, self.productsMenuClass = classContents


        if not os.path.exists(r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Products\Sources"):
            os.mkdir(r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Products\Sources")

        self.UnknownPage = False
        self.UnknownPageCount = 0
        self.Robot = False

        self.Links = list(set(self.getFileContent(self.AllDepsTXTPath)).copy())
       
        for currentLink in self.Links:

            def MainLoop(linkInput):
                """
                MainLoop takes all links one by one and
                extracts requested data accordingly
                """

                linkInput = linkInput.rstrip()
                
                def defineMenuName(link):
                    rawLocation = (link.replace(WMURL,"")).replace("\n","")
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

                    if not re.findall("[0-9]",tempList[(len(tempList)*-1)+1]):
                        name = " ".join(tempList[0:2])
                    else:
                        name = tempList[0]
                    return name.strip().capitalize()

                self.currentPageName = defineMenuName(linkInput)

                if not linkInput.startswith("https://www.walmart.com"):
                    # if link given is wrong, resets gc and reloads from next item
                    self.gc.close()
                    del self.gc
                    time.sleep(10)
                    print("gc is resetted")
                    self.gc = GeneralControls()
                    return 1

                self.gc.openURL(linkInput)
                time.sleep(2.5)
                pag.run("g1877, 169 c")
                pContent = self.gc.returnPageSourceStrFromInspector()
                soup =  BS(pContent,"html.parser")
                
                #static robotOrHuman solver:
                if not type(soup.find("h1")) == type(None):
                    if soup.find("h1").text.strip().lower() == "Robot or human?".lower(): # RobotOrHuman.txt
                        pag.run("g960,500")
                        pag.mouseDown()
                        pag.sleep(8)
                        pag.mouseUp()
                        pag.run("c")
                        time.sleep(10)
                        return MainLoop(linkInput)
                #dynamic robotOrHuman solver:
                dynamicRobotXPath = "html>body>div:nth-of-type(2)>div>div:nth-of-type(3)>div:nth-of-type(1)>div"
                if not type(soup.select_one(dynamicRobotXPath)) == type(None):
                    for i in soup.select_one(dynamicRobotXPath).find("p"):
                        if i.text == "Activate and hold the button to confirm that you're human. Thank You!":
                            pag.run("g 960,600")
                            pag.mouseDown()
                            pag.sleep(8)
                            pag.mouseUp()
                            pag.run("c")
                            time.sleep(10)
                            print("Robot Check Dynamic Is Passed!") 
                        else:
                            print("Robot Check Dynamic Is Not Found!")
                #Sorry for technical issues solver:
                issuesXPath = "html>body>div:nth-of-type(1)>div:nth-of-type(1)>div>div>div>div>main>div>span"
                if not type(soup.select_one(issuesXPath)) == type(None):
                    if soup.select_one(issuesXPath).text.__contains__("having technical issues"):
                        return MainLoop(linkInput)
                    
                subMenu = soup.findAll("div",{"class":self.subMenuClass})
                if subMenu:
                    self.UnknownPage = False

                    extractedLinks = []
                    subClass = "w_CI w_DH"
                    subClassesList = soup.findAll("div",{"class":subClass})
                    for i in subClassesList:
                        if i.findAll("a"):
                            for k in i.findAll("a"):
                                extractedLinks.append(k["href"])
                        else:
                            print("Can't find products under subMenu!!")
                    self.Links.extend(x for x in extractedLinks if x not in self.Links)

                else:

                    navbar = soup.find("nav",{"class":"mt6 mb5"})
                    if navbar:
                        """
                        If page has a navbar for products,
                        Extract page source
                        """

                        self.UnknownPage = False

                        if overWrite == True:
                            folderName = self.SourcesPath+"/"+self.currentPageName
                            if os.path.exists(folderName):
                                if len(os.listdir(folderName)) == 25:
                                    return 0

                        # creating a folder for same group of products
                        folderName = self.SourcesPath+"/"+self.currentPageName
                        if not os.path.exists(folderName):
                            os.mkdir(self.SourcesPath+"/"+self.currentPageName)

                        time.sleep(0.3)

                        

                        navbarList = (navbar.find("ul")).findAll("li")
                        
                        tempLinks = [linkInput]

                        if len(navbarList) > 2:
                            productPageCount = int(navbarList[-2].text)+1
                            for count in range(2, productPageCount):
                                tempLinks.append(linkInput+f"?page={count}")

                        for i in range(len(tempLinks)):
                            self.gc.openURL(tempLinks[i])
                            time.sleep(2.2)
                            pag.run("g1877, 169 c")
                            pContent = self.gc.returnPageSourceStrFromInspector()
                            writeToFile(pContent,self.SourcesPath+"/"+self.currentPageName+"/"+str(i+1)+".txt")
                            time.sleep(0.2)
                        #print("NAVBAR PASSED")
                        
                    else:

                        if self.UnknownPage == True:
                            print("There is an Unknown Page. Count: "+str(self.UnknownPageCount))
                            print("Unknown Page URL: "+linkInput)
                            self.UnknownPageCount += 1
                            self.UnknownPage = False
                            self.problemLinks.append(linkInput)
                            writeToFile(self.problemLinks,problemLinks,"writelines")

                        else:
                            self.UnknownPage = True
                            newClass = newDynamicInputTaker()
                            writeToFile(newClass, self.DynamicInputsPath, "writelines")
                            self.loadClassAttrs()
                            return MainLoop(linkInput)
                print("Link input is passed: " +currentLink)
            MainLoop(currentLink)

        #gc.finalize()       
                        

        return print("Mission Accomplished")




AllDepsLink = r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Products\ProductsLink.txt"
class reArranger():

    def __init__(self):
        self.oldContent = self.getContent()

    def getContent(self, reArrangeFilePath = AllDepsLink):
        with open(reArrangeFilePath,"r+",encoding="utf-8") as f1:
            icontent = f1.readlines()
        return icontent
    
    def reArranger(self):
        newContent = []
        for i in self.oldContent:
            if i.startswith("https://www.walmart.com/"):
                newContent.append(i)

            elif i.startswith("/browse/"):
                newContent.append("https://www.walmart.com"+i)

            elif i.startswith("/cp/"):
                newContent.append("https://www.walmart.com"+i)

            elif i.startswith("browse/"):
                newContent.append("https://www.walmart.com/"+i)

            else:
                print("This link is unuseable: \n"+i)
        return newContent

    def placeNewContent(self):
        Ncontent = self.reArranger()
        with open(AllDepsLink,"w",encoding="utf-8") as f1:
            f1.writelines(Ncontent)
        return print("New content is written")
#reArranger().placeNewContent()



m= Main()
m.TotalMission(overWrite = True)
endTime = time.ctime()
print(startTime)
print(endTime)



"""


try:
    m = Main()
    m.TotalMission()
except Exception as err:

    endTime = time.ctime()
    print(err)
    print(startTime)
    print(endTime)
    

"""
