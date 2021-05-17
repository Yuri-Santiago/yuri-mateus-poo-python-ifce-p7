from funcoes import *


class MovimentoFolha:

    def __init__(self, colaborador, descricao, valor, tipo_movimento):
        self.__colaborador = colaborador
        self.__descricao = checar_string(descricao)
        self.__valor = checar_float(valor)
        self.__tipo_movimento = tipo_movimento

    def get_colaborador(self):
        return self.__colaborador

    def get_descricao(self):
        return self.__descricao

    def get_valor(self):
        return self.__valor

    def get_tipo_movimento(self):
        return self.__tipo_movimento

    def set_colaborador(self, colaborador):
        self.__colaborador = colaborador

    def set_descricao(self, descricao):
        self.__descricao = checar_string(descricao)

    def set_valor(self, valor):
        self.__valor = checar_float(valor)

    def set_tipo_movimento(self, tipo_movimento):
        self.__tipo_movimento = tipo_movimento
