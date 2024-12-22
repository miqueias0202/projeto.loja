from cliente import Cliente
from vendedor import Vendedor

def menu_principal(cliente, vendedor):
    while True:
        print("\n|| Bem-vindo à Loja ||")
        print("1. Login Cliente\n2. Cadastrar Cliente\n3. Cadastrar Vendedor\n4. Login Vendedor\n5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if cliente.login():
                cliente.menu_cliente(cliente.get_nome())
        elif opcao == "2":
            cliente.cadastrar_clientes()
        elif opcao == "3":
            vendedor.cadastrar_vendedores()
        elif opcao == "4":
            vendedor.login_vendedores()
        elif opcao == "5":
            print("Obrigado por visitar a loja. Até logo!\n")
            break
        else:
            print("Opção inválida.\n")