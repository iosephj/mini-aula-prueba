from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor funcionando"

@app.route('/guardar', methods=['POST'])
def guardar():
    data = request.get_json()
    with open('respuestas.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([data['fecha'], data['alumno'], data['ejercicio'], data['respuesta'], data['correcto']])
    return 'OK', 200

app.run(host="0.0.0.0", port=81)
