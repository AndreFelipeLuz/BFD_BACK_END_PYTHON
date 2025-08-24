saldo_bancario = 1000.0

deposito = float(input("Digite o valor do depósito: "))
saque = float(input("Digite o valor do saque: "))
fator_juros = float(input("Digite o fator de juros (ex: 1.05 para 5%): "))

saldo_bancario += deposito
saldo_bancario -= saque
saldo_bancario *= fator_juros

print(f"O saldo bancário final é: R$ {saldo_bancario:.2f}")