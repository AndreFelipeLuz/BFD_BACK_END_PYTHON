usuarios = [{'nome': 'Carlos', 'idade': 30}, {'nome': 'Ana', 'idade': 25}, {'nome': 'Bruno', 'idade': 40}]
usuarios_ordenados = sorted(usuarios, key=lambda usuario: usuario['nome'])

print("Lista de usuários original:")
print(usuarios)
print("\nLista de usuários ordenada por nome:")
print(usuarios_ordenados)