from flask import request

from atividade06 import app
from atividade06.controller import objeto_json, response, select_objeto
from atividade06.model import itens, notas, produtos
from atividade06.model.itemnotafiscal import ItemNotaFiscal


@app.route('/itensnf/<int:id_nota>', methods=["GET"])
def ler_itens(id_nota):
    try:
        itens_nota = select_objeto(notas, id_nota).get_itens()
        itens_json = objeto_json(itens_nota)

        return response(200, 'itens', itens_json, 'Todos os itens da nota')
    except Exception as e:
        print(e)
        return response(400, 'itens', {}, 'ID inválido')


@app.route('/itemnf/<int:id_item>', methods=["GET"])
def ler_item(id_item):
    try:
        item = select_objeto(itens, id_item)
        item_json = objeto_json(item)

        return response(200, 'itens', item_json, 'Itens da nota')
    except Exception as e:
        print(e)
        return response(400, 'itens', {}, 'ID inválido')


@app.route('/itemnf', methods=["POST"])
def criar_item():
    try:
        body = request.json
        produto = select_objeto(produtos, body['produto'])
        item = ItemNotaFiscal(itens[-1].get_id() + 1, body['sequencial'], body['quantidade'], produto)
        itens.append(item)
        item_json = objeto_json(item)

        return response(201, 'item', item_json, 'Item criado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não criado')


@app.route('/itemnf/<int:id_item>', methods=["PUT"])
def atualizar_item(id_item):
    try:
        body = request.json
        item = select_objeto(itens, id_item)

        item.set_sequencial(body['sequencial'])
        item.set_quantidade(body['quantidade'])

        item_json = objeto_json(item)
        return response(200, 'item', item_json, 'Item atualizado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não atualizado')


@app.route('/itemnf/<int:id_item>', methods=["DELETE"])
def deletar_item(id_item):
    try:
        item = select_objeto(itens, id_item)
        itens.remove(item)

        item_json = objeto_json(item)
        return response(200, 'item', item_json, 'Item deletado')
    except Exception as e:
        print(e)
        return response(400, 'item', {}, 'Item não deletado')
