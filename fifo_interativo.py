fila = []

while True:
    print("\n=== Menu Da Fila ===")
    print("1 - Entra na fila")
    print("2 - Atender alguém")
    print("3 - Mostrar fila atual")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome:")
        fila.append(nome)
        print(f"{nome} entrou na fila.")

    elif opcao == "2":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"{atendido} foi atendido.")
        else:
            print("A fila está vazia. Ninguém para atender.")
    
    elif opcao == "3":
        if len(fila) > 0:
            print("fila atual:", fila)
        else:
            print("A fila está vazia.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opcao inválida. Tente Novamente.")