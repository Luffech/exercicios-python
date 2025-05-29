#Crie um programa que:

#Peça ao usuário um número

#Tente converter esse número para int

#Se der erro (ex: a pessoa digitar letra), mostre a mensagem: Entrada inválida! Por favor, digite um número inteiro.

while True:
    try: 
        numero = int(input("Digite um numero inteiro: "))
        break
    except:
        print("Entrada inválida! Por favor, digite o número inteiro.")

print(f"Você digitou o número:{numero}")