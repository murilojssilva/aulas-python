#coding: utf-8
'''Exercício 45'''

def par_impar(_valor):
    '''Função para calcular ímpares e pares'''
    if (num >= 1 or num <= 10):
        for i in range (1,11):
            print (num, "*", i ," = ", num * i)
    else:
        print ("Numero incorreto")

num = input ("Digite um numero inteiro entre 1 e 10: ")
par_impar(num)
