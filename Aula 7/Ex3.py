vendas_semana = [1200,1500,1100,2000,2500,1800,1300]

soma = sum(vendas_semana)
menor_valor = min(vendas_semana)

print(f'A soma total dos protudos é: {soma}\nE o menor valor recebido na semana foi: {menor_valor}'
      f'\nAlem disso o dia que teve menos venda foi: {vendas_semana.index(menor_valor)}')
