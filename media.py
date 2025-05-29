#Exercício 3: Leia duas notas, calcule a média e diga se o aluno foi aprovado (média ≥ 7).

nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota:"))

media = (nota1+nota2) / 2

print("Sua média é ", media)

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")