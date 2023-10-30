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
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, novo_nome):
        if type(novo_nome) == str:
            self.nome = novo_nome
        else:
            print("O nome deve ser do tipo string!")
            
    def get_preco(self):
        return self.preco
    
    def set_preco(self, novo_preco):
        if novo_preco >= 0:
            self.preco = novo_preco
        else:
            print("O preço não pode ser negativo!")
            
    def get_marca_produto(self):
        return self.marca_produto
    
    def set_marca_produto(self, nova_marca_produto):
        if type(nova_marca_produto) == str:
            self.nova_marca_produto = nova_marca_produto
        else:
            print("A marca do produto deve ser uma string!")
    
    def __str__(self):
        return f"{self.nome} - ({self.marca_produto})"
    
    def salvar_codigo_barras(self, path:str="./"):
        self.codigo_de_barras.save(f"{path}cod_barras_{self.nome}_{self.id_produto}.png")
    

class Roupa(Produto):
    def __init__(self, nome, valor, marca_produto, tipo_tecido):
        super().__init__(nome, valor, marca_produto)
        self.tipo_tecido = tipo_tecido
        
    def get_tipo_tecido(self):
        return self.tipo_tecido
    
    def set_tipo_tecido(self, novo_tipo_tecido):
        if type(novo_tipo_tecido) == str:
            self.tipo_tecido = novo_tipo_tecido
        else:
            print("O tipo do tecido deve ser uma string!")


class Chocolate(Produto):
    def __init__(self, nome, valor, marca_produto, sabor, peso_mg):
        super().__init__(nome, valor, marca_produto)
        self.sabor = sabor
        self.peso_mg = peso_mg
        
    def get_sabor(self):
        return self.sabor
    
    def set_sabor(self, novo_sabor):
        if type(novo_sabor) == str:
            self.sabor = novo_sabor
        else:
            print("O sabor deve estar no formato string!")
    
    def get_peso_mg(self):
        return self.peso_mg
    
    def set_peso_mg(self, novo_peso_mg):
        if novo_peso_mg >= 0:
            self.peso_mg = novo_peso_mg
        else:
            print("O peso, em miligramas, do chocolate não pode ser negativo!")


class Refrigerante(Produto):
    def __init__(self, nome, valor, marca_produto, tipo_recipiente, sabor):
        super().__init__(nome, valor, marca_produto)
        self.tipo_recipiente = tipo_recipiente
        self.sabor = sabor
        
    def get_tipo_recipiente(self):
        return self.tipo_recipiente
    
    def set_tipo_recipiente(self, novo_tipo_recipiente):
        if type(novo_tipo_recipiente) == str:
            self.tipo_recipiente = novo_tipo_recipiente
        else:
            print("O tipo do recipiente deve estar no formato string!")
            
    def get_sabor(self):
        return self.sabor
    
    def set_sabor(self, novo_sabor):
        if type(novo_sabor) == str:
            self.sabor = novo_sabor
        else:
            print("O sabor deve estar no formato string!")


prod_1 = Chocolate("Talento", 8, Marca.NESTLE, "Maracujá", 80)
prod_2 = Chocolate("Barra de Chocolate", 6.5, Marca.GAROTO, "Chocolate Amargo", 75)
prod_3 = Chocolate("Bombom Serenata", 1, Marca.GAROTO, "Amendoim", 10)

prod_4 = Roupa("Calça", -120, Marca.MARISA, "jeans")
prod_5 = Roupa("Vestido", 90, Marca.RENNER, "Malha Estampada")
prod_6 = Roupa("Jaqueta", 240, Marca.RENNER, "Couro")

prod_7 = Refrigerante("Fanta Laranja", 7, Marca.FANTA, "lata", "laranja")
prod_8 = Refrigerante("Coca-Cola", 12, Marca.COCA_COLA, "KS", "Coca-Cola")
prod_9 = Refrigerante("Guaraná", 9, Marca.GUARANA, "garrafa plástica", "Guaraná")


# Testa o setter para o atributo _preco
novo_preco = -25
prod_1.set_preco(novo_preco)

# Verifica se o preço foi alterado, se não for alterado aparece a mensagem de erro e o preço anterior do produto 1
preco_atual = prod_1.get_preco()
print(f"Novo preço: {preco_atual}")
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