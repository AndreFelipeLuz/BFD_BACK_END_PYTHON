def cadastrar_usuario(nome, email, **kwargs):
    print("Dados do usuário:")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")

cadastrar_usuario(nome="Ana", email="ana@email.com", idade=30, cidade="Salvador")
print("\n---")
cadastrar_usuario(nome="Carlos", email="carlos@email.com", profissao="Engenheiro", empresa="Tech Corp")