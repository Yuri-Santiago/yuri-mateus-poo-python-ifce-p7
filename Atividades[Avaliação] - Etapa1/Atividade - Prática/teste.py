from folha_pagamento import FolhaPagamento
from colaborador import Colaborador
from movimento_folha import MovimentoFolha
from tipo_movimento import TipoMovimento

if __name__ == '__main__':
    # Questão 1
    FP = FolhaPagamento(9, 2019)

    # Questão 2
    CL1 = Colaborador(100, 'Manoel Claudino', 'Av 13 de Maio 2081', '88671020', 'Benfica', '60020-060', '124543556-89',
                      4500)
    CL2 = Colaborador(200, 'Carmelina da Silva', 'Avenida dos Expedicionários 1200', '3035-1280', 'Aeroporto',
                      '60530-020', '301789435-54', 2500)
    CL3 = Colaborador(300, 'Gurmelina Castro Saraiva', 'Av João Pessoa 1020', '3235-1089', 'Damas', '60330-090',
                      '350245632-76', 3000)

    # Questão 3
    MF1 = MovimentoFolha(CL1, 'Salário', 4500, TipoMovimento.PROVENTO)
    MF2 = MovimentoFolha(CL1, 'Plano Saúde', 1000, TipoMovimento.PROVENTO)
    MF3 = MovimentoFolha(CL1, 'Pensão', 600, TipoMovimento.DESCONTO)

    MF4 = MovimentoFolha(CL2, 'Salário', 2500, TipoMovimento.PROVENTO)
    MF5 = MovimentoFolha(CL2, 'Gratificação', 1000, TipoMovimento.PROVENTO)
    MF6 = MovimentoFolha(CL2, 'Faltas', 600, TipoMovimento.DESCONTO)

    MF7 = MovimentoFolha(CL3, 'Salário', 3000, TipoMovimento.PROVENTO)
    MF8 = MovimentoFolha(CL3, 'Plano Saúde', 1000, TipoMovimento.PROVENTO)
    MF9 = MovimentoFolha(CL3, 'Pensão', 800, TipoMovimento.DESCONTO)

    movimentos = [MF1, MF2, MF3, MF4, MF5, MF6, MF7, MF8, MF9]

    # Questão 6
    for m in movimentos:
        FP.inserir_movimentos(m)

    # Questão 7
    for m in range(len(movimentos)):
        if m < 3:
            CL1.inserir_movimentos(movimentos[m])
        elif m < 6:
            CL2.inserir_movimentos(movimentos[m])
        else:
            CL3.inserir_movimentos(movimentos[m])

    print(FP.calcular_folha())
    print(CL1.calcular_salario())
    print(CL2.calcular_salario())
    print(CL3.calcular_salario())
