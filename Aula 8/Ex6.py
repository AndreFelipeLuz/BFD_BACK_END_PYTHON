def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    
    for caractere in texto:
        if caractere in vogais:
            contador += 1
            
    return contador

frase = "Programação em Python"
numero_de_vogais = contar_vogais(frase)
print(f"O número de vogais na frase '{frase}' é: {numero_de_vogais}")