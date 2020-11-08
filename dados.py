#coding: utf-8
"""
Projeto 1 da disciplina de Algoritmos e Programação de Computadores.
"""
import random
import sys


def rola_dados(_valor, _qtde):
    '''Função que faz o lançamento dos dados caso os mesmos possuam valores válidos'''
    global lados
    lados = []
    if int(dado)%2 == 0:
        for i in range(int(qtde)):
            numero_sorteado = random.randint(1, int(dado))
            print("Lancamento n. ", i + 1, " - ", numero_sorteado)
            lados.append(numero_sorteado)
    else:
        print("Tamanho do dado invalido.")
    if lados:
        print(dado, " dado(s) de ", qtde, " lados: ", lados)
    else:
        print("Dado fornecido possui a qtde de lados invalida")
def valida_dados(_info):
    '''Função que coleta do usuário os valores que ele deseja'''
    global dado
    global qtde
    dado = str(input("Forneca o tamanho do dado que sera rolado (ENTER para sair): "))
    if not dado:
        sys.exit()
    elif not dado.isnumeric() or int(dado) <= 0:
        while (not dado.isnumeric() or int(dado) <= 0):
            if not dado.isnumeric():
                print("A informação passada nao e valida!")
            elif int(dado) <= 0:
                print("O numero passado deve ser maior que 0!")
            dado = str(input("Forneca o tamanho do dado que sera rolado (ENTER para sair): "))
            if not dado:
                sys.exit()
    print(dado)
    qtde = str(input("Forneca o numero de dados que serao rolados (em branco == 1): "))
    if not qtde:
        qtde = str(1)
    elif not qtde.isnumeric() or int(qtde) <= 0:
        while (not qtde.isnumeric() or int(qtde) < 0):
            if not qtde.isnumeric():
                print("A informação passada nao e valida!")
            elif int(qtde) <= 0:
                print("O numero passado deve ser maior que 0!")
            qtde = str(input("Forneca o numero de dados que serao rolados (em branco == 1): "))
            if not qtde:
                qtde = str(1)

def main():
    '''Função principal do programa'''
    valida_dados(0)
    rola_dados(dado, qtde)
main()
