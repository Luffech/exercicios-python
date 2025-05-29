
senha_correta = "python123"

senha_digitada = input("Digite sua senha: ")

while senha_digitada != senha_correta:
    senha_digitada = input("Senha incorreta! Digite novamente: ")

print("Acesso liberado!")
