from flask import Flask, Response, request
import pandas as pd
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

file_to_open = open("models/baummethoden.pickle", "rb")
trained_model = pickle.load(file_to_open)
file_to_open.close()


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/hello_world")
def hello_world():
    return "<h1>test</h1> <p>Hello, World!</p>"


@app.route("/training_data")
def training_data():
    data = pd.read_csv("data/auto-mpg.csv", sep=";")
    return Response(data.to_json(), mimetype="application/json")


@app.route("/predict")
def predict():
    zylinder = request.args.get("zylinder")
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")

    feature_names = ["zylinder", "ps", "gewicht", "beschleunigung", "baujahr"]

    input_data = pd.DataFrame(
        [[zylinder, ps, gewicht, beschleunigung, baujahr]], columns=feature_names
    )
    prediction = trained_model.predict(input_data)

    return {"result": prediction.item(0)}
