class Cliente:
    def __init__(self, id_cliente, nome, codigo, cnpjcpf, tipo):
        self._id = id_cliente
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

    def set_cnpjcpf(self, cnpjcpf):
        self._cnpjcpf = cnpjcpf
