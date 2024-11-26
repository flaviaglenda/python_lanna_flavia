# Flávia Glenda e Lanna Kamilly
def cadastra_produto(nome, preco, quantidade):
    produto = {
        "nome": nome,
        "preço": preco,
        "quantidade": quantidade
    }
    return produto

produtos = []

for i in range(5):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    produtos = produtos + [cadastra_produto(nome, preco, quantidade)] 

print("\nProdutos cadastrados:")
for produto in produtos:
    print(produto)
