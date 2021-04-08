"""
3) Lista Encadeada (A retirada e a inserção de elementos se faz em qualquer posição da Lista).
   Usar os métodos da Lista Python que fazem menção nos seus parâmetros a índices.
"""
import random

# Criando nossa lista de tarefas que representará a lista encadeada
lista = ['exercitar', 'estudar', 'lavar a louça', 'passear com o cachorro', 'andar de bicicleta']

# Adicionando mais tarefas na nossa lista
lista.insert(0, 'arrumar a cama')
lista.insert(3, 'almoçar')
lista.insert(3, 'fazer o almoço')
lista.insert(5, 'escovar os dentes')

# Mostrando a lista de tarefas
print(f'\nA lista de tarefas contém {len(lista)} tarefas a serem cumpridas.')
print(f'{lista}\n')

# Fazendo algumas tarefas da lista
aleatorio = list(range(1, 5))
random.shuffle(aleatorio)
for x in aleatorio:
    print(f'Fazendo a tarefa: {lista[x]}.')
    lista.pop(x)

# Mostrando a lista atual
print(f'\nA lista de tarefas contém {len(lista)} tarefas a serem cumpridas.')
print(f'{lista}\n')

# Fim da Demonstração da Lista Encadeada
