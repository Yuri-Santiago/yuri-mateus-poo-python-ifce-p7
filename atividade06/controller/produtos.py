from flask import request

from atividade06 import app
from atividade06.controller import objeto_json, response, select_objeto
from atividade06.model import produtos
from atividade06.model.produto import Produto


@app.route('/produtos', methods=["GET"])
def ler_produtos():
    protudos_json = objeto_json(produtos)

    return response(200, 'produtos', protudos_json, 'Todos os produtos')


@app.route('/produto/<int:id_produto>', methods=["GET"])
def ler_produto(id_produto):
    try:
        produto = select_objeto(produtos, id_produto)
        produto_json = objeto_json(produto)

        return response(200, 'produto', produto_json, 'Produto selecionado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'ID inválido')


@app.route('/produto', methods=["POST"])
def criar_produto():
    try:
        body = request.json

        produto = Produto(produtos[-1].get_id() + 1, body['codigo'], body['descricao'], body['valor-unitario'])
        produtos.append(produto)
        produto_json = objeto_json(produto)

        return response(201, 'produto', produto_json, 'Produto criado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não criado')


@app.route('/produto/<int:id_produto>', methods=["PUT"])
def atualizar_produto(id_produto):
    try:
        body = request.json
        produto = select_objeto(produtos, id_produto)

        produto.set_codigo(body['codigo'])
        produto.set_descricao(body['descricao'])
        produto.set_valor_unitario(body['valor-unitario'])

        produto_json = objeto_json(produto)
        return response(200, 'produto', produto_json, 'Produto atualizado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não atualizado')


@app.route('/produto/<int:id_produto>', methods=["DELETE"])
def deletar_produto(id_produto):
    try:
        produto = select_objeto(produtos, id_produto)
        produtos.remove(produto)

        produto_json = objeto_json(produto)
        return response(200, 'produto', produto_json, 'Produto deletado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não deletado')
