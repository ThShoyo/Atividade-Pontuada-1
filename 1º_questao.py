import os
os.system ("clear")

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C, caso contrário, imprima que a A + B é maior que C. 

# Entrada


A = int(input ("Digite um número: "))
B = int(input ("Digite um número: "))
C = int(input ("Digite um número: "))

soma = A + B

if A + B < C:
    print ("É Menor")

else :
    print ("É Maior")