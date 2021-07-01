from produto import Produto


class Item:
    def __init__(self, self, quantidade):
        self._produto = self.set_produto(produto)
        self._quantidade = self.set_quantidade(quantidade)

    def get_produto(self):
        return self._produto

    def get_produto_nome(self):
        if isinstance(self._produto, Produto):
            return self._produto.get_nome()
        return 'Produto'

    def get_produto_descricao(self):
        if isinstance(self._produto, Produto):
            return self._produto.get_descricao()
        return 'Descricao do Produto'

    def get_produto_preco(self):
        if isinstance(self._produto, Produto):
            return self._produto.get_preco()
        return 0

    def get_quantidade(self):
        return self._quantidade

    def get_valor_item(self):
        return self.get_produto_preco() * self.get_quantidade()

    def set_produto(self, self):
        if produto is not None and isinstance(produto, Produto):
            self._produto = produto
            retorno = produto
        else:
            self._produto = None
            retorno = None
        return retorno

    def set_quantidade(self, quantidade):
        if quantidade > 0 and isinstance(quantidade, int):
            self._quantidade = quantidade
            retorno = quantidade
        else:
            self._quantidade = 0
            retorno = 0
        return retorno


if __name__ == '__main__':
    # Criando objetos com Valores inválidos
    produto1 = Produto('Feijão', 4.99, 'Feijão Mulato')
    produto2 = None
    produto3 = Produto('Leite', 3.99, 'Leite Integral')

    item1 = Item(produto1, 3)
    item2 = Item(produto1, -3)
    item3 = Item(produto2, 2)
    item4 = Item(produto2, 3.5)

    itens = [item1, item2, item3, item4]

    print('Valores Válidos')
    for i in itens:
        print(f'Nome do Produto: {i.get_produto_nome()}, Preço do Produto: {i.get_produto_preco()}, Quantidade de '
              f'Produtos: {i.get_quantidade()}, Valor Total do Item: {i.get_valor_item()}')

    # Utilizando os métodos para criar Itens Válidos
    produto2 = Produto('Arroz', 4.55, 'Arroz de Qualidade')

    item2.set_quantidade(5)

    item3.set_produto(produto2)

    item4.set_produto(produto3)
    item4.set_quantidade(1)

    print('\nValores Válidos')
    for i in itens:
        print(f'Nome do Produto: {i.get_produto_nome()}, Preço do Produto: {i.get_produto_preco()}, Quantidade de '
              f'Produtos: {i.get_quantidade()}, Valor Total do Item: {i.get_valor_item()}')
