#coding: utf-8
def palindromo(_palavra):
    '''
        Função responsável por pegar a palavra digitada
        anteriormente e verificar se ela é palíndromo.
    '''

    palavra_minuscula_sem_espacos = palavra.replace(' ', '').lower()
    palavra_invertida = palavra_minuscula_sem_espacos[::-1]
    if palavra_invertida == palavra_minuscula_sem_espacos:
        print("A string digitada é palindroma ! ")
    else:
        print("A string digitada não é palindroma !")

palavra = raw_input("Digite uma palavra: ")
#Apesar do erro invalid-name, não alterei por não se tratar de uma constate
palindromo(palavra)
