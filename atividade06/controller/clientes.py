from flask import request

from atividade06 import app
from atividade06.controller import objeto_json, response, select_objeto
from atividade06.model import clientes
from atividade06.model.cliente import Cliente


@app.route('/clientes', methods=["GET"])
def ler_clientes():
    clientes_json = objeto_json(clientes)

    return response(200, 'clientes', clientes_json, 'Todos os clientes')


@app.route('/cliente/<int:id_cliente>', methods=["GET"])
def ler_cliente(id_cliente):
    try:
        cliente = select_objeto(clientes, id_cliente)
        cliente_json = objeto_json(cliente)

        return response(200, 'cliente', cliente_json, 'Cliente selecionado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'ID inválido')


@app.route('/cliente', methods=["POST"])
def criar_cliente():
    try:
        body = request.json

        cliente = Cliente(clientes[-1].get_id() + 1, body['nome'], body['codigo'], body['cpf'], 'pessoa fisica')
        clientes.append(cliente)
        cliente_json = objeto_json(cliente)

        return response(201, 'cliente', cliente_json, 'Cliente criado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não criado')


@app.route('/cliente/<int:id_cliente>', methods=["PUT"])
def atualizar_cliente(id_cliente):
    try:
        body = request.json
        cliente = select_objeto(clientes, id_cliente)

        cliente.set_nome(body['nome'])
        cliente.set_codigo(body['codigo'])
        cliente.set_cnpjcpf(body['cpf'])

        cliente_json = objeto_json(cliente)
        return response(200, 'cliente', cliente_json, 'Cliente atualizado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não atualizado')


@app.route('/cliente/<int:id_cliente>', methods=["DELETE"])
def deletar_cliente(id_cliente):
    try:
        cliente = select_objeto(clientes, id_cliente)
        clientes.remove(cliente)

        cliente_json = objeto_json(cliente)
        return response(200, 'cliente', cliente_json, 'Cliente deletado')
    except Exception as e:
        print(e)
        return response(400, 'cliente', {}, 'Cliente não deletado')
