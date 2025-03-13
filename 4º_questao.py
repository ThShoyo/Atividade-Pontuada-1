import os
os.system ("clear")

qtd_morango=int(input("Digite a quantidade de morangos(kg): "))
qtd_macas=int(input("Digite a quantidade de macas(kg): "))

if qtd_morango <= 5:
    valor_mor = qtd_morango * 2.50
if qtd_morango > 5: 
    valor_mor = qtd_morango * 2.20
if qtd_macas <= 5:
    valor_mac = qtd_macas * 1.80
if qtd_macas > 5: 
    valor_mac = qtd_macas * 1.50

total_frutas = qtd_macas + qtd_morango
valor_total = valor_mac + valor_mor

if total_frutas > 10 or valor_total > 15:
    Valor = (valor_total * 0.9)
    print(f"Ganhou desconto de 10%, valor final: {Valor} ")
else: 
    print (f"Valor final: {valor_total}")