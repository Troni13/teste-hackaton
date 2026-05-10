import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# --- CONFIGURAÇÃO DO BANCO ---
# O Dokploy/IFSP envia a URL via DATABASE_URL. 
# Se não existir, ele cria o arquivo mascote_local.db no seu PC.
database_uri = os.getenv('DATABASE_URL')

if database_uri and database_uri.startswith("postgres://"):
    # Correção necessária para versões recentes do SQLAlchemy
    database_uri = database_uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri or 'sqlite:///mascote_local.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- MODELO DE EXEMPLO (Mascote) ---
class Mascote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    nivel = db.Column(db.Integer, default=1)
    energia = db.Column(db.Integer, default=0)

# Criar o banco na primeira execução
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return "Banco conectado com sucesso!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
