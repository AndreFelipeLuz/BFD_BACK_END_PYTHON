idade_minima = 18

idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= idade_minima:
    print("O usuário é maior de idade.")
elif idade_usuario == 16 or idade_usuario == 17:
    print("O usuário é menor e tem 16 ou 17 anos.")
else :
    print("O usuario é menor de idade")