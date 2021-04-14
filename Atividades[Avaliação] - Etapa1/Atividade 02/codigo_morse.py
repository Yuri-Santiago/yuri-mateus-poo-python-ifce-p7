tabela = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
          'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
          's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
          '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
          '7': '--...', '8': '---..', '9': '----.'}

print('Nesse Programa você deverá escrever uma mensagem para ser traduzida para o Código Morse.')
mensagem = input('Digite a Mensagem para ser Traduzida: ')

caracteres = []
for x in range(len(mensagem)):
    caractere = mensagem[x].lower()
    if caractere in tabela.keys():
        caracteres.append(caractere)

morse = list(map(lambda c: tabela[c], caracteres))
traduzido = ' '.join(morse)
print(f'A mensagem em Código Morse é:\n{traduzido}')
