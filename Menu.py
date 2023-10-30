import sys

# Valida o input entre start e end, usando a message
def input_validate(message, start, end):
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
    def __init__(self):
        self.menu = Menu()
        self.menu.add_option("Venda", 1)
        self.menu.add_option("Retorno", 1)
        self.menu.add_option("Restoque", 1)
        self.menu.add_option("Mostrar", 1)

    def execute(self):
        self.menu.execute()
