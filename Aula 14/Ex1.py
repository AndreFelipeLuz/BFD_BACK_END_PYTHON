class carro:
    def __init__(self, nome, cor):
        self.nome = nome  # Atributo para o nome do carro
        self.cor = cor    # Atributo para a cor do carro

    def descrever(self):
        print(f"Este é um {self.nome} da cor {self.cor}.")

carinfusca = carro("Fusca", "Azul")
carinXefrosso = carro("chevrolet","vermelho")

carinXefrosso.descrever()
carinfusca.descrever()