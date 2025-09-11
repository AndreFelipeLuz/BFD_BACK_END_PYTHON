def juntar_strings(*args):
    return "".join(args)

texto_concatenado = juntar_strings("Olá", " ", "mundo", "!")

print(texto_concatenado)