
from usuarios import cadastrar_usuario,consultar_usuario, usuarios_db
from produtos import cadastrar_produto,consultar_produto, produtos_db
from compras import realizar_compra, listar_compras, compras_db

def validacao(user):
    if user == []:
        print(f"a pessoa não possui compras registradas")
    else:
        print(f"retorno da consulta = {user}")

def test_fluxo_integra_compras():
    print("\nIniciando teste de integração do sistema de compras...\n")

     # Limpa os "bancos" em memória

    usuarios_db.clear()
    produtos_db.clear()
    compras_db.clear()


    # 1. Cadastrar usuários e testar

    assert cadastrar_usuario(1, "vivian")
    assert cadastrar_usuario(2, "eduarda")
    assert cadastrar_usuario(3, "pricila")
    assert cadastrar_usuario(4, "luana")
    assert cadastrar_usuario(5, "marcia")

    user = consultar_usuario(3)
    assert user == "pricila", f"Esperado 'pricila', obtido {user}"
    print(f"retorno da consulta Usuario = {user}")


    # 2. Cadastrar produtos e testar

    assert cadastrar_produto(1, "macarrão", 2.5)
    assert cadastrar_produto(2, "cuscuz", 1.99)
    assert cadastrar_produto(3, "pippos", 3.90)

    user = consultar_produto(2)
    validacao(user)
    assert user == {'nome': 'cuscuz', 'preco': 1.99}, f"Esperado 'cuscuz', obtido {user}"
    

    # 3. Realizar compra válida

    assert realizar_compra(1, {1,2})
    assert realizar_compra(2, {3,2})

    user = listar_compras(2)
    validacao(user)

    user = listar_compras(1)
    validacao(user)
    assert user == [{'produtos': {1, 2}, 'total': 4.49}], f"Esperado '[{'produtos': {1, 2}, 'total': 4.49}]', obtido {user}"


    # 4. Tentar compra com produto inválido

    assert realizar_compra(3, {2,6})

    user = listar_compras(3)
    print(f"retorno da consulta compra = {user}")

    assert user == [{'produtos': {1, 2}, 'total': 4.49}], f"Esperado '[{'produtos': {1, 2}, 'total': 4.49}]', obtido {user}"



    # 5. Verificar compras do usuário 1

    user = listar_compras(1)
    validacao(user) 
    assert user == [{'produtos': {1, 2}, 'total': 4.49}], f"Esperado '[{'produtos': {1, 2}, 'total': 4.49}]', obtido {user}"

    # 6. Verificar um usuário que não tem compras

    validacao(listar_compras(3)) 

    

# Executa o teste
if __name__ == "__main__":
    test_fluxo_integra_compras()
