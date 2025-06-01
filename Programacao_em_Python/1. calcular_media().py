#calcule a media

def calcular_media(notas):
    return sum(notas) / len(notas)

notas= []
for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = calcular_media(notas)
print("Média:", media)