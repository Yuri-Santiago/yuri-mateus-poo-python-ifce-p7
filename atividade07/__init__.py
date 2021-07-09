from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from controller import clientes
from controller import produtos
from controller import notas_fiscais
from controller import itens_notafiscal

from atividade07.model import tabelas
