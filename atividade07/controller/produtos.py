from flask import request

from atividade07 import app
from atividade07.controller import objeto_json, response
from atividade07.model import banco_adicionar, banco_remover, select_objeto
from atividade07.model.tabelas import Produto


@app.route('/produtos', methods=["GET"])
def ler_produtos():
    protudos_json = objeto_json(Produto.query.all())

    return response(200, 'produtos', protudos_json, 'Todos os produtos')


@app.route('/produto/<int:id_produto>', methods=["GET"])
def ler_produto(id_produto):
    try:
        produto = select_objeto(Produto, id_produto)
        produto_json = objeto_json(produto)

        return response(200, 'produto', produto_json, 'Produto selecionado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'ID inválido')


@app.route('/produto', methods=["POST"])
def criar_produto():
    try:
        body = request.json

        produto = Produto(body['codigo'], body['descricao'], body['valor-unitario'])
        banco_adicionar(produto)
        produto_json = objeto_json(produto)

        return response(201, 'produto', produto_json, 'Produto criado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não criado')


@app.route('/produto/<int:id_produto>', methods=["PUT"])
def atualizar_produto(id_produto):
    try:
        body = request.json
        produto = select_objeto(Produto, id_produto)

        produto.codigo = body['codigo']
        produto.descricao = body['descricao']
        produto.valor_unitario = body['valor-unitario']
        banco_adicionar(produto)

        produto_json = objeto_json(produto)
        return response(200, 'produto', produto_json, 'Produto atualizado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não atualizado')


@app.route('/produto/<int:id_produto>', methods=["DELETE"])
def deletar_produto(id_produto):
    try:
        produto = select_objeto(Produto, id_produto)
        banco_remover(produto)

        produto_json = objeto_json(produto)
        return response(200, 'produto', produto_json, 'Produto deletado')
    except Exception as e:
        print(e)
        return response(400, 'produto', {}, 'Produto não deletado')
