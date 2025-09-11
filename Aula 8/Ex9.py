def buscar_livro(titulo, **kwargs):
    print(f"Buscando livro: '{titulo}'")
    
    if kwargs:
        print("Filtros aplicados:")
        for chave, valor in kwargs.items():
            print(f"- {chave.capitalize()}: {valor}")
    else:
        print("Nenhum filtro adicional aplicado.")

buscar_livro("Dom Casmurro", autor="Machado de Assis", ano=1899)

buscar_livro("O Pequeno Príncipe")