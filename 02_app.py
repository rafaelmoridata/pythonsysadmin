#!/usr/local/bin/python3

from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')

def home():
    print('Minha nossa!')
    #return 'Você acessou esta magnifica API'
    #return jsonify({'status' : 'Running...'})
    return json.dumps({'status' : 'Running...'})

app.run(host='0.0.0.0', debug=True)
