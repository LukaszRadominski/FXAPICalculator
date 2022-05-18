import requests
import csv

# 1  metoda request do pobrania danych z API NBP
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json() # list słowników z NBP

# 2 Wybór listy rates i na jej podstawie utworzenie  plik csv o  kolumnach:
# currency;code;bid;ask  # Jako separator ustawiony jest  znak średnika. 

d_data = data[0] # wybór pierwszego elementu z listy tj słownika
  
rates_list=d_data['rates'] # wybór wartośći z ww słownika wg klucza rates

# utworzenie pliku csv
with open('FX.csv', 'w', newline='') as csvfile:
    fieldnames = ['currency', 'code', 'bid','ask'] 
    writer = csv.DictWriter(csvfile, delimiter =";",fieldnames=fieldnames) 
    writer.writeheader()
    for index in rates_list: 
         writer.writerow({'currency': index.get('currency'), 'code':index.get('code'),'bid': index.get('bid'), 'ask':index.get('ask')})





