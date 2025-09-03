cor_semaforo = input("Digite a cor do semáforo (verde, amarelo ou vermelho): ").lower()

match cor_semaforo:
    case "verde":
        print("Siga em frente!")
    case "amarelo":
        print("Atenção! Reduza a velocidade.")
    case "vermelho":
        print("Pare!")
    case _:
        print("Cor inválida. O sinal está com defeito.")