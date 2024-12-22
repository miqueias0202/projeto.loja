class Pessoa:
    def __init__(self, nome, telefone, email, cpf, senha):
        self.__nome = nome
        self.__telefone = telefone
        self.__email = email
        self.__cpf = cpf
        self.__senha = senha

    def get_nome(self):
        return self.__nome

    def get_telefone(self):
        return self.__telefone

    def get_email(self):
        return self.__email

    def get_cpf(self):
        return self.__cpf

    def get_senha(self):
        return self.__senha

class Endereco:
    def __init__(self, cep, bairro, rua, numero):
        self.__cep = cep
        self.__bairro = bairro
        self.__rua = rua
        self.__numero = numero

    def get_cep(self):
        return self.__cep

    def get_bairro(self):
        return self.__bairro

    def get_rua(self):
        return self.__rua

    def get_numero(self):
        return self.__numero

class Lojas:
    def __init__(self, nomeLoja, senha):
        self.nomeLoja = nomeLoja
        self.__senha = senha

    def get_senha(self):
        return self.__senha