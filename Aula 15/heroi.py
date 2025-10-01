class personagem:
    def __init__(self, nome):
        self.nome = nome
        self.hp = 100
    def sofrerDano(self, dano):
        self.hp -= dano
        if self.hp <0:
            hp = 0
    def curarSe(self, cura):
        self.hp += cura
        if self.hp>100:
            self.hp=100
    def mostrarNome(self):
        return self.nome
    def trocarNome(self,nome):
        self.nome = nome
    def mostrarVida(self):
        return self.hp
    def mostrarTudo(self):
        print(F"Vida do Heroi atual: {self.hp} e o nome do heroi é: {self.nome}")    
heroi = personagem("Heroi")
heroi.mostrarTudo()
heroi.sofrerDano(30)
print(heroi.mostrarVida())
heroi.curarSe(50)
print(heroi.mostrarVida())
heroi.trocarNome("João")
print(F"Novo nome do heroi é: {heroi.mostrarNome()}")
