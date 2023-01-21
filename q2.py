import json

with open("q2.json","r") as inF:
    content = json.load(inF)
reversed  = []
for x in content:
    reversed = [x] + reversed

with open("savingfile.txt", "w") as fifi:
    json.dump(reversed,fifi)
   


