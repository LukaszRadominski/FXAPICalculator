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
            if row['code'] == currency_type:
                course = row['bid']
                result=float(course)*float(currency_amount)
                return render_template("fxcalculator.html", result=result) 
    return currency_type 

if __name__ == '__main__':  
    app.run(debug=True) 









