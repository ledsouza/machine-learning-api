from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth

from textblob import TextBlob
from googletrans import Translator

import pickle
import numpy as np
from sklearn.linear_model import LinearRegression


def get_model() -> LinearRegression:
    filename = 'modelo.pkl'
    modelo = pickle.load(open(filename, 'rb'))
    return modelo


modelo = get_model()

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'leandro'
app.config['BASIC_AUTH_PASSWORD'] = 'admin'

basic_auth = BasicAuth(app)


@app.route("/")
def home():
    return "<p>Hello, World!</p>"


@app.route("/sentimento/<frase>")
def sentimento(frase):
    translator = Translator()
    frase_en = translator.translate(frase)
    tb = TextBlob(frase_en.text.replace("-", " "))
    polaridade = tb.sentiment.polarity
    return f"<h2>Polaridade: {polaridade}</h2>"


@app.route("/cotacao/", methods=["POST"])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    colunas = ["tamanho", "ano", "garagem"]
    input = [dados[col] for col in colunas]

    preco = modelo.predict([input])
    return jsonify(preco=preco[0])
