from verifica_triangulo import verificar

print('Nesse programa você escreverá 3 lados de um Triângulo e ele falará se esses lados formam um Triângulo.')
comprimento_a = int(input('Digite o Primeiro Lado do Triângulo: '))
comprimento_b = int(input('Digite o Segundo Lado do Triângulo: '))
comprimento_c = int(input('Digite o Terceiro Lado do Triângulo: '))

verificacao = verificar(comprimento_a, comprimento_b, comprimento_c)

if verificacao:
    print('Os valores passados formam um Triângulo. :)')
else:
    print('Esses valores não formam um Triângulo. :(')
