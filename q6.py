import json
from matplotlib import pyplot as plt
from datetime import datetime

with open("golddata.json.txt","r") as inF:
    content = json.load(inF)

us_prices = [x['United States(USD)'] for x in content] 
south_africa_prices = [s['South Africa(ZAR)'] for  s in content] 

us_2010 = [x['United States(USD)'] for x in content if datetime.strptime(x['Date'],'%d-%m-%Y').year == 2010]
south_africa_2010 = [x['South Africa(ZAR)'] for x in content]


date_list = [datetime.strptime(x['Date'],'%d-%m-%Y') for x in content]


plt.xlabel('Years')
plt.ylabel('Prices (USD)')
plt.bar(date_list,us_prices)
plt.show()


plt.xlabel('Years')
plt.ylabel('Prices (ZAR)')
plt.bar(date_list,south_africa_prices)
plt.show()