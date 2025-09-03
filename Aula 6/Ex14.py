SENHA_CORRETA = "python123"

senha_digitada = ""


while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")

    if senha_digitada != SENHA_CORRETA:
        print("Senha incorreta. Tente novamente.")

print("Senha correta! Login bem-sucedido.")