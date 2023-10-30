from enum import Enum
import aspose.barcode as barcode

class Marca(Enum):
    NESTLE = 101
    GAROTO = 102
    MARISA = 201
    RENNER = 202
    FANTA = 301
    COCA_COLA = 302
    GUARANA = 303
    
    def __str__(self):
        return self.name
    

class Produto():
    id_produto = 1

    def __init__(self, nome, preco, marca_produto):
        self.nome = nome
        self.preco = preco
        self.marca_produto = marca_produto
        self.id_produto = Produto.id_produto
        Produto.id_produto += 1
        
        gerador_codigo_barras = barcode.generation.BarcodeGenerator(barcode.generation.EncodeTypes.CODE_39_STANDARD)
        gerador_codigo_barras.code_text = f"{self.nome} - {self.id_produto}"

        self.codigo_de_barras = gerador_codigo_barras
        
    def __str__(self):
        return f"{self.nome} - ({self.marca_produto})"
    
    def salvar_codigo_barras(self, path:str="./"):
        self.codigo_de_barras.save(f"{path}cod_barras_{self.nome}_{self.id_produto}.png")
    

class Roupa(Produto):
    def __init__(self, nome, valor, marca_produto, tipo_tecido):
        super().__init__(nome, valor, marca_produto)
        self.tipo_tecido = tipo_tecido


class Chocolate(Produto):
    def __init__(self, nome, valor, marca_produto, sabor, peso_mg):
        super().__init__(nome, valor, marca_produto)
        self.sabor = sabor
        self.peso_mg = peso_mg


class Refrigerante(Produto):
    def __init__(self, nome, valor, marca_produto, tipo_recipiente, sabor):
        super().__init__(nome, valor, marca_produto)
        self.tipo_recipiente = tipo_recipiente
        self.sabor = sabor


prod_1 = Chocolate("Talento", 8, Marca.NESTLE, "Maracujá", 80)
prod_2 = Chocolate("Barra de Chocolate", 6.5, Marca.GAROTO, "Chocolate Amargo", 75)
prod_3 = Chocolate("Bombom Serenata", 1, Marca.GAROTO, "Amendoim", 10)

prod_4 = Roupa("Calça", 120, Marca.MARISA, "jeans")
prod_5 = Roupa("Vestido", 90, Marca.RENNER, "Malha Estampada")
prod_6 = Roupa("Jaqueta", 240, Marca.RENNER, "Couro")

prod_7 = Refrigerante("Fanta Laranja", 7, Marca.FANTA, "lata", "laranja")
prod_8 = Refrigerante("Coca-Cola", 12, Marca.COCA_COLA, "KS", "Coca-Cola")
prod_9 = Refrigerante("Guaraná", 9, Marca.GUARANA, "garrafa plástica", "Guaraná")

'''
print(prod_1)
print(prod_2)
print(prod_3)
print(prod_4)
print(prod_5)
print(prod_6)
print(prod_7)
print(prod_8)
print(prod_9)
'''