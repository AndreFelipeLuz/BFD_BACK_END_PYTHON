
numero = int(input("Digite um número inteiro de 1 a 7: "))

match numero:
    case 1:
        print("O dia da semana correspondente é: Domingo")
    case 2:
        print("O dia da semana correspondente é: Segunda-feira")
    case 3:
        print("O dia da semana correspondente é: Terça-feira")
    case 4:
        print("O dia da semana correspondente é: Quarta-feira")
    case 5:
        print("O dia da semana correspondente é: Quinta-feira")
    case 6:
        print("O dia da semana correspondente é: Sexta-feira")
    case 7:
        print("O dia da semana correspondente é: Sábado")
    case _:
        print("Erro: O número digitado não está entre 1 e 7.")