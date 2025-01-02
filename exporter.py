import json

with open("backup.json", "r") as file:
    data = json.load(file)

groups = data["groups"]

for g in groups:
    title = g["title"]
    tabs = g["tabs"]
    amountTabs = len(tabs)

    tabsToOpen = []

    fileName = f"files/{g['title']}.txt"
    with open(filename, "w") as file:
        counter = 0
        for tab in tabs:
            file.write(f"{counter} {tab['url']}\n")
            tabsToOpen.append(f"{counter} {tab['url']}\n")
            counter += 1
