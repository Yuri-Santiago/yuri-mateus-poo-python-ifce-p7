from produto import Produto
from item import Item
from compra import Compra


class Cliente:
    def __init__(self, nome):
        self._nome = self.set_nome(nome)
        self._compras = []

    def get_nome(self):
        return self._nome

    def get_compras(self):
        return self._compras

    def get_valor_cliente(self):
        return sum([compra.get_valor_compra() for compra in self._compras])

    def set_nome(self, nome):
        if nome != '' and isinstance(nome, str):
            self._nome = nome
            retorno = nome
        else:
            self._nome = 'Anônimo'
            retorno = 'Anônimo'
        return retorno

    def set_compras(self, lista):
        validacao = True
        for compra in lista:
            if not isinstance(compra, Compra):
                validacao = False
                break
        if validacao:
            self._compras = lista
            return 'Lista Válida'
        return 'Lista Inválida'

    def tamanho_lista(self):
        return len(self._compras)

    def add_compra(self, compra):
        if isinstance(compra, Compra):
            self._compras.append(compra)
            return 'Compra Adicionado'
        else:
            return 'Compra Inválido'

    def remover_compra(self, indice_compra):
        if isinstance(indice_compra, int) and indice_compra < self.tamanho_lista():
            self._compras.pop(indice_compra)
            return 'Compra Removido'
        return 'Índice Inválido'

    def listar_compras(self):
        resultado = ""
        contador = 1
        if self.tamanho_lista() > 0:
            for compra in self._compras:
                resultado += '\nCompra de Número: %d%s' % \
                             (contador, compra.listar_itens())
                contador += 1
            resultado += '\nValor Total do Cliente: %.2f R$' % self.get_valor_cliente()
        else:
            resultado += 'Sem Compras do Cliente\n'
        return resultado


if __name__ == '__main__':
    produto1 = Produto('Feijão', 4.99, 'Feijão Mulato')
    produto2 = Produto('Arroz', 4.55, 'Arroz de Qualidade')
    produto3 = Produto('Leite', 3.99, 'Leite Integral')

    produto4 = Produto('Notebook', 3599.99, 'Notebook Gamer Potente')

    produto5 = Produto('Ventilador', 190.55, 'Ventilados 6 pás')
    produto6 = Produto('Batedeira', 455.80, 'Batedeira Profissional')

    item1 = Item(produto1, 8)
    item2 = Item(produto2, 15)
    item3 = Item(produto3, 6)

    item4 = Item(produto4, 1)

    item5 = Item(produto5, 3)
    item6 = Item(produto6, 2)

    compra1 = Compra()
    compra2 = Compra()
    compra3 = Compra()

    compra1.add_item(item1)
    compra1.add_item(item2)
    compra1.add_item(item3)

    compra2.add_item(item4)

    compra3.add_item(item5)
    compra3.add_item(item6)

    cliente = Cliente('Yuri')

    print(f'Olá Cliente {cliente.get_nome()}, suas Compras são:\n{cliente.listar_compras()}')

    cliente.add_compra(compra1)
    cliente.add_compra(compra2)
    cliente.add_compra(compra3)

    print(f'Olá Cliente {cliente.get_nome()}, suas Compras são:\n{cliente.listar_compras()}')
