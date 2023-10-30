'''
class DeuRuimError(ZeroDivisionError):
    def __init__(self, message="Deu Ruim, mané!"): # essa mensagem é obrigatória no caso de exceções
        self.message = message
        super().__init__(self.message)


'''

class TipoIncorretoError(TypeError):
    def __init__(self, message="Tipo de dado inserido está incorreto, tente olhar a documentação e inserir novamente.") -> None:
        self.message = message
        super().__init__(self.message)
        
# teste da exceção criada acima
def teste():
    raise TipoIncorretoError()

try:
    teste()

except TipoIncorretoError as e:
    print(e.message)


