from random import randint

numeros = []

while len(numeros) < 6:
    aleatorio = randint(1, 60)
    if aleatorio not in numeros:
        numeros.append(aleatorio)

numeros.sort()
print(f'Os números que você deve jogar são: {numeros}')
