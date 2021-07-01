from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

from controller import clientes
from controller import produtos
from controller import notas_fiscais
from controller import itens_notafiscal
