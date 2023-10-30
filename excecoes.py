class DeuRuimError(ZeroDivisionError):
    def __init__(self, message="Deu Ruim, mané!"): # essa mensagem é obrigatória no caso de exceções
        self.message = message
        super().__init__(self.message)

# teste da exceção criada acima
def teste():
    raise DeuRuimError()

try:
    teste()
# a ordem dos excepts deve ser da mais específica para a mais genérica, porque o python para na primeira que dá certo.
except DeuRuimError:
    print("Pelo menos tentamos 2...")
except ZeroDivisionError:
    print("Pelo menos tentamos...")