clientes = ['João', 'Maria', 'José']
saldos = [1500, 2500, 800]

for indice, (cliente, saldo) in enumerate(zip(clientes, saldos)):
    print(f"Cliente {indice + 1}: {cliente}, Saldo: R$ {saldo:.2f}")