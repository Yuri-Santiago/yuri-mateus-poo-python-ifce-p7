from produto import Produto
from item import Item


class Compra:
    def __init__(self):
        self._itens = []

    def get_itens(self):
        return self._itens

    def get_valor_compra(self):
        return sum([item.get_valor_item() for item in self._itens])

    def set_itens(self, lista):
        validacao = True
        for item in lista:
            if not isinstance(item, Item):
                validacao = False
                break
        if validacao:
            self._itens = lista
            return 'Lista Válida'
        return 'Lista Inválida'

    def tamanho_lista(self):
        return len(self._itens)

    def add_item(self, item):
        if isinstance(item, Item):
            self._itens.append(item)
            return 'Item Adicionado'
        else:
            return 'Item Inválido'

    def remover_item(self, indice_item):
        if isinstance(indice_item, int) and indice_item < self.tamanho_lista():
            self._itens.pop(indice_item)
            return 'Item Removido'
        return 'Índice Inválido'

    def listar_itens(self):
        resultado = ""
        contador = 1
        if self.tamanho_lista() > 0:
            resultado += '\nItens:\n'
            for item in self._itens:
                resultado += '%4d:%20s|%16.2f R$|%4d|%20.2f R$\n' % \
                             (contador, item.get_produto_nome(), item.get_produto_preco(), item.get_quantidade(),
                              item.get_valor_item())
                contador += 1
            resultado += 'Valor Total da Compra: %.2f R$\n' % self.get_valor_compra()
        else:
            resultado += 'Sem items na Compra\n'
        return resultado

    def listar_itens_separados(self, dado):
        resultado = ""
        contador = 1
        if self.tamanho_lista() > 0:
            for item in self._itens:
                if dado == 'indice':
                    resultado += '%d\n' % contador
                elif dado == 'nome':
                    resultado += '%s\n' % item.get_produto_nome()
                elif dado == 'preco':
                    resultado += '%.2f R$\n' % item.get_produto_preco()
                elif dado == 'quantidade':
                    resultado += '%d\n' % item.get_quantidade()
                elif dado == 'total':
                    resultado += '%.2f R$\n' % item.get_valor_item()
                contador += 1
        return resultado


if __name__ == '__main__':
    # Testando a Classe
    produto1 = Produto('Feijão', 4.99, 'Feijão Mulato')
    produto2 = Produto('Arroz', 4.55, 'Arroz de Qualidade')
    produto3 = Produto('Leite', 3.99, 'Leite Integral')
    produto4 = Produto('', -5, False)

    item1 = Item(produto1, 3)
    item2 = Item(produto2, 1)
    item3 = Item(produto3, 6)
    item4 = Item(produto4, 2)
    item5 = None

    compra1 = Compra()
    compra2 = Compra()

    itens = [item1, item2, item3, item4, item5]
    compras = [compra1, compra2]

    print('Teste com Valores Inválidos')
    for i in itens:
        print(compra1.add_item(i))

    compra2.add_item(5)
    compra2.add_item(-2.6)
    compra2.add_item('oi')
    compra2.add_item(False)
    compra2.add_item(None)
    compra2.add_item([1, 2, 3, 4])

    for c in compras:
        print(f'\n{c.listar_itens()}')

    # Valores Válidos
    print('\nTestes com valores Válidos')
    item5 = Item(Produto('Óleo', 5, 'Óleo Light'), 2)

    itens2 = [item1, item2, item3, item5]

    print(compra1.set_itens(itens2))
    print(compra1.remover_item(10))
    print(compra1.remover_item('0'))
    print(compra1.remover_item(2))
    print(compra2.set_itens([item1, item2, item3, 5]))

    for c in compras:
        print(f'\n{c.listar_itens()}')

    print('\nNomes:')
    print(compra1.listar_itens_separados('nome'))
