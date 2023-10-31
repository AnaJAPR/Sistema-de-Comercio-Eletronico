
class TipoIncorretoError(TypeError):
    # Verifica se o tipo do dado está correto ou não
    def __init__(self, message="Tipo de dado inserido está incorreto, tente olhar a documentação e inserir novamente.") -> None:
        self.message = message
        super().__init__(self.message)


class PrecoNegativoError(ValueError):
    # Verifica se o preço é negativo (o que não faz sentido para o valor do produto)
    def __init__(self, message="Preço negativo inválido, o preço do produto deve ser maior ou igual a 0 para que a operação seja válida.") -> None:
        self.message = message
        super().__init__(self.message)


class MarcaInvalidaError(KeyError):
    # Verifica se a marca do produto é uma marca válida
    def __init__(self, message="A marca é inválida, tente conferir quais marcas são válidas e inserir uma nova.") -> None:
        self.message = message
        super().__init__(self.message)


if __name__ == "__main__":
    # teste da exceção criada acima
    def teste():
        raise TipoIncorretoError()

    try:
        teste()

    except TipoIncorretoError as e:
        print(e.message)


