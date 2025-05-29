# Exercício 11: Crie uma classe Pessoa com os atributos nome e idade. Crie um método apresentar() que imprime: "Sou [nome] e tenho [idade] anos."
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Sou {self.nome} e tenho {self.idade} anos.")

pessoa1 = Pessoa("Luiz", 35)

pessoa1.apresentar()
