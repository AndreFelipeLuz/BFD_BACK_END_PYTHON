valor_por_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_total = valor_por_hora * horas_trabalhadas

print(f"O salário total referente a este mês é: R$ {salario_total:.2f}")