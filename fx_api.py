import requests
import csv

# KROK 1  metoda request do pobrania danych z API NBP
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()


        # To, co mamy w data jest już pythonowym obiektem. Nawet nie musimy bawić się w operacje przy pomocy json.
print("\n LISTA SŁOWNIKÓW Z NBP \n")
print(type(data))
print(data)

# KROK 2 Trzeba z nich wybrać listę rates i na jej podstawie stworzyć plik csv. Plik ten powinien mieć następujące kolumny:
# currency;code;bid;ask  # Jako separator ustaw znak średnika, czyli ;.

        
print("\n PIERWSZY  i jedyny ELEMENT Z LISTY TO SŁOWNIK \n")
d_data = data[0]
print(type(d_data))
print(d_data)  


print("\n ZE SŁOWNIKA POBIERAM WARTOŚC PO KLUCZU RATES , KTÓRY JEST LISTĄ SŁOWNIKÓW\n")
rates_list=d_data['rates']
print(type(rates_list))
print(rates_list)


print("\n z LISTY_SŁOWNIKÓW ROBIĘ ODDZIELNE LISTY \n")
# help desk - zapisywanie danych do pliku CSV : https://www.youtube.com/watch?v=jKibaYZWtkE
# with open("C:\Users\p7\KODILLADWA\AU_FirstAPI_STUDY\RATES.txt",'w',newline='') as file: 

#with open - pozwana la otwierania i zapisywaniw w pliku 
# # najpierw podaję nazwę pliku lub ścieżke do niego, nastepnie tryb "w"-tu zapisuje +  zastępując nowa treścią, newline='' określa co bedie w kolejnym wierszu - tu nic
# as file - określa nazwę zmienej do ktora w kodzie bedzie odwoływała se do  naszego pliku

        # writer = csv.writer(file) #STOP NA PIERWSZYM FILMIE minuta  7,30: - MUSZE JESZCZE PRZEBUDOWAC LISTĘ JAK NA FILMNIE

# tworze obiekt który będdzie zapisywał do pliku (pochodzi z  modułu csv dlatego zaczyna się do csv)
# jako parametr podaję nazwę pliku ale parametrów może byc wiecej - jak najedziesz na writer to się wyświetli 


with open('FX.csv', 'w', newline='') as csvfile:
    fieldnames = ['currency', 'code', 'bid','ask'] 
    writer = csv.DictWriter(csvfile, delimiter =";",fieldnames=fieldnames) #  do ustawienia średnika użyto delimiter
    writer.writeheader()
    for index in rates_list: # dla każdego słownika z listy wstaw ....(podobnie w przykładzie AR CSVtest)
         writer.writerow({'currency': index.get('currency'), 'code':index.get('code'),'bid': index.get('bid'), 'ask':index.get('ask')})





#dodatkowo wydrukowałem: 
for index in rates_list:
        print(index.get('currency'))





# ODCZYT Z PLIKU CSV : https://www.youtube.com/watch?v=Z8HIhI-FZvg