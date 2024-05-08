
import os
import pandas as pd
import whisper
from spleeter.separator import Separator
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/separar')
def separarPista():
    
    musica = "C:/P2/throwback.mp3"  # Ruta del archivo de audio
    separator = Separator('spleeter:2stems')  # Inicializar el separador con el modelo de 2 stems
    separator.separate_to_file(musica, "C:/P2/")  # Separar las pistas y guardarlas en la carpeta especificada
    return "Pistas separadas con éxito"

@app.route('/saludar')
def saludar():
    return"hola"

if __name__ == '__main__':
    app.run(debug=True)

