from classes import Pessoa, Lojas
import getpass

class Vendedor(Pessoa, Lojas):
    def __init__(self, nome, telefone, email, cpf, senha, nomeLoja, produtos):
        Pessoa.__init__(self, nome, telefone, email, cpf, senha)
        Lojas.__init__(self, nomeLoja, senha)
        self.vendedores = []
        self.produtos = produtos
        self.categorias = ["Eletrônicos", "Roupas", "Livros", "Brinquedos", "Móveis"]
        self.nome = nome  

    def cadastrar_vendedores(self):
        print("\n|| Comece a criação de sua loja aqui! ||")
        nome = input(" Digite seu nome: ")
        while True:
            telefone = input(" Digite seu telefone: ")
            if telefone.isdigit():
                break
            else:
                print(" Telefone informado inválido.")
        email = input(" Digite seu email: ")
        while True:
            cpf = input(" Digite seu CPF: ")
            if cpf.isdigit():
                break
            else:
                print(" O CPF que foi digitado é inválido.")
        nomeLoja = input(" Digite o nome da sua loja: ")
        senha = getpass.getpass(" Digite sua senha: ")
        novoVendedor = Vendedor(nome, telefone, email, cpf, senha, nomeLoja, self.produtos)
        self.vendedores.append(novoVendedor)
        print(" Seu cadastro de vendedor foi feito com sucesso! ")

    def login_vendedores(self):
        print("\n|| Login dos Vendedores ||")
        email = input(" Digite o email: ")
        senha = getpass.getpass(" Digite sua senha: ")
        for vendedor in self.vendedores:
            if vendedor.get_email() == email and vendedor.get_senha() == senha:
                print(f" Login feito com sucesso, bem-vindo {vendedor.get_nome()} \n")
                self.menu_vendedor(vendedor.get_nome())
                return True
        print(" Email ou senha inválidos.\n")
        return False

    def add_produto(self):
        print("\n|| Adicionar Produto ||")
        nome_produto = input("Digite o nome do produto: ").lower()
        while True:
            preco = input("Digite o preço do produto: ")
            if preco.replace('.', '', 1).isdigit():
                break
            else:
                print(" Preço inválido ")
                
        print("\n Escolha uma categoria para o produto: ")
        for i, categoria in enumerate(self.categorias, 1):
            print(f"{i}. {categoria}")

        while True:
            escolha_categoria = input("Digite o número da categoria: ")
            if escolha_categoria.isdigit() and 1 <= int(escolha_categoria) <= len(self.categorias):
                categoria_produto = self.categorias[int(escolha_categoria) - 1].lower()
                break
            else:
                print("Escolha inválida. Tente novamente.")
                
        descricao_produto = input("Digite a descrição do produto: ")

        produto = {
            'nome': nome_produto,
            'preco': preco,
            'descricao': descricao_produto,
            'categoria': categoria_produto
        }
        self.produtos.append(produto)
        print("Produto adicionado com sucesso!")

    def apresentar_produtos(self):
        if not self.produtos:
            print(" Não há produtos ainda. ")
        else:
            for produto in self.produtos:
                print(f"Nome: {produto['nome']}\nPreço: {produto['preco']}\nDescrição: {produto['descricao']}\nCategoria: {produto['categoria']}\n")
 
    def menu_vendedor(self, nome):
        while True:
            print(f"\n|| Bem-vindo Vendedor: {nome} ! ||")
            print("1. Adicionar Produto\n2. Apresentar produtos\n3. Sair")
            opcao = input(" Escolha uma opção: ")

            if opcao == "1":
                self.add_produto()
            elif opcao == "2":
                self.apresentar_produtos()
            elif opcao == "3":
                break
            else:
                print(" Opção inválida.\n")
