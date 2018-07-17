from flask import Flask, jsonify
import json
from Blueprints.UsuariosView import usuarios
from Models.Model import db, app

app.register_blueprint(usuarios)

@app.route("/")
def hello():
    return jsonify({"version": 1.0, "message":"Bem vindos a explicação sobre APIs"})
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True,host="0.0.0.0")