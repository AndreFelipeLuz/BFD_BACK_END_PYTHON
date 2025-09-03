frase = "Python é uma linguagem de programação poderosa e Python é divertida"
palavras = frase.lower().split()
palavras_unicas = set(palavras)
numero_de_palavras_unicas = len(palavras_unicas)

print(f"A frase é: '{frase}'")
print(f"O número de palavras únicas na frase é: {numero_de_palavras_unicas}")