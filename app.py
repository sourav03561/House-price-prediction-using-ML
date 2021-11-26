from flask import Flask,request,redirect,url_for
import numpy as np
from joblib import  load
import pickle
from flask.templating import render_template

app = Flask(__name__)
@app.route("/<income>/<age>/<rooms>/<bed>/<population>")
def hello_world(income,age,rooms,bed,population):
    try:
        income = float(income)
        age = float(age)
        rooms = float(rooms)
        bed = float(bed)
        population = float(population)
        test_np_input = np.array([[income,age,rooms,bed,population]])
        model = pickle.load(open('model.sav','rb'))
        y_pred = model.predict(test_np_input)
        preds_as_str = str("{:.2f}".format(y_pred[0]))
        return render_template("index.html",predict=preds_as_str)
    except ValueError:
        return "Error"    

@app.route('/',methods=["POST", "GET"]) 
def home():
    if request.method == "POST":
        income = request.form["Income"]
        age = request.form["Age"]
        rooms = request.form["Rooms"]
        bed = request.form["Bed"]
        population = request.form["population"]
        return redirect(url_for("hello_world", income=income,age=age,rooms=rooms,bed=bed,population=population))
    else:
        return render_template("index.html")

if __name__ == '__main__':
	app.run(debug=True)
