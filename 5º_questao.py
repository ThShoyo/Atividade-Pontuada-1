import os
os.system ("clear")

valor_A = float(input("insira o número: "))
valor_B = float(input("insira o número: "))
operação = input("selecione a operacão: ")

match operação:
    case "+": 
        soma = valor_A + valor_B 
        print(f"O resultado da sua soma é: {soma}")
    case "-": 
        menos = valor_A - valor_B
        print(f"o resultado da sua subtração é: {menos}")
    case "/": 
        divisão = valor_A / valor_B
        print(f"o resultado da sua divisão  é: {divisão}")
    case "*": 
        multiplicacão = valor_A * valor_B
        print(f"o resultado da sua multiplicação é: {multiplicacão}")
    case _:
        print ("operação invalida")


