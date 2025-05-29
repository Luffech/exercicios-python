pilha = []

# 1. Adicionar elementos (colocar na pilha)
pilha.append("Prato 1")
pilha.append("Prato 2")
pilha.append("Prato 3")
pilha.append("Prato 4")

print("Pilha Atual:", pilha)

#Removendo o último (desempilha)
removido = pilha.pop()
print(f"{removido} foi retirado da pilha.")

print("Pilha atual:", pilha)
