from flask import Flask, render_template, redirect, url_for, request
import pymongo
from ubidots import ApiClient

app = Flask(__name__)

API_TOKEN = "BBFF-thUhhRPJojoHiUB78bozuZuPy2dKTv"
LABEL_TOMBOL = "64cb734bdfc2f3000b9aec5b"
api = ApiClient(token=API_TOKEN)
variable_tombol1 = api.get_variable(LABEL_TOMBOL)

@app.route('/')
def front():
    return render_template('front.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/suhu', methods=('GET','POST'))
def suhu ():
    for dataSuhu in inputSuhu.find().sort([('_id', -1)]).limit(1):
        tempMax = dataSuhu["tempHi"]
        tempMin = dataSuhu["tempLo"]

    if request.method == "POST":
        tempHi = request.form["tempHi"]
        tempLo = request.form["tempLo"]
        inputSuhu.insert_one({"tempHi":tempHi, "tempLo":tempLo})
        return redirect(url_for('suhu'))
        
    return render_template("suhu.html", tempMax=tempMax, tempMin=tempMin)

def toggle_value(current_value):
    if current_value == 0:
        return 1
    else:
        return 0

@app.route('/daya', methods=('GET','POST'))
def daya():
    if request.method == 'POST':
        current_value = variable_tombol1.get_values(1)[0]['value']
        new_value = toggle_value(current_value)
        variable_tombol1.save_value({'value': new_value})

    current_value = variable_tombol1.get_values(1)[0]['value']
    return render_template("daya.html",current_value=current_value)


@app.route('/laporan')
def laporan():
    return render_template('laporan.html')

@app.route('/pakan', methods=('GET','POST'))
def edit(): 
    for dataPakan in inputPakan.find().sort([('_id', -1)]).limit(1)  :
        jamPakan = dataPakan["jamPakan"]
        jamPakan2 = dataPakan["jamPakan2"]
        jamPakan3 = dataPakan["jamPakan3"]

    if request.method == "POST":
        pakan = request.form["jamPakan"] + ":00"
        pakan2 = request.form["jamPakan2"] + ":00"
        pakan3 = request.form["jamPakan3"] + ":00"
        inputPakan.insert_one({"jamPakan":pakan, "jamPakan2":pakan2,"jamPakan3":pakan3})
        return redirect(url_for('edit'))
        
    return render_template("pakan.html", jamPakan=jamPakan, jamPakan2=jamPakan2, jamPakan3=jamPakan3)




if __name__ == '__main__':
    app.run(debug=True)

