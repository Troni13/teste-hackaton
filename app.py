from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Tenta ler a variável de ambiente DATABASE_URL. Se não achar, mostra a mensagem padrão.
    db_status = os.getenv('DATABASE_URL', 'Banco não conectado (Rodando apenas o Flask)')
    return f"<h1>Mascote da Turma - Atualização automática funcionando!</h1><p>Status: {db_status}</p>"

if __name__ == '__main__':
    # Importante: host 0.0.0.0 permite que o container exponha a porta para o mundo
    app.run(host='0.0.0.0', port=5000)