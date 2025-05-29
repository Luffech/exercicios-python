# Exercício 10: Crie uma função chamada boas_vindas(nome) que imprime: "Olá, [nome]!"

def boas_vindas(nome):
    print(f"Olá,  {nome}!")

nome_usuario = input("Digite seu nome: ")
boas_vindas(nome_usuario)