#coding: utf-8
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
