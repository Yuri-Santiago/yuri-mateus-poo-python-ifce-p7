"""
1) Pilha (inserir e retirar pelo topo da Pilha). Considerar o topo como sendo o índice 0 da Lista.
"""

# Criando nossa lista vazia que representará a pilha
pilha = []

# Adicionando alguns pratos na nossa pilha
for x in range(1, 11):
    print(f'Prato de número {x} chegando na pilha')
    pilha.insert(0, x)

# Mostrando nossa pilha de pratos
print(f'\nNo momento temos {len(pilha)} pratos na pilha.')
print(f'{pilha}\n')

# Lavando alguns pratos da nossa pilha
for x in range(10, 5, -1):
    print(f'Lavando prato de número {x}')
    pilha.pop(0)

# Mostrando a pilha atual
print(f'\nNo momento temos {len(pilha)} pratos na pilha.')
print(f'{pilha}\n')

# Fim da Demonstração da Pilha
