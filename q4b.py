import json

with open("buildings.json.txt","r") as inF:
    content = json.load(inF)

floating = [x['height'] for x in content]
above_five = [s for s in floating if s > 5]
length_above_five = len(above_five)
sum_above_five = sum(above_five)
average_above_five = sum_above_five/length_above_five
print(average_above_five)