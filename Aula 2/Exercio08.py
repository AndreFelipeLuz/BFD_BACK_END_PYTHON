import datetime

hora_atual = datetime.datetime.now()
nome_usuario = input("Digite o seu nome:\n")

print(f'Olá, {nome_usuario}! Agora são {hora_atual.strftime("%H:%M")} horas.')
