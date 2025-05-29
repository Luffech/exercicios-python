# Criar o dicionário com dados informados pelo usuário

pessoa ={}

pessoa["nome"] = input("Digite seu nome: ")
pessoa["idade"] = input("Digite sua idade: ")
pessoa["cidade"] = input("Digite sua cidade: ")
pessoa["profissao"] = input("Digite sua profissão: ")
pessoa["telefone"] = input("Digite seu telefone: ")



print("\nDadors da pessoa:")
print("nome:", pessoa["nome"])
print("idade:", pessoa["idade"])
print("cidade:", pessoa["cidade"])
print("profissao:", pessoa["profissao"])
print("telefone:", pessoa["telefone"])

