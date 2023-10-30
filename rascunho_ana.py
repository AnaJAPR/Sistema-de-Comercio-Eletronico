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
    def __init__(self, nome, valor, codigo_de_barras, marca_produto, tipo_tecido):
        super().__init__(nome, valor, codigo_de_barras, marca_produto)
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

prod_1 = Cholocate("Talento", 8, 325341, "Nestle", "Maracujá", 80)
prod_2 = Chocolate("Barra de Chocolate", 6.5, 834863, "Garoto", "Chocolate Amargo", 75)
prod_3 = Chocolate("Bombom Serenata", 1, 142537, "Garoto", "Amendoim", 10)

prod_4 = Roupa("Calça", 120, 546372, "Marisa", "jeans")
prod_5 = Roupa("Vestido", 90, 547384, "Renner", "Malha Estampada")
prod_6 = Roupa("Jaqueta", 240, 336475, "C&A", "Couro")

prod_7 = Refrigerante("Fanta Laranja", 7, 546374, "Fanta", "lata", "laranja")
prod_8 = Refrigerante("Coca-Cola", 12, 647583, "Coca-Cola", "KS", "Coca-Cola")
prod_9 = Refrigerante("Guaraná", 9, 647583, "Guaraná", "garrafa plástica", "Guaraná")

print(prod_1.nome)
        
    