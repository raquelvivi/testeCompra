
from usuarios import cadastrar_usuario,consultar_usuario, usuarios_db
from produtos import cadastrar_produto, produtos_db
from compras import realizar_compra, listar_compras, compras_db

def test_fluxo_integra_compras():
    print("\nIniciando teste de integração do sistema de compras...\n")

     # Limpa os "bancos" em memória

    usuarios_db.clear()


    # 1. Cadastrar usuários e testar

    assert cadastrar_usuario(1, "vivian")
    assert cadastrar_usuario(2, "eduarda")
    assert cadastrar_usuario(3, "pricila")

    user = consultar_usuario(3)
    assert user == "pricila", f"Esperado 'pricila', obtido {user}"
    print(f"retorno da consulta = {user}")


    # 2. Cadastrar produtos e testar


    # 3. Realizar compra válida


    # 4. Tentar compra com produto inválido


    # 5. Verificar compras do usuário 1


    # 6. Verificar um usuário que não tem compras


# Executa o teste
if __name__ == "__main__":
    test_fluxo_integra_compras()
