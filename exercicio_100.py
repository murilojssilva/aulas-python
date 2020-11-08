#coding: utf-8
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
