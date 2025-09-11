def criar_saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a)!"

usuario_nome = input("Por favor, digite o seu nome: ")

mensagem = criar_saudacao(usuario_nome)
print(mensagem)
