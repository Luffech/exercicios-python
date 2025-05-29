#Exercício 6: Faça um programa que leia dois números e mostre a:

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

#Soma

soma = (numero1+numero2)
print(f"A soma de {numero1} mais o {numero2} é igual: {soma}")

#Subtração

subtracao = (numero1-numero2)
subtracao2 = (numero2-numero1)
print(f"A subtração do {numero1} menos o {numero2} é igual: {subtracao}, assim como a subtracao de {numero2} menos {numero1} é igual a: {subtracao2}")

#Multiplicação

multiplicacao = (numero1 * numero2)
print(f"A multiplicação de {numero1} vezes {numero2} é igual: {multiplicacao} ")

#Divisão

divisao = (numero1 / numero2)
divisao2 = (numero2 / numero1)

print(f"A divisão de {numero1} por {numero2} é igual a: {divisao}, assim como a divisão de {numero2} pelo {numero1} é igual a: {divisao2} ")