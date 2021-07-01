import json

from flask import Response


def objeto_json(objeto):
    if isinstance(objeto, list):
        json_final = []
        for objeto in objeto:
            json_final.append(objeto.dict())
        return json_final
    else:
        return objeto.dict()


def response(status, nome_conteudo, conteudo, mensagem='', nome_secundario='', conteudo_secundario=None):
    body = {nome_conteudo: conteudo}

    if conteudo_secundario:
        body[nome_secundario] = conteudo_secundario
    if mensagem:
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="api/json")


def select_objeto(lista, id_objeto):
    return [o for o in lista if o.get_id() == id_objeto][0]