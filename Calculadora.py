#Coding: utf-8
__author__ = 'Carlos Eduardo da Silva'
#Projeto 01

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
conta = int(input('Qual operação vc quer executar? [1]Soma [2]Subtração [3] Multiplicação [4] divisão [5] Exponenciação '))

class Calculadora:
    def __init__(self, numero1, numero2):
        self.n1 = numero1
        self.n2 = numero2
    def soma(self):
        return self.n1 + self.n2
    def sub(self):
        return self.n1 - self.n2
    def mult(self):
        return self.n1 * self.n2
    def div(self):
        return self.n1 / self.n2
    def expo(self):
        return self.n1 ** self.n2
calculadora = Calculadora(numero1, numero2)

if conta == 1:
    print(calculadora.soma())
elif conta == 2:
    print(calculadora.sub())
elif conta == 3:
    print(calculadora.mult())
elif conta == 4:
    print(calculadora.div())
elif conta == 5:
    print(calculadora.expo())
print('Terminou!!')

