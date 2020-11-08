#coding: utf-8
'''
    Exercício 109
'''
import random
def embaralha_palavra():
    '''
        Função que recebe uma palavra digitada e embaralha suas letras.
    '''
    palavra = raw_input("Insira uma palavra: ")
    embaralha = random.sample(palavra, len(palavra))
    palavra = ''.join(embaralha)
    print('MAIUSCULA: ', palavra.upper())
    print('minuscula: ', palavra.lower())

embaralha_palavra()
