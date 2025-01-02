import os
import json

def main():
    backupFilename = "backup.json"
    with open(backupFilename, "r") as file:
        data = json.load(file)

    groups = data["groups"]

    for g in groups:
        title = g["title"]
        tabs = g["tabs"]
        amountTabs = len(tabs)

        tabsToOpen = []

        
        filePath = getFolderPath(g['title'])
        
        with open(filePath, "w") as file:
            counter = 0
            for tab in tabs:
                file.write(f"{counter} {tab['url']}\n")
                tabsToOpen.append(f"{counter} {tab['url']}\n")
                counter += 1


def getFolderPath(groupName):
    folderName = "files"
    fileName = f"{groupName}.txt"

    scriptDir = os.path.dirname(os.path.abspath(__file__))

    folderPath = os.path.join(scriptDir, folderName)
    filePath = os.path.join(folderPath, fileName)

    if not os.path.exists(folderPath):
        os.makedirs(folderPath)

    return filePath



if (__name__ == "__main__"):
    main()