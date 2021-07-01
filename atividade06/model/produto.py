"""
    Módulo produto
    Classe Produto
    Atributos :
        id            - informado
        codigo        - informado
        descricao     - informado
        valorUnitario - informado. 
"""


class Produto:

    def __init__(self, id, codigo, descricao, valorUnitario):
        self._id = id
        self._codigo = codigo
        self._descricao = descricao
        self._valor_unitario = valorUnitario

    def get_id(self):
        return self._id

    def get_codigo(self):
        return self._codigo

    def get_descricao(self):
        return self._descricao

    def get_valor_unitario(self):
        return self._valor_unitario

    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_descricao(self, descricao):
        self._descricao = descricao

    def set_valor_unitario(self, valor_unitario):
        self._valor_unitario = valor_unitario

    def str(self):
        string = "\nId={3} Codigo={2} Descricao={1} Valor Unitario={0}".format(self._valor_unitario, self._descricao,
                                                                               self._codigo, self._id)
        return string

    def dict(self):
        return {'id': self.get_id(),
                'codigo': self.get_codigo(),
                'descricao': self.get_descricao(),
                'valor-unitario': self.get_valor_unitario()
                }


if __name__ == '__main__':
    produto = Produto(1, 100, 'Arroz', 5.5)
    print(produto.str())
