

from bs4 import BeautifulSoup as BS

"""
Imports products link to /Products/ProductsLink.txt
Links can be in {www.walmart....} for or after {.com}, {/....} form
"""

filePath = r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Saves\WmAllDeps=.txt"
def getFileContent():
    with open(filePath,"r") as dataFile:
        content = dataFile.read()
    return content



def extractLinks(content = getFileContent()):
    iContent = ""
    soup = BS(content,"html.parser")

    reqElements = soup.findAll("div",{"class":"w_CC"})
    
    #print(len(reqElements)) == 21
    
    for i in reqElements:
        for k in i.ul.find_all("li"):
            iContent += (k.a['href']+"\n")

    with open(r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Products\ProductsLink.txt","w+") as File:
        File.write(iContent)
    
extractLinks()
