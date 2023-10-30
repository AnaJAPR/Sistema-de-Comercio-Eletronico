from enum import Enum
import aspose.barcode as barcode

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
    def __init__(self, nome, valor, marca_produto, tipo_roupa, tipo_tecido):
        super().__init__(nome, valor, marca_produto)
        self.tipo_roupa = tipo_roupa
        self.tipo_tecido = tipo_tecido


class Cholocate(Produto):
    def __init__(self, nome, valor, marca_produto, sabor, peso_mg):
        super().__init__(nome, valor, marca_produto)
        self.sabor = sabor
        self.peso_mg = peso_mg


class Refrigerante(Produto):
    def __init__(self, nome, valor, marca_produto, tipo_recipiente, sabor):
        super().__init__(nome, valor, marca_produto)
        self.tipo_recipiente = tipo_recipiente
        self.sabor = sabor

    
class id_marca(Enum):
    Yoki = 34
    Nestle = 44
    
print(id_marca)

prod_1 = Cholocate("Talento", 8, "nestle", "prestigio", 80)
prod_1.salvar_codigo_barras()
print(prod_1)

    