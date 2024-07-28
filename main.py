from flask import Flask

from textblob import TextBlob
from googletrans import Translator

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
