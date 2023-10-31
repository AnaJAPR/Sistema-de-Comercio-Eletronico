from produtos import Chocolate, Roupa, Refrigerante, Marca
from inventario import Inventario 
import iterativo
import vendas

# Criando os produtos da loja
prod_1 = Chocolate("Talento", 8, Marca.NESTLE, "Maracujá", 80)
prod_2 = Chocolate("Barra de Chocolate", 6.5, Marca.GAROTO, "Chocolate Amargo", 75)
prod_3 = Chocolate("Bombom Serenata", 1, Marca.GAROTO, "Amendoim", 10)

prod_4 = Roupa("Calça", 120, Marca.MARISA, "jeans")
prod_5 = Roupa("Vestido", 90, Marca.RENNER, "Malha Estampada")
prod_6 = Roupa("Jaqueta", 240, Marca.RENNER, "Couro")

prod_7 = Refrigerante("Fanta Laranja", 7, Marca.FANTA, "lata", "laranja")
prod_8 = Refrigerante("Coca-Cola", 12, Marca.COCA_COLA, "KS", "Coca-Cola")
prod_9 = Refrigerante("Guaraná", 9, Marca.GUARANA, "garrafa plástica", "Guaraná")

# Criando a loja e adicionando os produtos nela
dama_shop = vendas.Loja("Dama Shop", [prod_1, prod_2, prod_3, prod_4, prod_5, prod_6, prod_7, prod_8, prod_9])

# Cria o menu da loja e o executa
iterativo.menu = iterativo.App(dama_shop)
iterativo.menu.execute()

