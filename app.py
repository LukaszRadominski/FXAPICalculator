# KROK 3: Drugą będzie prosty kalkulator walut. Postaraj się stworzyć formularz, w którym umieścisz pole typu select.
# Powinno ono zawierać kody walut, np. na podstawie poprzedniego zapytania do banku. 
# Jak działa taki select możesz sprawdzić np. tutaj.

# Powinno być jeszcze drugie pole, w którym wpiszemy, ile danej waluty chcemy kupić.
# Po kliknięciu w przycisk “Przelicz”, powinien nam się wyświetlić koszt takiej operacji w złotówkach (PLN).
# Postaraj się o estetyczny wygląd aplikacji.
# Kod umieść w serwisie GitHub i prześlij link Mentorowi, niech sprawdzi, czy już rwać włosy z głowy z powodu kursu franka szwajcarskiego.



from flask import render_template, Flask, url_for, request 
import csv 

app = Flask(__name__)  

@app.route("/fx")  
def simple(): 
    return render_template("fxcalculator.html") 

#with open('FX.csv', newline='') as csvfile:
#    reader = csv.DictReader(csvfile, delimiter =";") 
#    for row in reader:
#        print(row['code'], row['bid'])


@app.route("/calculate", methods=["post"]) 
def calculate():
    currency_type=request.form["currencyType"]
    currency_amount = int(request.form["currencyAmount"])  
    with open('FX.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter =";") 
        for row in reader:
            if row['currency']== currency_type:
                course = row['bid']
                result=course*currency_amount
            else:
                return "There is an error"
    
# if currency_type=="dolar amerykański": 
#        result=currency_amount*10
#    elif currency_type=="euro":
#        result=currency_amount*50
#    else:
#        return "There is an error"
    return render_template("fxcalculator.html", result=result)




if __name__ == '__main__':  
    app.run(debug=True) 









