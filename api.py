from flask import Flask, jsonify
from pymongo import MongoClient
import os
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)


@app.route('/')
def pagina_inicial():
    return '<h1>Hello!</h1>'

@app.route('/valordesp/<double:valor>')
def precodesp(valor):
    return f'O valor da despesa é {valor} reais.'

# Start flask program
if __name__=="__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
