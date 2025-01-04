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
        self.money = 1500

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
        print(f"Você recebeu um crédito de R$800,00 para utilizar nas suas compras!")

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

    def pesquise(self):
        print("\n|| Pesquise e adicione compras ao seu carrinho ||")
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

    def selecionar_compra(self):
        itens_selecionados = []
        while True:
            self.ver_carrinho()
            escolha = input("\n Digite o nome dos itens que deseja comprar (ou 'sair' para encerrar): ")
            if escolha.lower() == 'sair':
                break
            for item in self.carrinho:
                if item['nome'].lower() == escolha.lower():
                    itens_selecionados.append(item)
                    print(f"Item '{item['nome']}' selecionado para compra.")
                    break
            else:
                print("Produto não encontrado. Tente novamente.")
        return itens_selecionados
            
    def realizar_compra(self):
        itens_comprar = self.selecionar_compra()
        preco_comprar = sum(float(produto['preco']) for produto in itens_comprar)
        if preco_comprar <= self.money:
            self.money -= preco_comprar
            for item in itens_comprar:
                self.carrinho.remove(item)
            print(f"Compra finalizada com sucesso! Seu crédito atual é de R${self.money:.2f}.") 
        else: 
            print(f"Crédito insuficiente. Total da compra: R${preco_comprar:.2f}, seu crédito: R${self.money:.2f}.")

    def menu_cliente(self, nome):
        while True:
            print(f"\n || Bem-vindo, {nome} ||")
            print(f"Seu dinheiro total em sua conta é: {self.money}")
            print("\n1. Pesquise\n 2. Ver o seu carrinho\n 3. Realizar compra\n 4. Sair")
            opcao = input(" Digite a opção desejada: ")

            if opcao == "1":
                self.pesquise()
            elif opcao == "2":
                self.ver_carrinho()
            elif opcao == "3":
                self.realizar_compra()
            elif opcao == "4":
                break
            else:
                print(" Opção inválida.\n")
