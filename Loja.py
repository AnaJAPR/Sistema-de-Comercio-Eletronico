from test_invetario import Inventario

class Loja:
    """ Classe de uma loja genérica, com inventário e vendas próprias. """
    
    def __init__(self, nome, produtos):
        self.nome = nome
        self.inventario = Inventario(produtos)
        self.vendas = []

    def vender(self, produto, quantidade):
        if self.inventario.produtos[produto] >= quantidade:
            self.vendas.append([produto, quantidade])
            self.inventario.remover(produto, quantidade)
        else:
            print("Estoque insuficiente.")

    def repor(self, produto, quantidade):
        self.inventario.adicionar(produto, quantidade)

    def retornar(self, produto, quantidade):
        self.vendas.remove([produto, quantidade])
        self.inventario.adicionar(produto, quantidade)

    def mostrar_vendas(self):
        print("===  Vendas  ===")

        for venda in self.vendas:
            produto = venda[0]
            quantidade = venda[1]

            indice = self.inventario.pesquisa(produto)

            if indice == -1:
                continue

            preco = self.inventario.lista[indice].preco
            
            print(f"{produto:<10s} x {quantidade}  =  R${preco * quantidade}")
        
        print("================")

