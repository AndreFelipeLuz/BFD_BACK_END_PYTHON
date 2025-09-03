nota_minima = 7.0

nota_final = float(input("Digite a sua nota final: "))

if nota_final >= nota_minima:
    print("Aprovado!")

elif nota_final >= 5.0 and nota_final < nota_minima:
    print("Você não foi muito bem. Mas ainda consegue recuperar")

else:
    print("Reprovado!")