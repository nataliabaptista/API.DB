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

# Adicionando dados ao BD
@app.route('/despesa/<string:nome>/<float:valor>/<int:mes>/<int:ano>')
def infosdesp(nome, valor, mes, ano):
    data = {
        "nome": nome,
        "valor": valor,
        "mes": mes,
        "ano": ano,
    }
    DB.despesas.insert_one(data)
    return "OK"

@app.route('/faturamento/<string:nome>/<float:valor>/<int:mes>/<int:ano>')
def infosfatur(nome, valor, mes, ano):
    data = {
        "nome": nome,
        "valor": valor,
        "mes": mes,
        "ano": ano,
    }
    DB.faturamentos.insert_one(data)
    return "OK"

        ### Buscando dados do BD ###
# Busca com mês e ano
@app.route('/find/despesas/<int:mes>/<int:ano>')
def findDespesasma(mes, ano):
    listDespesas=[]
    for x in DB.despesas.find({'mes': mes, 'ano': ano}):
        dictDespesas={
            'nome':x['nome'],
            'valor':x['valor'],
            'mes':x['mes'],
            'ano':x['ano']
        }
        listDespesas.append(dictDespesas)
    return jsonify(listDespesas)

@app.route('/find/faturamentos/<int:mes>/<int:ano>')
def findFaturamentosma(mes, ano):
    listFaturamentos=[]
    for x in DB.faturamentos.find({'mes': mes, 'ano': ano}):
        dictFaturamentos={
            'nome':x['nome'],
            'valor':x['valor'],
            'mes':x['mes'],
            'ano':x['ano']
        }
        listFaturamentos.append(dictFaturamentos)
    return jsonify(listFaturamentos)
# Busca com ano
@app.route('/find/despesas/<int:ano>')
def findDespesasa(ano):
    listDespesas=[]
    for x in DB.despesas.find({'ano': ano}):
        dictDespesas={
            'nome':x['nome'],
            'valor':x['valor'],
            'mes':x['mes'],
            'ano':x['ano']
        }
        listDespesas.append(dictDespesas)
    return jsonify(listDespesas)

@app.route('/find/faturamentos/<int:ano>')
def findFaturamentosa(ano):
    listFaturamentos=[]
    for x in DB.faturamentos.find({'ano': ano}):
        dictFaturamentos={
            'nome':x['nome'],
            'valor':x['valor'],
            'mes':x['mes'],
            'ano':x['ano']
        }
        listFaturamentos.append(dictFaturamentos)
    return jsonify(listFaturamentos)
# Busca sem filtro
@app.route('/find/despesas')
def findDespesas(nome):
    listDespesas=[]
    for x in DB.despesas.find({'nome': nome}):
        dictDespesas={
            'nome':x['nome'],
            'valor':x['valor'],
            'mes':x['mes'],
            'ano':x['ano']
        }
        listDespesas.append(dictDespesas)
    return jsonify(listDespesas)

@app.route('/find/faturamentos')
def findFaturamentos(nome):
    listFaturamentos=[]
    for x in DB.faturamentos.find({'nome': nome}):
        dictFaturamentos={
            'nome':x['nome'],
            'valor':x['valor'],
            'mes':x['mes'],
            'ano':x['ano']
        }
        listFaturamentos.append(dictFaturamentos)
    return jsonify(listFaturamentos)







# Start flask program
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
