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
    print("\n--- PRODUTOS CADASTRADOS ---")
    for produto in produtos:
        print(produto)

def consultar_estoque(nome):
    for produto in produtos:
        if produto["nome"] == nome:
            print("Quantidade disponível:",
                  produto["quantidade"])
            return

    print("Produto não encontrado.")

cadastrar_produto("Teclado", 10)
cadastrar_produto("Mouse", 15)

listar_produtos()
consultar_estoque("Teclado")
