from flask import render_template, Flask, url_for, request 
import csv 

app = Flask(__name__)  

@app.route("/fx")  
def simple(): 
    return render_template("fxcalculator.html") 


@app.route("/calculate", methods=["POST"])     
def calculate():
    currency_type = request.form["currencyType"] 
    currency_amount = request.form["currencyAmount"] 
    with open('FX.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter =";") 
        for row in reader:
            print(row['code'])
            print(currency_type)
            if row['code'] == currency_type:
                course = row['bid']
                result=float(course)*float(currency_amount)
                print(course)
                print(result)
                return render_template("fxcalculator.html", result=result) 
            #else:
    return currency_type #"There is an error" # currency_amount # currency_type # "There is an error" 
   #  return render_template("fxcalculator.html", result=result) 



# PRÓBA  1 -   :
# currency_type = request.form["currencyType"]
#...............
# return currency_type > pod adresem  http://localhost:5000/calculate?currency_type=USD zwraca "dolar amerykański"
#  ale nie wykonuje pętli if row['currency']==currency_type:  >  wartość currency_type nie jest w row['currency']
#  gdy w miejsce currency_type: ,  wpisuję string np "dolar australijski" nadal nie wykonuje pętli if 

# ALE  poniższa funkcja działająca samodzielnine  -   zwraca wartośc "course"  poprawnie (przykład w readCSV.py)
# with open('FX.csv', newline='') as csvfile:
#    reader = csv.DictReader(csvfile, delimiter =";") 
#    for row in reader:
#        if row['currency']=="jen (Japonia)":
#            course = row['bid']
#            print(course)


# PRÓBA  2 - zmoiany w pliku HTML: ( app.py  - kod jak w  próbie 1)
# <form action="{{url_for('calculate')}}?currency_type=USD", method="post">  -  NIE DZIAŁA,

# <form action="{{url_for('calculate')}}?currencyType=USD", method="post">   -  NIE DZIAŁA,

# <form action="{{url_for('calculate')}}?currency_type=dolar amerykański", method="post">  -   NIE DZIAŁA,

# <form action="{{url_for('calculate')}}?currencyType=dolar amerykański", method="post">   -  NIE DZIAŁA, 

# <form action="{{url_for('calculate')}}?currency_type=currencyType", method="post">  -   NIE DZIAŁA,




# PRÓBA  3 - NIE DZIAŁA : 
# 1/ currency_type = request.form >>>  currency_type  to JSON file  {"currencyAmount": "1", "currencyType": "dolar ameryka\u0144ski"}
# 2/ d = json.loads(currency_type)  >>>>>>> utworzenie MultiDict 
# 3/ user_curency_type = d['currencyType'] >>>>>> pobranie z MultiDict danych wg klucza 





# IDEA 2 - sprawdź 
# if currency_type=="dolar amerykański": 
#        result=currency_amount*10
#    elif currency_type=="euro":
#        result=currency_amount*50
#    else:
#        return "There is an error"



# IDEA 4 - jak w ExampleLoginForm - najpierw przekazuję wszystkie dane do zmiennej data 
# a następnie z tej zmiennej pobieram to co potrzeba  

# @app.route("/calculate", methods=["post"]) 
# def calculate():
#    data = request.form
#    currency_type = data.get("currencyType")   # identyfikacja po name=....
# pozostałe bez zmian


# IDEA 5 
#with open('FX.csv', newline='') as csvfile:
#    reader = csv.DictReader(csvfile, delimiter =";") 
#    for row in reader:
#        print(row['code'], row['bid'])


if __name__ == '__main__':  
    app.run(debug=True) 









