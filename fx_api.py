import requests
import csv


response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json() 

d_data = data[0] 
  
rates_list=d_data['rates'] 

with open('FX.csv', 'w', newline='') as csvfile:
    fieldnames = ['currency', 'code', 'bid','ask'] 
    writer = csv.DictWriter(csvfile, delimiter =";",fieldnames=fieldnames) 
    writer.writeheader()
    for index in rates_list: 
         writer.writerow({'currency': index.get('currency'), 'code':index.get('code'),'bid': index.get('bid'), 'ask':index.get('ask')})





