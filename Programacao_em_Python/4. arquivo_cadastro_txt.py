with open("cadastros.txt", "w") as arquivo:
    for i in range(3):
        nome = input(f"Nome{i+1}: ")
        email = input(f"Email{i+1}: ")
        arquivo.write(f"{nome},{email}\n")

with open("cadastros.txt", "r") as arquivo:
    print("Cadastros:")
    for linha in arquivo:
        print(linha.strip())