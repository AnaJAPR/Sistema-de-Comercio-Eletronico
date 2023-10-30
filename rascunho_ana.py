from enum import Enum

class Produto():
    def __init__(self, nome, preco, codigo_de_barras, marca_produto):
        self.nome = nome
        self.preco = preco
        self.codigo_de_barras = codigo_de_barras
        self.marca_produto = marca_produto
        
    def __str__(self):
        return f"{self.nome} - R$ ({self.marca_produto})"
        
class Roupa(Produto):
    def __init__(self, nome, valor, codigo_de_barras, marca_produto, tipo_roupa, tipo_tecido):
        super().__init__(nome, valor, codigo_de_barras, marca_produto)
        self.tipo_roupa = tipo_roupa
        self.tipo_tecido = tipo_tecido

class Cholocate(Produto):
    def __init__(self, nome, valor, codigo_de_barras, marca_produto, sabor, peso_mg):
        super().__init__(nome, valor, codigo_de_barras, marca_produto)
        self.sabor = sabor
        self.peso_mg = peso_mg
    
class Refrigerante(Produto):
    def __init__(self, nome, valor, codigo_de_barras, marca_produto, tipo_recipiente, sabor):
        super().__init__(nome, valor, codigo_de_barras, marca_produto)
        self.tipo_recipiente = tipo_recipiente
        self.sabor = sabor
        
class id_marca(Enum):
    Yoki = 34
    Nestle = 44
    
print(id_marca)

prod_1 = Cholocate("Talento", 8, 325341, "nestle", "prestigio", 80)
print(prod_1.nome)
        
    