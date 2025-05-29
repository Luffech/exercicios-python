# 1º cria uma lista

fila = []

# 2º depois cria uma fila com pessoas (nome da lista.append("nome"))

fila.append("Ana")
fila.append("Bruno")
fila.append("Carlos")


print("Fila Atual:", fila)

# 3º Atender a primeira pessoa (remover do início da fila)

atendido = fila.pop(0)
print(f"{atendido} foi atendido.")

print("Fila Atual:", fila)

# 4º Mais uma pessoa entra na fila

fila.append("Diana")
print("Fila Atual:", fila)

# 5º Atender mais uma pessoa

atendido = fila.pop(0)
print(f"{atendido} foi atendido.")

print("Fila final:", fila)
