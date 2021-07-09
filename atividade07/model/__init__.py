from atividade07 import db
from atividade07.model.tabelas import Cliente, Produto, NotaFiscal, ItemNotaFiscal


def banco_adicionar(objeto):
    db.session.add(objeto)
    db.session.commit()


def banco_remover(objeto):
    db.session.delete(objeto)
    db.session.commit()


def select_objeto(classe, id):
    return classe.query.filter_by(id=id).first()


def criar_inicial():
    cliente1 = Cliente("Yuri Mateus", '100', '200.100.345-34', 'pessoa fisica')
    cliente2 = Cliente("Raquel Maciel", '200', '123.456.789-10', 'pessoa fisica')
    cliente3 = Cliente("Israel Leite", '300', '109.876.543-21', 'pessoa fisica')

    # Produtos
    produto1 = Produto(100, 'Arroz', 5.5)
    produto2 = Produto(200, 'Feijao', 4.5)
    produto3 = Produto(300, 'Batata', 6)

    # Notas Fiscais
    notafiscal1 = NotaFiscal(100, cliente1)
    notafiscal2 = NotaFiscal(200, cliente2)
    notafiscal3 = NotaFiscal(300, cliente3)

    # ItensNotaFiscal
    item1 = ItemNotaFiscal(1, 6, notafiscal1, produto1)

    item2 = ItemNotaFiscal(1, 8, notafiscal2, produto1)
    item3 = ItemNotaFiscal(2, 5, notafiscal2, produto2)

    item4 = ItemNotaFiscal(1, 10, notafiscal3, produto1)
    item5 = ItemNotaFiscal(2, 4, notafiscal3, produto2)
    item6 = ItemNotaFiscal(3, 7, notafiscal3, produto3)

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.add(item4)
    db.session.add(item5)
    db.session.add(item6)

    db.session.commit()
