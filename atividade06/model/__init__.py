from atividade06.model.cliente import Cliente
from atividade06.model.produto import Produto
from atividade06.model.notafiscal import NotaFiscal
from atividade06.model.itemnotafiscal import ItemNotaFiscal

# banco de dados

# Clientes
cliente1 = Cliente(1, "Yuri Mateus", 100, '200.100.345-34', 'pessoa fisica')
cliente2 = Cliente(2, "Raquel Maciel", 200, '123.456.789-10', 'pessoa fisica')
cliente3 = Cliente(3, "Israel Leite", 300, '109.876.543-21', 'pessoa fisica')

clientes = [cliente1, cliente2, cliente3]

# Produtos
produto1 = Produto(1, 100, 'Arroz', 5.5)
produto2 = Produto(2, 200, 'Feijao', 4.5)
produto3 = Produto(3, 300, 'Batata', 6)

produtos = [produto1, produto2, produto3]

# Notas Fiscais
notafiscal1 = NotaFiscal(1, 100, cliente1)
notafiscal2 = NotaFiscal(2, 200, cliente2)
notafiscal3 = NotaFiscal(3, 300, cliente3)

notas = [notafiscal1, notafiscal2, notafiscal3]

# ItensNotaFiscal
item1 = ItemNotaFiscal(1, 1, 6, produto1)

item2 = ItemNotaFiscal(2, 1, 8, produto1)
item3 = ItemNotaFiscal(3, 2, 5, produto2)

item4 = ItemNotaFiscal(4, 1, 10, produto1)
item5 = ItemNotaFiscal(5, 2, 4, produto2)
item6 = ItemNotaFiscal(6, 3, 7, produto3)

itens = [item1, item2, item3, item4, item5, item6]

# Adicionando os produtos
notafiscal1.adicionarItem(item1)

notafiscal2.adicionarItem(item2)
notafiscal2.adicionarItem(item3)

notafiscal3.adicionarItem(item4)
notafiscal3.adicionarItem(item5)
notafiscal3.adicionarItem(item6)
