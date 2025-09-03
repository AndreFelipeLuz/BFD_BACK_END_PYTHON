try:
    numero = int(input("Digite um número inteiro para ver a tabuada: "))

    print(f"\nTabuada de multiplicação do {numero}:")

    for i in range(1, 11):
        resultado = numero * i
        
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")