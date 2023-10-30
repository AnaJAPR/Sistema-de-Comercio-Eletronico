
class Inventario:
    def __init__(self, produtos: list[str]):

        prod_quant = dict()
        if type(produtos) != list:
            print("Não foi possível iniciar o inventário, tente inserir uma lista de produtos.")
        else:
            self.produtos_disponiveis = produtos

            for produto in produtos:
                prod_quant[produto] = 0

            self.prod_quant = prod_quant






mew_invent = Inventario(["choco", "leite"])

print(mew_invent)
