#coding: utf-8
'''
    Exercícios lista 4
'''
#Exercício 108
import random
def lancamento():
    '''
        Função que armazena os valores dos dados lançados.
        Tem como objetivo contar quantas vezez sai determinados valores.
    '''
    resultados_lancamento = []
    vetor_contadores = [0, 0, 0, 0, 0, 0]
    for i in range(0, 100):
        valor_dado = random.randint(1, 6)
        resultados_lancamento.append(valor_dado)
        vetor_contadores[valor_dado - 1] += 1
        i += 1
    return vetor_contadores

print(lancamento())
print("/--------------------------------/")

#Exercício 109
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
print("/--------------------------------/")
#Exercício 111
def mes_extenso(_data_padrao):
    '''
        Função que recebe uma data no formato datetime e converte para o texto por extenso.
    '''
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    aux = data_padrao.split("/")
    dia = int(aux[0])
    mes = int(aux[1])
    ano = int(aux[2])
    if ((1 < dia < 31) or (1 < mes < 12) or (0 > ano > 9999)):
        return "Data Inválida"
    return dia, " de ", meses[mes-1], " de ", ano

data_padrao = raw_input('Digite uma data no formato DD/MM/AAAA: ')
print(mes_extenso(data_padrao))
