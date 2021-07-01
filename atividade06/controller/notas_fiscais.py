from flask import request

from atividade06 import app
from atividade06.controller import objeto_json, response, select_objeto
from atividade06.model import notas, clientes
from atividade06.model.notafiscal import NotaFiscal


@app.route('/notasfiscais', methods=["GET"])
def ler_notas():
    notas_json = objeto_json(notas)

    return response(200, 'notas', notas_json, 'Todos as notas')


@app.route('/notafiscal/<int:id_nota>', methods=["GET"])
def ler_nota(id_nota):
    try:
        nota = select_objeto(notas, id_nota)
        nota_json = objeto_json(nota)

        return response(200, 'nota', nota_json, 'Nota selecionada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'ID inválido')


@app.route('/notafiscal', methods=["POST"])
def criar_nota():
    try:
        body = request.json

        cliente = select_objeto(clientes, body['cliente'])
        nota = NotaFiscal(notas[-1].get_id() + 1, body['codigo'], cliente)
        notas.append(nota)

        nota_json = objeto_json(nota)
        return response(201, 'nota', nota_json, 'Nota criada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não criada')


@app.route('/notafiscal/<int:id_nota>', methods=["PUT"])
def atualizar_nota(id_nota):
    try:
        body = request.json
        nota = select_objeto(notas, id_nota)
        cliente = select_objeto(clientes, body['cliente'])
        nota.set_codigo(body['codigo'])
        nota.setCliente(cliente)

        nota_json = objeto_json(nota)
        return response(200, 'nota', nota_json, 'Nota atualizada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não atualizada')


@app.route('/notafiscal/<int:id_nota>', methods=["DELETE"])
def deletar_nota(id_nota):
    try:
        nota = select_objeto(notas, id_nota)
        notas.remove(nota)

        nota_json = objeto_json(nota)
        return response(200, 'nota', nota_json, 'Nota deletada')
    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não deletada')


@app.route('/calculanf/<int:id_nota>', methods=["GET"])
def calcular_nota(id_nota):
    try:
        nota = select_objeto(notas, id_nota)
        nota.calcularNotaFiscal()

        nota_json = objeto_json(nota)
        return response(200, 'nota', nota_json, 'Nota calculada')

    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não calculada')


@app.route('/imprimenf/<int:id_nota>', methods=["GET"])
def imprimir_nota(id_nota):
    try:
        nota = select_objeto(notas, id_nota)
        impresso = nota.imprimirNotaFiscal()

        return response(200, 'nota', impresso, 'Nota impressa')

    except Exception as e:
        print(e)
        return response(400, 'nota', {}, 'Nota não impressa')