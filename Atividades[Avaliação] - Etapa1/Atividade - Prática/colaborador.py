from tipo_movimento import TipoMovimento
from movimento_folha import MovimentoFolha
from funcoes import *


class Colaborador:

    def __init__(self, codigo, nome, endereco, telefone, bairro, cep, cpf, salario_atual):
        self.__codigo = checar_inteiro(codigo)
        self.__nome = checar_string(nome)
        self.__endereco = checar_string(endereco)
        self.__telefone = checar_string(telefone)
        self.__bairro = checar_string(bairro)
        self.__cep = checar_string(cep)
        self.__cpf = checar_string(cpf)
        self.__salario_atual = checar_float(salario_atual)
        self.__movimentos = []

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_telefone(self):
        return self.__telefone

    def get_bairro(self):
        return self.__bairro

    def get_cep(self):
        return self.__cep

    def get_cpf(self):
        return self.__cpf

    def salario_atual(self):
        return self.__salario_atual

    def set_codigo(self, codigo):
        self.__codigo = checar_inteiro(codigo)

    def set_nome(self, nome):
        self.__nome = checar_string(nome)

    def set_endereco(self, endereco):
        self.__endereco = checar_string(endereco)

    def set_telefone(self, telefone):
        self.__telefone = checar_string(telefone)

    def set_bairro(self, bairro):
        self.__bairro = checar_string(bairro)

    def set_cep(self, cep):
        self.__cep = checar_string(cep)

    def set_cpf(self, cpf):
        self.__cpf = checar_string(cpf)

    def set_salario_atual(self, salario_atual):
        self.__salario_atual = checar_float(salario_atual)

    # Qustão 9
    def calcular_salario(self):
        total_proventos = 0
        total_descontos = 0
        for movimento in self.__movimentos:
            if movimento.get_tipo_movimento() == TipoMovimento.PROVENTO:
                if movimento.get_descricao() != 'Salário':
                    total_proventos += movimento.get_valor()
            else:
                total_descontos += movimento.get_valor()
        valor_liquido = (self.__salario_atual + total_proventos) - total_descontos
        return 'Codigo: %4d    Nome: %s\nSalário: %10.2f    Total Proventos: %10.2f    Total Descontos: %10.2f\nValor' \
               ' Líquido a Receber: %10.2f\n' % (self.__codigo, self.__nome, self.__salario_atual, total_proventos,
                                                 total_descontos, valor_liquido)

    # Questão 4
    def inserir_movimentos(self, movimento):
        if isinstance(movimento, MovimentoFolha):
            self.__movimentos.append(movimento)
            return 'Adicionado Com Sucesso!'
        return 'Movimento Inválido'
