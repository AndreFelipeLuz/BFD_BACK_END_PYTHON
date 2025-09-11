def calcular_media(*args):
    if not args:
        return 0.0
    
    soma = sum(args)
    quantidade = len(args)
    
    return soma / quantidade

media_exemplo = calcular_media(8.5, 9.0, 7.5)

print(f"A média das notas é: {media_exemplo:.2f}")