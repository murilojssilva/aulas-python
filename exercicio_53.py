#coding: utf-8
'''Exercício 53'''

def divisores(_valor):
    '''Função que verifica se o número é primo ou se possui divisores e quais são estes divisores'''
    qtd_divisores = 0
    div = []
    for i in range(num):
        if num%(i+1) == 0:
            qtd_divisores += 1
            div.append(i+1)
    if qtd_divisores == 2:
        print ("O numero e primo")
    else:
        print ("O numero nao e primo e seus divisores sao: ",div)

num = input('Digite um numero inteiro: ')

divisores(num)
