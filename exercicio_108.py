#coding: utf-8
'''
    Exercicio 108
'''
import random
def lancamento():
    '''
        Função que armazena os valores dos dados lançados.
        Tem como objetivo contar quantas vezez sai determinados valores.
    '''
    resultados_lancamento = []
    vetor_contadores = [0, 0, 0, 0, 0, 0]
    i = 0
    while i < 100:
        valor_dado = random.randint(1, 6)
        resultados_lancamento.append(valor_dado)
        if valor_dado == 1:
            vetor_contadores[0] += 1
        elif valor_dado == 2:
            vetor_contadores[1] += 1
        elif valor_dado == 3:
            vetor_contadores[2] += 1
        elif valor_dado == 4:
            vetor_contadores[3] += 1
        elif valor_dado == 5:
            vetor_contadores[4] += 1
        elif valor_dado == 6:
            vetor_contadores[5] += 1
        i += 1
    print(vetor_contadores)

lancamento()
