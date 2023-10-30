from rascunho_ana import Produto 
from rascunho_ana import Cholocate 
from rascunho_ana import Roupa 
from test_invetario import Inventario 
import Menu


class Loja:
    def __init__(self, nome, produtos):
        self.nome = nome
        self.inventário = Inventario(produtos)
        self.vendas = []

    def vender(self, produto, quantidade):
        if self.inventário.produtos[produto] >= quantidade:
            self.vendas.append([produto, quantidade])
            self.inventário.remover(produto, quantidade)
        else:
            print("Estoque insuficiente.")

    def repor(self, produto, quantidade):
        self.inventário.adicionar(produto, quantidade)

    def retornar(self, produto, quantidade):
        self.vendas.remove([produto, quantidade])
        self.inventário.adicionar(produto, quantidade)

    def show(self):
        print("===  Vendas  ===")

        for venda in self.vendas:
            produto = venda[0]
            quantidade = venda[1]

            indice = self.inventário.pesquisa(produto)
            preco = self.inventário.lista[indice].preco

            print(f"{produto:<10s} x {quantidade}  =  R${preco * quantidade}")
        
        print("================")

prod_1 = Cholocate("Talento", 8, 325341, "nestle", "prestigio", 80)
prod_2 = Roupa("Calça", 120, 546372, "Marisa", "calça", "jeans")

loja = Loja("Varejo", [prod_1, prod_2])
loja.repor('Talento', 100)

loja.vender('Talento', 3)
loja.vender('Calça', 10)
loja.show()