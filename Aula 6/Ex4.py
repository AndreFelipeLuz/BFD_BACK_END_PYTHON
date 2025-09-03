num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operador = input("Digite o operador aritmético (+, -, *, /, //, %): ")

if operador == '+':
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")

elif operador == '-':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")

elif operador == '*':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")

elif operador == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operador == '//':
    if num2 != 0:
        resultado = num1 // num2
        print(f"O resultado da divisão inteira é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

elif operador == '%':
    if num2 != 0:
        resultado = num1 % num2
        print(f"O resto da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

else:
    print("Operador inválido. Por favor, use +, -, *, /, // ou %.")