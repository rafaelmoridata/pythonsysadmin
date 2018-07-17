#!/usr/local/bin/python3

# Criar uma rota chamada "acessos" que retorna um json contendo 
# a data atual, e um contador que terá valor (por enquanto)
# {'date' : '2018-07-13', 'count' : 0}

from flask      import Flask, jsonify #, request #, make_response
#from datetime   import datetime
#from bson.json_util       import dumps as bdumps
#import json

from blueprints.usuario import usuario
#from config.mongo import db

app = Flask(__name__)
app.register_blueprint(usuario)


@app.route('/')
def home():
    return jsonify({'status' : 'Running...'})

#@app.route('/findusers')
#def findusers():
#    return jsonify({'status' : 'Running...'})


#@app.route('/findusers')
#def findusers():
#    return jsonify([json.loads(bdumps(u)) for u in db.usuarios.find()])


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
