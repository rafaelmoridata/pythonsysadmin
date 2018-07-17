#!/usr/local/bin/python3

from config.mongo import db
from flask import Blueprint, jsonify, request, make_response
from bson.json_util import dumps as bdumps
import json
#import jsonify

usuario = Blueprint('usuarios', __name__)

#data = {"nome" : "Leonardo"}
#data = {"nome" : "Maria Madalena", "email" : "mamada@ig.com"}

@usuario.route('/usuarios', methods=['GET', 'POST'])
def usuarios():
    # [{"nome" : "Jim Jones"}, {"nome" : "Charles Manson"}]
    #return 'Lista de usuarios'
    #return jsonify({"nome" : "Jim Jones"}, {"nome" : "Charles Manson"})
    if request.method == 'GET':
        return jsonify([json.loads(bdumps(u)) for u in db.usuarios.find()])
    else:
        usuario = request.get_json()
        keys = usuario.keys()
        for k in ('nome', 'email'):
            if k not in keys or not usuario[k].strip():
                return make_response(jsonify({'message' : 'Propriedade {0} obrigatória'.format(k)}), 400)
        #'nome' not in  usuario.keys() or not usuario['nome'].strip():
        #    return make_response(jsonify({'message' : 'Propriedade nome obrigatória'}), 400)
        #if 'email' not in  usuario.keys() or not usuario['email'].strip():
        #    return make_response(jsonify({'message' : 'Propriedade email obrigatória'}), 400)
        db.usuarios.insert(usuario)
        return jsonify({'message' : 'Usuário cadastrado com sucesso!'})