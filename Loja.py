from test_invetario import Inventario

class Loja:
    """ Classe de uma loja genérica, com inventário e vendas próprias. """
    
    def __init__(self, nome, produtos):
        self.nome = nome
        self.inventario = Inventario(produtos)
        self.vendas = []

    def vender(self, produto, quantidade):
        """ Vende certa quantia de um produto. """

        # Verifica se há a quantia no inventário
        if self.inventario.produtos[produto] >= quantidade:
            self.vendas.append([produto, quantidade])
            self.inventario.remover(produto, quantidade)
        else:
            print("Estoque insuficiente.")

    def repor(self, produto, quantidade):
        """ Repõe certa quantia no inventário. """
        
        self.inventario.adicionar(produto, quantidade)

    def retornar(self, produto, quantidade):
        """ Retorna certa venda feita. """

        # Verifica se a venda foi feita anteriormente
        if [produto, quantidade] in self.vendas:
            self.vendas.remove([produto, quantidade])
            self.inventario.adicionar(produto, quantidade)
        else:
            print("Esta venda não foi feita!")

    def mostrar_vendas(self):
        """ Mostra a lista das vendas feitas até então. """

        print("===  Vendas  ===")

        # Itera sobre cada venda na lista
        for venda in self.vendas:
            produto = venda[0]
            quantidade = venda[1]

            indice = self.inventario.pesquisa(produto)

            # Se o indice for -1, o produto não terá preço
            if indice == -1:
                continue

            preco = self.inventario.lista[indice].preco
            
            print(f"{produto:<10s} x {quantidade}  =  R${preco * quantidade}")
        
        print("================")

