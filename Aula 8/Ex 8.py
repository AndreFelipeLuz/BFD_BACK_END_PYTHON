def atualizar_perfil(perfil, **kwargs):
    perfil.update(kwargs)
    return perfil

perfil = {'nome': 'João', 'idade': 30}
perfil_atualizado = atualizar_perfil(perfil, idade=31, cidade="Rio de Janeiro")

print("Perfil original:", {'nome': 'João', 'idade': 30})
print("Perfil atualizado:", perfil_atualizado)