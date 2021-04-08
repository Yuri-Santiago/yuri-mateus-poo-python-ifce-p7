"""
2) Fila (Inserir no final da Fila. Considerar o final da fila o elemento de maior índice positivo.
   Retirar da Fila pelo elemento do inicio da Lista que tem o índice 0.)
"""

# Criando nossa lista vazia que representará a fila
fila = []

# Adicionando alguns elementos na nossa fila
for x in range(1, 13):
    print(f'Pessoa número {x} chegando na fila do banco')
    fila.append(x)

# Mostrando nossa fila do banco
print(f'\nAgora antes do banco abrir temos {len(fila)} pessoas na fila.')
print(f'{fila}\n')

# Agora o banco abriu e as pessoas vão sair da fila
for x in range(1, 11):
    print(f'Pessoa número {x} saindo da fila')
    fila.pop(0)

# Mostrando a fila atual
print(f'\nNo momento temos {len(fila)} tarefas na pilha.')
print(f'{fila}\n')

# Fim da Demonstração da Fila
