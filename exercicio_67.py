#coding: utf-8
'''Exercício 67'''

def salario(_valor):
    '''Função que calcula a variação do salário com o passar dos anos'''
    percentual = 0.015
    print ("Salario em 1995: ", _valor)
    for i in range (1,26):
        print ("Salario em ", i + 1995 ,": ", 1000 * (1 + percentual))
        percentual *= 2

salario(1000)
print ("-------------------------------")
valor_salario = input("Salario: ")
salario(valor_salario)
