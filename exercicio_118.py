#coding: utf-8
'''
    Exercício 118
'''
import random
import sys

def adivinhar_palavra():
    arquivo = open('listaDePalavras.txt', 'r')
    listaDePalavras = arquivo.readlines()
    arquivo.close()

    palavraEscolhida = listaDePalavras[random.randint(0, len(listaDePalavras) - 1)].strip()
    embaralha = random.sample(palavraEscolhida, len(palavraEscolhida))
    nova_palavra = ''.join(embaralha)
    print(nova_palavra)

    for cont in range (0, 6): 
        palavra_usuario  = raw_input('A palavra é: ')
        if palavra_usuario == palavraEscolhida:
            print("Parabens! Voce acertou!")
            sys.exit()
        else:
            print("Que pena! Você errou. Tente novamente!")

adivinhar_palavra()
