from rascunho_ana import Produto

class Inventario:
    """ Classe de um inventário que aceita apenas uma lista
        de objetos Produto e os armazena na memória.
    """

    def __init__(self, produtos: list[Produto]):
        self.produtos = dict()
        self.lista = produtos

        for produto in produtos:
            self.produtos[produto.nome] = 0

    def __len__(self):
        return len(self.produtos.size)

    def __getitem__(self, p):
        return self.produtos[p]

    def mostrar(self):
        print("-----------------------------------")
        print("|           Produto |  Quantidade |")

        for produto in self.produtos:
            print("|-------------------|-------------|")
            print(f"|         {produto:>9} |    {self.produtos[produto]:>8} |")

        print("-----------------------------------")

    def remover(self, produto, quantidade):
        # Remove a quantidade. A validação deve vir da Loja.
        self.produtos[produto] -= quantidade

    def adicionar(self, produto, quantidade):
        # Adiciona a quantidade.
        self.produtos[produto] += quantidade

    def pesquisa(self, nome):
        # Pesquisa o nome entre os produtos no inventário. Retorna o índice.
        for indice, produto in enumerate(self.lista):

            if produto.nome == nome:
                return indice

        return -1

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
