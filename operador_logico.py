
# Exercício 14: Peça a idade e se tem carteira de motorista. Se idade ≥ 18 e tem carteira = True, imprima "Pode dirigir".

idade = int(input("Qual sua idade: "))
cnh = input("Tem carteira de motorista? (s/n)")

tem_cnh = cnh.lower() == "s"

if idade >= 18 and tem_cnh:
    print("Mete o pé, porra!")
else:
    print("Não pode kraleon.")