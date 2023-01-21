import json


with open("buildings.json.txt","r") as inF:
    content = json.load(inF)

i = 1
for x in content:
    x["Unique id number"] = i
    i = i+1
with open("updated.txt", "w") as fifi:
    json.dump(content,fifi)
   