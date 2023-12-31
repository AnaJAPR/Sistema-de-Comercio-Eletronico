from enum import Enum
import aspose.barcode as barcode
import excecoes

# Cria classe com Enum de cada marca dos produtos do inventário
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

# Cria classe com as características gerais de um produto
class Produto():
    id_produto = 1
    
    # Testa se a marca do produto está na classe com os nomes e Enums de cada marca
    # Trata exceções de tipo dos demais atributos de um produto também
    marcas_validas = []
    for marca in Marca:
        marcas_validas.append(Marca[marca.name].name)

    def __init__(self, nome: str, preco: float|int, marca_produto):
    
        try:
            if type(nome) != str or type(preco) not in (int, float):
                raise excecoes.TipoIncorretoError
            if preco < 0:
                raise excecoes.PrecoNegativoError
            elif marca_produto.name not in Produto.marcas_validas:
                raise excecoes.MarcaInvalidaError
    
        except excecoes.TipoIncorretoError as err:
            print(err)
        except excecoes.PrecoNegativoError as err:
            print(err)
        except excecoes.MarcaInvalidaError as err:
            print(err)
            
        else:
            self.nome = nome
            self.preco = preco
            self.marca_produto = marca_produto

            self.id_produto = Produto.id_produto
            Produto.id_produto += 1
            
            # gera um código de barras automaticamente para cada produto criado
            gerador_codigo_barras = barcode.generation.BarcodeGenerator(barcode.generation.EncodeTypes.CODE_39_STANDARD)
            gerador_codigo_barras.code_text = f"{self.nome} - {self.id_produto}"

            self.codigo_de_barras = gerador_codigo_barras
        
    # Cria getters e setters para cada atributo da classe Produto
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
        if nova_marca_produto.name in Produto.marcas_validas:
            self.nova_marca_produto = nova_marca_produto
        else:
            print("A marca do produto deve ser uma string!")
    
    
    # Quando imprimir o produto, aparece esse string formatada com apenas o nome e a marca do produto        
    def __str__(self):
        return f"{self.nome} - ({self.marca_produto})"
    
    # Salva o código de barras criado para o produto
    def salvar_codigo_barras(self, path:str="./"):
        self.codigo_de_barras.save(f"{path}cod_barras_{self.nome}_{self.id_produto}.png")
    

# Cria classe com o primeiro tipo de produto: Roupa
class Roupa(Produto):
    def __init__(self, nome, valor, marca_produto, tipo_tecido):
        super().__init__(nome, valor, marca_produto)
        self.tipo_tecido = tipo_tecido
    
    # Cria get e set para o atributo específico dessa classe, já que os demais ela herdou da classe pai
    def get_tipo_tecido(self):
        return self.tipo_tecido
    
    def set_tipo_tecido(self, novo_tipo_tecido):
        if type(novo_tipo_tecido) == str:
            self.tipo_tecido = novo_tipo_tecido
        else:
            print("O tipo do tecido deve ser uma string!")


# Cria classe com o segundo tipo de produto: Chocolate
class Chocolate(Produto):
    def __init__(self, nome, valor, marca_produto, sabor, peso_mg):
        super().__init__(nome, valor, marca_produto)
        self.sabor = sabor
        self.peso_mg = peso_mg
    
    # Cria getter e setter para os dois atributos específicos dessa classe
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


# cria classe com terceiro tipo de produto: Refrigerante
class Refrigerante(Produto):
    def __init__(self, nome, valor, marca_produto, tipo_recipiente, sabor):
        super().__init__(nome, valor, marca_produto)
        self.tipo_recipiente = tipo_recipiente
        self.sabor = sabor
    
    # Cria getters e setters para os dois atributos específicos dessa classe
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


if __name__ == "__main__":
    # print(prod_2)
    # print(prod_3)
    # print(prod_4)
    # print(prod_5)
    # print(prod_6)
    # print(prod_7)
    # print(prod_8)
    # print(prod_9)
    pass
