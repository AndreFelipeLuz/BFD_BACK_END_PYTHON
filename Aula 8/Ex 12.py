precos = [85, 120, 50, 250, 99]
produtos_filtrados = list(filter(lambda preco: preco > 100, precos))

print("Preços originais:", precos)
print("Preços maiores que 100:", produtos_filtrados)