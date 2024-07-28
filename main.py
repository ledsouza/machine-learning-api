from flask import Flask

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


@app.route("/cotacao/<int:tamanho>")
def cotacao(tamanho):
    tamanho = np.array(tamanho).reshape(-1, 1)
    preco = modelo.predict(tamanho)[0]
    return f"{preco}"
