#coding: utf-8

'''
Exercícios Lista 3
'''

#Exercício 95
def imprimir(_numero):
    '''
        FUnção responsável por imprimir os números de 1 até n
    '''
    if isinstance(numero, int):
        i = 1
        while i <= numero:
            j = 1
            texto = ''
            while j <= i:
                texto += str(j) + "\t"
                j += 1
            print(texto)
            i += 1
numero = input("Digite um número: ")
#Apesar do erro invalid-name, não alterei por não se tratar de uma constate
imprimir(numero)
print ("/-----------------------/")

#Exercício 99
def retangulo(_linha, _coluna):
    '''
        Função responsável por imprimir o retângulo
    '''
    for i in range(linha):
        for j in range(coluna):
            if i == 0 and j == 0:
                print("+")
            elif i == 0 and j == coluna-1:
                print("+")
            elif i == linha-1 and j == 0:
                print("+")
            elif i == linha-1 and j == coluna-1:
                print("+")
            elif i == 0 and j != 0:
                print("-")
            elif i == linha-1 and j != 0:
                print("-")
            elif j == 0 and i != 0:
                print("|")
            elif j == coluna-1 and i != 0:
                print("|")
            else:
                print(" ")
        print("")

linha = input("Digite a quantidade de linhas: ")
#Apesar do erro invalid-name, não alterei por não se tratar de uma constate
coluna = input("Digite a quantidade de colunas: ")
#Apesar do erro invalid-name, não alterei por não se tratar de uma constate

if (1 >= linha < 20 and 1 >= coluna < 20):
    retangulo(linha, coluna)
else:
    retangulo(20, 20)
print ("/-----------------------/")

#Exercício 100
def cabecalho(_largura):
    '''
        Função responsável por imprimir o cabeçalho e o título.
        Não é necessário utilizar a variavel titulo como dependencia dessa função.
    '''
    print('*' * largura)
    print(titulo.center(largura))
    print('*' * largura)

largura = input("Digite um número: ")
#Apesar do erro invalid-name, não alterei por não se tratar de uma constate
titulo = raw_input("Digite um título: ")#Quando utilizo input, ocorre um erro de EOF.
#Por isso, utilizei o raw_input, apesar do erro dado no pylint
#Apesar do erro invalid-name, não alterei por não se tratar de uma constate

cabecalho(largura)
print ("/-----------------------/")

#Exercício 103
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
