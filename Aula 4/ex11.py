idade_minima = 18

idade_usuario = int(input("Digite sua idade: "))

maior_de_idade = idade_usuario >= idade_minima
menor_de_idade = idade_usuario < idade_minima

print(f"O usuário é maior de idade? {maior_de_idade}")
print(f"O usuário é menor de idade? {menor_de_idade}")