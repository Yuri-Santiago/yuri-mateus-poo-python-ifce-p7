from flask import request

from atividade07 import app
from atividade07.controller import objeto_json, response
from atividade07.model import select_objeto, banco_adicionar, banco_remover
from atividade07.model.tabelas import ItemNotaFiscal, NotaFiscal, Produto


@app.route('/itensnf/<int:id_nota>', methods=["GET"])
def ler_itens(id_nota):
    try:
        itens_nota = select_objeto(NotaFiscal, id_nota).itens
        itens_json = objeto_json(itens_nota)

        return response(200, 'itens', itens_json, 'Todos os itens da nota')
    except Exception as e:
        print(e)
        return response(400, 'itens', {}, 'ID inválido')


@app.route('/itemnf/<int:id_item>', methods=["GET"])
def ler_item(id_item):
    try:
        item = select_objeto(ItemNotaFiscal, id_item)
        item_json = objeto_json(item)

        return response(200, 'itens', item_json, 'Itens da nota')
    except Exception as e:
        print(e)
        return response(400, 'itens', {}, 'ID inválido')


@app.route('/itemnf', methods=["POST"])
def criar_item():
    try:
        body = request.json
        produto = select_objeto(Produto, body['produto'])
        item = ItemNotaFiscal(body['sequencial'], body['quantidade'], body['nota'], produto)
        item_json = objeto_json(item)
        banco_adicionar(item)

        return response(201, 'item', item_json, 'Item criado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não criado')


@app.route('/itemnf/<int:id_item>', methods=["PUT"])
def atualizar_item(id_item):
    try:
        body = request.json
        item = select_objeto(ItemNotaFiscal, id_item)

        item.sequencial = body['sequencial']
        item.quantidade = body['quantidade']
        banco_adicionar(item)
        item_json = objeto_json(item)
        return response(200, 'item', item_json, 'Item atualizado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não atualizado')


@app.route('/itemnf/<int:id_item>', methods=["DELETE"])
def deletar_item(id_item):
    try:
        item = select_objeto(ItemNotaFiscal, id_item)
        banco_remover(item)

        item_json = objeto_json(item)
        return response(200, 'item', item_json, 'Item deletado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não deletado')
