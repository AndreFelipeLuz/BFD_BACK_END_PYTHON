Operacao = int(input("Qual operação deseja Escreva \n0 para Soma"
+ "\n1 para Subtração \n2 para multiplicação \n3 para divisão" 
"\n4 para divisão inteira \n5 para modulo"+"\n6 para exponeciacão\n"))

numero_um = int 
numero_dois = int

match Operacao :
    case 0:
        numero_um = int(input("Digite um numero para somar "))
        numero_dois = int(input("Digite outro numero para somar "))
        print(f"O seu numero Somado é {numero_um+numero_dois}")
    case 1: 
        numero_um = int(input("Digite um numero para subtrair "))
        numero_dois = int(input("Digite outro numero para Subtrair "))
        print(f"O seu numero subtraido é {numero_um-numero_dois}")
    case 2:
        numero_um = int(input("Digite um numero para Multiplicar "))
        numero_dois = int(input("Digite outro numero para Multiplicar "))
        print(f"O seu numero Multiplicado é {numero_um*numero_dois}")
    case 3:
        numero_um = int(input("Digite um numero para Dividir "))
        numero_dois = int(input("Digite outro numero para Dividir "))
        print(f"O seu numero Dividido é {numero_um/numero_dois}")
    case 4:
        numero_um = int(input("Digite um numero para Dividir inteiramente "))
        numero_dois = int(input("Digite outro numero para Dividir inteiramente "))
        print(f"O seu numero Dividido inteiramente é {numero_um//numero_dois}")
    case 5:
        numero_um = int(input("Digite um numero para Modular "))
        numero_dois = int(input("Digite outro numero para Modular "))
        print(f"O seu numero modulado é {numero_um%numero_dois}")
    case 6:
        numero_um = int(input("Digite um numero para Expoer "))
        numero_dois = int(input("Digite outro numero para Expoer "))
        print(f"O seu numero Exponenciado é {numero_um**numero_dois}")
    
    
    