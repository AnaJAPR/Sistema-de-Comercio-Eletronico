import sys

def input_validate(message, start, end):
    """ Valida o input entre start e end, usando uma mensagem. """

    while True:
        try:
            choice = int(input(message))
            
            if start <= choice <= end:
                return choice
        
        except TypeError:
            print("Digite apenas inteiros!")
        except BaseException:
            print(f"Inválido, tente números entre {start} e {end}.")


class Menu:
    """ Classe de um menu genérico que mostra e executa certas operações. """

    def __init__(self):
        self.options = [['Sair', 'exit']]

    def add_option(self, nome, function):
        """Adiciona uma opção e função ao menu"""

        self.options.append([nome, function])
    
    def show(self):
        """ Mostra o menu e suas opções na tela. """

        print("=" * 5)
        print("Menu")
        print("=" * 5 + "\n")

        # Itera sobre as opções do menu, mostrando-as
        for code, option in enumerate(self.options):
            print(f"[{code}] - {option[0]}")

        print()

    def execute(self):
        """ Executa o menu, mostrando suas opções e validando a escolha do usuário. """

        while True:
            self.show()
            choice = input_validate("Escolha uma opção: ", 0, len(self.options) - 1)

            if choice == 0:
                sys.exit(0)
            else:
                self.options[choice][1]()
                input("...Enter para continuar...\n")

class App:
    """ Classe de um aplicativo que encapsula o menu da loja e o executa. """

    def __init__(self, loja):
        self.loja = loja
        self.menu = Menu()

        # Adiciona todas opções do menu
        self.menu.add_option("Venda", self.vender)
        self.menu.add_option("Retorno", self.retornar)
        self.menu.add_option("Restoque", self.repor)
        self.menu.add_option("Mostrar venda", self.loja.mostrar_vendas)
        self.menu.add_option("Mostrar inventário", self.loja.inventario.mostrar)
        self.menu.add_option("Salvar código de barras", self.codigo_barra)

    def vender(self):
        """ Encapsula o método vender da Loja ao Menu. """

        produto = self.pede_nome()
        quantidade = self.pede_quantidade()

        self.loja.vender(produto, quantidade)

    def retornar(self):
        """ Encapsula o método retornar da Loja ao Menu. """

        produto = self.pede_nome()
        quantidade = self.pede_quantidade()

        self.loja.retornar(produto, quantidade)

    def repor(self):
        """ Encapsula o método repor da Loja ao Menu. """

        produto = self.pede_nome()
        quantidade = self.pede_quantidade()

        self.loja.repor(produto, quantidade)

    def codigo_barra(self):
        """ Encapsua o método de salvar código de barras do Produto. """

        produto = self.pede_nome()

        indice = self.loja.inventario.pesquisa(produto)
        self.loja.inventario.lista[indice].salvar_codigo_barras()

        print("Código de barras gerado com sucesso.")

    def pede_nome(self):
        """ Recebe o nome de um produto válido. """

        while True:
            nome = input("Digite o nome do produto: ")

            if nome == '0':
                sys.exit(1)

            if self.loja.inventario.pesquisa(nome) == -1:
                print("Produto não está no inventário! Digite 0 para sair.")
                continue
            else:
                break

        return nome
            
    def pede_quantidade(self):
        """ Recebe uma quantidade em inteiros positivos. """

        quantidade = input_validate("Digite a quantidade: ", 0, 1000)

        return quantidade

    def execute(self):
        """ Encapsula o executar do menu. """

        self.menu.execute()



if __name__ == "__main__":
    pass