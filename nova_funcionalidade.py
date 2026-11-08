# Nova funcionalidade do sistema

def verificar_estoque(quantidade):

    if quantidade <= 5:
        print("Alerta: Estoque baixo!")

    else:
        print("Estoque em quantidade adequada.")


verificar_estoque(3)
verificar_estoque(20)