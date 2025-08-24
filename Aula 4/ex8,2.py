saldo_bancario = 1000.0

print("Olá! Seu saldo atual é de R$ 1000.00.")

print("\nEscolha uma opção:")
print("1 - Para Depósitar")
print("2 - Para Sacar")
print("3 - Para Aplicar juros")

escolha = input("Digite o número da sua escolha: ")

match escolha:
    case '1':
        deposito = float(input("Digite o valor do depósito: "))
        saldo_bancario += deposito
        print(f"Depósito de R$ {deposito:.2f} realizado com sucesso.")
    case '2':
        saque = float(input("Digite o valor do saque: "))
        saldo_bancario -= saque
        print(f"Saque de R$ {saque:.2f} realizado com sucesso.")
    case '3':
        fator_juros = float(input("Digite o fator de juros (ex: 1.05 para 5%): "))
        saldo_bancario *= fator_juros
        print(f"Juros de {fator_juros * 100 - 100:.2f}% aplicados com sucesso.")
    case _:
        print("Opção inválida. Por favor, reinicie o programa e escolha uma opção válida.")

if escolha in ['1', '2', '3']:
    print(f"Seu novo saldo é: R$ {saldo_bancario:.2f}")