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

    def apresentar_produtos(self, categoria=None):
        if categoria:
            produtos_filtrados = [produto for produto in self.produtos if produto['categoria'] == categoria]
            if produtos_filtrados:
                for produto in produtos_filtrados:
                    print(f"Nome: {produto['nome']}\nPreço: {produto['preco']}\nDescrição: {produto['descricao']}\nCategoria: {produto['categoria']}\n")
                return produtos_filtrados
            else:
                print(f"Não há produtos na categoria {categoria}.")
                return []
        else:
            if not self.produtos:
                print("Não há produtos ainda.")
                return []
            else:
                for produto in self.produtos:
                    print(f"Nome: {produto['nome']}\nPreço: {produto['preco']}\nDescrição: {produto['descricao']}\nCategoria: {produto['categoria']}\n")
                return self.produtos

    def altera_produtos(self):
        print("\n|| Gerenciar Produtos ||")
        for i, categoria in enumerate(self.categorias, 1):
            print(f"{i}. {categoria}")

        while True:
            escolha = input("Digite o número da categoria do produto: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(self.categorias):
                categoriaEscolhida = self.categorias[int(escolha) - 1].lower()
                break
            else:
                print("Escolha inválida, tente novamente.")

        produtosEncontrados = self.apresentar_produtos(categoriaEscolhida)
        if not produtosEncontrados:
            return
        
        while True:
            escolha_produto = input("\nDigite o nome do produto que deseja alterar ou apagar (ou 'sair' para encerrar): ")
            if escolha_produto.lower() == 'sair':
                break
            for produto in produtosEncontrados:
                if produto['nome'].lower() == escolha_produto.lower():
                    print(f"\n1. Alterar Produto '{produto['nome']}'")
                    print("2. Apagar Produto")
                    escolha_acao = input("Escolha a ação desejada (1 ou 2): ")

                    if escolha_acao == '1':
                        novo_nome = input("Digite o novo nome do produto (ou pressione Enter para manter o atual): ").lower()
                        novo_preco = input("Digite o novo preço do produto (ou pressione Enter para manter o atual): ")
                        nova_descricao = input("Digite a nova descrição do produto (ou pressione Enter para manter a atual): ")

                        if novo_nome:
                            produto['nome'] = novo_nome
                        if novo_preco.replace('.', '', 1).isdigit():
                            produto['preco'] = novo_preco
                        if nova_descricao:
                            produto['descricao'] = nova_descricao

                        print("Produto alterado com sucesso")
                    elif escolha_acao == '2':
                        self.produtos.remove(produto)
                        print("Produto apagado com sucesso")
                    return
            else:
                print("Produto não encontrado. Tente novamente.")

    def menu_vendedor(self, nome):
        while True:
            print(f"\n|| Bem-vindo Vendedor: {nome} ! ||")
            print("1. Adicionar Produto\n2. Apresentar produtos\n3. Gerenciar Produto\n4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.add_produto()
            elif opcao == "2":
                self.apresentar_produtos()
            elif opcao == "3":
                self.altera_produtos()
            elif opcao == "4":
                break
            else:
                print("Opção inválida.\n")
