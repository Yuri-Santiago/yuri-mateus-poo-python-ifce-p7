class Produto:
    def __init__(self, nome, preco, descricao):
        self._nome = self.set_nome(nome)
        self._preco = self.set_preco(preco)
        self._descricao = self.set_descricao(descricao)

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_descricao(self):
        return self._descricao

    def set_nome(self, nome):
        if nome != '' and isinstance(nome, str):
            self._nome = nome
            retorno = nome
        else:
            self._nome = 'Produto'
            retorno = 'Produto'
        return retorno

    def set_preco(self, preco):
        if preco > 0 and (isinstance(preco, float) or isinstance(preco, int)):
            self._preco = float(preco)
            retorno = float(preco)
        else:
            self._preco = 0
            retorno = 0
        return retorno

    def set_descricao(self, descricao):
        if descricao != '' and isinstance(descricao, str):
            self._descricao = descricao
            retorno = descricao
        else:
            self._descricao = 'Descrição do Produto'
            retorno = 'Descrição do Produto'
        return retorno


if __name__ == '__main__':
    # Testando os métodos Set do Produto com Dados inválidos
    produto1 = Produto('Feijão', 4.99, 'Feijão Mulato')
    produto2 = Produto(6, 5, 5)
    produto3 = Produto('', -3, 'Arroz de Qualidade')
    produto4 = Produto(True, 0, '')

    produtos = [produto1, produto2, produto3, produto4]

    print('Valores Inválidos')
    for p in produtos:
        print(f'Nome do Produto: {p.get_nome()}, Preço do Produto: {p.get_preco()}, Descrição do Produto: '
              f'{p.get_descricao()}')

    # Criando Dados válidos
    produto2.set_nome('Óleo')
    produto2.set_descricao('Óleo Light')

    produto3.set_nome('Arroz')
    produto3.set_preco(4.55)

    produto4.set_nome('Leite')
    produto4.set_preco(3.99)
    produto4.set_descricao('Leite Integral')

    print('\nValores Válidos')
    for p in produtos:
        print(f'Nome do Produto: {p.get_nome()}, Preço do Produto: {p.get_preco()}, Descrição do Produto: '
              f'{p.get_descricao()}')
