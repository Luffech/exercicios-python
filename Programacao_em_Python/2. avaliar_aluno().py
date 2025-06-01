#avaliação de aluno

def calcular_media(notas):
    return sum(notas) / len(notas)

def avaliar_aluno(media):
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")


notas = [float(input("Nota 1: ")), float(input("Nota 2: ")), float(input("Nota 3: "))]
media = calcular_media(notas)
avaliar_aluno(media)