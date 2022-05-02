
import os

filePath = "C:/Users/Lenovo/Desktop/NewFile.txt"


def createNewFile(info: str, path = filePath, writeType="write"):
    if os.path.exists(path):
        return print("File Already exists")
    else:
        with open(path,"x",encoding="utf-8") as f1:
            if writeType == "write":
                f1.write(info)
            elif writeType == "writelines":
                f1.writelines(i+"\n" for i in info)
        return print(f"Created and written on: {path.split('/')[-1]}")


def writeToFile(info: str, path = filePath, writeType="write"):
    if not os.path.exists(path):
        return createNewFile(info, path, writeType)
    else:
        with open(path,"w+",encoding="utf-8") as f1:
            if writeType == "write":
                f1.write(info)
            elif writeType == "writelines":
                f1.writelines(i+"\n" for i in info)
    return print(f"Written on: {path.split('/')[-1]}")


def getContent(path, readType = "read"):
    if readType == "read":
        with open(path,"r",encoding="utf-8") as f1:
            return f1.read()

    elif readType == "readlines":
        with open(path,"r",encoding="utf-8") as f1:
            return f1.readlines()



