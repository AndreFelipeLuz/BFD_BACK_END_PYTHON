def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for caractere in texto:
        if caractere in vogais:
            contador += 1
    return contador

texto_exemplo = "Olá, Programação Python!"
quantidade_vogais = contar_vogais(texto_exemplo)

print(f"O texto '{texto_exemplo}' tem {quantidade_vogais} vogais.")