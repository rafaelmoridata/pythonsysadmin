#!/usr/local/bin/python3

# Tentar printar o ID e o Nome dos usuarios
# Exibir somente os registros de ID par

import requests

#data = {"nome" : "Leonardo"}
#data = {"nome" : "Maria Madalena", "email" : "mamada@ig.com"}

response = requests.get('http://127.0.0.1:5000/usuarios')
data = response.json()

print('{0:.>10}{1:.>30}'.format('ID', 'NOME'))
for u in data['usuarios']:
    if u['id'] % 2 == 0:   # exibe somente id par
        print('{0:.>10}{1:.>30}'.format(u['id'], u['nome'])) # formatacao, preenche com ponto



#print(response.json())

#response = requests.post('http://127.0.0.1:5000/usuarios', json=data)
#response = requests.put('http://127.0.0.1:5000/usuarios/7', json=data)
#response = requests.put('http://127.0.0.1:5000/usuarios/7', json=data)

#Tentar executar a rota "delete" de um usuário qualquer

#print(response.json())
