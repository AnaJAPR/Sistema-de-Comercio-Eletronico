class Loja:
    def __init__(self, nome):
        self.nome = nome
        self.inventário = Inventário()
        self.vendas = []

        self.inventário.adicionar('Chocolate', 10)

    def vender(self, produto, quantidade):
        self.vendas.append([produto, quantidade])
        self.inventário.remover(produto, quantidade)

    def repor(self, produto, quantidade):
        self.inventário.adicionar(produto, quantidade)

    def retornar(self, produto, quantidade):
        self.vendas.remove([produto, quantidade])
        self.inventário.adicionar(produto, quantidade)

    def show(self):
        for venda in vendas:
            print(f"{self.venda[0]} x {self.venda[1]} = {self.inventário.produtos[venda[0]]}")