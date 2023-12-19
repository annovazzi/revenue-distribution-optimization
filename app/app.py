# app/app.py

from flask import render_template
from app import app

@app.route('/')
def index():
    # Adicione a lógica para exibir a página inicial aqui
    return render_template('index.html')
