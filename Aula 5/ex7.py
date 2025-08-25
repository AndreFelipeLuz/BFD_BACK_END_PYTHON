idade_motorista = int(input("Qual a sua idade? "))
tem_carteira_str = input("Você tem carteira de motorista? (True/False) ")

tem_carteira = tem_carteira_str.lower() == "true"

pode_dirigir = idade_motorista >= 18 and tem_carteira

print(f"Pode dirigir? {pode_dirigir}")