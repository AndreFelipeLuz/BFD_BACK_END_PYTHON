try:
    nota = int(input("Digite uma nota de 1 a 5: "))
    match nota:
        case 1:
            print("Péssimo. Precisamos melhorar.")
        case 2:
            print("Insuficiente. Vamos trabalhar para subir de nível.")
        case 3:
            print("Regular. Há espaço para crescer.")
        case 4:
            print("Bom. Ótimo trabalho!")
        case 5:
            print("Excelente. Parabéns pelo desempenho!")
        case _:
            print("Erro: A nota deve ser um número inteiro entre 1 e 5.")

except ValueError:
    print("Erro: Por favor, digite um número inteiro válido.")