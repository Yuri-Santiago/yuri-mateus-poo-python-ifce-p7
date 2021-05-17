from funcoes import *
from movimento_folha import MovimentoFolha
from tipo_movimento import TipoMovimento


class FolhaPagamento:

    def __init__(self, mes, ano):
        self.__mes = checar_inteiro(mes)
        self.__ano = checar_inteiro(ano)
        self.__total_descontos = 0
        self.__total_proventos = 0
        self.__movimentos = []

    def get_mes(self):
        return self.__mes

    def get_ano(self):
        return self.__ano

    def get_total_descontos(self):
        return self.__total_descontos

    def get_total_proventos(self):
        return self.__total_proventos

    def get_movimentos(self):
        return self.__movimentos

    def set_mes(self, mes):
        self.__mes = checar_inteiro(mes)

    def set_ano(self, ano):
        self.__mes = checar_inteiro(ano)

    # Questão 8
    def calcular_folha(self):
        total_salarios = 0
        for movimento in self.__movimentos:
            if movimento.get_tipo_movimento() == TipoMovimento.PROVENTO:
                if movimento.get_descricao() == 'Salário':
                    total_salarios += movimento.get_valor()
                else:
                    self.__total_proventos += movimento.get_valor()
            else:
                self.__total_descontos += movimento.get_valor()
        total_pagar = (total_salarios + self.__total_proventos) - self.__total_descontos

        return 'Total de Salários = %10.2f    Total de Proventos = %10.2f    Total de Descontos = %10.2f\nTotal a ' \
               'Pagar = %10.2f\n' % (total_salarios, self.__total_proventos, self.__total_descontos, total_pagar)

    # Questão 4
    def inserir_movimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self.__movimentos.append(movimento)
            return 'Adicionado Com Sucesso!'
        return 'Movimento Inválido'

    def inserir_colaboradores(self):
        pass
