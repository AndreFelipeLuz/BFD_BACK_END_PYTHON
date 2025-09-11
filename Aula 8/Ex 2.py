def inverter_texto(texto):
    return texto[::-1]

texto_original = "Olá, mundo!"
texto_invertido = inverter_texto(texto_original)

print(f"Texto original: {texto_original}")
print(f"Texto invertido: {texto_invertido}")