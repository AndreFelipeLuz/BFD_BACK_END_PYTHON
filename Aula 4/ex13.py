idade = int(input("Insira sua Idade: "))
possui_carteira = True 

pode_dirigir = (idade >= 18) and possui_carteira

print(f"pode dirigir? {pode_dirigir}")