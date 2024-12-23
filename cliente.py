from classes import Pessoa, Endereco
import getpass

class Cliente(Pessoa, Endereco):
    def __init__(self, nome, telefone, email, cpf, senha, cep, bairro, rua, numero, vendedor):
        Pessoa.__init__(self, nome, telefone, email, cpf, senha)
        Endereco.__init__(self, cep, bairro, rua, numero)
        self.clientes = []
        self.categorias = ["Eletrônicos", "Roupas", "Livros", "Brinquedos", "Móveis"]
        self.vendedor = vendedor
        self.nome = nome
        self.carrinho = [] 

    def cadastrar_clientes(self):
        print("\n || Comece seu cadastro ||")
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
        print("\n|| Por favor coloque seu endereço de entrega ||")
        while True:
            cep = input(" Digite seu CEP: ")
            if cep.isdigit():
                break
            else:
                print(" CEP inválido. ")
        bairro = input(" Digite seu bairro: ")
        rua = input(" Digite sua rua: ")
        while True:
            numero = input(" Digite seu número: ")
            if numero.isdigit():
                break
            else:
                print(" Número inválido.")
        senha = getpass.getpass(" Digite sua senha: ")
        novoCliente = Cliente(nome, telefone, email, cpf, senha, cep, bairro, rua, numero, self.vendedor)
        self.clientes.append(novoCliente)
        print(" Cliente cadastrado com sucesso! ")

    def login(self):
        print("\n|| Login ||")
        email = input(" Digite o email: ")
        senha = getpass.getpass(" Digite sua senha: ")
        for cliente in self.clientes:
            if cliente.get_email() == email and cliente.get_senha() == senha:
                print(f" Login feito com sucesso, bem-vindo {cliente.get_nome()} \n")
                self.menu_cliente(cliente.get_nome())
                return True
        print(" Email ou senha inválidos ou ainda nao possui cadastro. \n")
        return False

    def pesquisar_produtos(self, categoriaEscolhida):
        produtosEncontrados = [produto for produto in self.vendedor.produtos if produto['categoria'] == categoriaEscolhida]

        if produtosEncontrados:
            print(f" Produtos da categoria: {categoriaEscolhida}")
            for produto in produtosEncontrados:
                print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Descrição: {produto['descricao']}")
            return produtosEncontrados
        else:
            print(f" Nenhum produto encontrado na categoria {categoriaEscolhida}.")
            return []

    def add_carrinho(self):
        print("\n|| Adicionar ao Carrinho ||")
        for i, categoria in enumerate(self.categorias, 1):
            print(f"{i}. {categoria}")

        while True:
            escolha = input(" Digite o número da categoria que está procurando: ")
            if escolha.isdigit() and 1 <= int(escolha) <= len(self.categorias):
                categoriaEscolhida = self.categorias[int(escolha) - 1].lower()
                break
            else:
                print(" Escolha inválida, tente novamente. ")

        produtosEncontrados = self.pesquisar_produtos(categoriaEscolhida)
        if not produtosEncontrados:
            return
        while True:
            escolha_produto = input("\nDigite o nome do produto que deseja adicionar ao carrinho (ou 'sair' para encerrar): ")
            if escolha_produto.lower() == 'sair':
                break
            for produto in produtosEncontrados:
                if produto['nome'].lower() == escolha_produto.lower():
                    self.carrinho.append(produto)
                    print(f"Produto '{produto['nome']}' adicionado ao carrinho.")
                    break
            else:
                print("Produto não encontrado na lista. Tente novamente.")

    def ver_carrinho(self):
        if self.carrinho:
            print("\n|| Produtos no Carrinho ||")
            for produto in self.carrinho:
                print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Descrição: {produto['descricao']}")
        else:
            print("\nSeu carrinho está vazio.")

    def menu_cliente(self, nome):
        while True:
            print(f"\n || Bem-vindo, {nome} ||")
            print(" 1. Adicionar ao carrinho\n 2. Ver o seu carrinho\n 3. Sair")
            opcao = input(" Digite a opção desejada: ")

            if opcao == "1":
                self.add_carrinho()
            elif opcao == "2":
                self.ver_carrinho()
            elif opcao == "3":
                break
            else:
                print(" Opção inválida.\n")
