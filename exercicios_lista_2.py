#coding: utf-8
'''Exercícios lista 2'''
#Exercicio 34
for i in range (0,7):
    print ((i+1)*2)
print ("-----------------------")
for i in range (0,7):
    print (((i+1)*2)-1)
print ("/-----------------------/")

#Exercício 42
for i in range (1,25):
    print (i*2)
print ("/-----------------------/")

#Exercício 45
def par_impar(_valor):
    '''Função para calcular ímpares e pares'''
    if (num >= 1 or num <= 10):
        for j in range (1,11):
            print (num, "*", j ," = ", num * j)
    else:
        print ("Numero incorreto")

num = input ("Digite um numero inteiro entre 1 e 10: ")
par_impar(num)
print ("/-----------------------/")

#Exercício 53

def divisores(_valor):
    '''Função que verifica se o número é primo ou se possui divisores e quais são estes divisores'''
    qtd_divisores = 0
    div = []
    for j in range(num):
        if num%(j+1) == 0:
            qtd_divisores += 1
            div.append(j+1)
    if qtd_divisores == 2:
        print ("O numero e primo")
    else:
        print ("O numero nao e primo e seus divisores sao: ",div)

num = input('Digite um numero inteiro: ')
divisores(num)
print ("/-----------------------/")


#Exercício 67

def salario(_valor):
    '''Função que calcula a variação do salário com o passar dos anos'''
    percentual = 0.015
    print ("Salario em 1995: ", _valor)
    for j in range (1,26):
        print ("Salario em ", j + 1995 ,": ", _valor * (1 + percentual))
        percentual *= 2

salario(1000)
print ("-------------------------------")
valor_salario = input("Salario: ")
salario(valor_salario)
print ("/-----------------------/")
