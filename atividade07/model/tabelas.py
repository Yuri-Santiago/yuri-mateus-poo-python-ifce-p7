import datetime

from atividade07 import db


class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer(), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    codigo = db.Column(db.String(30), nullable=False)
    cnpjcpf = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    notas = db.relationship('NotaFiscal', backref='cliente', lazy='joined')

    def __init__(self, nome, codigo, cnpjcpf, tipo):
        self.nome = nome
        self.codigo = codigo
        self.cnpjcpf = cnpjcpf
        self.tipo = tipo

    def __repr__(self):
        return f'Cliente {self.nome}, código {self.codigo}, cpf {self.cnpjcpf}'

    def dict(self):
        return {'id': self.id,
                'nome': self.nome,
                'codigo': self.codigo,
                'cnpjcpf': self.cnpjcpf,
                'tipo': self.tipo
                }


class Produto(db.Model):
    __tablename__ = 'produtos'
    id = db.Column(db.Integer(), primary_key=True)
    codigo = db.Column(db.String(30), nullable=False)
    descricao = db.Column(db.String(50), nullable=False)
    valor_unitario = db.Column(db.Float(), nullable=False)
    itens = db.relationship('ItemNotaFiscal', backref='produto', lazy='joined')

    def __init__(self, codigo, descricao, valor_unitario):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor_unitario

    def __repr__(self):
        return f'Produto {self.descricao}, código {self.codigo}, preço {self.valor_unitario}'

    def dict(self):
        return {'id': self.id,
                'codigo': self.codigo,
                'descricao': self.descricao,
                'valor-unitario': self.valor_unitario
                }


class NotaFiscal(db.Model):
    __tablename__ = 'notasfiscais'
    id = db.Column(db.Integer(), primary_key=True)
    codigo = db.Column(db.String(30), nullable=False)
    data = db.Column(db.DateTime(), default=datetime.datetime.now())
    valor_nota = db.Column(db.Float(), nullable=False)
    id_cliente = db.Column(db.Integer(), db.ForeignKey('clientes.id'), nullable=False)
    itens = db.relationship('ItemNotaFiscal', backref='nota', lazy='joined')

    def __init__(self, codigo, cliente):
        self.codigo = codigo
        self.valor_nota = 0.0
        self.cliente = cliente

    def __repr__(self):
        return f'Nota código {self.codigo}, nota data e hora {self.data}, nota valor {self.valor_nota}'

    def dict(self):
        return {'id': self.id,
                'codigo': self.codigo,
                'data': str(self.data),
                'cliente': self.cliente.dict(),
                'itens': [i.dict() for i in self.itens if self.itens is not None],
                'valor-nota': self.valor_nota
                }

    def calcularNotaFiscal(self):
        valor = 0.0
        for item in self.itens:
            valor = valor + item.valor_item
        self.valor_nota = valor

    def data_formatada(self):
        data_hora_lista = str(self.data).split()
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
                     self.cliente.codigo, ' ', self.cliente.nome,
                     self.cliente.cnpjcpf,
                     linha,
                     linha,
                     ' ', ' ', ' ', ' ',
                     '-' * 4, '-' * 56, '-' * 5, '-' * 12, '-' * 18)

        if len(self.itens) > 0:
            for itemnota in self.itens:
                resultado += '\n\n%s%3s%s' % (itemnota.sequencial, ' ', itemnota.descricao)
                resultado += ' ' * (60 - len(itemnota.descricao))
                resultado += '%5d%17.2f%23.2f' % (itemnota.quantidade, itemnota.valor_unitario,
                                                  itemnota.valor_item)

        resultado += '\n%s\nValor Total: %.2f' % (linha, self.valor_nota)

        return resultado


class ItemNotaFiscal(db.Model):
    __tablename__ = 'itensnotasfiscais'
    id = db.Column(db.Integer(), primary_key=True)
    sequencial = db.Column(db.String(30), nullable=False)
    quantidade = db.Column(db.Integer(), nullable=False)
    valor_item = db.Column(db.Float(), nullable=False)
    id_nota = db.Column(db.Integer(), db.ForeignKey('notasfiscais.id'), nullable=False)
    id_produto = db.Column(db.Integer(), db.ForeignKey('produtos.id'), nullable=False)

    def __init__(self, sequencial, quantidade, nota, produto):
        self.sequencial = sequencial
        self.quantidade = quantidade
        self.nota = nota
        self.produto = produto
        self.valor_item = quantidade * produto.valor_unitario

    def __repr__(self):
        return f'Item sequencial {self.sequencial}, item quantidade {self.quantidade}, valor item {self.valor_item}'

    def dict(self):
        return {'id': self.id,
                'sequencial': self.sequencial,
                'quantidade': self.quantidade,
                'produto': self.produto.dict(),
                'valor-item': float(self.quantidade * self.produto.valor_unitario)
                }

    def calcula_item(self):
        self.valor_item = self.quantidade * self.produto.valor_unitario