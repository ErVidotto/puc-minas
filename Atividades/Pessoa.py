nome = input( "Digite Seu nome")
curso = input ("Digite seu curso")
idade = int(input("Digite sua idade"))
print(" Eu "+ nome + " Idade" + str(idade) + " Estou fazendo o curso " + curso  )

class Pessoa:

    def __init__(self):
        self.nome = ""
        self.sexo = ""
        self.idade = 0
        self.peso = 0.0
        self.cor = ""
        self.altura = 0.0
        