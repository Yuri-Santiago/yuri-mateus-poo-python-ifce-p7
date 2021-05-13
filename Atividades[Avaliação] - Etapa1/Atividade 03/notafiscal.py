"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            itens     - informado
            valornota - calculado. 
"""
import datetime
from cliente import Cliente
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal:
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo = codigo
        self._cliente = cliente
        self._data = datetime.datetime.now()
        self._itens = []
        self._valorNota = 0.0

    def get_valor_nota(self):
        return self._valorNota

    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente = cliente

    def adicionarItem(self, item):
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self._itens:
            valor = valor + item.get_valor_item()
        self._valorNota = valor

    def data_formatada(self):
        data_hora_lista = str(self._data).split()
        data_lista = data_hora_lista[0].split('-')
        data_final = f'{data_lista[2]}/{data_lista[1]}/{data_lista[0]}'
        return data_final

    def imprimirNotaFiscal(self):
        linha = '-' * 111
        resultado = '%s\n' \
                    'NOTA FISCAL%100s\n' \
                    'Cliente:%6d%4sNome: %s\n' \
                    'CPF/CNPJ: %s\n' \
                    '%s\n' \
                    'ITENS\n' \
                    '%s\n' \
                    'Seq%3sDescrição%52sQTD%7sValor Unit%12sPreço\n' \
                    '%s  %s    %s     %s     %s' % \
                    (linha,
                    self.data_formatada(),
                    self._cliente.get_codigo(), ' ', self._cliente.get_nome(),
                    self._cliente.get_cnpjcpf(),
                    linha,
                    linha,
                    ' ', ' ', ' ', ' ',
                    '-'*4, '-'*56, '-'*5, '-'*12, '-'*18)

        if len(self._itens) > 0:
            for itemnota in self._itens:
                resultado += '\n\n%s%3s%s' % (itemnota.get_sequencial(), ' ', itemnota.get_descricao())
                resultado += ' ' * (60 - len(itemnota.get_descricao()))
                resultado += '%5d%17.2f%23.2f' % (itemnota.get_quantidade(), itemnota.get_valor_unitario(),
                                                      itemnota.get_valor_item())

        resultado += '\n%s\nValor Total: %.2f' % (linha, self._valorNota)

        print(resultado)
