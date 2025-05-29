#Mini-Projeto: Sistema de Cadastro
#Desafio Final:
#Peça nome, idade e email do usuário;
#Armazene em um dicionário;
#Adicione a uma lista de cadastros;
#Imprima todos os cadastros ao final.

cadastros = []

quantidade = int(input("Quantas pessoas você quer cadastrar? "))

for i in range(quantidade):
    print(f"nCadastro {i+1}:")
    cadastro = {}

    cadastro["nome"] = input("Por favor, digite seu nome: ")
    cadastro["idade"] = input("Por favor, digite sua idade: ")
    cadastro["email"] = input("Por favor, digite seu email: ")

    cadastros.append(cadastro)

print("\n=== Todos os cadastro ===")
for i, cadastro in enumerate(cadastros, start=1):
    print(f"\nPessoa {i}:")
    for chave, valor in cadastro.items():
        print(f"{chave.capitalize()}: {valor}")


