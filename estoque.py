# Sistema de Gestão de Estoque

produtos = []

def cadastrar_produto(nome, quantidade):
    produto = {
        "nome": nome,
        "quantidade": quantidade
    }
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    for produto in produtos:
        print(produto)

cadastrar_produto("Teclado", 10)
listar_produtos()
