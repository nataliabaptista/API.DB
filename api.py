from flask import Flask, jsonify
from pymongo import MongoClient
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Conexão MongoDB
client = MongoClient('mongodb+srv://nataliabaptista:aquila12@clusterapp.d9hcl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
DB = client['db-dicas-roca']

@app.route('/')
def pagina_inicial():
    return '<h1>API Dicas da Roça</h1>'

@app.route('/despesa/<string:nome>/<float:valor>')
def infosdesp(nome, valor):
    data = {
        "nome": nome,
        "valor": valor
    }
    DB.despesas.insert_one(data)
    return "OK"

@app.route('/faturamento/<string:nome>/<float:valor>')
def infosfatur(nome, valor):
    data = {
        "nome": nome,
        "valor": valor
    }
    DB.faturamentos.insert_one(data)
    return "OK"

@app.route('/find/despesas/<string:nome>/')
def findDespesas():
    listDespesas=[]
    for x in DB.despesas.find({}):
        dictDespesas={
            'nome':x['nome'],
            'valor':x['valor']
        }
        listDespesas.append(dictDespesas)
    return jsonify(listDespesas)

@app.route('/find/faturamentos/')
def findFaturamentos():
    listFaturamentos=[]
    for x in DB.faturamentos.find({}):
        dictFaturamentos={
            'nome':x['nome'],
            'valor':x['valor']
        }
        listFaturamentos.append(dictFaturamentos)
    return jsonify(listFaturamentos)

# Start flask program
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
