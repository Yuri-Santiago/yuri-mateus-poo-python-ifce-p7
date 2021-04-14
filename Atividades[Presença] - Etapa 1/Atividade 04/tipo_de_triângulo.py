print('Nesse programa você escreverá 3 lados de um Triângulo e ele lhe mostrará o tipo do Triângulo.')
lado_a = int(input('Digite o Primeiro Lado do Triângulo: '))
lado_b = int(input('Digite o Segundo Lado do Triângulo: '))
lado_c = int(input('Digite o Terceiro Lado do Triângulo: '))

if lado_a == lado_b and lado_b == lado_c:
    print('O Triângulo é Equilátero')
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print('O Triângulo é Isósceles')
else:
    print('O Triângulo é Escaleno')
