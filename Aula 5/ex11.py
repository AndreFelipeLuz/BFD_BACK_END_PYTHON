custo_por_dia = 60.00
custo_por_km = 0.15


dias_alugados = float(input("Quantos dias o carro foi alugado? "))
km_rodados = float(input("Quantos Km foram percorridos? "))
valor_dias = dias_alugados * custo_por_dia
valor_km = km_rodados * custo_por_km

preco_total = valor_dias + valor_km

print(f"O valor total a pagar é de: R$ {preco_total:.2f}")