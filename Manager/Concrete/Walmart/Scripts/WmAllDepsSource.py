

from Abstract import *

#from datetime import datetime as dt



WalmartURL = "https://www.walmart.com/"
WmAllDepsURL = "https://www.walmart.com/all-departments"



gc = GeneralControls()
gc.openURL(WmAllDepsURL)

gc.exportPageSource(r"C:\Users\Lenovo\source\repos\Manager\Manager\Concrete\Walmart\Saves\WmAllDeps=.txt")




