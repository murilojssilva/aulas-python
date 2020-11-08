#coding: utf-8
'''
    Exercício 117
'''
import random
import sys
def jogo_forca():
    arquivo = open("listaDePalavras.txt", "r")
    listaDePalavras = arquivo.readlines()
    arquivo.close()

    palavraEscolhida = listaDePalavras[random.randint(0, len(listaDePalavras) - 1)].upper().strip()
    palavraAdivinhada = ["_"] * len(palavraEscolhida)

    numTentativas = 0
    erros = 0

    print(" ".join(palavraAdivinhada))

    while True:
        p = raw_input("Digite uma letra: ").upper().strip()
        cont = 0
        if p in palavraEscolhida:
            for pa in palavraEscolhida:
                if pa == p:
                    palavraAdivinhada[cont] = p
                cont += 1
            if "_" not in " ".join(palavraAdivinhada):
                print("Parabéns! Voce ganhou!")
                print(palavraEscolhida)
                break
        else:
            erros += 1
            if erros >= 6:
                print("Voce perdeu! A palavra escolhida era ", palavraEscolhida)
                sys.exit()
            else:
                print("Voce errou pela ",  erros, " vez. Tente novamente.")
        print(" ".join(palavraAdivinhada))

jogo_forca()
