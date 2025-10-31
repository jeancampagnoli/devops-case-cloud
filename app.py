from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Uma variável de ambiente para mostrar a atualização
    version = os.environ.get('APP_VERSION', '1.0')
    return f"<h1>Olá! Bem-vindo ao Case DevOps e Cloud!</h1><p>Versão da Aplicação: {version}</p>"

@app.route('/health')
def health_check():
    # Rota para o monitoramento verificar se a app está no ar
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)