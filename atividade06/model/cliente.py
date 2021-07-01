"""
    Módulo cliente -
    Classe Cliente - 
    Atributos:
        _id       - chave primária    - informado
        _nome     - nome do cliente   - informado
        _codigo   - codigo do cliente - informado
        _cnpjcpf  - cnpj ou cpf       - informado
        _tipo     - tipo do cliente   - informado
                    (Pessoa Fisica ou Juridica)
        
"""


class Cliente:
    def __init__(self, id, nome, codigo, cnpjcpf, tipo):
        self._id = id
        self._nome = nome
        self._codigo = codigo
        self._cnpjcpf = cnpjcpf
        self._tipo = tipo

    def str(self):
        string = "\nId={4} Codigo={2} Nome={3} CNPJ/CPF={1} Tipo={0}".format(self._tipo, self._cnpjcpf, self._codigo,
                                                                             self._nome, self._id)
        return string

    def get_id(self):
        return self._id

    def get_codigo(self):
        return self._codigo

    def get_nome(self):
        return self._nome

    def get_cnpjcpf(self):
        return self._cnpjcpf

    def set_nome(self, nome):
        self._nome = nome

    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_cnpjcpf(self, cnpjcpf):
        self._cnpjcpf = cnpjcpf

    def dict(self):
        return {'id': self.get_id(),
                'codigo': self.get_codigo(),
                'cpf': self.get_cnpjcpf(),
                'nome': self.get_nome()
                }


if __name__ == '__main__':
    cliente = Cliente(1, "Jose Maria", 100, '200.100.345-34', 'pessoa fisica')
    print(cliente.str())
