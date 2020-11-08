"""
Projeto 2 da disciplina de Algoritmos e Programação de Computadores.
"""
import random
import sys


def valida_dados(_info):
    '''Função que coleta do usuário os valores que ele deseja'''
    global valor_chute
    valor_chute = input("Chute um numero entre 1 e 100 (ENTER para sair): ")
    if not valor_chute:
        sys.exit()
    elif not valor_chute.isnumeric() or int(valor_chute) <= 0 or int(valor_chute) > 100:
        while (not valor_chute.isnumeric() or int(valor_chute) <= 0 or int(valor_chute) > 100):
            if not valor_chute.isnumeric():
                print("A informação passada nao e valida!")
            elif (int(valor_chute) <= 0 or int(valor_chute) > 100):
                print("O numero passado deve ser maior que 0 ou menor ou igual a 100!")
            valor_chute = input("Chute um numero entre 1 e 100 (ENTER para sair): ")
            if not valor_chute:
                sys.exit()
    if int(valor_chute) == int(valor_resposta):
        print("Parabens! Voce acertou a resposta!")
    return valor_chute

def testa_chute(_chute, _resposta):
    '''Função que verifica se o número coletado pelo usuário é o mesmo que o que foi sorteado'''
    if int(valor_chute) == int(valor_resposta):
        print("Parabens! Voce acertou a resposta!")
    else:
        while int(valor_chute) != valor_resposta:
            if int(valor_chute) > int(valor_resposta):
                print("O chute foi muito alto!")
            else:
                print("O valor foi muito baixo!")
            valida_dados(0)
def main():
    '''Função principal do programa'''
    global valor_resposta
    valor_resposta = random.randint(0, 100)
    valida_dados(0)
    testa_chute(valor_chute, valor_resposta)

main()
