from flask import Flask, jsonify
from pymongo import MongoClient
import os
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)
# Conexão MongoDB
client = MongoClient('mongodb+srv://nataliabaptista:aquila12@clusterapp.d9hcl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
DB = client['db-dicas-roca']

@app.route('/')
def pagina_inicial():
    return '<h1>Hello!</h1>'

@app.route('/despesa/<string:nome>/<float:valor>')
def infosdesp(nome, valor):
    data = {
        "nome": nome,
        "valor": valor
    }
    DB.despesas.insert_one(data)
    return "OK"


# Start flask program
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
