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
        colaboradores = [self.__movimentos[0].get_colaborador()]
        resultado = 'Folha de Pagamento da Empresa:\n'

        for movimento in self.__movimentos:
            if movimento.get_colaborador().get_codigo() not in [c.get_codigo() for c in colaboradores]:
                colaboradores.append(movimento.get_colaborador())
            if movimento.get_tipo_movimento() == TipoMovimento.PROVENTO:
                self.__total_proventos += movimento.get_valor()
            else:
                self.__total_descontos += movimento.get_valor()

        total_salarios = sum([c.get_salario_atual() for c in colaboradores])
        total_pagar = (total_salarios + self.__total_proventos) - self.__total_descontos

        resultado += 'Total de Salários = %10.2f    Total de Proventos = %10.2f    Total de Descontos = %10.2f\nTotal' \
                     ' a Pagar = %10.2f\n' % (total_salarios, self.__total_proventos, self.__total_descontos,
                                              total_pagar)

        for i, colaborador in enumerate(colaboradores):
            resultado += f'\nFolha Individual do Colaborador {i + 1}:\n{colaborador.calcular_salario()}'

        return resultado
    # Questão 4
    def inserir_movimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self.__movimentos.append(movimento)
            return 'Adicionado Com Sucesso!'
        return 'Movimento Inválido'

    def inserir_colaboradores(self):
        pass
