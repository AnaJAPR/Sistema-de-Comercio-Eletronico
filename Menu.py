import sys
from rascunho_ana import Produto 
from rascunho_ana import Chocolate 
from rascunho_ana import Roupa 
from rascunho_ana import Refrigerante
from test_invetario import Inventario
from Loja import Loja 

def input_validate(message, start, end):
    """ Valida o input entre start e end, usando uma mensagem. """

    while True:
        try:
            choice = int(input(message))
            
            if start <= choice <= end:
                return choice
        except TypeError:
            print("Digite apenas inteiros!")
        except:
            print(f"Inválido, tente números entre {start} e {end}.")


class Menu:
    """ Classe de um menu genérico que mostra e executa certas operações. """

    def __init__(self):
        self.options = [['Sair', 'exit']]

    def add_option(self, nome, function):
        """Adiciona uma opção e função ao menu"""

        self.options.append([nome, function])
    
    def show(self):
        """ Printa o menu e suas opções na tela. """

        print("=" * 5)
        print("Menu")
        print("=" * 5 + "\n")

        for code, option in enumerate(self.options):
            print(f"[{code}] - {option[0]}")

        print()

    def execute(self):
        """ Executa o menu, printando suas opções e validando a escolha do usuário. """

        while True:
            self.show()
            choice = input_validate("Escolha uma opção: ", 0, len(self.options) - 1)

            if choice == 0:
                sys.exit(0)
            else:
                self.options[choice][1]()

class App:
    """ Classe de um aplicativo que encapsula o menu da loja e o executa. """
    def __init__(self, loja):
        self.loja = loja
        self.menu = Menu()

        self.menu.add_option("Venda", self.loja.vender)
        self.menu.add_option("Retorno", self.loja.retornar)
        self.menu.add_option("Restoque", self.loja.repor)
        self.menu.add_option("Mostrar venda", self.loja.mostrar_vendas)
        self.menu.add_option("Mostrar inventário", self.loja.inventario.mostrar)

    def execute(self):
        self.menu.execute()

prod_1 = Chocolate("Talento", 8, "nestle", "prestigio", 80)
prod_2 = Roupa("Calça", 120, "Marisa", "jeans")

loja = Loja("Varejo", [prod_1, prod_2])
menu = App(loja)
menu.execute()