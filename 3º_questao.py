import os
os.system ("clear")

#Faça um algoritmo que leia dois valores inteiros A e B se os valores forem iguais deverá se somar os dois, caso contrário multiplique A por B.
#Ao final de qualquer um dos cálculos deve-se atribuir o resultado para uma variável C e mostrar seu conteúdo na tela.

Valor_A = int(input ("Digite um número: "))
Valor_B = int(input ("Digite um número: "))

if Valor_A == Valor_B:
    C = Valor_A + Valor_B
    print(C)

else: 
    C = Valor_A * Valor_B
    print(C)
