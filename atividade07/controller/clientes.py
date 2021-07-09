from flask import request

from atividade07 import app
from atividade07.controller import objeto_json, response
from atividade07.model import banco_adicionar, banco_remover, select_objeto
from atividade07.model.tabelas import Cliente


@app.route('/clientes', methods=["GET"])
def ler_clientes():
    clientes_json = objeto_json(Cliente.query.all())

    return response(200, 'clientes', clientes_json, 'Todos os clientes')


@app.route('/cliente/<int:id_cliente>', methods=["GET"])
def ler_cliente(id_cliente):
    try:
        cliente = select_objeto(Cliente, id_cliente)
        cliente_json = objeto_json(cliente)

        return response(200, 'cliente', cliente_json, 'Cliente selecionado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'ID inválido')


@app.route('/cliente', methods=["POST"])
def criar_cliente():
    try:
        body = request.json

        cliente = Cliente(body['nome'], body['codigo'], body['cpf'], 'pessoa fisica')
        banco_adicionar(cliente)
        cliente_json = objeto_json(cliente)

        return response(201, 'cliente', cliente_json, 'Cliente criado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não criado')


@app.route('/cliente/<int:id_cliente>', methods=["PUT"])
def atualizar_cliente(id_cliente):
    try:
        body = request.json
        cliente = select_objeto(Cliente, id_cliente)

        cliente.nome = body['nome']
        cliente.codigo = body['codigo']
        cliente.cnpjcpf = body['cpf']
        banco_adicionar(cliente)

        cliente_json = objeto_json(cliente)
        return response(200, 'cliente', cliente_json, 'Cliente atualizado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não atualizado')


@app.route('/cliente/<int:id_cliente>', methods=["DELETE"])
def deletar_cliente(id_cliente):
    try:
        cliente = select_objeto(Cliente, id_cliente)

        banco_remover(cliente)
        cliente_json = objeto_json(cliente)
        return response(200, 'cliente', cliente_json, 'Cliente deletado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não deletado')
