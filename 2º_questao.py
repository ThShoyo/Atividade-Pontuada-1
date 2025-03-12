import os
os.system ("clear")

#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. 
#Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos). Por fim, mostre os dados do usuário.

nome = (input("Digite seu nome: ")) .upper()
sexo = (input("Digite M ou F para o sexo: ")) .upper()

match sexo:
    case "F": 
        estado_civil = (input("Casada ou Solteira: ")) .upper()
        match estado_civil:
            case "Casada":
                tempo_casada = int (input("Tempo de casada:"))
                print (f"Nome: (nome)")
                print (f"Sexo: (sexo)")
                print (f"Estado Civil: (estado_civil)")
                print (f"Tempo de casada: (tempo_casada)")



    case "M":
        print (f"Nome: (nome)")
        print ( f"GEnero: (sexo)")
    case _: 
        print ("Opção Inválida")            