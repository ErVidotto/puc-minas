class Pessoa:

    def __init__(self):
        self.nome = ""
        self.sexo = ""
        self.idade = 0
        self.peso = 0.0
        self.cor = ""
        self.altura = 0.0
        
    def calcular_idade_dias(self, idade):
        return idade * 365
    
    def calcular_idade_mes(self, idade):
        return (idade * 12)
    
lista_pessoas = []

for x in range(2):
    pessoa = Pessoa()
    pessoa.nome = input("Digite seu nome: ")
    pessoa.cor = input("Digite sua cor: ")
    pessoa.idade = int(input("Digite sua idade: "))
    pessoa.peso = float(input("Digite seu peso: "))
    pessoa.sexo = input("Digite seu sexo: ")
    pessoa.altura = float(input("Digite sua altura: "))
    lista_pessoas.append(pessoa)

for p in lista_pessoas:
    print("Nome ...: " + pessoa.nome)
    print("Idade ..: " + str(pessoa.idade))
    print("Sexo ...: " + pessoa.sexo)
    print("Peso ...: " + str(pessoa.peso))
    print("Altura .: " + str(pessoa.altura))
    print("Cor ....: " + pessoa.cor)
    print("Dias vividos ..: " + str(pessoa.calcular_idade_dias(pessoa.idade)))
    print("Meses vividos .: " + str(pessoa.calcular_idade_mes(pessoa.idade)))
    print("*****************")