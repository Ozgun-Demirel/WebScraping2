


from bs4 import BeautifulSoup as BS



from Abstract import *




path = r"C:\Users\Lenovo\source\repos\Manager\Manager\Chips.txt"


content = getContent(path)

soup  = BS(content,"html.parser")



productsMenuClass = "flex flex-wrap w-100 flex-grow-0 flex-shrink-0 ph2 pr0-xl pl4-xl mt0-xl mt3"

container = soup.find("div",{"class":productsMenuClass})

#links = container.findAll("a",{"class":"absolute w-100 h-100 z-1"})
links = container.findAll("a")

for i in links:
    print(i["link-identifier"])

print(len(links))


# From navbar Function:


