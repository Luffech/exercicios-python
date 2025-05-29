class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Eu sou {self.nome} e tenho {self.idade} anos.")
        
        

quantidade = int(input("Quantas pessoas você quer cadastrar? "))

pessoas = []

for i in range (quantidade):
    nome = input("Qual seu nome? ")
    idade = int(input("Qual sua idade? "))
    pessoa = Pessoa(nome, idade)
    pessoas.append(pessoa)

print("\nApresentações: ")
for p in pessoas:
    p.apresentar()