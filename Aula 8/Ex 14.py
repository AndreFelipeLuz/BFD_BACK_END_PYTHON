nomes = ['João', 'Maria', 'Pedro']
sobrenomes = ['Silva', 'Santos', 'Rocha']
nomes_completos = list(map(lambda nome, sobrenome: f"{nome} {sobrenome}", nomes, sobrenomes))
print(nomes_completos)