pessoa ={}

pessoa["nome"] = input("Digite seu nome: ")
pessoa["idade"] = input("Digite sua idade: ")
pessoa["cidade"] = input("Digite sua cidade: ")
pessoa["profissao"] = input("Digite sua profissão: ")
pessoa["telefone"] = input("Digite seu telefone: ")

print("\nDados completos:")
for chave, valor in pessoa.items():
    print(f"{chave.capitalize()}: {valor}")