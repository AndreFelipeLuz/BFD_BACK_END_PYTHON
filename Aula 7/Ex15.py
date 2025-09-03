nomes = ['Teclado', 'Mouse']
precos = [250, 120]
estoques = [10, 25]

produtos = zip(nomes, precos, estoques)

for produto in produtos:
    print(produto)