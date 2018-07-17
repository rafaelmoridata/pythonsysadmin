#!/usr/local/bin/python3

# Criar uma rota chamada "acessos" que retorna um json contendo 
# a data atual, e um contador que terá valor (por enquanto)
# {'date' : '2018-07-13', 'count' : 0}

from flask      import Flask, jsonify
from datetime   import datetime
import json

app = Flask(__name__)

def write_file_cont(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as f:
            contador = f.read()
            if contador == '':
                contador = 1
            else:
                contador = int(contador) + 1
        with open(nome_arquivo, 'w') as f:
            f.write(str(contador))
            #return f.readlines()
        return contador
    except Exception as e:
        return "Erro: {}".format(e)



@app.route('/')
def home():
    write_file_cont('03_app_route.txt')
    return jsonify({'status' : 'Running...'})


@app.route('/acessos') # http://192.168.205.71:5000/acessos
def acessos():
    c = write_file_cont('03_app_route.txt')
    date = datetime.now().strftime('%Y%m%d_%H%I%S')
    return jsonify({'date' : date, 'count' : c})


# Toda vez que uma rota for acessada, abrir um arquivo de texto e
# incrementar +1 no valor dentro do arquivo
# Quando acessar a rota /acessos retornar este valor em count
# with open, function, 


app.run(host='0.0.0.0', debug=True)
