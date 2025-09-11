def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Erro: divisão por zero.")
    return a / b

try:
    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))
    
    resultado = None

    if operacao == '+':
        resultado = soma(num1, num2)
    elif operacao == '-':
        resultado = subtracao(num1, num2)
    elif operacao == '*':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/':
        resultado = divisao(num1, num2)
    else:
        raise ValueError("Erro: operação inválida.")

except ValueError as ve:
    print(ve)
except ZeroDivisionError as zde:
    print(zde)
except Exception:
    print("Ocorreu um erro inesperado.")
else:
    print(f"O resultado da operação é: {resultado}")
finally:
    print("Fim do programa.")