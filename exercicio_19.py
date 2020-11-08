#coding: utf-8
'''Exercício 19'''
num_1 = input("Digite um numero: ")
num_2 = input("Digite outro numero: ")
num_3 = input("Digite o último numero: ")


if (num_1 > num_2 and num_1 > num_3):
    print ("Maior numero: ", num_1)
elif (num_2 > num_1 and num_2 > num_3):
    print ("Maior numero: ", num_2)
elif (num_3 > num_1 and num_3 > num_2):
    print ("Maior numero: ", num_3)
elif (num_1 == num_2 and num_1 > num_3):
    print ("Valores iguais como maior numero ", num_1)
elif (num_2 == num_3 and num_2 > num_1):
    print ("Valores iguais como maior numero ", num_2)
elif (num_1 == num_3 and num_1 > num_2):
    print ("Valores iguais como maior numero ", num_1)
else:
    print ("Valores iguais: ", num_1)
