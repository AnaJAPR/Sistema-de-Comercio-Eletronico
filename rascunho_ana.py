from enum import Enum

class Produto():
    def __init__(self, nome, valor, codigo_de_barras, marca_produto):
        self.nome = nome
        self.valor = valor
        self.codigo_de_barras = codigo_de_barras
        self.marca_produto = marca_produto
        


class id_marca(Enum):
    Yoki = 34
    Nestle = 44
    
print(id_marca)
        
    