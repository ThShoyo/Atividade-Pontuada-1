import os
os.system ("clear")

#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas. 
#Programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 6,0), média até 4,0, o aluno está em recuperação, caso a média seja inferior a 4,0 o aluno será reprovado.

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))

soma = primeira_nota + segunda_nota
media = soma / 2

print(f"Média: {media}")

if media > 6:
    print ("Aprovado")

else:
    print ("Reprovado")