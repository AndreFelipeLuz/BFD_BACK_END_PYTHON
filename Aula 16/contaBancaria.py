from abc import ABC, abstractmethod

class contaBancaria(ABC):
    def __init__(self,valor =0):
        if valor < 0:
            self.valor = 0
        else:
            self.valor = valor
    
    @abstractmethod
    def depositar(self,valor):
        pass
    
    @abstractmethod
    def sacar(self,valor):
        pass
    
class contaCorrente(contaBancaria):
    def __init__(self, valor):
        super().__init__(valor)
        self.taxaManutencao = 5
    
    def depositar(self,valor):
        if valor < 1:
            print("Valor depositado tem que ser no minimo 1 real ou mais.")
        else:
            self.valor += valor
            print(f"Saldo atual: {self.valor}")
    
    def sacar(self,valor):
        if valor < 1:
            print("Valor sacado tem que ser no minimo 1 real ou mais.")
        else:
            if valor + self.taxaManutencao < self.valor:
                self.valor -= valor + self.taxaManutencao
                print(f"Saldo atual: {self.valor}")
            else:
                print("O valor de saque excede sua conta bancaria.")

class contaPoupanca(contaBancaria):
    def __init__(self, valor):
        super().__init__(valor)
        self.taxaJuros = 0.5
    
    def depositar(self,valor):
        if valor < 1:
            print("Valor depositado tem que ser no minimo 1 real ou mais.")
        else:
            self.valor += valor
            self.aplicarJuros()
            print(f"Saldo atual: {self.valor}")
            
    def sacar(self,valor):
        if valor < 1:
            print("Valor sacado tem que ser no minimo 1 real ou mais.")
        else:
            if valor < self.valor:
                self.valor -= valor
                print(f"Saldo atual: {self.valor}")
            else:
                print("O valor de saque excede sua conta bancaria.")
                
    def aplicarJuros(self):
        juros = self.taxaJuros * self.valor
        self.valor += juros
        print(f"Depósito de {self.valor} realizado com sucesso na Conta Poupança.")


Saito = [contaCorrente(20), contaPoupanca(20)]
for contaBancaria in Saito:
    contaBancaria.depositar(50)
    contaBancaria.depositar(-50)
    print("-" * 20)
    contaBancaria.sacar(5)
    contaBancaria.sacar(100)
    print("-" * 20)