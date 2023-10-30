class Inventario:
    def __init__(self, produtos: list[Produto]):
        self.produtos = dict()
        self.lista = produtos

        for produto in produtos:
            self.produtos[produto] = 0

    def __len__(self):
        return len(self.produtos.size)

    def __getitem__(self, p):
        return self.produtos[p]

    def __str__(self):
        pass

    def remover(self, produto, quantidade):
        self.produtos[produto] -= quantidade

    def adicionar(self, produto, quantidade):
        self.produtos[produto] += quantidade

    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self, produtos):
        if isinstance(produtos, list):
            self.__lista = produtos
        else:
            print("Não foi possível iniciar o inventário, tente inserir uma lista de produtos.")
            raise Exception









