pilha = []

while True:
    print("\n=== Menu de Pilha ===")
    print("1 - Adicionar Item")
    print("2 - Remover item")
    print("3 - Ver Pilha")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item a empilhar: ")
        pilha.append(item)
        print(f"{item} foi empilhado.")
    
    elif opcao == "2":
        if len(pilha) > 0:
            removido = pilha.pop()
            print(f"{removido} foi removido da pilha")
        else:
            print("A pilha está vazia!")

    elif opcao == "3":
        if len(pilha) > 0:
            print("Pilha atual:", pilha)
        else:
            print("A pilha está vazia.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")